# pujokes.py
# A simple Python script to tell random programming jokes

import pyjokes

def tell_joke():
    joke = pyjokes.get_joke(language="en", category="all")
    print("\nHere's a joke for you:\n")
    print(joke)

if __name__ == "__main__":
    print("Welcome to PUJOKES - Get a dose of programmer humor!")
    tell_joke()
