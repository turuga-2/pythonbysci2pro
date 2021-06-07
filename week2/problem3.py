import sys


def main():
    hindu_line = "पायथन एक अद्भुत प्रोग्रामिंग भाषा है जिसके माध्यम से मैं बहुत कुछ हासिल कर सकता हूं।"

    print(type(hindu_line))
    # hindu_line is a string variable

    encoded_line = hindu_line.encode()
    print("The encoded version version will be", encoded_line)
    print(type(encoded_line))

    return 0


if __name__ == "__main__":
    sys.exit(main())
