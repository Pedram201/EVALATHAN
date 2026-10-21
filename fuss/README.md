<p align="center">
  <img src="fuss-logo.png" alt="FUSS logo: an older woman with round glasses" width="280">
</p>

<h1 align="center">F U S S</h1>

FUSS (For-User Session Switch) is a timer a person can turn on inside software they use for a long time. It is not an agent, not medical advice, and not a lock.

The panel is a small card. The FUSS logo sits in the center. The first question is whether to use it. If yes, the person sets the sitting length, how often the reminder appears, which days it runs, and an optional end date. They can also ask the screen to cover itself for a ten-minute break.

## Drop it into a web page

Copy this `fuss` folder next to your pages. The folder holds `fuss.js`, `fuss-logo.png`, and this readme. Before `</body>`:

```html
<script src="fuss/fuss.js"></script>
```

That is the whole install for a site or a web app. It runs in current browsers on Windows and Mac. The same files run on Linux. There is no separate Mac build and no separate Windows build.

## Drop it into a desktop app

If the software is not a web page, show this folder in a web view: WebView2 on Windows, WKWebView on Mac. Point the view at `fuss/index.html`. The timer is the same file either way.

## What gets remembered

The choices stay in the browser's local storage on that computer. A person can press **Not now**. A small **FUSS** button remains so they can open it later.

A developer who wants a starting setup for every install can leave the defaults in the script: 25 minutes a sitting, a reminder every 15 minutes, all days, no end date. Each person still has to tick the box and press **Use FUSS**. FUSS does not start a timer for someone who said no.

## What Menschly looks for

Menschly, the Evalathan evaler for a real stop, treats `function bindFuss` in `fuss.js` as a timer in the source. A sentence in a README is not a timer.
