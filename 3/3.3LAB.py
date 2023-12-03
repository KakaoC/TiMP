print('Введите полный путь к файлу ')
s = str(input()) 
file = open(s) 
if not (file.closed): 
    n = 1 
    for line in file:
        s = line.strip() 
        print(str(n) + ': ' + s) 
        n = n + 1
    file.close()
else:
    print('файл невозможно открыть')
    file.close()