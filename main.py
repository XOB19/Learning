# TIPE DATA
data_string = 'snappy'
data_integer = 10
data_float = 5.3
data_boolean = True
data_complex = complex(5,6)


# CASTING DATA
a = 10
print('nilai a : ' + str(a))

# Mengambil Input Data dari User
data = input('masukan data : ')
print('data = ',data,'type = ',type(data))

# Operasi Aritmatika
pertambahan = '+'
pengurangan = '-'
perkalian = '*'
pembagian = '/'
eksponen_pangkat = '**'
modulus = '%'
floor_division = '//'
"() - exponen - perkalian-floor division - pertambahan"

# Operasi Komporasi (>,<,>=,<=,==,!=,is,is not)
a = 4 # assigment objek
b = 4
hasil = a is b
hasil2 = a is not b
print(hasil)
print(hasil2)
'''
is bisa digunakan hanya pada objek
'''

# Operasi Logika atau Boolean (not,or,and,xor(^))
## NOT (Kebalikan data awal)
print('===NOT===')
a = 4
c = not a
print('data a : ',a)
print('data c',c)

## OR (jika salah satu ada True maka True)
print('===OR====')
a = True
b = True
c = a or b
print(a,'OR',b,'=',c)
a = True
b = False
c = a or b
print(a,'OR',b,'=',c)
a = False
b = True
c = a or b
print(a,'OR',b,'=',c)
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)

## AND (jika salah satu ada False maka False)
print('===AND====')
a = True
b = True
c = a and b
print(a,'AND',b,'=',c)
a = True
b = False
c = a and b
print(a,'AND',b,'=',c)
a = False
b = True
c = a and b
print(a,'AND',b,'=',c)
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)

## XOR (jika beda maka True)
print('===XOR====')
a = True
b = True
c = a ^ b
print(a,'XOR',b,'=',c)
a = True
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)

# Operator Bitwise (operator masing-masing bit) ANGKA BINER
x = 9
y = 5

## bitwise OR (|)(jika salah satu ada True maka True)
z = x | y
print('\n=======OR======')
print('nilai : ',x,' , binary :',format(x,'08b'))
print('nilai : ',y,' , binary :',format(y,'08b'))
print('----------------(|)')
print('nilai : ',z,' , binary :',format(z,'08b'))

## bitwise AND (&)(jika salah satu ada False maka False)
z = x & y
print('\n=======AND======')
print('nilai : ',x,' , binary :',format(x,'08b'))
print('nilai : ',y,' , binary :',format(y,'08b'))
print('----------------(&)')
print('nilai : ',z,' , binary :',format(z,'08b'))

## bitwise XOR (^)(jika beda maka True)
z = x ^ y
print('\n=======XOR======')
print('nilai : ',x,' , binary :',format(x,'08b'))
print('nilai : ',y,' , binary :',format(y,'08b'))
print('----------------(^)')
print('nilai : ',z,' , binary :',format(z,'08b'))

## bitwise NOT (~)(miror dari o)
z = ~x
print('\n=======NOT======')
print('nilai : ',x,' , binary :',format(x,'08b'))
print('nilai : ',y,' , binary :',format(y,'08b'))
print('----------------(~)')
print('nilai : ',z,' , binary :',format(z,'08b'))
'''kalo pengen nge-flip 1->0/0->1 pake ini'''
print('----------------(^)')
v = 0b0000001001
w = 0b1111111111
print('nilai : ',v^w,' , binary :',format(v^w,'08b'))

## shift right (geser kanan)
z = x >> 2
print('\n=======>>======')
print('nilai : ',x,' , binary :',format(x,'08b'))
print('nilai : ',y,' , binary :',format(y,'08b'))
print('----------------(>>)')
print('nilai : ',z,' , binary :',format(z,'08b'))

## shift left (geser kiri)
z = x << 2
print('\n=======<<======')
print('nilai : ',x,' , binary :',format(x,'08b'))
print('nilai : ',y,' , binary :',format(y,'08b'))
print('----------------(<<)')
print('nilai : ',z,' , binary :',format(z,'08b'))

# Operator Assignment
t = 5

t += 2 #sama aja a = a + 2
t -= 2 #sama aja a = a - 2
t *= 2 #sama aja a = a * 2
t /= 2 #sama aja a = a / 2
t %= 2 #sama aja a = a % 2
t //= 2 #sama aja a = a // 2
t **= 2 #sama aja a = a ** 2

## Operator assigment bitwise
###  OR
u = True
print('\nnilai u =',u)
u |= False
print('nilai u |= False, nilai u menjadi',u)
u = False
print('\nnilai u =',u)
u |= False
print('nilai u |= False, nilai u menjadi',u)

###  AND
u = True
print('\nnilai u =',u)
u &= False
print('nilai u &= False, nilai u menjadi',u)
u = False
print('\nnilai u =',u)
u &= False
print('nilai u &= False, nilai u menjadi',u)

###  XOR
u = True
print('\nnilai u =',u)
u ^= False
print('nilai u ^= False, nilai u menjadi',u)
u = False
print('\nnilai u =',u)
u ^= False
print('nilai u ^= False, nilai u menjadi',u)

### geser-geser
u = 0b0100
print('\nnilai u =',format(u,'04b'))
u >>= 2
print('nilai u >>= 2 False, nilai u menjadi',format(u,'04b'))
u <<= 2
print('nilai u <<= 2 False, nilai u menjadi',format(u,'04b'))

# Pengenalan String
print('"hai apa kabar"')
print("'hai apa kabar'")
print("hai apa kabar a'tole")
print('hai apa kabar a\'tole') #tanda petik
print("C:\\user\\Ucup") #backlash
print("ucup\t\t\tjauh") #tab biar dijauhin
print("ucup \bdekat") #backspace biar mendekat
print("baris pertama \nbaris kedua") # LF -> line feed (unix,macos,linux)
print("baris pertama \rbaris kedua") # CR -> carriage return (commodore,acos,lisp)
print("baris pertama \r\nbaris kedua") # CRLF -> line feed carriage return (windows)
print(r'C:\new folder') # raw string (semuanya dianggap string termasuk simbol)
print('''
nama : ucup
kelas : 3
''') # multiline literal string (biar langsung enter)
print(r''' 
nama : ucup
kelas : 3
website : www.ucup-jago.com/newID
''') # multiline literal sring and raw (gabungan)

