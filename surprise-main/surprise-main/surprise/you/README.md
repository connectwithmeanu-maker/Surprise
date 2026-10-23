# For You, Always — Boyfriend Surprise Website ♡

A deep-romantic, supportive Streamlit website to remind someone you love that they are cared for during a difficult time. It works before any photos, music, or video are added.

## Project structure
```text
for_you_boyfriend_surprise/
├── app.py
├── requirements.txt
├── content.json
├── README.md
└── assets/
    ├── photos/
    ├── music/
    └── video/
```

## Add media
- Couple photos: `assets/photos/` — JPG, JPEG, PNG, WEBP.
- Songs: `assets/music/` — MP3, WAV, M4A, OGG.
- Short video message: `assets/video/` — MP4, MOV, WEBM.
- The app discovers supported files automatically. It still runs if these folders are empty.

## Personalize
Edit `content.json` to change `his_name`, site title, opening message, love letter, memory cards, reminders, reasons, and final message. Keep JSON valid.

## Upload to GitHub
1. Extract the ZIP.
2. Create a GitHub repository.
3. Upload all files and folders (not just `app.py`).
4. Add photos to `assets/photos/` and commit.

**Privacy:** Public repositories can expose photos and media. Upload only what you are comfortable sharing, and check current Streamlit deployment visibility options.

## Free Streamlit Community Cloud deployment
1. Visit https://share.streamlit.io/ and sign in with GitHub.
2. Create an app from your repository.
3. Select your branch (usually `main`) and set main file path to `app.py`.
4. Deploy and test the site on phone and desktop.

## Media limits
GitHub blocks individual files larger than 100 MB. Compress videos to reasonably small H.264 MP4 files.
