 #!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :.

    Args:
    text (str): The input string.

    Raises:
    TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Remove leading spaces after punctuation and handle text line by line
    i = 0
    length = len(text)
    
    while i < length:
        # Print the character
        print(text[i], end="")

        # If we find punctuation, print a newline
        if text[i] in '.?:':
            print("\n")
            # Skip any spaces following the punctuation mark
            while i + 1 < length and text[i + 1] == " ":
                i += 1

        # Proceed to the next character
        i += 1
