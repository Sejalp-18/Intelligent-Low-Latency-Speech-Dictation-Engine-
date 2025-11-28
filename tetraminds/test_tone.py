from engine.tone import ToneAdjuster

def test_tone():
    print("Initializing Tone Adjuster...")
    adjuster = ToneAdjuster()
    
    samples = [
        ("I'm gonna go to the store cause I wanna buy stuff.", "Formal"),
        ("I cannot go to the store because I do not want to buy items.", "Casual"),
        ("Hey guys, what's up?", "Formal"),
        ("Hello everyone, how are you?", "Casual")
    ]
    
    print("\nTesting Tone Adjustment:")
    for text, mode in samples:
        adjusted = adjuster.adjust_tone(text, mode)
        print(f"Original ({mode} target): '{text}'")
        print(f"Adjusted: '{adjusted}'\n")

if __name__ == "__main__":
    test_tone()
