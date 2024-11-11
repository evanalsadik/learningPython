class binatangbuas:
    def __init__(self, umur, cakar, taring):
        self.umur = umur
        self.cakar = cakar
        self.taring = taring 
        
    def berlari(self):
        print("60 km/s")
        
    def mati(self):
        print("telah mokad dua hari lalu")
    
        
class harimau(binatangbuas):
    def __init__(self, umur, cakar, taring):
        super().__init__(umur, cakar, taring) 
        
    def berburu(self):
        print("sendiri")

class singa(binatangbuas):
    def __init__(self, umur, cakar, taring, surai):
        super().__init__(umur, cakar, taring)
        self.surai = surai

    def berburu(self):
        print("rame-rame")

jedy = harimau(3, 4, 6)
abdul = singa(5, 9, 10, "lebat")

print ("\n\nini harimau namanya jedy")
print (jedy.cakar)
print (jedy.taring)
print (jedy.umur)
jedy.mati()
jedy.berburu()

print ("ini singa namanya abdul")
print (abdul.umur)
print (abdul.taring)
print (abdul.cakar)
print (abdul.surai)
abdul.berlari()
abdul.berburu()

print ("\nmereka suka bergelut seperti madara dan hasirama")