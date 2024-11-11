#bitwise
#fokus pada bilangan biner (bagian format) dimana ada 0 dan 1.

# OR / |
a = 9
b = 5
c = a | b
print (c, format(c, '08b'))

# AND / &
c = a & b
print (c, format(c, '08b'))

# XOR / ^
c = a ^ b
print (c, format(c, '08b'))

# NOT / ~
c = ~a
print (c, format(c, '08b'))

#shifting

#SHIFT RIGHT / >>
c = a >> 1
print (c, format(c, '08b'))

#SHIFT LEFT / <<
c = a << 1
print (c, format(c, '08b'))

