#operasi assignment

#operasi matematika biasa
a = 5
#a = a + 1
#print (a)

#lebih singkat (hasil sama - cara berbeda)
a += 1
print (a)

a -= 2
print (a)

a *= 5
print (a)

a /= 2
print (a)

b = 10
b %= 3
print (b)

b = 10
b //= 3
print (b)

c = 7
c **= 2
print (c, "\n")


#operasi binary
e = True
e |= False
print ("\n", e)
e = False
e |= False
print (e)

e = True
e &= False
print ("\n", e)
e = True
e &= True
print (e)

e = True
e ^= False
print ("\n", e)
e = True
e ^= True
print (e)

#geser geser (angka biner)
f = 0b0100
print ("\n", f, format(f, "04b"))

f >>= 2
print (f, format(f, "04b"))

f <<= 1
print (f, format(f, "04b"))








