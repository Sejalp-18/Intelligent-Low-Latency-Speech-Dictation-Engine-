class ToneAdjuster:
    def __init__(self):
        pass

    def adjust_tone(self, text, mode="Neutral"):
        """
        Adjust the tone of the text.
        Modes: Formal, Casual, Concise, Neutral
        """
        if not text:
            return ""
            
        if mode == "Formal":
            return self._to_formal(text)
        elif mode == "Casual":
            return self._to_casual(text)
        elif mode == "Concise":
            return self._to_concise(text)
        else:
            return text

    def _to_formal(self, text):
        # Expanded rule-based formalization
        replacements = {
            r"\bcan't\b": "cannot",
            r"\bwon't\b": "will not",
            r"\bdon't\b": "do not",
            r"\bi'm\b": "I am",
            r"\bit's\b": "it is",
            r"\bgonna\b": "going to",
            r"\bwanna\b": "want to",
            r"\bgotta\b": "have to",
            r"\blet's\b": "let us",
            r"\bwhat's\b": "what is",
            r"\bthere's\b": "there is",
            r"\bthat's\b": "that is",
            r"\bwho's\b": "who is",
            r"\bhe's\b": "he is",
            r"\bshe's\b": "she is",
            r"\bthey're\b": "they are",
            r"\bwe're\b": "we are",
            r"\byou're\b": "you are",
            r"\bshouldn't\b": "should not",
            r"\bwouldn't\b": "would not",
            r"\bcouldn't\b": "could not",
            r"\bisn't\b": "is not",
            r"\baren't\b": "are not",
            r"\bwasn't\b": "was not",
            r"\bweren't\b": "were not",
            r"\bhasn't\b": "has not",
            r"\bhaven't\b": "have not",
            r"\bhadn't\b": "had not",
            r"\bdoesn't\b": "does not",
            r"\bdidn't\b": "did not",
            r"\bkids\b": "children",
            r"\bthanks\b": "thank you",
            r"\bhi\b": "hello",
            r"\bhey\b": "hello",
            r"\bguys\b": "everyone",
            r"\byeah\b": "yes",
            r"\bnope\b": "no",
            r"\bokay\b": "acceptable",
            r"\bok\b": "acceptable",
            r"\bawesome\b": "excellent",
            r"\bcool\b": "good",
            r"\bstuff\b": "items",
            r"\bthings\b": "aspects"
        }
        import re
        for pattern, replacement in replacements.items():
            text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
        return text

    def _to_casual(self, text):
        # Expanded rule-based casualization
        replacements = {
            r"\bcannot\b": "can't",
            r"\bwill not\b": "won't",
            r"\bdo not\b": "don't",
            r"\bI am\b": "I'm",
            r"\bit is\b": "it's",
            r"\bgoing to\b": "gonna",
            r"\bwant to\b": "wanna",
            r"\bhave to\b": "gotta",
            r"\blet us\b": "let's",
            r"\bwhat is\b": "what's",
            r"\bthere is\b": "there's",
            r"\bthat is\b": "that's",
            r"\bwho is\b": "who's",
            r"\bhe is\b": "he's",
            r"\bshe is\b": "she's",
            r"\bthey are\b": "they're",
            r"\bwe are\b": "we're",
            r"\byou are\b": "you're",
            r"\bshould not\b": "shouldn't",
            r"\bwould not\b": "wouldn't",
            r"\bcould not\b": "couldn't",
            r"\bis not\b": "isn't",
            r"\bare not\b": "aren't",
            r"\bwas not\b": "wasn't",
            r"\bwere not\b": "weren't",
            r"\bhas not\b": "hasn't",
            r"\bhave not\b": "haven't",
            r"\bhad not\b": "hadn't",
            r"\bdoes not\b": "doesn't",
            r"\bdid not\b": "didn't",
            r"\bchildren\b": "kids",
            r"\bthank you\b": "thanks",
            r"\bhello\b": "hey",
            r"\beveryone\b": "guys",
            r"\byes\b": "yeah",
            r"\bno\b": "nope",
            r"\bacceptable\b": "okay",
            r"\bexcellent\b": "awesome",
            r"\bgood\b": "cool",
            r"\bitems\b": "stuff",
            r"\baspects\b": "things"
        }
        import re
        for pattern, replacement in replacements.items():
            text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
        return text

    def _to_concise(self, text):
        # Remove filler adjectives/adverbs (very basic list)
        removals = [
            r"\bvery\b", r"\breally\b", r"\bquite\b", r"\bjust\b", 
            r"\bactually\b", r"\bbasically\b", r"\bliterally\b"
        ]
        import re
        for pattern in removals:
            text = re.sub(pattern, "", text, flags=re.IGNORECASE)
        return re.sub(r"\s+", " ", text).strip()

if __name__ == "__main__":
    adjuster = ToneAdjuster()
    sample = "I am really going to the store."
    print(f"Formal: {adjuster.adjust_tone(sample, 'Formal')}")
    print(f"Casual: {adjuster.adjust_tone(sample, 'Casual')}")
    print(f"Concise: {adjuster.adjust_tone(sample, 'Concise')}")
