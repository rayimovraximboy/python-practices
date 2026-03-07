# students = ["Alice", "Bob", "CHarline", 'David', "Eve"]
# for student in students:
#     print(student)

# # 1 - interatsiya student = "Alice"
# # 2 - interatsiya student = "Bob"
# # 3 - interatsiya student = "Charlie"
# # 4 - interatsiya student = "David"
# # 5 - interatsiya student = "Eve"

# for guest in students:
#     print(f"Hurmatli {guest}, sizni interviewga taklif qilmoqchiman.")
#     print("Hurmat bilan, Al-Xorazmiy vorislari loyihasi.")

# # Sonlar ro'yhati uchun for loop
# even_numbers = list(range(2, 51, 2)) # 2 dan 50 gacha bo'lgan sonlar ro'yhati
# for number in even_numbers:
#     print(number)

# print("Dastur tugadi.")

# # 1 ning kvadrati 1 ga teng.
# # 2 ning kvadrati 4 ga teng.    
# # 3 ning kvadrati 9 ga teng.
# sonlar = list(range(1, 11)) # 1 dan 10 gacha bo'lgan sonlar ro'yxati
# for son in sonlar:
#     print(f"{son} ning kvadrati {son ** 2} ga teng.")


# # takrorlash operatorlari
# # loop - skil
# # 1. for loop
# # 2. while loop
# students = ['Elbek', 'Maftuna', "G'ulomjon", 'Mahliyo', 'Dilbek']
# # print(students[0])
# # print(students[1])
# # print(students[2])
# # print(students[3])
# # print(students[4])
# for student in students:    
#     print(student)

# numbers = list(range(20))
# # start_default_value = 0
# # stop = 20
# # step_default_value = 1
# print(numbers)  

# for number in numbers:
#     print(number)

# people = ["Dilbek", "Ronoldo", "Mbappe", "Vini Jr"]
# for person in people:
#    print(person)

# # 2 - usul: range() funksiyasi yordamida indekslar orqali iteratsiya qilish
# for index in range(len(people)):
#     print(index)
#     print(people[index])

# print("Dastur tugadi")

# # 1 - iteratsiya index = 0, people[index] = "Alice"
# # 2 - iteratsiya index = 1, people[index] = "Bob"
# # 3 - iteratsiya index = 2, people[index] = "Chalice"
# # 4 - iteratsiya index = 3, people[index] = "David"
# # 5 - iteratsiya index = 4, people[index] = "Eve"

# # 1 dan 100 gacha bo'lgan sonlarni chiqarish
# sonlar = list(range(1, 100))
# for son in sonlar:
#     print(son)    
# 2-usul
# for son in range(1, 101):
#     print(son)

# ro'yhat elementlarini index orqali olish
# for index in range(len(sonlar)):
#     print(index)
#     print(sonlar[index])

# 1-marta: index = 0 => sonlar(0) = 1
# 2-marta: index = 1 => sonlar(1) = 2
# ...
# 99-marta: index = 98 => sonlar[98] = 99


# # 1 ning kvadrati 1 ga teng
# # 2 ning kvadrati 4 ga teng
# # 3 ning kvadrati 9 ga teng
# for number in range(1, 20):
#     print(f"{number} ning kvadrati {number ** 2} ga teng")

# number_of_friends = input("do'stingizni sonini kiriting")
# friends = []
# if (number_of_friends == 0):
#     print("Sizning do'stingiz yo'qmi?")
# else:
#     for n in range(5):
#        friend = input(f"{n + 1}-dostingizni kiriting")
#        friends.append(friend)
# print(friends)

# Amaliyot
# ismlar = ("Xursand", "Akmal", "Jamshid", "Asilbek", "Murodbek")
# for ism in ismlar:
#     print(f"Salom aleykum, {ismlar}. Maktabga xush kelibsiz")

# print(f"Code {len(ismlar)} marta takrorlanadi")

# # 10 dan 100 gacha bo'lgan  sonlarni chiaring va undan toq sonlar toping
# sonlar = list(range(11, 100, 2)) 
# for son in sonlar:
#     print(son**3)

# # 5 ta sevimli kino kiritinh
# kinolar = []
# for k in range(5):
#     kino = input(f"{k + 1} sevimli kinoingiz qaysilar?")
#     kinolar.append(kinolar)
# print(kinolar)    

# # Nechta odam bilan gaplashganingizni yozing
# ismlar = []
# for n in range(3):
#     ism = input(f"{n + 1}Bugun necha kishi bn suhbat qildingiz?")
#     ismlar.append(ism)
# print(ismlar)

# for son in range(11):
#     print(son)

# s = 0
# numbers = [12, 5, 18, 25, 23]
# for number in numbers:
#     # print(number)
# # print(sum(numbers))
#  s += number # s = s + number
# print(s)

# summa = 0
# # 1 dan 50 gacha b'lgan
# for son in range(1, 50, 2):
#    summa += son

# print(summa)

# numbers = [12, 5, 18, 25, 23, 88]
# import math
# l = len(numbers)
# k = 1
# for number in numbers:
#     k *= number
# a = math.pow(k, 1 / 1)
# print(a)
# # o'rtacha qiymati = s / lenght
# o'rta geometrik = 
# for number in numbers:
#     s += number
# average_value = s / len(numbers)
# print(average_value)

# # 1 dan 20 gacha bo'lgan juft sonlarni o'rta arifmetikini toping
# s = 0
# for number in range(1, 21, 2):
#     s += number

# nums = list(range(1, 21, 2))
# average_value = s / len(nums)
# print(average_value)

# n! = 1 * 2 * 3 * ... * (n - 1) * n
# k = 1


# for son in range(1, 20): 
#     k *= son # k = k * son

# print(k)

# 1 dan 10 gacha bo'lgan juft sonlarni ko'paytmasi va yig'indisiga nisbati
# s = 0
# k = 1
# numbers = range(2, 11, 2)

# for n in numbers:
#     s += n
#     k *= n
# sum_even = sum(numbers)
# a = k / sum_even

# print(a)


# 1 dan 20 gacha bo'lgan juft sonlarni ko'paytmasi va yig'indisiga nisbati
# s = 0
# k = 1
# for number in range(1, 21):
#     if number % 2 == 0:
#          k *= number
#     else:
#          s *= number

# y = k / s
# print(y)
# s = 0
# counter = 0
# numbers = [7, 97, -58, 90]
# for number in numbers:
#     if number % 2 == 0:
#         s += number
#         counter += 1

# print(s / counter)

# s = 0
# counter = 0
# numbers = [97, 97, -92, 14, 22]
# for son in numbers:
#     if son % 2 == 0:
#         s += son
#     elif son % 3 == 0:
#         s += son
#     elif son % 5 == 0:
#         s += son

# print(s)

# s = 0
# counter = 0
# numbers = [76, 12, 51, 50, 98]
# for number in numbers:
#     if number % 2 == 1:
#         s += number
#         counter += 1

# print(s / counter)

# Vazifa
# 115-mashq
# numbers =[85, 15, 57, 68, 18, 67, 7, 45, 69, 21, 1, 5, 98, 34]
# m = int(input("m sonni kiriting"))    
# s = 0
# for number in numbers:
#         if number < m:
#                 s += number ** 2

# print(s)
# 122-mashq
# numbers = [44, 59, -75, 73]
# s = 0
# p = 0
# n = int(input("n sonni kiriting "))
# kv_yigindi = 0
# for son in numbers: 
#     p += son **2
#     s += son

# ortacha_qiymat = s / len(numbers)
# print(p)
# print(ortacha_qiymat)

# 126-mashq
import math
# nums = [7, 24, -5, 23, 99, -3, 24, 51]
# # nums[2] = 12
# s = 0
# for num in nums:
#     s += num
# lenght = len(nums)
# average_value = s / len(nums)
# log_value = math.log(average_value)

# for index in range(lenght):
#     if nums[index] < 0:
#         nums[index] = log_value
# print(k)
#  
# Vazifa
# 110
# k = 31
# m = 3
# numbers = [7, 11, 83, 18, 31]
# n = int(input("n sonni kiriting"))
# s = 1
# t  = False
# for son in numbers:
#     if son % k == 0 or son % m == 0:
#         s *= son
#         t = True

# print(s) 
# 104
# numbers = [74, 0, 1, 33]
# min_value = min(numbers)
# last_element = numbers[-1]
# # print(numbers.index(1)) // 2
# # numbers[3] = 75
# min_index = numbers.index(min_value)                                                                          
# numbers[min_index] = last_element
# numbers[-1] = min_value
# print(*numbers)

k = int(input("k o'rinni o'zingiz kiriting"))
numbers = [29, 50, -14, 4, 27, -56]
max_value = max(numbers)
max_index = numbers.index(max_value) 
numbers[max_index] = numbers[k - 1]        
numbers[k - 1] = max_value                                                         
print(*numbers)

# a = 5 
# b = 2
# result: a = 2; b = 5
# 1-usul
# a, b = b, a
 
# 2-usul
# c = a
# a = b
# b = c
# print(a, b)


# numbers = [3, 17, -59]
# s = 0
# for index in range(len(numbers)):
#     if (index + 1) % 2 == 0:
#       s += numbers[index]

# for number in numbers:
#    if number % 2 == 1:
#       print(number / s, " ")
#    else:
#       print(number, " ")

