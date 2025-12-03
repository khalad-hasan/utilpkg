def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def word_count(s):
    return len(s.split())

def reverse_string(s):
    return s[::-1]

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result
