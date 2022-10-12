# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все элементы списка, где есть буква 'a'

list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#1 способ
print(list_1[2]+list_1[4]+list_1[6]+list_1[7])
print(list_1[1],list_1[5])

# 2 способ
new_list = []
for x in list_1:
    if type(x) is int:
        new_list.append(x)
print(sum(new_list))

letter = 'a'
new_list = []
for word in list_1:
    if type(word) is str:
        if letter in word:
            new_list.append(word)
print(new_list)

#3 способ
# result_2 = list(filter(lambda x: type(x) is int,list_1))
# print(sum(result_2))
#
# letter = 'a'
# result = list(filter(lambda x: type(x) is str and letter in x,list_1))
# print(result)



