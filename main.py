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
    print("\n\n\n")

def libre(x, y, longueur, sens):
    if sens == "H":
        for i in range(x, x + longueur):
            if ordonnees[y][i] != "O":
                print("On ne peut superposer 2 bateau !\n\n\n")
                return False
        return True
    if sens == "V":
        for i in range(y, y + longueur):
            if ordonnees[i][x] != "O":
                print("On ne peut superposer 2 bateau !\n\n\n")
                return False
        return True

def porte_avion(x, y, sens):
    x -= 1
    y -= 1
    if sens == "H":
        if x > 5:
            print("X trop grand !")
            return
        if libre(x, y, 5, "H") == True:
            for i in range(5):
                ordonnees[y][x] = "≕"
                x += 1
            afficher_grille()
            return x
    if sens == "V":
        if y > 5:
            print("Y trop grand !")
            return
        if libre(x, y, 5, "V") == True:
            for i in range(5):
                ordonnees[y][x] = "≕"
                y += 1
            afficher_grille()
            return x
        
def cuirasse(x, y, sens):
    x -= 1
    y -= 1
    if sens == "H":
        if x > 6:
            print("X trop grand !")
            return
        if libre(x, y, 4, "H") == True:
            for i in range(4):
                ordonnees[y][x] = "⇛"
                x += 1
            afficher_grille()
            return x
    if sens == "V":
        if y > 6:
            print("Y trop grand !")
            return
        if libre(x, y, 4, "V") == True:
            for i in range(4):
                ordonnees[y][x] = "⇛"
                y += 1
            afficher_grille()
            return x
        
def croiseur(x, y, sens):
    x -= 1
    y -= 1
    if sens == "H":
        if x > 7:
            print("X trop grand !")
            return
        if libre(x, y, 3, "H") == True:
            for i in range(3):
                ordonnees[y][x] = "⇒"
                x += 1
            afficher_grille()
            return x
    if sens == "V":
        if y > 7:
            print("Y trop grand !")
            return
        if libre(x, y, 3, "V") == True:
            for i in range(3):
                ordonnees[y][x] = "⇒"
                y += 1
            afficher_grille()
            return x
        
def sous_marin(x, y, sens):
    x -= 1
    y -= 1
    if sens == "H":
        if x > 7:
            print("X trop grand !")
            return
        if libre(x, y, 3, "H") == True:
            for i in range(3):
                ordonnees[y][x] = "⧐"
                x += 1
            afficher_grille()
            return x
    if sens == "V":
        if y > 7:
            print("Y trop grand !")
            return
        if libre(x, y, 3, "V") == True:
            for i in range(3):
                ordonnees[y][x] = "⧐"
                y += 1
            afficher_grille()
            return x

def destroyer(x, y, sens):
    x -= 1
    y -= 1
    if sens == "H":
        if x > 8:
            print("X trop grand !")
            return
        if libre(x, y, 2, "H") == True:
            for i in range(2):
                ordonnees[y][x] = "⊳"
                x += 1
            afficher_grille()
            return x
    if sens == "V":
        if y > 8:
            print("Y trop grand !")
            return
        if libre(x, y, 2, "V") == True:
            for i in range(2):
                ordonnees[y][x] = "⊳"
                y += 1
            afficher_grille()
            return x

def tirer(x, y):
    try:
        x[y - 1] = "X"
        afficher_grille()
    except:
        print("Erreur !")

porte_avion(10, 6, "V")

cuirasse(10, 2, "V")

croiseur(8, 1, "H")

sous_marin(5, 1, "H")

destroyer(9, 5, "V")

tirer(A, 2)