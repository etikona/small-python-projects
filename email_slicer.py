# Collect Email from the user
# Split the email using @, the first part as the user name, the second part as gonna be domain.
# Split domain using .

def main():
    print("Welcome to the email slicer")
    print("")


    email_input = input("Input your email address: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("User name : ", username)
    print("Domain : ", domain)
    print("Extension : ", extension)


main()    