import re

def pyjail():
    pattern = re.compile("[a-zA-Z0-9]")
    while True:
        code = input(">")

        if re.findall(pattern,code):
            print("Some characters in your code are banned.")
        elif len(code) > 12:
            print("Your code is too long.")
        else:
            eval(code)