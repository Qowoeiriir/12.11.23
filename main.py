# Задача 1

# class Passport():
#     def __init__(self, first_name, last_name, country, date_of_birth, numb_of_pasport):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.date_of_birth = date_of_birth
#         self.country = country
#         self.numb_of_pasport = numb_of_pasport
#
#     def PrintInfo(self):
#         print("\nFullname: ", self.first_name, " ", self.last_name)
#         print("Date of birth: ", self.date_of_birth)
#         print("County: ", self.country)
#         print("Passport number: ", self.numb_of_pasport)
#
#
# class ForeignPassport(Passport):
#     def __init__(self, first_name, last_name, country, date_of_birth, numb_of_pasport, visa):
#         super().__init__(first_name, last_name, country, date_of_birth, numb_of_pasport)
#         self.visa = visa
#
#     def PrintInfo(self):
#         super().PrintInfo()
#         print("Visa: ", self.visa)
#
#
# PassportList = []
# request = ForeignPassport('Ivan', 'Ivanov', 'Russia', '12.03.1967', '123456789', 'USA')
# PassportList.append(request)
# request = Passport('Иван', 'Иванов', 'Россия', '12.03.1967', '45001432')
# PassportList.append(request)
# request = ForeignPassport('Peter', 'Smit', 'USA', '01.03.1990', '21435688', 'Germany')
# PassportList.append(request)
# for emp in PassportList:
#     emp.PrintInfo()

# Задача 2

# class Equipment:
#     def __init__(self, name, make, year):
#         self.name = name
#         self.make = make
#         self.year = year
#
#     def action(self):
#         return 'Не определено'
#
#     def __str__(self):
#         return f'{self.name} {self.make} {self.year}'
#
#
# class Printer(Equipment):
#     def __init__(self, series, name, make, year):
#         super().__init__(name, make, year)
#         self.series = series
#
#     def __str__(self):
#         return f'{self.name} {self.series} {self.make} {self.year}'
#
#     def action(self):
#         return 'Печатает'
#
# class Scaner(Equipment):
#     def __init__(self, name, make, year):
#         super().__init__(name, make, year)
#
#     def action(self):
#         return 'Сканирует'
#
#
# class Xerox(Equipment):
#     def __init__(self, name, make, year):
#         super().__init__(name, make, year)
#
#     def action(self):
#         return 'Копирует'
#
# sklad = []
#
# scaner = Scaner('Mustek','BearPow 1200CU', 2010)
# sklad.append(scaner)
#
# xerox = Xerox('Xerox','Phaser 3120', 2019)
# sklad.append(xerox)
#
# printer = Printer("1200",'hp', 'Laser Jet', 2018)
# sklad.append(printer)
#
# print("На складе имеются:")
#
# for x in sklad:
#      print(x,end=' ')
#      print(x.action())
#
# for x in sklad:
#      if isinstance(x,Printer):
#          sklad.remove(x)
#
# print("На складе осталось:")
# for x in sklad:
#       print(x,end=' ')
#       print(x.action())

# Задача 3

# from random import
#
# class Soldier:
#            def __init__(self,name='Noname',health = 100):
#                self.name = name
#                self.health = health
#            def set_name(self, name):
#                self.name = name
#            def make_kick(self, enemy):
#                enemy.health -= 20
#            if enemy.health<0:
#                        enemy.health = 0
#                self.health += 10
#
# print(self.name, "бьет", enemy.name)
# print('%s = %d' % (enemy.name, enemy.health))

# Задача 4

# import time, random
#
# class Card:
#     NumsList = ['Джокер', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
#     MastList = ['Пики', 'Крести', 'Бубни', 'Черви']
#
#     def __init__(self, i, j):
#         self.Mastb = self.MastList[i - 1]
#         self.Num = self.NumsList[j - 1]
#
# class DeckOfCards:
#     def __init__(self):
#         self.deck = [None] * 56
#         k = 0
#         for i in range(1, 4 + 1):
#             for j in range(1, 14 + 1):
#                 self.deck[k] = Card(i, j)
#                 k += 1
#
#     def shuffle(self):
#         random.shuffle(self.deck)
#
#     def get(self, i):
#         if 0 <= i <= 55:
#             answer = self.deck[i].Num
#             answer += " "
#             answer += self.deck[i].Mastb
#         else:
#             answer = "В колоде только 56 карт"
#         return answer
#
# d = DeckOfCards()
# d.shuffle()
# print('Выберите карту из колоды в 56 карт: ')
# a = int(input())
# if a <= 56:
#     card = d.get(a - 1)
#     print(f'Вы взяли карту: {card}', end='.\n')
# else:
#     print("В колоде только 56 карт")

# Задача 5

# class Vector3D:
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def display(self):
#         print(f'{self.x}, {self.y}, {self.z}')
#
#     def read(self):
#         self.x = int(input('Введите x: '))
#         self.y = int(input('Введите y: '))
#         self.z = int(input('Введите z: '))
#
#     def __add__(self, other):
#         if isinstance(other, Vector3D):
#             return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
#         else:
#             raise ValueError("Можно добавить только один объект")
#
#     def __sub__(self, other):
#         if isinstance(other, Vector3D):
#             return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
#         else:
#             raise ValueError("Можно только вычесть другой объект Vector3D.")
#
#     def __mul__(self, other):
#         if isinstance(other, int) or isinstance(other, float):
#             return Vector3D(self.x * other, self.y * other, self.z * other)
#         elif isinstance(other, Vector3D):
#             return self.x * other.x + self.y * other.y + self.z * other.z
#         else:
#             raise ValueError("Умножение не поддерживается для этого типа данных.")
#
#     def __matmul__(self, other):
#         if isinstance(other, Vector3D):
#             return Vector3D(
#                 self.y * other.z - self.z * other.y,
#                 self.z * other.x - self.x * other.z,
#                 self.x * other.y - self.y * other.x,
#             )
#         else:
#             raise ValueError("Можно вычислить векторное произведение только с другим объектом Vector3D.")
#
# vec1 = Vector3D(4, 1, 2)
# vec1.display()
#
# vec2 = Vector3D()
# vec2.read()
#
# vec3 = Vector3D(1, 2, 3)
#
# vec4 = vec1 + vec2
# vec4.display()
#
# a = vec4 * vec3
# print(a)
#
# vec4 = vec1 * 10
# vec4.display()
#
# vec4 = vec1 @ vec3
# vec4.display()

# Задача 6

# import math
# class Triangle:
#     def __init__(self, side1, side2):
#         self.side1 = side1
#         self.side2 = side2
#
#     def increase_side(self, percent):
#         self.side1 *= 1 + percent / 100
#         self.side2 *= 1 + percent / 100
#
#     def decrease_side(self,  percent):
#         self.side1 *= 1 - percent / 100
#         self.side2 *= 1 - percent / 100
#
#     def radius_of_circumscribed_circle(self):
#         return (self.side1 * self.side2) / (2 * math.sqrt(self.side1**2 + self.side2**2))
#
#     def perimeter(self):
#         return self.side1 + self.side2 + math.sqrt(self.side1**2 + self.side2**2)
#
#     def angles(self):
#         angle1 = math.degrees(math.asin(self.side1 / self.perimeter()))
#         angle2 = math.degrees(math.asin(self.side2 / self.perimeter()))
#         angle3 = 180 - angle1 - angle2
#         return angle1, angle2, angle3
#
# triangle = Triangle(5, 8)
# print(f"Стороны: {triangle.side1} {triangle.side2}")
#
# triangle.increase_side(10)
# print(f"Стороны после увеличения на 45%: {triangle.side1} {triangle.side2}")
#
# triangle.decrease_side(15)
# print(f"Стороны после уменьшения на 30%: {triangle.side1} {triangle.side2}")
#
# print(f'Радиус окружности: {triangle.radius_of_circumscribed_circle()}')
# print(f'Периметр треугольника: {triangle.perimeter()}')
# print(f'Значения углов: {triangle.angles()}')

# Задача 7

# class Bus:
#     def __init__(self):
#         self.speed = 0
#         self.capacity = 0
#         self.maxSpeed = 100
#         self.passengers = []
#         self.hasEmptySeats = False
#         self.seats = {}
#
#     def boarding(self, passenger_names):
#         for name in passenger_names:
#             if len(self.passengers) < self.capacity:
#                 self.passengers.append(name)
#                 self.seats[name] = True
#                 print(f"{name} сел в автобус.")
#             else:
#                 print(f"Нет свободных мест для {name}.")
#
#     def getOff(self, passenger_names):
#         for name in passenger_names:
#             if name in self.passengers:
#                 self.passengers.remove(name)
#                 self.seats[name] = False
#                 print(f"{name} вышел из автобуса.")
#             else:
#                 print(f"{name} его нет в автобусе.")
#
#     def increaseSpeed(self, value):
#         if self.speed + value <= self.maxSpeed:
#             self.speed += value
#             print(f"Скорость увеличилась до {self.speed} км/ч.")
#         else:
#             print("Автобус не может превышать максимальную скорость.")
#
#     def decreaseSpeed(self, value):
#         if self.speed - value >= 0:
#             self.speed -= value
#             print(f"Скорость снизилась до {self.speed} км/ч.")
#         else:
#             print(f"Скорость не может быть ниже 0 км/ч.")
#
#     def __contains__(self, passenger_name):
#         return passenger_name in self.passengers
#
#     def __iadd__(self, passenger_name):
#         self.boarding([passenger_name])
#         return self
#
#     def __isub__(self, passenger_name):
#         self.getOff([passenger_name])
#         return  self
#
# bus = Bus()
# bus.capacity = 50
# bus.boarding(['Костя', 'Cтёпа', 'Никита'])
# bus.increaseSpeed(25)
# bus += "Стёпа"
# bus -= "Никита"
# if "Костя" in bus:
#     print("Костя сел в автобус")



