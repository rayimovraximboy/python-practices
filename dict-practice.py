# Amaliyot
# 1
otam = {
    "ismi": "Anvar",
    "t_yil": 1984,
    "shahri": "Urganch",
    "manzili": "Xorazm viloyati",
    "kasbi": "Elektrik"
}
print(otam)
print(f"Otamning ismi {otam['ismi']}.")
print(f"Otam {otam['t_yil']} yilda tug'ilgan.")
print(f"Otamning kasbi {otam['kasbi']}.")

onam = {
    "ismi": "Sanobar",
    "t_yil": 1983,
    "shahri": "Urganch",
    "manzili": "Xorazm viloyati",
    "kasbi": "oshpaz"
}
print(onam)
print(f"Onamning ismi {onam['ismi']}.")
print(f"Onam {onam['t_yil']} yilda tug'ilgan.")
print(f"Onamning kasbi {onam['kasbi']}.")

# 2
taomlar = {
    "dilbek": "osh",
    "gulomjon": "manti",
    "elbek": "shashlik",
    "behruz": "somsa"
}
print(taomlar)
print(f"Dilbekning sevimli taomi {taomlar['dilbek']}.")
print(f"G'ulomjonning sevimli taomi {taomlar['gulomjon']}.")
print(f"Elbekning sevimli taomi {taomlar['elbek']}.")
print(f"Behruzning sevimli taomi {taomlar['behruz']}.")
# 3
python_lugat = {
    "integer": "butun son",
    "float": "o'nli son",
    "string": "matn",
    "if": "shart operatori",
    "else": "aks holda",
    "for": "takrorlash sikli",
    "while": "shartli sikl",
    "list": "ro'yxat",
    "dictionary": "lug'at",
    "boolean": "True yoki False qiymat"
}
text = input("Kalit so'zini kiriting: ")
print(python_lugat.get(text, "Bunday so'z mavjud emas"))
# 4
soz = input("So'z kiriting: ")
if soz in python_lugat:
    print("Tarjimasi:", python_lugat[soz], "deb tarjima qilinadi.")
else:
    print("Bunday so'z mavjud emas")
