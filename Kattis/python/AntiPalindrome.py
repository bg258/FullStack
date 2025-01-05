def anti_palindrome():
    import sys
    sentence = sys.stdin.read().splitlines()
    print(sentence)

anti_palindrome()

    
    












# Anti-palindrome
"""
## Problem Description
A **palindrome** is a sequence of two or more characters that reads the same both forward and backward. Examples include "pp", "ehe", and "ere" from the text "Happy days are here again." (ignoring spaces, punctuation, and case). An **anti-palindrome** is a sequence of two or more characters that contains no palindromes.

Your task is to determine if a given text contains any palindromes. If it does, output `Palindrome`. Otherwise, output `Anti-palindrome`.

### Input
- A single line of text containing alphabetic and non-alphabetic characters.
- The text will:
  - Be at most 80 characters long.
  - Contain at least one alphabetic character.

### Output
- Print `Palindrome` if the text contains or is itself a palindrome.
- Print `Anti-palindrome` if no palindromes are found.

"""