import random
a = int(input("Количество случайных чисел:"))
with open("numbers_random.txt", "w") as file:
    for i in range(a):
        file.write(str(random.randint(1, 500)) + "\n")
