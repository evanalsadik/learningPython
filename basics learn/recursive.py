def password():
    pw = input("masukkan password: ")
    if pw == "12":
        print("akses diterima")
    else:
        print("akses ditolak")
        password()
        
password()


import time

def _recurse():
    string = "python"
    number = 0
    for i in string:
        number += 10
        print(i.center(number))
        time.sleep(0.4)
        if i == string[-1]:
            _recurse()
            
_recurse()
        