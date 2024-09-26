import time
import random

print("BlackJack Oyunuma Hoşgeldiniz!")

while True:
    baslangic = input("Bir Seçeneği Seç\n1 - Oyuna Başla\n2 - Oyun Nasıl Oynanır?\n>>> ")

    if baslangic == "2":
        print("Bu adrese Git : https://tr.wikipedia.org/wiki/Yirmibir")
        break
    
    if baslangic == "1":
        print("Oyun Başlıyor!")

        sayilar = [2, 3, 4, 5, 6, 7, 8, 9]

        bot = random.choice(sayilar)*3

        sen = random.choice(sayilar)

        print("Şu anki eliniz : ")
        print(sen) 

        while True:
            dord = input("Devammı Durcanmı : ")

            if dord == "devam":
                sen = sen+random.choice(sayilar)
                print("Yeni Eliniz : ")
                print(sen)

            if dord == "dur":
                print("Botun Eli :")
                print(bot)
                time.sleep(1)
                print("\nSenin Elin :")
                print(sen)
                time.sleep(0.5)

                if sen > 21:
                    print("Kaybettiniz Maalesef...")
                    break

                elif bot > sen:
                    print("Kaybettiniz Maalesef...")
                    break

                elif bot < sen:
                    print("Kazandınız Helal!!!")
                    break