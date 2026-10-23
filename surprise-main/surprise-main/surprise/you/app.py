import json
from pathlib import Path
import streamlit as st

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"
PHOTOS, MUSIC, VIDEO = ASSETS / "photos", ASSETS / "music", ASSETS / "video"
st.set_page_config(page_title="For You, Always", page_icon="♡", layout="wide", initial_sidebar_state="collapsed")

DEFAULT = {
 "his_name":"My Favorite Person","site_title":"For You, Always",
 "subtitle":"A soft place to land, whenever the world feels heavy.",
 "opening_note":"You don't have to be okay every minute. You don't have to have all the answers today. I just want you to remember that you matter, you are loved, and you don't have to carry everything alone.",
 "letter_title":"A little note for your heart",
 "love_letter":"Hey love,\\n\\nI know things may feel heavier than usual right now. I wish I could take every worry from your mind and replace it with peace, but I know I can't fix everything with words. So here's what I can promise: you don't have to pretend with me. You can have quiet days, confused days, tired days, and days when you don't know what to say. You are still worthy of love on every single one of them.\\n\\nI believe in the person you are, even when you find it hard to believe in yourself. Please take things one step at a time. Rest when you need to, celebrate the tiny wins, and remember that a difficult chapter is not the whole story. I am proud of you for making it through days nobody else fully sees.\\n\\nI may not always have the perfect advice, but I can listen, cheer for you, remind you to eat, make you laugh, or simply sit beside you. You don't have to earn my care by being strong all the time.\\n\\nI'm here for the real you—not just the happiest version. One day at a time, okay? You mean so much to me. ♡",
 "memories":[{"title":"The way we laugh","text":"The small, silly moments that somehow become the memories we keep closest."},{"title":"Our little world","text":"The looks, jokes, and tiny traditions that only make sense to us."},{"title":"The ordinary days","text":"Not every beautiful memory is a big event. Sometimes it's just being near you."}],
 "reminders":[{"title":"You are allowed to rest.","text":"Pausing is not failing. You are a human being, not a machine."},{"title":"You don't need to solve everything tonight.","text":"Choose the next small step. The rest can wait until you're ready."},{"title":"Your worth isn't measured by one hard season.","text":"A difficult day, mistake, or setback doesn't define your whole life."},{"title":"You can tell me the truth.","text":"You don't need to pretend you're fine just to protect me from your feelings."},{"title":"Tiny progress still counts.","text":"Getting through today can be enough. I am cheering for you."},{"title":"You deserve good things, too.","text":"Please don't forget to leave room for joy, kindness, and hope."}],
 "reasons":["The way you make me laugh without even trying.","Your heart, even when you are too hard on yourself.","The effort you put in, even when nobody notices.","The little things you remember.","The way being around you can make an ordinary day special.","Your dreams and the person you are becoming.","Your honesty and your realness.","The comfort of being able to be myself with you.","Your resilience, even when you don't feel strong.","Simply because you are you—not because you have to prove anything."],
 "song_caption":"If words aren't enough, let this song say a little more.",
 "final_message":"You don't have to shine every day. Even the moon has phases. I'll be cheering for you through all of yours.",
 "sign_off":"Always in your corner ♡"
}
try:
    with open(ROOT / "content.json", encoding="utf-8") as f:
        content = {**DEFAULT, **json.load(f)}
except Exception:
    content = DEFAULT

def txt(x):
    return str(x)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap');
.stApp{background:radial-gradient(ellipse at 12% 0%,#44253f 0%,#251729 38%,#17131f 100%);color:#f5edf4}
.block-container{max-width:1080px;padding-top:1.8rem;padding-bottom:4rem}
h1,h2,h3{font-family:'Playfair Display',Georgia,serif!important;color:#fff1f7}
p,li,div{font-family:'DM Sans',Arial,sans-serif}
.hero{text-align:center;padding:3.4rem 1.2rem 3rem;border:1px solid rgba(216,189,138,.35);border-radius:28px;background:linear-gradient(135deg,rgba(70,39,66,.78),rgba(38,28,49,.85));box-shadow:0 24px 70px rgba(0,0,0,.22)}
.eyebrow,.kicker{text-transform:uppercase;letter-spacing:.2em;font-size:.72rem;font-weight:700;color:#d8bd8a}
.hero h1{font-size:clamp(2.6rem,7vw,5.4rem);line-height:1.05;margin:.8rem 0 1rem}
.hero p{max-width:700px;margin:.6rem auto;color:#dfd0e1;line-height:1.8;font-size:1.05rem}
.heart{font-size:2rem;color:#e4aec3;letter-spacing:.45rem}
.section{padding-top:2.4rem}
.soft-card{height:100%;padding:1.25rem 1.3rem;border:1px solid rgba(217,164,186,.18);border-radius:20px;background:rgba(255,255,255,.055);box-shadow:0 10px 35px rgba(0,0,0,.08)}
.soft-card h3{margin:.45rem 0 .6rem;font-size:1.35rem}
.soft-card p{color:#cdbed1;line-height:1.75}
.quote{font-family:'Playfair Display',Georgia,serif;font-size:clamp(1.45rem,3vw,2.25rem);line-height:1.5;text-align:center;color:#f2dce8;padding:1.7rem 1rem}
.letter{white-space:pre-wrap;line-height:1.95;font-size:1.02rem;color:#e1d4e4}
.final-card{text-align:center;padding:3rem 1rem;margin-top:2.5rem;border:1px solid rgba(216,189,138,.38);border-radius:26px;background:linear-gradient(135deg,rgba(68,37,63,.88),rgba(33,25,45,.9))}
.final-card h2{font-size:clamp(2rem,5vw,3.5rem)}
.stButton button{border-radius:999px;border:1px solid #d8bd8a;background:#f1dce7;color:#2d1c31;font-weight:700;padding:.65rem 1.2rem}
.stButton button:hover{background:#fff0f6;border-color:#f1dce7;color:#251729}
div[data-testid="stExpander"]{border-radius:16px;border-color:rgba(217,164,186,.2);background:rgba(255,255,255,.035)}
footer{visibility:hidden}
@media(max-width:640px){.block-container{padding-left:1rem;padding-right:1rem}.hero{padding:2.4rem .9rem}}
</style>
""", unsafe_allow_html=True)

if "opened" not in st.session_state:
    st.session_state.opened = False

st.markdown(f'<div class="hero"><div class="heart">♡ ✦ ♡</div><div class="eyebrow">A little reminder, made just for you</div><h1>{txt(content.get("site_title"))}</h1><p><strong>{txt(content.get("his_name"))}</strong></p><p>{txt(content.get("subtitle"))}</p></div>', unsafe_allow_html=True)
st.write("")
if not st.session_state.opened:
    _, mid, _ = st.columns([1, 1.25, 1])
    with mid:
        st.markdown('<div class="quote">“This is not a place where you need to be strong. This is a place where you can just be you.”</div>', unsafe_allow_html=True)
        if st.button("♡ Open this little surprise", use_container_width=True):
            st.session_state.opened = True
            st.rerun()
        st.caption("A small pause in your day, with a lot of love behind it.")
    st.stop()

st.snow()
st.markdown(f'<div class="quote">“{txt(content.get("opening_note"))}”</div>', unsafe_allow_html=True)

st.markdown('<div class="section"><div class="kicker">01 · Us, in little frames</div><h2>Memories I would choose again</h2></div>', unsafe_allow_html=True)
photos = sorted([p for p in PHOTOS.iterdir() if p.is_file() and p.suffix.lower() in {".jpg",".jpeg",".png",".webp"}]) if PHOTOS.exists() else []
if photos:
    cols = st.columns(3)
    for i, p in enumerate(photos):
        with cols[i % 3]:
            st.image(str(p), use_container_width=True, caption=p.stem.replace("_"," ").title())
else:
    st.info("📷 Add your photos to `assets/photos/` in GitHub. JPG, JPEG, PNG, and WEBP are supported.")

st.markdown('<div class="section"><div class="kicker">02 · The little things</div><h2>Little moments I would choose again</h2></div>', unsafe_allow_html=True)
cols = st.columns(3)
for i, memory in enumerate(content.get("memories", [])):
    with cols[i % 3]:
        st.markdown(f'<div class="soft-card"><div class="kicker">Memory {i+1:02d}</div><h3>{txt(memory.get("title",""))}</h3><p>{txt(memory.get("text",""))}</p></div>', unsafe_allow_html=True)
        st.write("")

st.markdown(f'<div class="section"><div class="kicker">03 · From my heart to yours</div><h2>{txt(content.get("letter_title"))}</h2></div>', unsafe_allow_html=True)
with st.container(border=True):
    st.markdown(f'<div class="letter">{txt(content.get("love_letter",""))}</div>', unsafe_allow_html=True)

st.markdown('<div class="section"><div class="kicker">04 · Keep these close</div><h2>A few things I hope you remember</h2></div>', unsafe_allow_html=True)
cols = st.columns(2)
for i, reminder in enumerate(content.get("reminders", [])):
    with cols[i % 2]:
        st.markdown(f'<div class="soft-card"><div class="kicker">A reminder for you</div><h3>♡ {txt(reminder.get("title",""))}</h3><p>{txt(reminder.get("text",""))}</p></div>', unsafe_allow_html=True)
        st.write("")

st.markdown('<div class="section"><div class="kicker">05 · Just because</div><h2>Reasons you matter to me</h2></div>', unsafe_allow_html=True)
with st.expander("Open when you need a little reminder ♡"):
    for i, reason in enumerate(content.get("reasons", []), 1):
        st.markdown(f"**{i:02d}.** {txt(reason)}")

st.markdown('<div class="section"><div class="kicker">06 · A soundtrack for this moment</div><h2>Press play, if you need a pause</h2></div>', unsafe_allow_html=True)
st.write(txt(content.get("song_caption","")))
music = sorted([p for p in MUSIC.iterdir() if p.is_file() and p.suffix.lower() in {".mp3",".wav",".m4a",".ogg"}]) if MUSIC.exists() else []
if music:
    for song in music:
        st.caption(song.stem.replace("_"," ").title())
        st.audio(str(song))
else:
    st.caption("Optional: add an audio file (.mp3, .wav, .m4a, .ogg) to `assets/music/`.")
videos = sorted([p for p in VIDEO.iterdir() if p.is_file() and p.suffix.lower() in {".mp4",".mov",".webm"}]) if VIDEO.exists() else []
if videos:
    with st.expander("A little video message 🎞️"):
        for vid in videos:
            st.video(str(vid))

st.markdown(f'<div class="final-card"><div class="heart">♡ ✦ ♡</div><div class="eyebrow">Whenever you need to remember</div><h2>{txt(content.get("final_message"))}</h2><p style="font-size:1.05rem;color:#dfd0e1;margin-top:1.5rem;">{txt(content.get("sign_off"))}</p></div>', unsafe_allow_html=True)
st.write("")
if st.button("↻ Read it again"):
    st.session_state.opened = False
    st.rerun()
st.caption("Made with care just for you 💫")
