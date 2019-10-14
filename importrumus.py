#mengimpor modul RumusFisika
import RumusFisika

def main():
    # rumus gaya
    m = 10 
    a = 8 

    Gaya = RumusFisika.Gaya(m, a)

    print("Gaya")
    print("massa\t: ", m)
    print("percepatan\t: ", a)
    print ("gaya\t= ", Gaya)


    # rumus usaha
    f = 12
    s = 10

    Usaha = RumusFisika.Usaha(f, s)
    
    print("Usaha")
    print("gaya\t: ", f)
    print("jarak\t: ", s)
    print ("usaha\t: ", Usaha)

    # rumus energi
    m = 5 
    g = 10
    h = 7

    Energi = RumusFisika.Energi(m, g, h)
    
    print("Energi")
    print("massa\t: ", m)
    print("percepatan\t: ", g)
    print("tinggi\t: ", h)
    print("energi\t= ", Energi)

if __name__ =="__main__":
    main()

    

    
