input_string = input("Enter a string: ")

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
total_vowels = 0
vowel_counts = {}

for char in input_string:
    if char in vowels:
        total_vowels += 1
        vowel_counts[char] = vowel_counts.get(char, 0) + 1

print(f"Original string: {input_string}")
print(f"Total number of vowels: {total_vowels}")
print("Vowel counts (case-sensitive):")
for vowel, count in vowel_counts.items():
    print(f"  {vowel}: {count}")