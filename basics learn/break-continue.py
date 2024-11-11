x = "sup man, get the fuck out of my face"

#for-loop berhenti
for i in x:
    print(i, "\n\n")
    if i == "y":
        break

#for-loop skip
for i in x:
    if i == "u":
        continue 
    print(i, "\n")
    
#while-loop berhenti 
n = 0

while True:
    n += 1
    print(n, "\n")
    if n == 20:
        break
    
#while-loop skip
n = 0

while True:
    n += 1
    if n == 10:
        continue
    print(n)
    if n == 20:
        break