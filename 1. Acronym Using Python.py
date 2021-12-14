# 1- Acronym using python

user_input = str(input('Enter a phrase:'))

text = user_input.split(' ')

# newlist = [ele[0:1].upper() for ele in text]   a list comprehension method
short_text = ''
for ele in text:
    short_text = short_text + ele[0:1].upper()

print(short_text)
