print("Masukan Bilangan Ke-1 :")
bilangan1=int(input())
print("Masukan Bilangan Ke-2 :")
bilangan2=int(input())
print("Masukan Bilangan ke-3 :")
bilangan3=int(input())

print("\n")

if (bilangan1 > bilangan2) and (bilangan1 > bilangan3) :
    print("Bilangan Pertama Lebih Besar Dari Bilangan Kedua Dan Ketiga")
elif (bilangan2 > bilangan1) and (bilangan2 > bilangan3) :
    print("Bilangan Kedua Lebih Besar Dari Bilangan Pertama Dan Ketiga ")
elif (bilangan3 > bilangan1) and (bilangan3 > bilangan2) :
    print("Bilangan Ketiga Lebih Besar Dari Bilangan Pertama Dan Kedua")
else:
    print("Semua Bilangan Sama Besar Nya")
