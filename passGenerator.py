import random


def generate_password(length):
    password = ""
    for i in range(length):
        password += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%^&*")
    return password


length = int(input("Введите длину пароля: "))
print("Сгенерированный пароль:", generate_password(length))