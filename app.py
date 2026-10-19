from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="UroPredictive", layout="wide")

html = (Path(__file__).parent / "uropredictive.html").read_text(encoding="utf-8")
components.html(html, height=2200, scrolling=True)
