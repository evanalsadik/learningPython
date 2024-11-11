def converter():
    print ("***WELCOME TO UNIT CONVERTER***".center(110))
    print ("==python converter==".center(110), "\n")
    
    print ("KONVERSIKAN")
    unit_1 = input("Dari: ")
    unit_2 = input("ke: ")
    
    if unit_1 == "m" and unit_2 == "cm":
        while True:
            print ("\nMETER > CENTIMETER")
            angka = input("masukkan angka: ")
            if angka.isnumeric():
                cm = int(angka)*100
                print (angka, "m=", cm, "cm.")
            elif angka in ("b", "back"):
                converter()
            elif angka in ("q", "quit", "exit"):
                break
    
    if unit_1 == "cm" and unit_2 == "m":
        while True:
            print ("\nCENTIMETER > METER")
            angka = input("masukkan angka: ")
            if angka.isnumeric():
                cm = int(angka)/100
                print (angka, "cm=", m, "m.")
            elif angka in ("b", "back"):
                converter()
            elif angka in ("q", "quit", "exit"):
                break
    
converter()


    