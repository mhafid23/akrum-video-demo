
import streamlit as st
import base64
from cryptography.fernet import Fernet

st.set_page_config(page_title="AKRUM Secure Video Encryptor", layout="wide")

# Custom CSS for a cleaner, more modern look
st.markdown("""
    <style>
        .main {
            background-color: #0f1117;
            color: #f5f5f5;
            font-family: 'Segoe UI', sans-serif;
        }
        h1, h2 {
            color: #00bfff;
        }
        .stButton>button {
            background-color: #00bfff;
            color: white;
            font-weight: bold;
            border-radius: 10px;
        }
        .stFileUploader {
            border: 2px dashed #00bfff;
            padding: 2em;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("AKRUM Secure Video Encryptor")
st.write("Drop a video file below (up to 1GB) to encrypt it securely using AKRUM's entropy engine.")

uploaded_video = st.file_uploader("Upload your video file (.mp4)", type=["mp4"])

if uploaded_video:
    video_bytes = uploaded_video.read()

    st.video(video_bytes)
    st.success("Video loaded successfully. Generating encryption key...")

    # Simulate AKRUM entropy-based key
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(video_bytes)
    decrypted_data = cipher.decrypt(encrypted_data)

    st.subheader("Encryption Key (for demonstration only)")
    st.code(key.decode())

    st.subheader("Encrypted Output (preview)")
    st.code(encrypted_data[:100].decode('latin1') + "...", language="text")

    st.download_button("Download Encrypted File",
                       data=encrypted_data,
                       file_name=f"encrypted_{uploaded_video.name}",
                       mime="application/octet-stream")

    st.subheader("Decrypted Video Preview")
    st.video(decrypted_data)
    st.success("Decryption successful! Secure transmission demonstrated.")

else:
    st.info("Awaiting a video file upload.")

st.markdown("---")
st.caption("AKRUM is protected by US Patent No. 10,078,492 B2. This demo illustrates secure video transmission using entropy-based encryption.")
