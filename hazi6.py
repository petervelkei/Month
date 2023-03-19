# fv, ami bekér egy dátumot és eldönti, hogy milyen évszak - adja vissza az eredményt
# 2023-01-15
# tél: 12 01 02
# tavasz: 03 04 05
# nyár: 06 07 08
# ősz: 09 10 11


ido = input("adjon meg egy dátumot: ")
honap = ""
kellfigyelni = False

for betu in ido:

  # ÁLLAPOTGÉP
    # az első kötőjelnél nincs bekapcsolva, akkor bekapcsoljuk
    if betu == "-" and kellfigyelni == False:
        kellfigyelni = True
    # azért else, hogy ne történjen meg azonnal, legkorábban a köv. ciklusban
    elif kellfigyelni == True and betu == "-":
        kellfigyelni = False
      
    if kellfigyelni == True:
      if betu != "-":
        honap += betu


if honap == "12" or honap == "01" or honap == "02":
    print("Tél")
elif honap == "03" or honap == "04" or honap == "05":
    print("Tavasz")
elif honap == "06" or honap == "07" or honap == "08":
    print("Nyár")
elif honap == "09" or honap == "10" or honap == "11":
    print("Ősz")
else:
    print("Ilyen dátum nem létezik.")

