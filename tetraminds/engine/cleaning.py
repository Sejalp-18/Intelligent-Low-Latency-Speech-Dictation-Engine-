import re

class TextCleaner:
    def __init__(self):
        self.fillers = [
            r"\bumm\b", r"\buhh\b", r"\buh\b", r"\bum\b", 
            r"\blike\b", r"\byou know\b", r"\bmatlab\b", 
            r"\bactually\b", r"\bbasically\b", r"\bliterally\b",
            r"\bI mean\b", r"\bsort of\b", r"\bkind of\b"
        ]
        # Compile regex for efficiency
        self.filler_pattern = re.compile("|".join(self.fillers), re.IGNORECASE)

    def remove_fillers(self, text):
        """
        Remove filler words from the text.
        """
        if not text:
            return ""
        # Replace fillers with empty string
        cleaned_text = self.filler_pattern.sub("", text)
        # Clean up multiple spaces
        cleaned_text = re.sub(r"\s+", " ", cleaned_text).strip()
        return cleaned_text

    def remove_repetitions(self, text):
        """
        Remove immediate repetitions of words or phrases.
        e.g. "I went to to the store" -> "I went to the store"
        """
        if not text:
            return ""
        
        # Remove repeated words (case insensitive)
        # \b(\w+)\s+\1\b matches "word word"
        text = re.sub(r"\b(\w+)(?:\s+\1\b)+", r"\1", text, flags=re.IGNORECASE)
        
        # Remove repeated phrases (simple 2-3 word n-grams)
        # This is a basic heuristic. For more complex cases, we might need a sliding window.
        # Captures "phrase phrase" where phrase is 1-4 words
        # This regex is tricky, let's stick to a simpler iterative approach for phrases if regex fails
        
        # Regex for repeated phrases of 1-4 words
        # (\b(?:\w+\s*){1,4})\s+\1\b
        # This might be too aggressive or slow, but let's try a safe version
        
        # Iterative approach for robustness
        words = text.split()
        if not words:
            return ""
        
        cleaned_words = []
        i = 0
        while i < len(words):
            # Check for 1-word repetition
            if i + 1 < len(words) and words[i].lower() == words[i+1].lower():
                cleaned_words.append(words[i])
                i += 2 # Skip the next one
                continue
            
            # Check for 2-word repetition
            if i + 3 < len(words) and \
               words[i].lower() == words[i+2].lower() and \
               words[i+1].lower() == words[i+3].lower():
                cleaned_words.append(words[i])
                cleaned_words.append(words[i+1])
                i += 4 # Skip the repetition
                continue
                
            cleaned_words.append(words[i])
            i += 1
            
        return " ".join(cleaned_words)

if __name__ == "__main__":
    cleaner = TextCleaner()
    sample = "Umm I went to to the store basically you know."
    print(f"Original: {sample}")
    print(f"Cleaned: {cleaner.remove_repetitions(cleaner.remove_fillers(sample))}")
