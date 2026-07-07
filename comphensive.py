# TASK:30/06/2026
# Separate Vowels and Consonants

string = "hi hello raju"

vowels = ""
consonants = ""

for ch in string:
    if ch.isalpha():
        if ch in "aeiouAEIOU":
            vowels += ch + " "
        else:
            consonants += ch + " "

print("String      :", string)
print("Vowels      :", vowels)
print("Consonants  :", consonants)