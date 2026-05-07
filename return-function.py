# print("a" * 3) # a harfi 3 marta takrorlanadi
# print("abc" * 5) # abc harfi 5 marta takrorlanadi
# print("abc" + 2) # TypeError: can only concatenate str (not "int") to str         
# print("abc" / 5) # TypeError: unsupported operand type(s) for /: 'str' and 'int'

# def is_even(num = 8):
#     if num % 2 == 0:
#         return "Juft son"
#     else:
#         return "Toq son"

# print(is_even(4)) # Juft son
# result = is_even(7)
# print(result) # Toq son

# Ternary operator yordamida yuqoridagi  is_even funksiyasini qisqartirish mumkin:
# syntax: value_if_true if condition else value_if_false
# def is_even(num):   
#     return "Juft son" if num % 2 == 0 else "Toq son"

# print(is_even(4)) # Juft son
# print(is_even(7)) # Toq son

# # a = int(input("Son kiriting: "))
# # print(is_even(a))


# vowels = ["a", "e", "i", "o", "u"]
# def count_vowles(text):
#     count = 0
#     for char in text:
#         if char in vowels:
#             count += 1
#     return count

# print(count_vowles("javascript")) # 3
# print(count_vowles("frontender")) # 2
# print(count_vowles("bbbb")) #0

# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     """Toliq isma qaytaruvchi funksiya"""
#     if otasining_ismi: # otasining_ismi mavjudligini tekshiramiz
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()

# talaba1 = toliq_ism_yasa('olim','hakimov') #otasining_ismi kiritilmadi
# talaba2 = toliq_ism_yasa('hakim','olimov','abrorovich')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
    return avto
avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
print(avto1)
print(avto2)




