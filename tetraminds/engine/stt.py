import os
import numpy as np
from faster_whisper import WhisperModel

class STTEngine:
    def __init__(self, model_size="tiny", device="cpu", compute_type="int8"):
        """
        Initialize the STT Engine with faster-whisper.
        Args:
            model_size (str): Size of the model (tiny, base, small, medium, large).
            device (str): Device to run on ('cpu' or 'cuda').
            compute_type (str): Quantization type ('int8', 'float16', 'float32').
        """
        print(f"Loading Whisper model: {model_size} on {device}...")
        self.model = WhisperModel(model_size, device=device, compute_type=compute_type)
        print("Whisper model loaded.")

    def transcribe(self, audio_data, sample_rate=16000):
        """
        Transcribe audio data.
        Args:
            audio_data (np.ndarray): Audio data as a numpy array.
            sample_rate (int): Sample rate of the audio.
        Returns:
            str: Transcribed text.
        """
        # faster-whisper expects audio as a float32 numpy array
        if audio_data.dtype != np.float32:
            audio_data = audio_data.astype(np.float32)
        
        # Normalize if needed (Whisper usually handles this, but good practice)
        # if np.abs(audio_data).max() > 1.0:
        #     audio_data = audio_data / np.abs(audio_data).max()

        segments, info = self.model.transcribe(audio_data, beam_size=5, language="en")
        
        text = ""
        for segment in segments:
            text += segment.text + " "
        
        return text.strip()

if __name__ == "__main__":
    # Test stub
    print("Initializing STT Engine...")
    stt = STTEngine()
    print("STT Engine ready.")
