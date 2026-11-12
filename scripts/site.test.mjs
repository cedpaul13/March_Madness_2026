import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import test from "node:test";
import { runInNewContext } from "node:vm";

const html = readFileSync(new URL("../docs/index.html", import.meta.url), "utf8");
const bootScript = html.match(/<script>([\s\S]*?)<\/script>/)[1];

function boot(getItem = () => null) {
  const attributes = new Map();
  const warnings = [];
  const app = {};
  const document = {
    documentElement: { setAttribute: (key, value) => attributes.set(key, value) },
    createElement: () => ({ setAttribute() {} }),
  };
  runInNewContext(bootScript, {
    window: app,
    document,
    localStorage: { getItem },
    console: { warn: (...args) => warnings.push(args) },
  });
  return { app, attributes, warnings };
}

function portrait({ fallback = null, placeholder = null } = {}) {
  const attributes = new Map(fallback ? [["data-fallback", fallback]] : []);
  const children = [];
  const image = {
    alt: "Example Team",
    onerror: () => {},
    hidden: false,
    previousElementSibling: placeholder,
    parentNode: { appendChild: (element) => children.push(element) },
    getAttribute: (key) => attributes.get(key) ?? null,
    removeAttribute: (key) => attributes.delete(key),
  };
  return { image, children };
}

test("a failed backup portrait becomes initials without a preceding placeholder", () => {
  const { app } = boot();
  const { image, children } = portrait({ fallback: "backup.png" });
  app.imgFallback(image);
  assert.equal(image.src, "backup.png");
  assert.equal(image.hidden, false);
  assert.equal(children.length, 0);

  app.imgFallback(image);
  assert.equal(image.onerror, null);
  assert.equal(image.hidden, true);
  assert.equal(children.length, 1);
  assert.equal(children[0].textContent, "ET");
});

test("a failed portrait reveals its existing initials instead of duplicating them", () => {
  const { app } = boot();
  const placeholder = {
    hidden: true,
    classList: { contains: (name) => name === "mono" },
    setAttribute() {},
  };
  const { image, children } = portrait({ placeholder });
  app.imgFallback(image);
  assert.equal(placeholder.hidden, false);
  assert.equal(image.hidden, true);
  assert.equal(image.onerror, null);
  assert.equal(children.length, 0);
});

test("blocked preference storage does not prevent page initialization or image recovery", () => {
  const { app, attributes, warnings } = boot(() => {
    throw new Error("Storage blocked");
  });
  assert.equal(attributes.get("data-theme"), "dark");
  assert.equal(warnings.length, 2);
  const { image, children } = portrait();
  app.imgFallback(image);
  assert.equal(children[0].textContent, "ET");
});
