
# 4.4. Используя лямбда выражение, получите результат перемножения значений в списке
from functools import reduce

my_list = [20, 15, 2]
positive_list = reduce(lambda x, y: x*y, my_list)
print(positive_list)

#positive_list = (lambda x, y: x*y, my_list)
