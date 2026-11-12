sentence = input("Enter a sentence:")
vowels = 0
consonants = 0
digits = 0
spaces = 0
special_chars = 0

for char in sentence:
    if char.lower() in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isdigit():
        digits += 1
    elif char == " ":
        spaces += 1
    else:
        special_chars +=1

words = len(sentence.split())
total_letters = vowels + consonants

if total_letters > 0:
    vowel_percentage = (vowels / total_letters) * 100
else:
    vowel_percentage = 0

print("========================")
print("DOCUMENT ANALYSIS REPORT")
print("========================")

print("Sentence:", sentence)
print("Words:", words)
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special_chars)
print("Total letters:", total_letters)
print(f"Vowel percentage: {vowel_percentage}")