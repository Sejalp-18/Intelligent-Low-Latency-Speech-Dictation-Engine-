import time
import logging
from .stt import STTEngine
from .cleaning import TextCleaner
from .grammar import GrammarCorrector
from .tone import ToneAdjuster

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DictationPipeline:
    def __init__(self):
        logger.info("Initializing Dictation Pipeline...")
        self.stt = STTEngine(model_size="tiny", device="cpu") # Use tiny for speed
        self.cleaner = TextCleaner()
        self.grammar = GrammarCorrector(device="cpu")
        self.tone = ToneAdjuster()
        logger.info("Pipeline initialized.")

    def process(self, audio_data, tone_mode="Neutral"):
        """
        Process audio data through the full pipeline.
        Returns:
            dict: Result containing final text and latency metrics.
        """
        metrics = {}
        start_total = time.time()

        # 1. STT
        start_stt = time.time()
        raw_text = self.stt.transcribe(audio_data)
        metrics["stt_latency"] = (time.time() - start_stt) * 1000
        metrics["raw_text"] = raw_text

        if not raw_text:
            return {
                "final_text": "",
                "raw_text": "",
                "metrics": metrics,
                "total_latency": (time.time() - start_total) * 1000
            }

        # 2. Cleaning (Fillers + Repetition)
        start_clean = time.time()
        cleaned_text = self.cleaner.remove_fillers(raw_text)
        cleaned_text = self.cleaner.remove_repetitions(cleaned_text)
        metrics["cleaning_latency"] = (time.time() - start_clean) * 1000
        metrics["cleaned_text"] = cleaned_text

        # 3. Grammar Correction
        start_grammar = time.time()
        grammatically_correct_text = self.grammar.correct(cleaned_text)
        metrics["grammar_latency"] = (time.time() - start_grammar) * 1000
        metrics["grammar_text"] = grammatically_correct_text

        # 4. Tone Adjustment
        start_tone = time.time()
        final_text = self.tone.adjust_tone(grammatically_correct_text, tone_mode)
        metrics["tone_latency"] = (time.time() - start_tone) * 1000
        
        metrics["total_latency"] = (time.time() - start_total) * 1000
        
        return {
            "final_text": final_text,
            "raw_text": raw_text,
            "metrics": metrics
        }

if __name__ == "__main__":
    # Mock audio processing test would go here
    pass
