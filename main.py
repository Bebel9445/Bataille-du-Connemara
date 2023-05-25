A = ["O","O","O","O","O","O","O","O","O","O"]
B = ["O","O","O","O","O","O","O","O","O","O"]
C = ["O","O","O","O","O","O","O","O","O","O"]
D = ["O","O","O","O","O","O","O","O","O","O"]
E = ["O","O","O","O","O","O","O","O","O","O"]
F = ["O","O","O","O","O","O","O","O","O","O"]
G = ["O","O","O","O","O","O","O","O","O","O"]
H = ["O","O","O","O","O","O","O","O","O","O"]
I = ["O","O","O","O","O","O","O","O","O","O"]
J = ["O","O","O","O","O","O","O","O","O","O"]

ordonnees = [A, B, C, D, E, F, G, H, I, J]


def afficher_grille():
    for i in ordonnees:
        print(*i, sep="  ")

def cuirassé(x, y, orientation):
    y-=1
    if orientation == "H":
        if y > 6:
            print("X trop grand !")
            return
        for i in range(5):
            x[y] = "C"
            y += 1
        afficher_grille()
        return x
    if orientation == "V":
        if x not in ordonnees[:6]:
            print("Mauvais Y")
            return
        for i in range(10):
            if x == ordonnees[i]:
                position = i
        for j in range(5):
            ordonnees[position][y] = "C"
            position += 1
        afficher_grille()

def tirer(x, y):
    try:
        x[y - 1] = "X"
        return x
    except:
        print("Erreur !")



tirer(A, 2)

cuirassé(A, 1, "V") 