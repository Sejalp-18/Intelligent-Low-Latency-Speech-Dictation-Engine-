import streamlit as st
import sounddevice as sd
import numpy as np
import time
from engine.pipeline import DictationPipeline

st.set_page_config(page_title="Intelligent Dictation", layout="wide")

@st.cache_resource
def load_pipeline():
    return DictationPipeline()

try:
    pipeline = load_pipeline()
    st.success("Pipeline Loaded Successfully!")
except Exception as e:
    st.error(f"Failed to load pipeline: {e}")
    st.stop()

st.title("Intelligent Low-Latency Speech Dictation")
st.markdown("### Ready-to-Use Output, No LLMs")

col1, col2 = st.columns(2)

with col1:
    st.header("Controls")
    tone_mode = st.selectbox("Select Tone/Style", ["Neutral", "Formal", "Casual", "Concise"])
    duration = st.slider("Recording Duration (seconds)", 1, 100, 5)
    
    if st.button("Record & Process"):
        with st.spinner(f"Recording for {duration} seconds..."):
            # Record audio
            fs = 16000
            recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
            sd.wait()
            st.success("Recording complete. Processing...")
            
            # Process
            result = pipeline.process(recording.flatten(), tone_mode)
            
            # Display Results
            st.session_state.result = result

with col2:
    st.header("Results")
    if 'result' in st.session_state:
        res = st.session_state.result
        metrics = res["metrics"]
        
        st.subheader("Final Output")
        st.text_area("Ready-to-Use Text", res["final_text"], height=150)
        
        with st.expander("See Pipeline Steps"):
            st.markdown(f"**Raw Transcript:** {res['raw_text']}")
            st.markdown(f"**Cleaned:** {metrics.get('cleaned_text', '')}")
            st.markdown(f"**Grammar Corrected:** {metrics.get('grammar_text', '')}")
            
        st.subheader("Latency Metrics (ms)")
        cols = st.columns(4)
        cols[0].metric("STT", f"{metrics['stt_latency']:.0f} ms")
        cols[1].metric("Cleaning", f"{metrics['cleaning_latency']:.0f} ms")
        cols[2].metric("Grammar", f"{metrics['grammar_latency']:.0f} ms")
        cols[3].metric("Tone", f"{metrics['tone_latency']:.0f} ms")
        
        st.metric("Total Latency", f"{metrics['total_latency']:.0f} ms", delta_color="inverse")
        
        if metrics['total_latency'] <= 1500:
            st.success("✅ Latency Requirement Met (<= 1500ms)")
        else:
            st.warning("⚠️ Latency Requirement Exceeded")

st.markdown("---")
st.markdown("Built with `faster-whisper`, `T5-small`, and `Streamlit`.")
