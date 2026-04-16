import streamlit as st
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import tempfile

# ------------------------------
# PAGE CONFIG
# ------------------------------
st.set_page_config(page_title="Baby Cry Analyzer", layout="centered")

# ------------------------------
# HEADER
# ------------------------------
st.title("👶 Baby Cry Analyzer")
st.markdown("### 🎤 AI-Powered Baby Emotion Detection System")

st.markdown("---")

# ------------------------------
# INPUT
# ------------------------------
duration = st.slider("⏱ Recording Duration (seconds)", 1, 10, 3)

# ------------------------------
# BUTTON
# ------------------------------
if st.button("🎙 Start Recording"):
    st.info("Recording... Please wait")

    fs = 44100
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()

    st.success("Recording Completed ✅")

    # Save audio
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    write(temp_file.name, fs, recording)

    # Play audio
    st.audio(temp_file.name)

    st.markdown("---")

    # ------------------------------
    # FAKE AI PREDICTION
    # ------------------------------
    classes = ["🍼 Hunger", "😴 Sleep", "⚠️ Pain", "🧷 Discomfort"]
    probs = np.random.dirichlet(np.ones(4), size=1)[0]

    # ------------------------------
    # RESULTS
    # ------------------------------
    st.subheader("📊 Prediction Analysis")

    for i, c in enumerate(classes):
        st.progress(float(probs[i]))
        st.write(f"{c}: {round(probs[i]*100,2)}%")

    final_index = np.argmax(probs)
    final = classes[final_index]
    confidence = round(probs[final_index] * 100, 2)

    st.markdown("---")

    # ------------------------------
    # FINAL RESULT
    # ------------------------------
    st.success(f"🧠 Final Prediction: {final}")
    st.info(f"🔥 Confidence Level: {confidence}%")

    # ------------------------------
    # SUGGESTIONS
    # ------------------------------
    if "Hunger" in final:
        st.warning("🍼 Suggestion: Feed the baby")
    elif "Sleep" in final:
        st.warning("😴 Suggestion: Put baby to sleep")
    elif "Pain" in final:
        st.warning("⚠️ Suggestion: Check for illness")
    else:
        st.warning("🧷 Suggestion: Check diaper or environment")
