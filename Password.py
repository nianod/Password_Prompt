#This program will keep prompting you to enter your password untill you enter the correct password

user_password = 'abcdef'

enter_password = input('Enter your password: ')

while enter_password != user_password:
 print('Incorrect password. Try again dude!')
enter_password = input('Enter your password: ')

print('Bravoo🥳 Correct password!')