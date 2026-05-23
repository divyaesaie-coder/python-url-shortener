#url generator

import random
import string

urls = {}

while True:
    print("1) Shorten URL")
    print("2) Open short URL")
    print("3) Exit")

    ch = input("Choose: ")

    if ch == "1":
        url = input("Enter the URL: ")

        code = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

        urls[code] = url

        print("Short URL: short.ly/" + code)

    elif ch == "2":
        code = input("Enter short code(enter words only after slash: ")

        if code in urls:
            print("Original URL:", urls[code])
        else:
            print("Invalid code")

    elif ch == "3":
        print("Thank you!")
        break
