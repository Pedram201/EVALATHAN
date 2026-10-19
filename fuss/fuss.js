/* FUSS (For-User Session Switch). One folder, any web page, Windows or Mac. */
(function () {
  var KEY = "fuss.settings.v1";
  var tick = null;

  function base() {
    var script = document.currentScript;
    if (!script || !script.src) return "";
    return script.src.replace(/[^/]+$/, "");
  }

  function read() {
    try {
      return JSON.parse(localStorage.getItem(KEY) || "{}");
    } catch (e) {
      return {};
    }
  }

  function write(state) {
    localStorage.setItem(KEY, JSON.stringify(state));
  }

  function todayName() {
    return ["sun", "mon", "tue", "wed", "thu", "fri", "sat"][new Date().getDay()];
  }

  function allowedToday(state) {
    if (!state.days || !state.days.length) return true;
    return state.days.indexOf(todayName()) !== -1;
  }

  function beforeUntil(state) {
    if (!state.until) return true;
    var end = new Date(state.until + "T23:59:59");
    return Date.now() <= end.getTime();
  }

  function remaining(state) {
    var mins = Number(state.minutes || 25);
    if (!state.started) return mins;
    var elapsed = (Date.now() - state.started) / 60000;
    return Math.max(0, mins - elapsed);
  }

  function el(tag, attrs, text) {
    var node = document.createElement(tag);
    if (attrs) {
      Object.keys(attrs).forEach(function (key) {
        if (key === "class") node.className = attrs[key];
        else node.setAttribute(key, attrs[key]);
      });
    }
    if (text) node.textContent = text;
    return node;
  }

  function ensureStyle() {
    if (document.getElementById("fuss-style")) return;
    var style = el("style", { id: "fuss-style" });
    style.textContent = [
      ".fuss-card{position:fixed;z-index:2147483000;right:16px;bottom:16px;width:min(340px,calc(100vw - 24px));background:#fffaf3;color:#1c140c;border:1px solid #e4d3bf;border-radius:12px;box-shadow:0 10px 30px rgba(28,20,12,.18);font:15px/1.4 Calibri,Segoe UI,sans-serif;padding:16px}",
      ".fuss-card img{display:block;width:96px;height:96px;object-fit:contain;margin:0 auto 8px}",
      ".fuss-card h2{margin:0 0 8px;text-align:center;font-size:18px}",
      ".fuss-card p{margin:0 0 8px}",
      ".fuss-card label{display:block;margin:8px 0;font-size:14px}",
      ".fuss-row{display:flex;gap:8px;flex-wrap:wrap;margin-top:8px}",
      ".fuss-card button{font:inherit;border:0;border-radius:8px;padding:8px 12px;background:#c45c26;color:#fff;cursor:pointer}",
      ".fuss-card button.fuss-quiet{background:#efe6da;color:#1c140c}",
      ".fuss-days{display:flex;gap:6px;flex-wrap:wrap}",
      ".fuss-days label{display:flex;gap:4px;align-items:center}",
      ".fuss-toast{position:fixed;z-index:2147483001;left:50%;top:16px;transform:translateX(-50%);width:min(420px,calc(100vw - 24px));background:#1c140c;color:#fffaf3;border-radius:12px;padding:14px;font:15px/1.4 Calibri,Segoe UI,sans-serif}",
      ".fuss-cover{position:fixed;inset:0;z-index:2147483002;background:rgba(28,20,12,.92);color:#fffaf3;display:flex;align-items:center;justify-content:center;text-align:center;padding:24px;font:18px/1.45 Calibri,Segoe UI,sans-serif}",
      ".fuss-launcher{position:fixed;z-index:2147482999;right:16px;bottom:16px;border:0;border-radius:999px;padding:8px 12px;background:#c45c26;color:#fff;font:14px Calibri,Segoe UI,sans-serif;cursor:pointer}"
    ].join("");
    document.head.appendChild(style);
  }

  function showToast(text, actions) {
    var old = document.getElementById("fuss-toast");
    if (old) old.remove();
    var box = el("div", { id: "fuss-toast", class: "fuss-toast" });
    box.appendChild(el("p", null, text));
    if (actions) box.appendChild(actions);
    document.body.appendChild(box);
  }

  function coverFor(ms) {
    var box = el("div", { class: "fuss-cover" });
    var msg = el("p");
    box.appendChild(msg);
    document.body.appendChild(box);
    var until = Date.now() + ms;
    var step = function () {
      var left = Math.max(0, Math.ceil((until - Date.now()) / 1000));
      msg.textContent = "Ten-minute break. " + left + " seconds left. Stand up. FUSS is a timer, not medical advice.";
      if (left <= 0) {
        box.remove();
        var state = read();
        state.on = false;
        state.started = 0;
        write(state);
        return;
      }
      setTimeout(step, 1000);
    };
    step();
  }

  function arm() {
    if (tick) clearInterval(tick);
    tick = setInterval(function () {
      var state = read();
      if (!state.on || !state.started || !allowedToday(state) || !beforeUntil(state)) return;
      var left = remaining(state);
      var every = Number(state.remindEvery || 15);
      var elapsed = (Date.now() - state.started) / 60000;
      var bucket = Math.floor(elapsed / every);
      if (bucket > 0 && bucket !== state.lastPing) {
        state.lastPing = bucket;
        write(state);
        var row = el("div", { class: "fuss-row" });
        var take = el("button", null, "Take a break");
        var keep = el("button", { class: "fuss-quiet" }, "Keep working");
        row.appendChild(take);
        row.appendChild(keep);
        showToast("About " + Math.round(left) + " minutes left on this sitting.", row);
        take.addEventListener("click", function () {
          var live = read();
          document.getElementById("fuss-toast").remove();
          if (live.cover) coverFor(10 * 60 * 1000);
          live.on = false;
          write(live);
        });
        keep.addEventListener("click", function () {
          var node = document.getElementById("fuss-toast");
          if (node) node.remove();
        });
      }
      if (left <= 0) {
        state.on = false;
        write(state);
        if (state.cover) coverFor(10 * 60 * 1000);
        else showToast("Your sitting ended. Look away and say the point in your own words.");
      }
    }, 15000);
  }

  function field(label, input) {
    var row = el("label");
    row.appendChild(document.createTextNode(label + " "));
    row.appendChild(input);
    return row;
  }

  function openPanel() {
    var old = document.getElementById("fuss-card");
    if (old) old.remove();
    var launcher = document.getElementById("fuss-launcher");
    if (launcher) launcher.remove();
    ensureStyle();
    var state = read();
    var card = el("div", { id: "fuss-card", class: "fuss-card", role: "dialog", "aria-label": "FUSS timer" });
    var img = el("img", { src: base() + "fuss-logo.png", alt: "FUSS logo: an older woman with round glasses" });
    card.appendChild(img);
    card.appendChild(el("h2", null, "FUSS"));
    card.appendChild(el("p", null, "I'm FUSS. I can help you time your use of this software, so a long sitting does not become a rabbit hole or a sore wrist."));
    var ack = el("input", { type: "checkbox", id: "fuss-ack" });
    if (state.ack) ack.checked = true;
    card.appendChild(field("I understand this is only a timer. It is not medical advice, not a diagnosis, and not a replacement for a workplace rule.", ack));
    var mins = el("input", { type: "number", id: "fuss-mins", min: "5", max: "180", value: String(state.minutes || 25) });
    var every = el("input", { type: "number", id: "fuss-every", min: "5", max: "60", value: String(state.remindEvery || 15) });
    var until = el("input", { type: "date", id: "fuss-until", value: state.until || "" });
    card.appendChild(field("Minutes in one sitting", mins));
    card.appendChild(field("Remind me every (minutes)", every));
    card.appendChild(field("Use this until (optional date)", until));
    var daysWrap = el("div", { class: "fuss-days" });
    ["mon", "tue", "wed", "thu", "fri", "sat", "sun"].forEach(function (day) {
      var box = el("input", { type: "checkbox", value: day });
      if (!state.days || state.days.indexOf(day) !== -1) box.checked = true;
      var lab = el("label");
      lab.appendChild(box);
      lab.appendChild(document.createTextNode(day));
      daysWrap.appendChild(lab);
    });
    card.appendChild(el("p", null, "Days this reminder is allowed"));
    card.appendChild(daysWrap);
    var cover = el("input", { type: "checkbox", id: "fuss-cover" });
    if (state.cover) cover.checked = true;
    card.appendChild(field("Cover the screen for a 10-minute break when I accept one.", cover));
    var row = el("div", { class: "fuss-row" });
    var start = el("button", { type: "button", id: "fuss-on" }, "Use FUSS");
    var stop = el("button", { type: "button", id: "fuss-off", class: "fuss-quiet" }, "Not now");
    row.appendChild(start);
    row.appendChild(stop);
    card.appendChild(row);
    var status = el("p", { id: "fuss-status" });
    status.textContent = state.on ? "Timer on." : "Timer off.";
    card.appendChild(status);
    document.body.appendChild(card);

    function chosenDays() {
      return Array.prototype.map.call(daysWrap.querySelectorAll("input:checked"), function (node) {
        return node.value;
      });
    }

    start.addEventListener("click", function () {
      if (!ack.checked) {
        status.textContent = "Tick the box first. FUSS is a timer, not a medical tool.";
        return;
      }
      var next = {
        ack: true,
        on: true,
        minutes: Math.min(180, Math.max(5, Number(mins.value || 25))),
        remindEvery: Math.min(60, Math.max(5, Number(every.value || 15))),
        until: until.value || "",
        days: chosenDays(),
        cover: cover.checked,
        started: Date.now(),
        lastPing: 0,
        dismissed: false
      };
      write(next);
      card.remove();
      launcherButton();
      arm();
    });
    stop.addEventListener("click", function () {
      var next = read();
      next.on = false;
      next.started = 0;
      next.dismissed = true;
      next.ack = ack.checked;
      write(next);
      card.remove();
      launcherButton();
    });
  }

  function launcherButton() {
    if (document.getElementById("fuss-launcher") || document.getElementById("fuss-card")) return;
    ensureStyle();
    var button = el("button", { id: "fuss-launcher", class: "fuss-launcher", type: "button" }, "FUSS");
    button.addEventListener("click", openPanel);
    document.body.appendChild(button);
  }

  function bindFuss(root) {
    if (root) openPanel();
  }

  function boot() {
    var state = read();
    if (state.on && allowedToday(state) && beforeUntil(state)) arm();
    if (!state.dismissed && !state.on) openPanel();
    else launcherButton();
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();

  window.bindFuss = bindFuss;
})();
