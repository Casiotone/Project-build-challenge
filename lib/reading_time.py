import math

def reading_time(text, words_per_minute = 200):
    words = len(text.split())
    minutes = math.ceil(words / words_per_minute)
    return f'Estimated reading time: {minutes} minute{"s" if minutes > 1 else ""}'