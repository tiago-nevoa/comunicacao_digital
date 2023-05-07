from exercise3 import password_generator

five_strong_passwords = []

for num in range(5):
    five_strong_passwords.append(password_generator())

print("The 5 Passwords are:")
print(five_strong_passwords)