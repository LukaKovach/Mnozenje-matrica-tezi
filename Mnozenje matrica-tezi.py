redak_a = int(input('Broj redaka matrice a: '))
stupac_a = int(input('Broj stupaca matrice a: '))
redak_b = int(input('Broj redaka matrice b: '))
stupac_b = int(input('Broj stupaca matrice b: '))
a = [[0] * stupac_a for i in range(redak_a)]
b = [[0] * stupac_b for j in range(redak_b)]

if stupac_a == redak_b:
    # Unos i ispis matrice A
    for i in range(redak_a):
        for j in range(stupac_a):
            a[i][j] = int(input("Unesite element u " + str(i+1) + " retku i " + str(j+1) + " stupcu matrice A:"))
    print('A')
    for redak in a:
        print(redak)

    # Unos i ispis matrice B
    for i in range(redak_b):
        for j in range(stupac_b):
            b[i][j] = int(input("Unesite element u " + str(i+1) + " retku i " + str(j+1) + " stupcu matrice A:"))
    print('B')
    for redak in b:
        print(redak)

    c = [[0] * stupac_b for i in range(redak_b)]

    # Mnozenje matrice A i B
    for i in range(redak_a):
        for j in range(stupac_b):
            for l in range(redak_b):
                c[i][j] = c[i][j] + a[i][l] * b[l][j]
    # Ispis matrice C
    print('C')
    for redak in c:
        print(redak)

else:
    print("Matrice nisu ulancane!")
