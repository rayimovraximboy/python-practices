def foydalanuvchi_malumotlari(ismi, familiyasi, tugilgan_yili, tugilgan_joyi, email=None, tel_raqam=None):
    foydalanuvchi = {
        'ism': ismi,
        'familiya': familiyasi,
        't_yil': tugilgan_yili,
        't_joy': tugilgan_joyi, 
        'email': email,
        'tel_raqam': tel_raqam
    }
    return foydalanuvchi

foydalanuvchi1 = foydalanuvchi_malumotlari('Olim','Hakimov',1990,'Urganch')
foydalanuvchi2 = foydalanuvchi_malumotlari('Lola','Hakimova',1992,'Urganch','sanobar@gmail.com','912345678')
print(foydalanuvchi1)
print(foydalanuvchi2)

def meva_turlari(nomi, rangi, narhi=None):
    meva = {
        'nomi': nomi,
        'rangi': rangi,
        'narh': narhi,
        'qayerda pishadi': 'O\'zbekiston'
    }
    return meva

meva1 = meva_turlari('olma', 'qizil')
meva2 = meva_turlari('gilos', 'yashil', 5000)
print(meva1)
print(meva2)

def telfon_turlari(brendi, modeli, rangi, narhi=None):
    telefon = {
        'brendi': brendi,
        'modeli': modeli,
        'rangi': rangi,
        'narh': narhi,
        'qayerda ishlab chiqarilgan': 'Xitoy'
    }
    return telefon

telefon1 = telfon_turlari('Redmi', 'Note 10', 'teal', 2000500)
telefon2 = telfon_turlari('Samsung', 'Galaxy S21', 'yashil')
print(telefon1)     
print(telefon2)