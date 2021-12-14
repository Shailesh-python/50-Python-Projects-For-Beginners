# Username and Domain name extractor:

email = str(input("enter your email:"))

# strip() acts like a trim in excel
email = email.strip()

# index give the index number of required character in string like find or search in excel
start = int(email.index('@'))

username = email[:start]
domain_name = email[start + 1:]
print('Your Username is {} and Domain name is {}'.format(username, domain_name))
