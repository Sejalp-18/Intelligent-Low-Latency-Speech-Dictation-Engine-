from engine.grammar import GrammarCorrector
import time

def test_grammar():
    print("Initializing Grammar Corrector...")
    corrector = GrammarCorrector(device="cpu")
    
    samples = [
        "Me goes to store yesterday.",
        "She don't like apples.",
        "I has a cat."
    ]
    
    print("\nTesting Grammar Correction:")
    for sample in samples:
        start = time.time()
        corrected = corrector.correct(sample)
        duration = (time.time() - start) * 1000
        print(f"Original: '{sample}' -> Corrected: '{corrected}' ({duration:.0f}ms)")

if __name__ == "__main__":
    test_grammar()
