
import streamlit as st

st.set_page_config(page_title="AKRUM Secure Video Encryptor", layout="centered")

st.title("AKRUM Secure Video Encryptor")
st.markdown("Drop a video file below (up to 1GB) to encrypt it securely using AKRUM's entropy engine.")

uploaded_file = st.file_uploader(
    "Upload your video file (.mp4, .mpeg4, .mov)", 
    type=["mp4", "mpeg4", "mov"]
)

if uploaded_file:
    st.success("File uploaded successfully!")
    st.video(uploaded_file)
    st.markdown("Encryption and secure transmission demo would run here.")

st.markdown("---")
st.caption("AKRUM is protected by US Patent No. 10,078,492 B2. This product demo illustrates secure video transmission using entropy from cellular automata.")
