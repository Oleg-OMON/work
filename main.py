Data = input("Дата:")
work = input("Задача:")
print(Data,work)


Data2 = input("Дата:")
work2 = input("Задача:")
print(Data2, work2)


Data3 = input("Дата:")
work3 = input("Задача:")
print(Data3, work3)

print(Data,work,Data2,work2,Data3,work3)


diary = {Data: [work]}
diary2 = {Data2: [work2]}
diary3 = {Data3: [work3]}
print(diary[Data])