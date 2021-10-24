print(" Program Konversi Rupiah ke Asing")
#judul Program

print("")
#Membuat Fungsi mata_uang_dunia
def mata_uang_dunia():
    print("Menu")
    print(" 1. IDRtoUSD (Rp.14.230,80)")
    print(" 2. IDRtoSGD (Rp.10.555,19)")
    print(" 3. IDRtoEUR (Rp.16.570,41)")
    print(" 4. IDRtoJPY (Rp.125,41)")
    print(" 5. Selesai")

print("")

#kondisi awal variabel
masukan=0
mata_uang=0
hasil=0

#kondisi while
while True:
    mata_uang_dunia()
    pilihan=input("Masukan Pilihan:")
    pilihan=int(pilihan)

    if pilihan==1:
        masukkan=input("Masukkan nominal:")
        masukkan=int(masukkan)
        print("")
        mata_uang=14230
        hasil=masukkan/mata_uang
        print(f" {masukkan} Rupiah senilai dengan {hasil} Dollar")
        print("") 

    if pilihan==2:
        masukkan=input("Masukkan nominal:")
        masukkan=int(masukkan)
        print("")
        mata_uang=10555
        hasil=masukkan/mata_uang
        print(f" {masukkan} Rupiah senilai dengan {hasil} SGD")
        print("") 

    if pilihan==3:
        masukkan=input("Masukkan nominal:")
        masukkan=int(masukkan)
        print("")
        mata_uang=16570
        hasil=masukkan/mata_uang
        print(f" {masukkan} Rupiah senilai dengan {hasil} EUR")
        print("") 
    if pilihan==4:
        masukkan=input("Masukkan nominal:")
        masukkan=int(masukkan)
        print("")
        mata_uang=125
        hasil=masukkan/mata_uang
        print(f" {masukkan} Rupiah senilai dengan {hasil} JPY")
        print("") 

#program berhenti jika 5 dimasukkan
    if pilihan==5:
       print("Program selesai")
       break




