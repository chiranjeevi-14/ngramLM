import re
import random
from collections import defaultdict

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = text.split()
    return tokens

def build_ngram_model(tokens, n=5):
    model = defaultdict(list)
    for i in range(len(tokens) - n + 1):
        context = tuple(tokens[i:i+n-1])
        next_word = tokens[i+n-1]
        model[context].append(next_word)
    return model

def generate_text(model, seed, length=40):
    words = seed.lower().split()
    for _ in range(length):
        context = tuple(words[-4:])
        if context not in model:
            break
        words.append(random.choice(model[context]))
    return " ".join(words)

if __name__ == "__main__":
    with open("data/sherlock.txt", "r", encoding="utf-8") as file:
        text = file.read()

    tokens = preprocess(text)
    model = build_ngram_model(tokens, n=5)

    seeds = [
        "it was a very",
        "holmes looked at the",
        "the man was standing"
    ]
    for seed in seeds:
        print("\nInput:", seed)
        print("Output:", generate_text(model, seed))
