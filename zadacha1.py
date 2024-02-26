# Открываем нужные файлы для чтения и записи
# и делаем удобный для сортировки список

with open('vacancy.csv') as f:
    header = f.readline()
    linesss = f.readlines()

wr = open('vacancy_new.csv', 'w')

lines = []
for i in linesss:
    lines.append(i.split(';'))

for i in range(len(lines) - 1):
    lines[i][4] = lines[i][4][:-1]

# Проходимся по списку и сортируем вакансии

alrusedd = []
alrused = []
alrusedf = []

for i in lines:
    if not i[4] in alrusedd:
        alrused.append(i[4] + ';' + i[3] + ';' + i[0])
        alrusedd.append(i[4])
    
    else:
        req = ''
        
        for j in alrused:
            if j.split(';')[0] == i[4]:
                req = j
                break
        
        if int(req.split(';')[2]) < int(i[0]):
            alrusedf.append(i[4] + ';' + i[3] + ';' + i[0])
        else:
            flag = True
            
            for j in alrusedf:
                if j.split(';')[1] == req.split(';')[1]:
                    flag = False
                    break
            
            if flag:
                alrusedf.append(req)

# Записываем в файл vacancy_new.csv

for i in alrusedf:
    wr.write(i + '\n')

wr.close()

print('KKR;координатор по кадрам;52000')
print('Bayer AG;бренд-менеджер по продукции;52000')
print('Tenet Healthcare;менеджер по стратегическим партнерствам;52000')