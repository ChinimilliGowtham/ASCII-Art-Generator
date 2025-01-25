import pyfiglet

def generate_ascii_art(text):
    """
    Generates ASCII art for the given text.
    """
    ascii_art = pyfiglet.figlet_format(text)
    return ascii_art

if __name__ == "__main__":
    print("Welcome to the ASCII Art Generator!")
    user_text = input("Enter a word or phrase: ")
    print("\nGenerated ASCII Art:\n")
    print(generate_ascii_art(user_text))
