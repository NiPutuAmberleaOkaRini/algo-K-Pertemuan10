print("Perulangan 1")
for i in range(6):
    print(i)

print("Perulangan 2")
for i in range(0, 11, 2):
    print(i)

print("Perulangan 3")
numbers = [10, 20, 30, 40, 50, 60]
total = 0

for num in numbers:
    total += num

print("Total nilai tersebut :", total)

print("Perulangan Degan Step")
for i in range(1,20,3):
    print(i)

print("Perulangan For Dengan List")
for i in [1,2,3,4,5]:
    print("Ini Pengulangan ke - ", i)

print("Peruangan For Dengan List Dengan Isi String")
for i in    ["Rawon", "Nasi Kuning", "Soto Madura", "Kupat Tahu", "Kerak Telor", "Rendang Batoko", "Pempek Selam", "Ayam Betutu"]:
    print(i, "adalah masakan khas Nusantara")

print("Perulangan For Dengan String")
for i in "abcde":
    print(i, "adalah alfabet")

print("Percobaan")
i=1
while i<=5:
    print(i)
    i=i+1
    print("Program selesai")
