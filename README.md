# Syllabus Sakhi AI — Streamlit Wrapper

A minimal **Streamlit** app that embeds the live Syllabus Sakhi AI (hosted on Dify).

- Live Dify URL: https://udify.app/chat/EbRtbiXuqvvp6EyI
  
- Live streamlit URL: https://syllabus-sakhi-ai-assistant.streamlit.app/

## Local run

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
cd to current folder
streamlit run app.py
# Open http://localhost:8501

```

## Deploy to Streamlit Community Cloud

1. Create a GitHub repo (e.g., `syllabus-sakhi-streamlit`).
2. Add `streamlit_app.py` and `requirements.txt` (and this README).
3. Go to https://share.streamlit.io → **New app** → select your repo → `streamlit_app.py`.
4. Deploy. Done.

## Deploy to Hugging Face Spaces

1. Create a Space → **Streamlit**.
2. Upload `streamlit_app.py` and `requirements.txt`.
3. The Space will build and serve automatically.
