import time
import numpy as np
from engine.pipeline import DictationPipeline

def test_pipeline():
    print("Initializing pipeline for verification...")
    try:
        pipeline = DictationPipeline()
    except Exception as e:
        print(f"Failed to initialize pipeline: {e}")
        return

    print("Pipeline initialized. Running test...")
    
    # Create a dummy audio signal (silence) just to test the flow
    # In a real test we'd need a wav file, but let's see if it crashes on empty/silence
    # or we can try to mock the STT part if needed.
    # Actually, faster-whisper might complain about silence or random noise.
    # Let's try to pass a simple zero array.
    dummy_audio = np.zeros(16000 * 2, dtype=np.float32) # 2 seconds of silence
    
    try:
        result = pipeline.process(dummy_audio, tone_mode="Neutral")
        print("Pipeline processed successfully.")
        print("Result:", result)
    except Exception as e:
        print(f"Pipeline processing failed: {e}")

if __name__ == "__main__":
    test_pipeline()
