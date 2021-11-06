# P7_labspy02

Repository ini dibuat memenuhi tugas pertemuan 7 Bahasa Pemograman (modul praktikum 2) - Teknik Informatika

![Gambar 1](Screenshots/Tugas.png)


### Menentukan Bilangan Terbesar Dari Nilai Yang Diinputkan

    Pada pertemuan ke-7 ini saya mendapatkan tugas dari Dosen bahasa pemograman Teknik Informatika - 
    Universitas Peita Bangsa. Untuk membuat aplikasi yang menentukan bilangan terbesar dari tiga nilai yang 
    client/user inputkan menggunakan bahasa program python.

Pada repository ini saya akan menjelaskan *Flowchart* yang telah saya buat dan bisa dilihat berikut file nya. [flowchat tugas pertemuan 7 menentukan bilangan terbesar yang diinput](flowerchat.pdf)

* Berikut source code yang saya buat untuk menjadi aplikasi yang bisa menentukan bilangan terbesar
````python
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
````
* Langkah pertama yaitu membuat sebuah inputan untuk menentukan bilangan terbesar. yaitu dengan printah:
* Langkah kedua yaitu saatnya menentukan logika untuk menemukan bilangan terbesar dari angka yang akan di inputkan diatas. 

Dengan menjelaskan fungsi-fugsi pada source code yang dilampirkan diatas : 

````python
    if (bilangan1 > bilangan2) and (bilangan1 > bilangan3) :
````
Pada syntax diatas bahwa terdapat dua pengecekan pada angka pertama yaitu: 

1. (bilangan1 > bilangan2) -> Apakkah angka pertama lebih besar dari angka kedua DAN

2. (Bilangan1 > bilangan3) -> Apakah angka pertama lebih besar dari angka ketiga.

* Apabila jika pengecekan bersifat benar (Angka Pertama Lebih Besar Dari Angka Kedua Dan Tiga), maka sytem akan menampilkan output berupa : 

````python
print(f"Bilangan pertama ({bilangan1}) lebih besar dari bilangan ketiga")
````
Dan akan memunculkan hasil seperti berikut :**Bilangan pertama ({bilangan1}) lebih besar dari bilangan kedua dan ketiga** 

* Jika dalam pengecekan ada yang salah atau nilai pertama tidak lebih besar dari nilai kedua dan ketiga, maka akan melakukan pengecekan selanjutya ke fungsi elif yaitu dengan source berik

````python
    elif (bilangan2 > bilangan1) and (bilangan2 > bilangan3) :
````    
Pada syntax diatas dijelaskan bahwa terdapat dua pengecekan pada angka kedua nya, yaitu :
1. (bilangan2 > bilangan1) = Apakah bilangan kedua lebih besar dari bilangan pertama dan
2. (bilangan2 > bilangan3) = Apakah bilangan kedua lebih besar dari bilangan ketiga. 

````python
print(f"Bilangan kedua ({bilangan2)} lebih besar dari bilangan pertama dan ketiga")
````
Dan akan menampilkan hasil seperti : **Bilangan kedua ({bilangan2)} lebih besar dari bilangan pertama dan ketiga**

* Seperti langkah di atas, jika dalam pengecekan salah atau bilangan kedua lebih kecil dari bilangan pertama dan ketiga system akan melanjutkan ke pengecekan selanjutnya :

    Untuk pengecekan selanjutnya saya akan melakuka pengecekan berupa Semua Bilangan Sama Besar Nya

Untuk membuat pengecekan kondisi tersebut dengan menggunakan syntax/source code berikut:

````python 
    elif (bilangan1 == bilangan2) and (bilangan1 == bilangan3) and (bilangan2 == bilangan3) 
````

    Pada syntax diatas dijelaskan terdapat tiga pengecekan pada semmua variable, yaitu : 1. (bilangan1 == bilangan2) Apakah bilangan pertama lebih besar dari bilangan kedua dan 2. (bilangan1 == bilangan3) Apakah bilangan pertama lebih besar dari bilangan ketiga dan 3. (bilangan2 == bilangan3) Apakah bilangan kedua lebih besar dari bilangan ketiga.

Setelah dilakukan pengecekan dan ternnyata semua angka sama besar, maka system akan menampilkan output dengan perintah berikut : 

````python
    print("Semua Bilangan Sama Besar Nya")
````

    Dari syntax diatas akan menampilkan hasil berupa Semua Bilangan Sama Besarnya

* Dan terakhir system sudah memperoses untuk melakukan pengecekan pada If, Elif maka system harus menentukan pilihan terakhir dengan menggunakan fungsi else menurut kondisi dimana system telah melakukan pengecekan pada fungsi if dan else tetapi tidak ada hasil yang di inginkan menempatkan kasus program ini, saya melakukan pengecekan kondisi :

    Pengecekan pertama pada bilangan1 apakah lebih besar, jika tidak maka melakukan pengecekan ke bilangan2 jika masih belum menampilkan, mari kita coba.

    Untuk menampilkan hasil akhir, maka hanya dengan menggunakan syntax sebagai berkut :
````python
    else:
        print(f"Bilangan ketiga ({bilangan3}) lebih besar dari bilangan pertama dan kedua")
`````

    Pada syntax diatas akan menampilkan hasil berupa : Bilangan ketiga ({bilangan3}) lebih besar dari bilangan pertama dan kedua

Saya akan menampilkan contoh berupa gambar, dengan menggunakan hasil output Bilangan ketiga ({bilangan3}) lebih besar dari bilangan pertama dan kedua 
1. Saya akan mencoba melakukan inputan dengan bilangan terbesar ada diinputan ketiga.

![Gambar 2](Screenshots/Hasil1.png)

2. Saya akan mencoba dengan menampilkan bilangan terbesar adalah bilangan pertama. 

![Gambar 3](Screenshots/Hasil2.png)

3.Dan sekarang saya akan menampilkan contoh dengan bilangan sama besar dengan bilangan pertama dan kedua. 

![Gambar 4](Screenshots/Hasil3.png)

# Selesai