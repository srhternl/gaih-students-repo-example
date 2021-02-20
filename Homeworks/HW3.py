def prime_first(number): # asal sayı hesaplayan 1. fonksiyonum.
    if number !=1 and number !=0:
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            print("Prime numbers between 0-500:", number)

def prime_second(number): # asal sayı hesaplayan 2. fonksiyonum.
    if number !=1 and number !=0:
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            print("Prime numbers between 500-1000:", number)

for i in list(range(1000)): # 0-500 ve 500-1000 arası asal sayıları hesaplayıp, ekrana yazdıran döngüm.
    if i < 500:
        prime_first(i)
    else:
        prime_second(i)
