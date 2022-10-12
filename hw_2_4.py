# Задание 2.4
# Напишите программу, которая печатает введенный текст заданное количество раз,
# построчно. Текст и количество повторений нужно ввести с помощью input()

input_text = input("Введите текст: ") + "\n"
number_repetitions = int(input("Введите количество повторений текста: "))
text = input_text * number_repetitions
print(text)

# 2 вариант решения
num = int(input("Введите количество повторений текста: "))
world = input("Введите текст: ")
x = 1
while num >= x:
    print(world)
    num = num - 1
