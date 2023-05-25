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

def porte_avion(x, y, orientation):
    x -= 1
    y -= 1
    if orientation == "H":
        if x > 5:
            print("X trop grand !")
            return
        for i in range(5):
            ordonnees[y][x] = "A"
            x += 1
        afficher_grille()
        return x
    if orientation == "V":
        if y > 5:
            print("Y trop grand !")
            return
        for i in range(5):
            ordonnees[y][x] = "A"
            y += 1
        afficher_grille()
        return x

def tirer(x, y):
    try:
        x[y - 1] = "X"
        return x
    except:
        print("Erreur !")

porte_avion(10, 6, "V")

tirer(A, 2)