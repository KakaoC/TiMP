with open("numbers.txt", "r") as file:
    line = file.readline()
    k = 0
    while line:
        k += 1
        line = file.readline()
print(k)