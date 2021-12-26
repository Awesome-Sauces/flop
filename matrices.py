class matrice():
    def create(x, y):
        flopMt = []
        # Makes X axis
        if y == 0:
            flopMt.append([])
            for f in range(x):
                flopMt[0].append(0)
        else:
            for f in range(y):
                flopMt.append([])
            for j in range(len(flopMt)):
                for l in range(x):
                    flopMt[j].append(0)
        # Makes Y axis

        return flopMt
    def get(MATRICE, x, y):
        temp = MATRICE[y]
        return temp[x]
    def set(MATRICE, x222, y, value):
        MATRICE[y][x] = value
        return MATRICE



inst = matrice.create(x=3, y=9)

print(matrice.set(inst, x=2, y=3, value=320320320320))

