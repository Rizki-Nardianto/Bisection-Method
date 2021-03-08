import numpy as np
import matplotlib.pyplot as plt

def inputdata(nilai_a, nilai_b):
    nilai_a= float(input("Masukan data awal a : "))
    nilai_b= float(input("Masukan data awal b : "))
    return (nilai_a, nilai_b)

def y(x):
    return (x**3-(7*x)+1)

def checkAB(nilai_a, nilai_b):
    if(y(nilai_a)*y(nilai_b)<0):
        return True
    else:
        return False

def updateData(nilai_a, nilai_b):
    nilai_c= (nilai_a + nilai_b)/2
    if(y(nilai_a)*y(nilai_c)<0):
        nilai_b = nilai_c
    else :
        nilai_a = nilai_c
    return (nilai_a, nilai_b)

def process(nilai_a,nilai_b, prc):
    while(abs(y(nilai_a))>prc or abs(y(nilai_b))>prc):
        nilai_a, nilai_b = updateData(nilai_a, nilai_b)

    if(abs(y(nilai_a))>abs(y(nilai_b))):
        return nilai_b
    else:
        return nilai_a
    # return (a,b)
   

def main():
    nilai_a= 0
    nilai_b= 0
    prc= 0
    result = 0
    nilai_a, nilai_b = inputdata(nilai_a, nilai_b)
    if(checkAB(nilai_a, nilai_b)):
        print ("Data sesuai bisa dilanjutkan")
        prc = float(input("Masukan nilai error toleransi : "))
        result = process(nilai_a, nilai_b,prc)
        print ("Hasil = ",result," Dengan nilai y(x) ",y(result))
    else:
        print ("Data tidak sesuai tidak bisa dilanjutkan")

    x = np.linspace(nilai_a,nilai_b,100)
    plt.plot(x, f(x))
    plt.grid()
    plt.xlabel("Grafik Fungsi y(x)")
    plt.show()
    
main()

