import socket
import sys
import threading
import time





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
    print("\n\n\n")
    for i in ordonnees:
        print(*i, sep="  ")


def convert(convert):
    convert_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    convert_list_min = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    for i in range(len(convert_list)):
        if convert == convert_list[i]:
            convert = i + 1
            return int(convert)
    for j in range(len(convert_list_min)):
        if convert == convert_list_min[j]:
            convert = j + 1
            return int(convert)

def libre(x, y, longueur, sens):
    if sens == "H":
        for i in range(x, x + longueur):
            if ordonnees[y][i] != "O":
                print("\n\n\nOn ne peut superposer 2 bateau !")
                return False
        return True
    if sens == "V":
        for i in range(y, y + longueur):
            if ordonnees[i][x] != "O":
                print("\n\n\nOn ne peut superposer 2 bateau !")
                return False
        return True

def porte_avion(y, x, sens):
    if not isinstance(x, int):
        print("ERREUR : L'abscisse n'est pas un entier !!")
        return
    y = convert(y)
    x -= 1
    try:
        y -= 1 # type: ignore
    except:
        print("ERREUR : L'ordonnée n'est pas une lettre ou est trop grand (A-J) !!")
        return
    if sens == "H":
        if x > 5:
            print("X trop grand !")
            return
        if x < 0:
            print("X trop petit !")
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
        if x < 0:
            print("X trop petit !")
            return
        if libre(x, y, 5, "V") == True:
            for i in range(5):
                ordonnees[y][x] = "≕"
                y += 1
            afficher_grille()
            return x
        
def cuirasse(y, x, sens):
    if not isinstance(x, int):
        print("ERREUR : L'abscisse n'est pas un entier !!")
        return
    y = convert(y)
    x -= 1
    try:
        y -= 1 # type: ignore
    except:
        print("ERREUR : L'ordonnée n'est pas une lettre ou est trop grand (A-J) !!")
        return
    if sens == "H":
        if x > 6:
            print("X trop grand !")
            return
        if x < 0:
            print("X trop petit !")
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
        if x < 0:
            print("X trop petit !")
            return
        if libre(x, y, 4, "V") == True:
            for i in range(4):
                ordonnees[y][x] = "⇛"
                y += 1
            afficher_grille()
            return x
        
def croiseur(y, x, sens):
    if not isinstance(x, int):
        print("ERREUR : L'abscisse n'est pas un entier !!")
        return
    y = convert(y)
    x -= 1
    try:
        y -= 1 # type: ignore
    except:
        print("ERREUR : L'ordonnée n'est pas une lettre ou est trop grand (A-J) !!")
        return
    if sens == "H":
        if x > 7:
            print("X trop grand !")
            return
        if x < 0:
            print("X trop petit !")
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
        if x < 0:
            print("X trop petit !")
            return
        if libre(x, y, 3, "V") == True:
            for i in range(3):
                ordonnees[y][x] = "⇒"
                y += 1
            afficher_grille()
            return x
        
def sous_marin(y, x, sens):
    if not isinstance(x, int):
        print("ERREUR : L'abscisse n'est pas un entier !!")
        return
    y = convert(y)
    x -= 1
    try:
        y -= 1 # type: ignore
    except:
        print("ERREUR : L'ordonnée n'est pas une lettre ou est trop grand (A-J) !!")
        return
    if sens == "H":
        if x > 7:
            print("X trop grand !")
            return
        if x < 0:
            print("X trop petit !")
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
        if x < 0:
            print("X trop petit !")
            return
        if libre(x, y, 3, "V") == True:
            for i in range(3):
                ordonnees[y][x] = "⧐"
                y += 1
            afficher_grille()
            return x

def destroyer(y, x, sens):
    if not isinstance(x, int):
        print("ERREUR : L'abscisse n'est pas un entier !!")
        return
    y = convert(y)
    x -= 1
    try:
        y -= 1 # type: ignore
    except:
        print("ERREUR : L'ordonnée n'est pas une lettre ou est trop grand (A-J) !!")
        return
    if sens == "H":
        if x > 8:
            print("X trop grand !")
            return
        if x < 0:
            print("X trop petit !")
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
        if x < 0:
            print("X trop petit !")
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

# porte_avion(input("Ordonnée du porte-avions --> "), int(input("Abscisse du porte-avions --> ")), input("Orientation (V/H) --> "))

# cuirasse(input("Ordonnée du cuirassé --> "), int(input("Abscisse du cuirassé --> ")), input("Orientation (V/H) --> "))

# croiseur(input("Ordonnée du croiseur --> "), int(input("Abscisse du croiseur --> ")), input("Orientation (V/H) --> "))

# sous_marin(input("Ordonnée du sous-marin --> "), int(input("Abscisse du sous-marin --> ")), input("Orientation (V/H) --> "))

# destroyer(input("Ordonnée du destroyer --> "), int(input("Abscisse destroyer --> ")), input("Orientation (V/H) --> "))

# tirer(input("Ordonnée du tir --> "), int(input("Abscisse du tir --> ")))





def receive_messages(client_socket):
    gotID = False
    id = None
    while True:
        try:
            data = client_socket.recv(1024)
            if data:
                if not gotID:
                    id = data.decode()
                    gotID=True
                if data.decode() == "PPA":
                    porte_avion(input("coordonée A-J"),int(input("coordonée 1-10")),input("sens : V-H"))


            else:
                # No data received, server has disconnected
                client_socket.close()
                break
        except:
            client_socket.close()
            break


def ping(socket):
    while True :
        time.sleep(1)
        ping="ping"
        socket.send(ping.encode())


ip = input("entrez l'ip du serveur : ")
port = input("entrez le port du serveur (vide pour défaut 10000) : ")

if port == "":
    port = 10000

try:
    port = int(port)
except: 
    print("erreur a l'entrée du port(étape conversion string -> int )")
    exit()

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (ip, port)
print(sys.stderr, 'connecting to %s port %s' % server_address)

try:
    sock.connect(server_address)

    # Start a separate thread to receive messages from the server
    # receive_thread = threading.Thread(target=receive_messages, args=(sock,))
    # receive_thread.start()
    # ping_thread = threading.Thread(target=ping, args=(sock,))
    # ping_thread.start()
    receive_messages(sock)







    # while True:
    #     message = input('Message: ')
    #     if message == 'quit':
    #         break
    #     sock.send(message.encode())

except ConnectionRefusedError:
    print("Server is not available.")
finally:
    sock.close()