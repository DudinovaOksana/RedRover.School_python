# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом.
# Если состав одинаковый, print("Equal')

family_1 = input("Enter family 1 members ").split(",")
family_2 = input("Enter family 2 members ").split(",")
count_1 = len(family_1)
count_2 = len(family_2)

if count_1<count_2:
     print("Family 2 is bigger than family 1")
elif count_1>count_2:
     print("Family 1 is bigger than family 2")
elif count_1 == count_2:
     print("Equal")
