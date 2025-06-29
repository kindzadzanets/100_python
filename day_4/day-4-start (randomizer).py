# https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences
# подключение внешнего кодового модуля (random)
import random
# import module1

# искомое значение для генерации случайного числа - зерно(seed), по-умолчанию Python использует локальное время компьютера как зерно, так же его можно установить вручную. От этого значения зависят все последующие генерации (ниже)
random.seed(89)


# случайное целое число
random_integer = random.randint(0, 10)
print(random_integer)


# случайная дробь, НО диапазон всегда: 0 - 0.99999999 .
random_float = random.random()
print(random_float)

# расширить диапазон случайной дроби можно умножением.
random_float_five = random_float * 5
print(random_float_five)

# случайная дробь с настраеваемым диапазоном от меньшего к большему числу, включая граничные значения
random_float_upper = random.uniform(5, 0)
print(random_float_upper)

# print(module1.pi)
