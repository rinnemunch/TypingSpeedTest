import random
import time


sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing fast takes practice and focus.",
    "Python makes programming fun and productive."
]

target = random.choice(sentences)

print("Type this:")
print("\n" + target)
input("Press Enter to start...")

start = time.time()
typed = input("\nStart typing: ")
end = time.time()

elapsed = round(end - start, 2)

words = len(target.split())
wpm = round((words / elapsed) * 60)

# print(f"\n⏱ You took {elapsed} seconds")
# print(f"⌨️  Your Speed: {wpm} words per minute")
