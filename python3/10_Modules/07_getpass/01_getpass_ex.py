from getpass import getpass, getuser

user_name = input('User Name:')
pass_word = getpass('Password:')

print("user_name -", user_name)
print("pass_word -", pass_word)

print('getuser()', getuser())
