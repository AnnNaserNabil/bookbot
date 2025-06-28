# stats.py

def count_words(text):
    words = text.split()
    return len(words)


def count_chars(text):
    char_counts = {}
    for char in text.lower():
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def sorted_char_counts(char_counts):
    # Create list of dicts with only alphabetical chars
    filtered = [
        {"char": char, "num": count}
        for char, count in char_counts.items()
        if char.isalpha()
    ]
    # Sort descending by count
    filtered.sort(key=lambda x: x["num"], reverse=True)
    return filtered
