# Открываем нужные файлы для чтения и записи
# и делаем удобный для сортировки список

with open('vacancy.csv') as f:
    header = f.readline()
    linesss = f.readlines()

wr = open('vacancy2.csv', 'w')

lines = []
for i in linesss:
    lines.append(i.split(';'))

for i in range(len(lines) - 1):
    lines[i][4] = lines[i][4][:-1]

# Проходимся по списку и сортируем вакансии

alrused = []
alrusedd = []

for i in lines:
    if not i[4] in alrusedd:
        alrused.append(i[4] + ';' + i[2] + ';' + i[3])
        alrusedd.append(i[4])

for i in alrused:
    wr.write(i + '\n')

wr.close()

print('В компании FedEx есть заданная профессия: классный руководитель, з/п в такой компании составит: 50400')