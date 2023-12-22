import random


car = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ?!@#$"

password = []

for i in range(10):
    c = random.choice(car)
    password.append(c)

secret_password = "".join(password)

print(secret_password)