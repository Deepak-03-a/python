email = input("Enter your email: ")

username = email[ : email.index("@")]

subdomain = email[email.index("@") + 1 : email.index(".") ]

topleveldomain = email[email.index(".") : ]



print(f"Your username is {username}, subdomain name is {subdomain} and TLD is {topleveldomain}")