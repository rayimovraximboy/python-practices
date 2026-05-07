# lambda function - anonymous(maxfiy, nomalum) function
# syntax:
# lambda arguments : expression(ifoda)
# x = lambda a : a % 5
# print(x(12))

# import math as m
# uzunlik = lambda pi, r : 2 * pi * r
# print(uzunlik(m.pi, 5))

# def daraja(n):
#     return lambda x : x ** n

# kvadrat = daraja(2)
# print(kvadrat(5))
# kub = daraja(3)
# print(kub(7))




# map() va filter()
# numbers = list(map(int, input().split()))
sonlar = [5, 8, -8, 0, 13]
# sonlar2 = []
# for son in sonlar:
#     sonlar2.append(son * 2)


# print(sonlar2)

# map(function, iterable)
print(list(map(lambda x : x * 2, sonlar)))
print(list(map(lambda x : x % 3, sonlar)))

# filter(function, iterable)
print(list(filter(lambda x: x > 5, sonlar)))
students = ['Dilbek', 'Elbek', 'Lobar', "G'ulomjon", "Bexruz", "Zilola", "Lola", "Zuhra"]
new_lst = list(map(lambda ism: ism.lower(), students))
print(list(filter(lambda ism: ism.startswith('l'), new_lst)))

def function(x):
    return x + 5

print(list(map(function, sonlar)))
