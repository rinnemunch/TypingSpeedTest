import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing fast takes practice and focus.",
    "Python makes programming fun and productive."
]

target = random.choice(sentences)

print("Type this:")
print("\n" + target)
