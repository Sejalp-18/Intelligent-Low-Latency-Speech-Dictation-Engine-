from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

class GrammarCorrector:
    def __init__(self, model_name="vennify/t5-base-grammar-correction", device="cpu"):
        """
        Initialize the Grammar Corrector.
        Args:
            model_name (str): Name of the model to load.
            device (str): Device to run on ('cpu' or 'cuda').
        """
        self.device = device
        print(f"Loading Grammar model: {model_name} on {device}...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)
        print("Grammar model loaded.")

    def correct(self, text):
        """
        Correct grammar in the text.
        """
        if not text:
            return ""
        
        # vennify/t5-base-grammar-correction expects "grammar: " prefix
        input_text = "grammar: " + text
        
        input_ids = self.tokenizer.encode(input_text, return_tensors="pt").to(self.device)
        
        outputs = self.model.generate(
            input_ids, 
            max_length=128, 
            num_beams=4, 
            early_stopping=True
        )
        
        corrected_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return corrected_text

if __name__ == "__main__":
    corrector = GrammarCorrector()
    sample = "Me goes to store yesterday."
    print(f"Original: {sample}")
    print(f"Corrected: {corrector.correct(sample)}")
