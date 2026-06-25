#1
def char_frequency(s):
    freq = {}

    for ch in s:
        if ch != " ":
            freq[ch] = freq.get(ch, 0) + 1

    return freq
#2
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
#3
def first_unique_char(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s:
        if freq[ch] == 1:
            return ch

    return None
#4
def reverse_words(sentence):
    words = sentence.split()
    return " ".join(words[::-1])
#5
def count_vowels_consonants(s):
    vowels = "aeiou"
    v = c = 0

    for ch in s.lower():
        if ch.isalpha():
            if ch in vowels:
                v += 1
            else:
                c += 1

    return v, c
#6
if __name__ == "__main__":
    text = input("Enter a string: ")

    print("\nCharacter frequency:", char_frequency(text))
    print("Is palindrome:", is_palindrome(text))
    print("First unique character:", first_unique_char(text))
    print("Reversed words:", reverse_words(text))

    vowels, consonants = count_vowels_consonants(text)
    print("Vowels:", vowels)
    print("Consonants:", consonants)

    print("\nDay 12 complete.")
