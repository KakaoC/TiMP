print('Введите полный путь к файлу')
s = str(input()) 
file = open(s)
if not(file.closed): 
    n = 1
    for line in file:
        if (n > 5): 
            break 
        n = n + 1
        print(line.strip()) 
    file.close() 
else:
    print('файл невозможно открыть')
    file.close()
