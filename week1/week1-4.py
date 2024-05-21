def is_palindrome(text):
    """
    Checks if the given text is a palindrome.
    Returns True if it is, False otherwise.
    """
    cleaned_text = text
    cleaned_text = ''.join(text.split()).lower()
    for i in range(len(cleaned_text) // 2):
        if cleaned_text[i] != cleaned_text[-(i + 1)]:
            return False
    return True

user_input = input("Enter some text: ")
#Never odd or even palindromes
if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome!")
else:
    print(f"'{user_input}' is not a palindrome.")