saldo_awal = 5000
deposit = input('Berapa mau depositnya: ')

try:
    deposit = int(deposit)
except ValueError:
    try:
        deposit = float(deposit)
    except ValueError:
        print('Masukkan harus berupa angka.')
        exit()

saldo_total = saldo_awal + deposit
hutang = 50_000

print('Total saldo awal Anda dengan deposit adalah: ' + str(saldo_total))

if saldo_total >= hutang:
    print('Anda bisa bayar hutang.')
else:
    print('Anda belum bisa bayar hutang.')
