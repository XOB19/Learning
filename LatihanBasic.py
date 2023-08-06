#Latihan Perhitungan Sederhana(konversi suhu)
print('\n Masukan Konversi Suhu \n')

## Farenhaei to Kelvin
farenheit1 = float(input('masukan suhu dalam farenheit : '))

celcius1 = (5/9)*(farenheit1 - 32)
kelvin1 = celcius1 + 273
print('fareheit to kelvin',kelvin1)

## Kelvin to Farenheit
kelvin2 = float(input('masukan suhu dalam kelvin : '))

celcius2 = (kelvin2 - 273)
farenheit2 = (9/5)*(celcius2 + 32) 

print('fareheit to kelvin',farenheit2)

#Latihan Komparasi dan Logika
## ---------0+++++++5--------8++++++11--------
inputuser = float(input('masukan angka : '))

data1 = inputuser > 0
data2 = inputuser < 5
data3 = inputuser > 8
data4 = inputuser < 11

hasil1 = data1 and data2
hasil2 = data3 and data4

isCorect1 = hasil1 or hasil2

print('angka yang anda masukan : ',isCorect1)

## +++++++0-------5++++++8-------11++++++
inputuser = float(input('masukan angka : '))

data5 = inputuser < 0
data6 = inputuser > 5
data7 = inputuser < 8
data8 = inputuser > 11

hasil3 = data6 and data7
hasil4 = data5 or data8

isCorect2 = hasil3 or hasil4

print('angka yang anda masukan : ',isCorect2)

#
