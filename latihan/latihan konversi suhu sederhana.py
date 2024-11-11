#konversi suhu
print ("**Program Konversi Suhu**".center(50), "\n")

#celcius
celsius = float(input("masukkan suhu dalam Celsius: "))

#reamur
reamur = (4/5) * celsius;
print ("suhu dalam reamur adalah: ", reamur, " reamur\n")

#fahrenheit
fahrenheit = ((9/5) * celsius) + 32;
print ("suhu dalam fahrenheit adalah: ", fahrenheit, " fahrenheit\n")

#kelvin
kelvin = celsius + 273;
print ("suhu dalam kelvin adalah: ", kelvin, " kelvin\n")
