import re

def welcome():
    print('''
_______           ________                      _______________   ________    _____  
\   _  \ ___  ___/  _____/_____    _____   ____ \_____  \   _  \  \_____  \  /  |  | 
/  /_\  \\  \/  /   \  ___\__  \  /     \_/ __ \ /  ____/  /_\  \  /  ____/ /   |  |_
\  \_/   \>    <\    \_\  \/ __ \|  Y Y  \  ___//       \  \_/   \/       \/    ^   /
 \_____  /__/\_ \\______  (____  /__|_|  /\___  >_______ \_____  /\_______ \____   | 
       \/      \/       \/     \/      \/     \/        \/     \/         \/    |__|      
''')
    print("This is a Pyjail I've made especially for you, and all you want is in this file directory.\n")
    print("Many commonly used characters are banned, and there are also restrictions on character length.\n")
    print("However, I can kindly give you a hint that the Python version is greater than 3.7.\n")
    print("JUST DO IT.")

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

welcome()
pyjail()
