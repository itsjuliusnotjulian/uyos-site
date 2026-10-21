"""Builds uyos.io: python3 build.py  ->  writes the .html files next to it (GitHub Pages serves them).
Each page is (file, title, description, body); the header and footer are shared."""
import sys
from pathlib import Path

# Stale since 2026-10-20: the published pages were edited by hand (Terms, Privacy, gender-neutral wording) and this
# script would overwrite them with old text. Edit the .html files directly.
sys.exit("build.py is out of date: edit the .html files directly (running it would undo published changes).")

ROOT = Path(__file__).parent
EMAIL = "hello@uyos.io"
UPDATED = "October 17, 2026"

NAV = [("index.html", "Home"), ("anamnesis.html", "Anamnesis"), ("support.html", "Support")]
WHERE = "Washington State, USA"

# Simple line icons (24×24, stroke = currentColor).
def icon(paths):
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true">{paths}</svg>')

ICON = {
    "lock": icon('<rect x="4" y="10" width="16" height="11" rx="2.5"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/>'),
    "heart": icon('<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>'),
    "mail": icon('<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="m4 7 8 6 8-6"/>'),
    "text": icon('<path d="M4 7V5h11v2M9.5 5v14M7 19h5"/><path d="M14 12v-1.5h6V12M17 10.5V19M15.5 19h3"/>'),
    "mic": icon('<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/>'),
    "photo": icon('<rect x="3" y="5" width="18" height="14" rx="2.5"/><circle cx="9" cy="10" r="2"/><path d="m21 16-5-5-9 8"/>'),
    "play": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5.5v13a1 1 0 0 0 1.5.86l11-6.5a1 1 0 0 0 0-1.72l-11-6.5A1 1 0 0 0 8 5.5z"/></svg>',
}


def device(src, alt, cls="", lazy=True):
    load = ' loading="lazy"' if lazy else ""
    return f'<div class="device {cls}"><img src="{src}" alt="{alt}"{load}></div>'


QUESTIONS = ['What did Sunday mornings look like when you were a girl?', "What song was playing during a moment you'll never forget?", "What's a smell that instantly brings back a memory?", "What's something one of your parents always used to say?", 'What was your wedding day like?', "What's the best advice anyone ever gave you?", "What's a tradition your family had that you loved?", "What's a word from back home that you still use?", 'What work are you most proud of in your life?', 'Who taught you to cook?']


def ribbon():
    items = "".join(f"<span>{q}</span>" for q in QUESTIONS)
    return f'<div class="ribbon" aria-hidden="true"><div class="track">{items}{items}</div></div>'


def page(file, title, description, body, nav_current=None):
    nav = "".join(f'<a href="{href}"{" aria-current=\"page\"" if href == (nav_current or file) else ""}>{label}</a>'
                  for href, label in NAV if href != "index.html")
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#090d10">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<link rel="icon" href="img/favicon.png">
<link rel="preload" href="fonts/fraunces-latin-full-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="style.css">
<script src="site.js" defer></script>
</head>
<body>
<header class="glass">
  <a class="mark" href="index.html"><i></i>Uyos</a>
  <nav aria-label="Main">{nav}<a class="cta" href="mailto:{EMAIL}">Contact</a></nav>
</header>
<main>
{body}
</main>
<footer class="foot">
  <div class="cols">
    <div class="brand"><p class="label" style="color:var(--accent)">Uyos</p>
      <p style="margin-top:12px;max-width:24em;color:var(--on-dark)">Apps for the people we love. An independent studio in {WHERE}.</p></div>
    <div><h4>Apps</h4><nav><a href="anamnesis.html">Anamnesis</a>
      <a class="arrow" href="https://www.youtube.com/channel/UCwXGdEm0_i_grfxJ1KwvSEw">AuraDeepDive</a></nav></div>
    <div><h4>Help</h4><nav><a href="support.html">Support</a><a href="privacy.html">Privacy</a><a href="terms.html">Terms</a>
      <a href="mailto:{EMAIL}">{EMAIL}</a></nav></div>
  </div>
  <p class="fine">© 2026 Uyos · {WHERE}</p>
  <div class="wordmark" aria-hidden="true">Uyos</div>
</footer>
</body>
</html>
"""
    (ROOT / file).write_text(html)


def doc_band(title, sub=""):
    return f"""<div class="tiles" style="padding-bottom:0"><section class="doc-head">
  <h1>{title}</h1>{sub}
</section></div>"""


INDEX = f"""
<div class="tiles">
  <section class="tile hero-tile">
    <div class="glow" style="width:60vmax;height:60vmax;left:50%;top:40%;transform:translateX(-50%);background:#2340d6;opacity:.35"></div>
    <p class="tag">New · Anamnesis</p>
    <h1>Anamnesis</h1>
    <p class="purpose">Reliving our life's journey.</p>
    <p class="sub">One question a day. Answered in her own voice. Kept as a book the family can hear forever.</p>
    <div class="links"><a class="btn gold" href="anamnesis.html">Learn more</a><a class="more" href="mailto:{EMAIL}?subject=Anamnesis%20testing">Ask to try it</a></div>
    <div class="rise">
      {device("img/anamnesis-onboard.jpg", "", "side", False)}
      {device("img/anamnesis-today.jpg", "Anamnesis: today's question, with one big button to answer", "", False)}
      {device("img/anamnesis-book.jpg", "", "side", False)}
    </div>
    <p class="corner l">An app by Uyos<br>Washington State, 2026</p>
    <p class="corner r">iPhone · in testing</p>
  </section>

  {ribbon()}

  <div class="grid2">
    <section class="tile reveal" style="background:radial-gradient(90% 70% at 50% 90%, #6d4fb0 0%, #2a1f4d 55%, #120d22 100%)">
      <span class="idx">02</span>
      <p class="tag" style="color:#e7b4ff">Coming to iPhone</p>
      <h2>Daily Catechism</h2>
      <p class="sub">One teaching a day. A verse to hear. A place on the map. Then it ends.</p>
      <div class="art"><span class="cross">✛</span></div>
    </section>
    <section class="tile reveal" style="background:radial-gradient(90% 70% at 50% 90%, #e2672a 0%, #5a1f0c 60%, #1a0904 100%)">
      <span class="idx">03</span>
      <p class="tag" style="color:#ffc29a">Coming to iPhone</p>
      <h2>Fitness coach</h2>
      <p class="sub">Coaching from your own Apple Health data. Streaks that reward showing up.</p>
      <div class="art"><svg class="rings" viewBox="0 0 200 200" aria-hidden="true">
        <circle class="bg" cx="100" cy="100" r="86"/><circle class="fg" cx="100" cy="100" r="86" style="stroke:#ff6b2c;--to:300"/>
        <circle class="bg" cx="100" cy="100" r="64"/><circle class="fg" cx="100" cy="100" r="64" style="stroke:#ffc23d;--to:420"/>
        <circle class="bg" cx="100" cy="100" r="42"/><circle class="fg" cx="100" cy="100" r="42" style="stroke:#7de3c8;--to:560"/></svg></div>
    </section>
    <section class="tile reveal" style="grid-column:1/-1">
      <span class="idx">04</span>
      <p class="tag" style="color:#e85fa5">On YouTube</p>
      <h2>AuraDeepDive</h2>
      <p class="sub">How trends rise, peak and get monetized. In under a minute, with dated sources.</p>
      <div class="links"><a class="more arrow" href="https://www.youtube.com/channel/UCwXGdEm0_i_grfxJ1KwvSEw" style="color:#e85fa5">Watch</a></div>
      <div class="art"><svg class="trend" viewBox="0 0 600 260" aria-hidden="true">
        <defs><linearGradient id="tg" x1="0" x2="1"><stop offset="0" stop-color="#2340d6"/><stop offset=".5" stop-color="#e85fa5"/><stop offset="1" stop-color="#e5432d"/></linearGradient>
        <linearGradient id="ta" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e85fa5" stop-opacity=".35"/><stop offset="1" stop-color="#e85fa5" stop-opacity="0"/></linearGradient></defs>
        <path class="area" d="M10 230 C 120 225, 180 200, 230 140 S 280 46, 300 46 S 340 90, 380 150 S 480 190, 590 196 L 590 250 L 10 250 Z"/>
        <path class="line" d="M10 230 C 120 225, 180 200, 230 140 S 280 46, 300 46 S 340 90, 380 150 S 480 190, 590 196"/>
        <circle class="ring" cx="300" cy="46" r="10"/><circle class="peak" cx="300" cy="46" r="7"/>
        <text x="20" y="252">RISE</text><text x="282" y="24">PEAK</text><text x="520" y="180">AFTER</text></svg></div>
    </section>
  </div>
</div>

<section class="statement reveal">
  <p class="label" style="color:var(--sea-ink)">How we work</p>
  <p class="big"><span class="dim">No ads. No selling. No tracking.</span> <span class="lit">Just what you make, on your own phone.</span></p>
  <p class="muted" style="font-size:20px;max-width:32em">Every app starts with someone we know, and doesn't ship until it works for them. Write to <a href="mailto:{EMAIL}">{EMAIL}</a> and Julius, who runs Uyos, reads it himself.</p>
</section>
"""

STEPS = [
    ("img/anamnesis-onboard.jpg", "Welcome screen", "One", "A gentle start.",
     "She picks what she loves, puts her picture on the front of her book and chooses when she'd like her question. Every step is spoken aloud."),
    ("img/anamnesis-today.jpg", "Today's question", "Two", "One question a day.",
     "Chosen from what she loves, never the same one twice. One big button to answer, and “Another” if today's isn't right."),
    ("img/anamnesis-record.jpg", "Recording a story", "Three", "She just talks.",
     "Her words appear as she speaks. She can pause as long as she likes; the app waits. One button when she's done."),
    ("img/anamnesis-book.jpg", "Her book of stories", "Four", "Her book grows.",
     "Every story becomes a page, by month, with her voice a tap away. Old photos get their stories told, too."),
]
STORY_STEPS = "".join(
    f'<div data-step="{i}"><span class="num">{n}</span><h3>{h}</h3><p>{p}</p>{device(src, alt, "inline")}</div>'
    for i, (src, alt, n, h, p) in enumerate(STEPS))
STORY_SCREENS = "".join(f'<img src="{src}" alt="{alt}"{" class=\"on\"" if i == 0 else ""}>' for i, (src, alt, *_r) in enumerate(STEPS))

ANAMNESIS = f"""
<div class="tiles">
  <section class="tile hero-tile">
    <div class="glow" style="width:55vmax;height:55vmax;left:50%;top:45%;transform:translateX(-50%);background:#2340d6;opacity:.35"></div>
    <img src="img/anamnesis-icon.png" alt="Anamnesis app icon" style="width:84px;height:84px;border-radius:20px;box-shadow:0 18px 40px rgba(0,0,0,.4)">
    <h1>Her stories.<br><em>In her voice.</em></h1>
    <p class="sub">Every day, Anamnesis asks one question about her life, read aloud in a warm voice. She answers by talking. Her family keeps every word.</p>
    <div class="links"><a class="btn gold" href="mailto:{EMAIL}?subject=Anamnesis%20testing">Ask to try it</a><a class="more" href="#how">See how it works</a></div>
    <div class="rise one">{device("img/anamnesis-today.jpg", "Anamnesis: today's question", "float", False)}</div>
    <p class="corner l">Anamnesis<br>Reliving our life's journey</p>
    <p class="corner r">iPhone · in testing<br>Works without internet</p>
  </section>

  <section class="tile voice" style="background:#2340d6">
    <p class="label" style="color:#fff;opacity:.75">Hear the voice of Anamnesis</p>
    <button type="button" class="playbtn" data-play="audio/question.mp3" aria-label="Play the voice of Anamnesis">{ICON["play"]}</button>
    <q>What do you hope your grandchildren will always know about our family?</q>
    <div class="wave" aria-hidden="true">{"<i></i>" * 24}</div>
  </section>

  {ribbon()}
</div>

<div class="wrap" id="how">
  <div class="sec-title reveal"><p class="eyebrow">How it works</p><h2>Five minutes a day.<br><em style="color:var(--gold-ink)">A book for a lifetime.</em></h2></div>
  <div class="story">
    <div class="steps">{STORY_STEPS}</div>
    <div class="pin"><div class="device">{STORY_SCREENS}</div></div>
  </div>
</div>

<div class="wrap">
  <div class="sec-title reveal"><p class="eyebrow">Made for grandparents</p><h2>Simple enough for anyone.</h2></div>
  <div class="bento reveal">
    <div class="b4 dark"><span class="idx">01</span><h3>Big type. Big buttons.<br>One thing per screen.</h3><p>And every step read aloud, so nothing has to be squinted at.</p><div class="huge gold">Aa</div></div>
    <div class="b2 goldt"><span class="idx">02</span><h3>Works anywhere.</h3><p>No internet needed. The voice is built into the app.</p><div class="huge" style="color:var(--gold-ink);font-size:110px">∞</div></div>
    <div class="b2"><span class="idx">03</span><h3>Her voice, kept.</h3><p>The recording itself is saved, not just the words.</p>
      <div class="wave playing" style="margin-top:auto;height:60px" aria-hidden="true">{"<i style='background:var(--sea-ink)'></i>" * 18}</div></div>
    <div class="b4"><span class="idx">04</span><h3>Photos with stories.</h3><p>Pick an old photo and tell the story behind it. The two stay together.</p>
      <div class="polaroids" aria-hidden="true"><div>The garden, 1981</div><div>Our wedding</div><div>Sunday lunch</div></div></div>
    <div class="b3"><span class="idx">05</span><h3>Private by design.</h3><p>Stories stay on her phone. No ads, no accounts, no selling. <a href="privacy.html#anamnesis">Details</a>.</p><div class="huge" style="color:var(--sea-ink);font-size:120px">{ICON["lock"].replace('<svg ', '<svg width="110" height="110" ')}</div></div>
    <div class="b3 dark"><span class="idx">06</span><h3>Questions chosen<br>from what she loves.</h3><p>Cooking, faith, family, music, gardening. Never the same one twice.</p><div class="huge gold">59</div></div>
  </div>
</div>

<div class="wrap">
  <div class="sec-title reveal"><p class="eyebrow">Questions</p><h2>Good to know</h2></div>
  <div class="faq reveal">
    <details><summary>Does it need the internet?</summary><p>No. The voice is built into the app and her words are written down on the iPhone itself, so it works anywhere.</p></details>
    <details><summary>Who can hear the stories?</summary><p>Only whoever holds the phone. Sharing with family is coming, and will be off unless the family sets it up.</p></details>
    <details><summary>What if she'd rather type?</summary><p>Every question can be answered in writing, too.</p></details>
    <details><summary>How do we get it?</summary><p>Anamnesis is in private testing on iPhone. <a href="mailto:{EMAIL}?subject=Anamnesis%20testing">Write to us</a> to join.</p></details>
  </div>
</div>

<div class="tiles" style="padding-top:70px">
  <section class="callbox reveal">
    <h2>Give someone you love a place for <em>their stories.</em></h2>
    <p>Anamnesis is in private testing. Tell us who it's for and we'll send an invitation.</p>
    <a class="btn gold" href="mailto:{EMAIL}?subject=Anamnesis%20testing">Ask to try Anamnesis</a>
  </section>
</div>
"""

PUBLISHING = f"""
{doc_band("AuraDeepDive publishing", '<p class="lede">Uyos publishes the AuraDeepDive YouTube channel using a private publishing tool that runs on Uyos\'s own computer. It is used only by Uyos, for its own channel, and is not offered to the public.</p>')}
<section class="wrap narrow doc">
  <h2>What the tool does with YouTube</h2>
  <p>With the channel owner's permission, given once through Google's sign-in, the tool:</p>
  <ul class="muted">
    <li>uploads videos that Uyos made to the AuraDeepDive channel, as private or scheduled until a person approves them;</li>
    <li>sets each video's title, description, thumbnail and playlists;</li>
    <li>reads the channel's own analytics and comments, so Uyos can see what's working and reply.</li>
  </ul>
  <p>It acts only on Uyos's own channel. It does not access anyone else's YouTube account, and it never makes a video public without a person's approval.</p>
  <p class="callout">This tool uses YouTube API Services. By using it you agree to the <a href="https://www.youtube.com/t/terms">YouTube Terms of Service</a>, and Google's handling of data is described in the <a href="https://policies.google.com/privacy">Google Privacy Policy</a>. How the tool handles the data it receives is in our <a href="privacy.html#youtube">privacy policy</a>.</p>
</section>
"""

PRIVACY = f"""
{doc_band("Privacy", f'<p class="updated">Last updated {UPDATED}</p><div class="toc"><a href="#anamnesis">Anamnesis</a><a href="#youtube">YouTube and Google data</a><a href="#website">This website</a></div>')}
<article class="wrap narrow doc">
  <p class="callout">Short version: our apps keep what you make on your own device. We don't sell data, show ads or track you across apps and websites. If something here is unclear, write to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

  <h2 id="anamnesis">Anamnesis</h2>
  <ul>
    <li><b>What it keeps:</b> your name, the interests you pick, an optional photo of yourself, your answers (voice recordings, the words written down from them, and anything you type), photos you choose to tell stories about, and your reminder time.</li>
    <li><b>Where:</b> on your iPhone, inside the app. We don't receive any of it.</li>
    <li><b>Speech to text:</b> your words are written down using Apple's speech recognition on the iPhone itself where your iPhone supports it. Where it doesn't, Apple may process the audio; see Apple's privacy policy.</li>
    <li><b>Microphone and photos:</b> the microphone is used only while you are telling a story; photos are read only when you pick one.</li>
    <li><b>Family sharing (if you turn it on later):</b> your stories can be copied to your family's own private server so they can listen too. It's off unless your family sets it up, and it's never shared with anyone else.</li>
    <li><b>Deleting:</b> delete a story in the app, or delete the app to remove everything.</li>
    <li><b>Children:</b> Anamnesis is meant for adults and isn't directed at children under 13.</li>
  </ul>

  <h2 id="youtube">AuraDeepDive publishing and Google user data</h2>
  <p>Uyos uses a private publishing tool for its own AuraDeepDive channel (<a href="publishing.html">what it is</a>). When the channel owner signs in with Google, the tool receives permission to manage that channel's videos and to read its analytics and comments.</p>
  <ul>
    <li><b>What it accesses:</b> the signed-in channel's videos, playlists, thumbnails, comments and analytics, through the YouTube Data API and YouTube Analytics API.</li>
    <li><b>How it's used:</b> only to upload and manage Uyos's own videos and to report on the channel's performance to Uyos. Nothing else.</li>
    <li><b>Storage:</b> the sign-in token is kept in a file only the tool's user account can read, on Uyos's own computer, whose disk is encrypted. Channel data is used to answer a request and is not kept beyond Uyos's own records of its videos.</li>
    <li><b>Sharing:</b> Google user data is never sold, never used for advertising, never shared with third parties and never used to train AI models.</li>
    <li><b>Limited Use:</b> the tool's use and transfer of information received from Google APIs adheres to the <a href="https://developers.google.com/terms/api-services-user-data-policy">Google API Services User Data Policy</a>, including the Limited Use requirements.</li>
    <li><b>Revoking access:</b> remove the tool's access at any time at <a href="https://myaccount.google.com/permissions">myaccount.google.com/permissions</a>; the stored token stops working immediately. To have it deleted too, write to <a href="mailto:{EMAIL}">{EMAIL}</a>.</li>
    <li>The tool uses YouTube API Services; see the <a href="https://www.youtube.com/t/terms">YouTube Terms of Service</a> and the <a href="https://policies.google.com/privacy">Google Privacy Policy</a>.</li>
  </ul>

  <h2 id="website">This website</h2>
  <p>uyos.io sets no cookies, runs no analytics and loads nothing from other companies. It is hosted on GitHub Pages, whose servers, like any web server, see your IP address when you visit.</p>

  <h2>Changes and contact</h2>
  <p>If this policy changes, we'll update the date above. Questions or requests: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
  <p>Uyos is an independent studio run by its founder, Julius, in {WHERE}.</p>
</article>
"""

TERMS = f"""
{doc_band("Terms", f'<p class="updated">Last updated {UPDATED}</p>')}
<article class="wrap narrow doc">
  <p>These terms cover Uyos's apps and this website.</p>
  <h2>Using our apps</h2>
  <ul>
    <li>What you create in our apps (your stories, recordings, photos and notes) is yours.</li>
    <li>Use the apps lawfully and don't record people without their consent.</li>
    <li>Apps in testing may change or have bugs. Keep copies of anything you can't bear to lose; we'll help if something goes wrong.</li>
  </ul>
  <h2>No warranty</h2>
  <p>The apps are provided as they are, without warranties. To the extent the law allows, Uyos isn't liable for indirect or consequential losses from using them.</p>
  <h2>YouTube</h2>
  <p>Where Uyos software uses YouTube API Services, the <a href="https://www.youtube.com/t/terms">YouTube Terms of Service</a> apply.</p>
  <h2>Contact</h2>
  <p><a href="mailto:{EMAIL}">{EMAIL}</a> · Uyos, run by its founder, Julius, in {WHERE}. These terms are governed by the laws of the State of Washington.</p>
</article>
"""

SUPPORT = f"""
{doc_band("Support", f'<p class="lede">A real person answers. Write to <a href="mailto:{EMAIL}">{EMAIL}</a> and we\'ll reply, usually within a day.</p>')}
<article class="wrap narrow doc">
  <h2>Anamnesis</h2>
  <ul>
    <li><b>It doesn't hear me:</b> on the iPhone, open Settings → Anamnesis and turn on Microphone and Speech Recognition.</li>
    <li><b>No daily reminder:</b> Settings → Notifications → Anamnesis → Allow Notifications.</li>
    <li><b>Listening to a story:</b> open My Book and tap the page.</li>
    <li><b>Something else:</b> write to us with what happened and, if you can, a screenshot.</li>
  </ul>
  <h2>Privacy requests</h2>
  <p>See our <a href="privacy.html">privacy policy</a>, or write to the address above.</p>
</article>
"""

if __name__ == "__main__":
    page("index.html", "Uyos", "Uyos makes calm, useful apps and stories worth keeping.", INDEX)
    page("anamnesis.html", "Anamnesis", "Anamnesis: reliving our life's journey. One question a day, answered in your own voice.", ANAMNESIS)
    page("publishing.html", "AuraDeepDive publishing", "How Uyos publishes its AuraDeepDive YouTube channel, and what the publishing tool does with YouTube data.", PUBLISHING, "support.html")
    page("privacy.html", "Privacy", "Uyos privacy policy: Anamnesis, AuraDeepDive publishing and Google user data.", PRIVACY, "privacy.html")
    page("terms.html", "Terms", "Uyos terms of use.", TERMS, "terms.html")
    page("support.html", "Support", "Help with Uyos apps.", SUPPORT)
    (ROOT / "CNAME").write_text("uyos.io\n")
    print("built")
