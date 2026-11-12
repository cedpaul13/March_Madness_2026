import assert from "node:assert/strict";
import { execFileSync, spawnSync } from "node:child_process";
import { mkdtempSync, mkdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import test from "node:test";

const deployScript = readFileSync(new URL("./deploy_site.sh", import.meta.url), "utf8");
const gitBinary = execFileSync("sh", ["-c", "command -v git"], { encoding: "utf8" }).trim();
const gitEnvironment = {
  ...process.env,
  GIT_CONFIG_COUNT: "2",
  GIT_CONFIG_KEY_0: "commit.gpgsign",
  GIT_CONFIG_VALUE_0: "false",
  GIT_CONFIG_KEY_1: "core.hooksPath",
  GIT_CONFIG_VALUE_1: "/dev/null",
};

function fixture(t) {
  const directory = mkdtempSync(join(tmpdir(), "mm26-deploy-test-"));
  t.after(() => rmSync(directory, { recursive: true, force: true }));
  const root = join(directory, "source");
  const remote = join(directory, "remote.git");
  mkdirSync(join(root, "docs"), { recursive: true });
  const git = (...args) => execFileSync(gitBinary, args, {
    cwd: root, env: gitEnvironment, encoding: "utf8", stdio: ["ignore", "pipe", "pipe"],
  }).trim();
  git("init", "--bare", remote);
  git("init", "-b", "main");
  git("config", "user.name", "Site test");
  git("config", "user.email", "site-test@example.invalid");
  git("remote", "add", "origin", remote);
  writeFileSync(join(root, "deploy.sh"), deployScript);
  writeFileSync(join(root, "docs/index.html"), "<!doctype html><title>Fixture</title>");
  writeFileSync(join(root, "docs/design.css"), "body { color: red; }");
  writeFileSync(join(root, "docs/ncaa-logo.svg"), '<svg aria-label="NCAA"></svg>');
  return {
    root, remote, git, directory,
    deploy: (env = {}) => spawnSync("bash", ["deploy.sh"], {
      cwd: root, env: { ...gitEnvironment, ...env }, encoding: "utf8",
    }),
  };
}

test("publishing includes the page, stylesheet and logo and allows a subsequent deployment", (t) => {
  const site = fixture(t);
  const first = site.deploy();
  assert.equal(first.status, 0, first.stderr);
  assert.match(site.git("--git-dir", site.remote, "show", "gh-pages:index.html"), /Fixture/);
  assert.match(site.git("--git-dir", site.remote, "show", "gh-pages:design.css"), /red/);
  assert.match(site.git("--git-dir", site.remote, "show", "gh-pages:ncaa-logo.svg"), /NCAA/);
  writeFileSync(join(site.root, "docs/design.css"), "body { color: blue; }");
  const second = site.deploy();
  assert.equal(second.status, 0, second.stderr);
  assert.match(site.git("--git-dir", site.remote, "show", "gh-pages:design.css"), /blue/);
  assert.match(site.git("--git-dir", site.remote, "show", "gh-pages:ncaa-logo.svg"), /NCAA/);
});

test("publishing rejects a concurrent update instead of overwriting it", (t) => {
  const site = fixture(t);
  const first = site.deploy();
  assert.equal(first.status, 0, first.stderr);
  const previous = site.git("--git-dir", site.remote, "rev-parse", "gh-pages");
  writeFileSync(join(site.root, "docs/design.css"), "body { color: blue; }");
  const second = site.deploy();
  assert.equal(second.status, 0, second.stderr);
  const concurrent = site.git("--git-dir", site.remote, "rev-parse", "gh-pages");
  site.git("--git-dir", site.remote, "update-ref", "refs/heads/gh-pages", previous);
  writeFileSync(join(site.root, "docs/design.css"), "body { color: green; }");

  const bin = join(site.directory, "bin");
  mkdirSync(bin);
  writeFileSync(join(bin, "git"), `#!/usr/bin/env node
const { spawnSync, execFileSync } = require("node:child_process");
const args = process.argv.slice(2);
const result = spawnSync(${JSON.stringify(gitBinary)}, args, { encoding: "utf8" });
if (args[0] === "ls-remote" && result.status === 0) {
  execFileSync(${JSON.stringify(gitBinary)}, ["--git-dir", ${JSON.stringify(site.remote)}, "update-ref", "refs/heads/gh-pages", ${JSON.stringify(concurrent)}]);
}
process.stdout.write(result.stdout || "");
process.stderr.write(result.stderr || "");
process.exit(result.status ?? 1);
`, { mode: 0o755 });
  const rejected = site.deploy({ PATH: `${bin}:${process.env.PATH}` });
  assert.notEqual(rejected.status, 0);
  assert.match(rejected.stderr, /stale info/);
  assert.equal(site.git("--git-dir", site.remote, "rev-parse", "gh-pages"), concurrent);
  assert.match(site.git("--git-dir", site.remote, "show", "gh-pages:design.css"), /blue/);
});
