import numpy as np

# A. OPERASI MATEMATIKA

'''Ini adalah Vektor(maktriks) Numpy'''
#operasi yang dilakukan oleh Numpy pada matrix adalah elementwise
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])

'''Ini adalah List'''
c = [1,2,3,4,5]
d = [5,11,7,8,9]

'''Operasi Numpy dan List'''

# Pertambahan
print(a+b) #--- Akan menjumlahkan dari setiap elemen dari array a dan b
print(c+d) #--- Akan menyatukan semua elemen, yang diurut berdasarkan urutan variabel

# Pengurangan
print(a-b)   #--- Akan melakukan operasi Numpy seperti halnya operasi matematika pada setiap elemennya
# print(c-d) #--- Operasi matematika tidak berlaku bagi list

# Perkalian
print(a*b)

# Pembagian
print(a/b)

# Kuadrat
print(a**b)


# B.INDEXING, SLICING, dan ITERASI

a = np.array([1,7,3,-2,5])
b = np.array([5,6,7,8,9])

# 1. Indexing
print(f"elemen kedua dari array 'a' adalah {a[1]}")
print()

# 2. Slicing
    # Slicing Matriks 1 Dimensi
print(f"elemen pertama hingga keempat adalah:\n==>{a[0:4]}")
A = np.array([1, 2, 3, 4, 5])
print(A[2])  # Mengakses elemen ke-2

    # Slicing Matrik 2 Dimensi
B = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(B[1, 2]) 
    # Slicing Matriks 3 dimensi
C = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(C[1, 0, 1])  # Mengakses elemen matriks ke-1, baris ke-0, kolom ke-1
print(C)


# 3. Iterasi (Looping)
print()
c = 0
print("daftar elemen dari array a adalah:\n=>")
for i in a:
    c +=1
    print(f"elemen {c} adalah ==>  {i}")
print()

# C. PERKALIAN MATRIX

'''Perkalian Matrix pada Numpy (yang biasa), bukanlah perkalian 
matrix seperti halnya pada matematika, melainakn disebut elemetwise.
Perkalian Matrix dapat dilakukan menggunakan operator 'dot' '''
a = np.array([[1,2],[4,5]])
c = np.array([[3,2],[2,5]])
b = np.ones([2,2])
# 1. Cara Pertama
hasil = np.dot(a,b)
print(f"Ini adalah hasil perkalian Matrix, cara 1:\n{hasil}")

# 2. Cara Kedua
hasil = a.dot(c)  #---memasukkan objek b ke dalam dot yang menempel pada 'a'? (OOP)
print(f"Ini adalah hasil perkalian Matrix, cara 2:\n{hasil}")

# D. MANIPULASI MATRIX
'''gausa diafalin, lihat aja dokumentasi dr Web Python'''
'''Berikut operator-operator umum digunakan'''

a = np.array(
    [[7,6,4],
     [9,11,7]])

# 1. Shape 
print(f"Ukuran matriks 'a' adalah : {a.shape}")
# 2. Transpose : Tanpa merubah elemen matriks aslinya
print(f"Cara 1 -- Transpose dari matriks 'a' adalah:\n{a.transpose()}\n")
print(f"Cara 2 -- Transpose dari matriks 'a' adalah:\n{np.transpose(a)}\n")
print(f"Cara 3 -- Transpose dari matriks 'a' adalah:\n{a.T}\n")
# 3. Flatten Array, menjadi matriks 1 dimensi (vektor) : Tanpa merubah elemen matriks aslinya
print(f"Cara 1 -- Flatten matiks 'a' adalah:\n{a.ravel()}\n")
print(f"Cara 2 -- Flatten matiks 'a' adalah:\n{np.ravel(a)}\n")
# 4. Reshape Matrix : Tanpa merubah elemen matriks aslinya
print(f"Reshape dari matrix a adalah:\n{a.reshape(3,2)}")
# 5. Resize Matrix : Merubah elemen dan struktur matriks aslinya
print()
a.resize(3,2)
print("struktur matrix 'a' berubah, sifat manipulasi 'Resize' beda dari yg lain:\n")
print(a)

# E. STACKING DAN PENYUSUNAN (CONCATENATE,HSTACK,VSTACK)
a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6]])

# 1. Stacking Vertikal
vstack = np.vstack((a,b)) 
print(f"ini adalah hasil Vertikal-Stack dengan V-stack):\n{vstack}")
print()
con_stack = np.concatenate((a,b),axis=0)
print(f"ini adalah hasil Vertikal-Stack dengan Concatenate):\n{vstack}")

# 2. Stacking Horizontal
print(f"ini adalah hasil Vertikal-Stack dengan H-Stack):\n{vstack}")
hstack = np.hstack((a, b.T)) # ditranspose dulu boiar sama size nya (horizontal stack)

# F. ADVANCED ARRAY 

# 1. Membuat matrix dengan tipe data tertentu

a = np.array([[1,2,3],[6,4,2]],dtype = float)
print(a)

# 2.Membuat Array dengan menggunakan Function ('def')
def kuadrat (baris,kolom):
    return (kolom**2)

def jumlah (baris,kolom):
    return (baris+kolom)

b = np.fromfunction(kuadrat, (2,3), dtype = int)
c = np.fromfunction(jumlah, (3,2), dtype = float)
print()
print(b)
print()
print(c)
print()

# 3. Membuat Array atau matrix dengan Iterasi (looping)
d = [x*x for x in range(5)]
print(d)

# 4. Multi Type Array
dtipe = [('nama','S255'),('tinggi',int)]

data = [
    ('Jaya', 170),
    ('Eunike', 165)
]
e = np.array(data,dtype = dtipe)
print(e)

for row in e:       # untuk menghilangkan atribut b'
    print((row['nama'].decode('utf-8'), row['tinggi']))

# G. MENGURUTKAN DAN SORTING PADA ARRAY/MATRIX DI NUMPY

a = np.array([5,6,7,9,2,6,3,1])

# 1. Nilai Terkecil dan Terbesar beserta posisi ataupun indexnya
print(f"\nNilai terkecil dari array 'a' adalah:\n==> {a.min()}")
print(f"Posisi nilai terkecil array a' adalah:\n==> {a.argmin()}")
print(f"Nilai terbesar dari array 'a' adalah:\n==> {a.max()}")
print(f"Posisi nilai terbesar dari array 'a' adalah:\n==> {a.argmax()}\n")

# 2. Mengurutkan Nilai Terkecil hingga nilai terbesar
    # Dimensi 1
print(f"1 Dimensi =>\nNilai terurut dari array 'a' adalah:\n==>{np.sort(a)}\n")    # kecil ke gede
print(f"1 Dimensi =>\nIndex terurut dari array 'a' adalah:\n==>{np.argsort(a)}\n") # kecil ke gede

    # Dimensi 1
a = np.array([[1, 2],
              [3, 4]])
print(f"2 Dimensi =>\nNilai terurut dari array 'a' adalah ==>\n{np.sort(a)}\n")
print(f"2 Dimensi =>\nIndex terurut dari array 'a' adalah ==>\n{np.argsort(a)}\n")

# 3.Mengurutkan nilai Daftar/dict
dtipe = [('nama','S255'),('tinggi',int)]

data = [
    ('Jaya', 170),
    ('Eunike', 165)
]
e = np.array(data,dtype = dtipe)
print(e)
print()
print(np.sort(e,order='tinggi'))

a = np.array([1, 2])
b = np.array([2, 1])

print(np.cross(a,b))

# H. PERKALIAN VEKTOR

# 1. dot
'''Hasil perkalian dot antar vektor merupakan skalar(satuannya).'''
a = np.array([1,2])
b = np.array([3,1])

result = np.dot(a,b)
print(result)

# 2. Cross
'''Hasil perkalian 'cross' antar vektor merupkan vektor juga nanti. Karena 3 dimensi(pada umumnya)
Jika, a dicross ke b hasilnya '-', sebaliknya '+' '''
a = np.array([1,2,0])
b = np.array([3,1,0])
result1 = np.cross(a,b)
print(result1) 


# Aljabar Linear: Invers dan Determinan Matriks
'''Invers dan Determinan ini berfungsi untuk menyelesaikan masalah persamaan linear'''

a = ([[1,-1],
      [1,1]])
print(a)

# 1. Invers 
a_inv = np.linalg.inv(a)
print(a_inv)
#hasil perkalian: dot
result = np.dot(a,a_inv)    #matriks identitas (I)
print(result)

# 2. Determinan
a_det = np.linalg.det(a)
a_detinv = np.linalg.det(a_inv)
print(a_det)
print(a_detinv)
#hasil perkalian det: dot --> 1
result = np.dot(a_det,a_detinv)
print(result)

# Solusi Persamaan Linear
A = np.array([[2,3],[1,2]])



