import random

pass_len = int(input('Enter the password length:'))
numberofpass = int(input('Enter the number of passwords to generate:'))

alpha_a = 'abcdefghijklmnopqrstuvwxyz'
alpha_A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeric = '0123456789'
sp_char = '!@#$%^&*()'

combination = alpha_A + alpha_a + numeric + sp_char

for i in range(1, numberofpass+1):
    print('Password number {0} is {1}'.format(i, ''.join(random.sample(combination, pass_len))))
