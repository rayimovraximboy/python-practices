# # do'stlar bilan gaplashish
# dostlar = ['Dilbek', 'Elbek', 'Gulomjon', 'Gulomjon2', 'Bexruz']
# print(f"Salom {dostlar[0]}, bugun choyhona bormi\n{dostlar[1]} choyxonaga boramizmi?")
# print(f"{dostlar[0]} va {dostlar[3]} sinfdoshlar")

# # sonlar bila ishlash
# sonlar = [ 15, 22.5, 35, 123, -95.3, 7, 8, 20]
# sonlar[1] = 22.5
# print(sonlar[1] + sonlar[5])

# # tarixiy va futbol shaxslari
# t_shaxslar = ['Jaloliddin Manguberdi','Hukmdor Usmon', 'Al-Xorazmiy']
# f_shaxslar = ['Cristiono Ranoldo', 'Steve Jobs', 'Kilyan Mbappe']
# print(f"Men tarixiy shaxslardan {t_shaxslar[2]} bilan,\n futbol shaxslardan esa {f_shaxslar[0]} bilan,suhbat qilishni istar edim.")

# # friends nomli ro'yhat
# friends = []
# friends.append('Dilbek')
# friends.append('Sherzod')
# friends.append('Jaxongir')
# friends.append('Jamshid')
# friends.append('Aslbek')
# print(friends)

# # yuqoridagi ro'yhatni remove bilan o'chirish
# friends.remove('Aslbek')
# friends.remove('Dilbek')
# print(friends)

# #ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shish
# friends.append('Xursand')
# friends.insert(1, 'Dilshod')
# friends.insert(3, 'Bexruz')
# print(friends)

# friends = ['Dilbek', 'Elbek', 'Gulomjon', 'Gulomjon2', 'Bexruz']
# # List.sort()
# friends.sort()
# print(friends)
# friends.sort(reverse=True)
# print(friends)
# # sorted() function
# sorted_list =sorted(friends)
# print(sorted_list)

# nums = [12, -5, 0, 8.75, 99, 10]
# nums.sort(reverse=True)
# print(nums)
# print(sorted(nums, reverse=True)) 

# # list() function
# users = ['Jhon', 'alisa', 'aziz', 'alex']
# cars = list(('BMV', 'Nissan GTR', 'Audi', 'Ford'))
# print(cars)

# range() - ma'lum bir oraliqdagi sonlarni shakllantirish uchun ishlatiladi
# range(start, stpo, step?)
# step_default_value = 1
# range(1, 10) # 1, 2, 3, 4, 5, 6, 7, 8, 9
print(list(range(1, 10))) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_nums = list(range(2, 20, 2))
print(even_nums)
odd_nums = list(range(1, 20, 2))
print(odd_nums)

# Sodda ro'yxat ustida sodda amallar
narxlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# min() / max() / sum()
eng_arzon = min(narxlar)
eng_qimmat = max(narxlar)
yigindi = sum(narxlar)
print(eng_arzon, eng_qimmat, yigindi)

# Ro'yxat kesib olish
students = ('Akmal', 'Jasur', 'Asal', 'Kumush', 'Maftuna', 'Dilshod')
# new_list = list[start_index : end_index]
# 1-case
students1 = students[2 : 5]
students2 = students[0 : 2]
print(students1, students2)
# 2-case
students3 = students[2 : ] # start_index dan boshlab oxrigacha kesib oladi
print(students3)
# 3-case
students4 = students[ : 4] # ro'yxat boshidan end_index gacha kesadi
print(students4)

# 0 dan boshlab indekslanadi
# manfiy index -41 dan boshlanadi (-1, -2, -3)
print(students[-1])
print(students[-2])
print(students[-5])
print(students[-4 : -2])

# # Ro'yxatdan nusxa(copy) olish
# # 1. Shallow(sayoz) copy
# sonlar = [1, 5, -5, 12]
# # sonlar2 = sonlar
# # sonlar2.append(77)
# # sonlar.insert(2, -8)
# # print(sonlar2)

# # 2.Deep(chuqur) copy
# sonlar3 = sonlar[:]
# sonlar3.append(8)
# print(sonlar3)
# print(sonlar)

# # deep copy using copy library
# import copy
# original_list = [1, 2, [3, 4], 5]
# deep_copy = copy.deepcopy(original_list)

# deep_copy[2].append(99)
# print(deep_copy)
# print(original_list)

# # Tuple - o'zgarmas ro'yhat
# toys = ('bus', 'car', 'bear', 'snake', 'dino')
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])
# # toys[1] = 'dragon'
# # print(toys) # error

# toys =list(toys)
# toys[1] = 'dragon'
# toys.remove('dino')
# toys.append('mcqueen')
# toys = tuple(toys)
# print(toys)

# Amaliyot
# davlatlar = ['Ispaniya', 'Fransiya', 'Portugaliya', 'Angliya', 'Italiya']
# print(davlatlar)
# print(sorted(davlatlar))
# print(sorted(davlatlar, reverse= True))
# davlatlar.reverse()
# print(davlatlar)
# #reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
# davlatlar.reverse()
# print(davlatlar)

# davlatlar.sort()
# print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar)

# sonlar = list(range(120,1200,2))
# # boshidan 20 ta element
# print(sonlar[ : 20])
# # o'rtasidan 20 ta element
# print(sonlar[ -20 : ])
# # oxirdan 20 ta element
# length = len(sonlar)
# start_index = length // 2 - 10
# end_index  = length // 2 + 10
# print(sonlar[start_index : end_index])

# #taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
# taomlar = ['osh','somsa','baliq','shashlik','barak']
# print(taomlar)

# range(start, stop, step)
# nonushta = taomlar [:]
# nonushta.remove('somsa')
# nonushta.remove('shashlik')
# nonushta.remove('barak')
# nonushta.append('pecheniya va qaymoq')
# nonushta.append('issiq non')

# print(taomlar)
# print(nonushta)
# nonushta = tuple(nonushta)
# taomlar[0] = "non va bogrsoq"





