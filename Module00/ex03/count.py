import sys
import string


def text_analyzer(
    text
):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given tex
    """

    lowercase = 0
    uppercase = 0
    punctuation = 0
    space = 0

    for character in text:
        if character.islower():
            lowercase += 1
        elif character.isupper():
            uppercase += 1
        elif character.isspace():
            space += 1
        elif character in string.punctuation:
            punctuation += 1

    print(f"""
    The text contains {len(text)} character(s):
    - {uppercase} upper letter(s)
    - {lowercase} lower letter(s)
    - {punctuation} punctuation mark(s)
    - {space} space(s)
    """)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Error: no argument is provided", file=sys.stderr)
    elif len(sys.argv) > 2:
        print("Error: more than one argument is provided", file=sys.stderr)
    else:
        text_analyzer(sys.argv[1])
    