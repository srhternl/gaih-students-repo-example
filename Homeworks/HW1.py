import random # random fonksiyonun import ettim.

prime_numbers = list() # asal sayıları listede tutmak için değişken tanımladım.

for i in range(1, 1000): # 1-1000 arasındaki asal sayıları bulan döngüm.
    if i != 1 and i != 0:
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            prime_numbers.append(i)

matrix = [["" for i in range(3)] for j in range(3)] # Liste biçiminde 3x3 default bir matris tanımladım.

for row in range(len(matrix)): # matrisin satır ve sütununa asal sayıları rastgele yerleştirdiğim döngü.
    for column in range(len(matrix)):
        matrix[row][column] = prime_numbers[random.randint(0, len(prime_numbers) - 1)]

print(matrix) # matrisimi ekrana yazdırıyorum.