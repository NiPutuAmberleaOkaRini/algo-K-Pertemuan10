print("Angka Fibonacci")
n = int(input("Masukkan jumlah angka Fibonacci : "))
a, b = 0, 1

for _ in range (n):
    print(a, end=" ")
    a, b = b, a + b

print("Bilangan Prima")
number = int(input("Masukkan angka : "))
is_prime = True

for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break

if is_prime and number > 1:
    print(number, "adalah bilangan prima")
else:
    print(number, "bukan bilangan prima")
