lista = [0]*9
znakovi = [" "]*9
win = 0

for j in range(9):
    while True:
        x = int(input("Unos: "))
        if x>=1 and x<=9:
            if lista[x-1]==0:
                break
            else:
               print("Polje je zauzeto\n")
        else:
            print("Unesite unos od 1 do 9\n")
    if j%2==0:
        lista[x-1] = 1
        znakovi[x-1] = "X"
    else:
        lista[x-1] = 2
        znakovi[x-1] = "O"


    print("\nStanje:\n")
    
    for i in range(3):
        print(f"{znakovi[0+i*3]} | {znakovi[1+i*3]} | {znakovi[2+i*3]}\n----------")
    print("\n")

    
    #redovi i stupci
    for i in range(3):
        if lista[0+i*3]==lista[1+i*3]==lista[2+i*3]:
            if lista[0+i*3]==1:
                win = 1
                break
            elif lista[0+i*3]==2:
                win = 2
                break
        if lista[0+i]==lista[3+i]==lista[6+i]:
            if lista[0+i]==1:
                win = 1
                break
            elif lista[0+i]==2:
                win = 2
                break
            
    #dijagonale
    if lista[0]==lista[4]==lista[8] or lista[2]==lista[4]==lista[6]:
        if lista[4]==1:
            win = 1
        elif lista[4]==2:
            win = 2

    if win==2:
        print("O je pobjednik")
        break
    elif win==1:
        print("X je pobjednik")
        break

    if j==8:
        print("Nema pobjednika")
