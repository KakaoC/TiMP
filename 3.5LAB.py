with open("numbers.txt", "r") as file:
    line = file.readline()
    s = []
    while line:
        k = line.split()
        s += k
        line = file.readline()
    print(sum(map(int, s)))
