def ftDebut():
    repMenu = 0
    while repMenu != "1" and repMenu != "2" and repMenu != "3": 
        repMenu = input("Que voulez-vous faire ? Tapez 1 pour afficher une partition, 2 pour creer une partition et 3 pour modifier une partitions, un compositeur, ...")
    if (repMenu == "1"):
        ftAffiche()
    elif (repMenu == "2"):
        ftAdd()
    elif (repMenu == "3"):
        ftModif()
        
def ftAffiche():
    print("Quelle partition recherchez-vous ?")
    identifiant = input("Quel est l'identifiant de la partition ? 0 si vous ne savez pas")
    titre = input("Quel est le titre de la partition ? 0 si vous ne savez pas")
    compositeur = input("Quel est le nom du compositeur ? 0 si vous ne savez pas")
    mouvement = input("Quel est le mouvement de la partition ? 0 si vous ne savez pas")
    instruments = []
    instruments.append(input("Quel instrument y a t-il ? Tapez 0 si vous souhaitez arrêter d'en taper ou si vous ne savez plus"))
    i = 0
    while (instruments[i] != "0"):
        instruments.append(input("Quel instrument y a t-il ? Tapez 0 si vous souhaitez arrêter d'en taper"))
        i = i + 1
    monFichier = open("fichier_stocke.csv", "r")
    lines = [line.strip('\n') for line in monFichier.readlines()]
    i = 0
    for line in lines:
        mots = line.split(",")
        lines[i] = mots
        i = i + 1
    monFichier.close()
    print('\nListe :')
    for x in lines:
        if (((x[0].lower().startswith(identifiant) == True) or (identifiant == "0")) and ((x[1].lower().startswith(titre) == True) or (titre == "0")) and ((x[2].lower().startswith(compositeur) == True) or (compositeur == "0")) and ((x[3].lower().startswith(mouvement) == True) or (mouvement == "0"))):
            r = len(x)
            k = 0
            for h in instruments:
                diff = 1
                for u in x[4:r]:
                    if (u.lower().startswith(h) == True) or (h == "0"):
                        diff = 0
                if diff == 1:
                    k = 1
            if (k == 0):
                print(x[0] + ',' + x[1] + ',' + x[2] + ',' + x[3], end = "")
                for p in x[4:r + 1]:
                    print(',' + p, end="")
                print('\n', end = "")

def ftAdd():
    identifiant = input("Quel est l'identifiant de la partition ? 0 si vous ne savez pas")
    titre = input("Quel est le titre de la partition ? 0 si vous ne savez pas")
    compositeur = input("Quel est le nom du compositeur ? 0 si vous ne savez pas")
    mouvement = input("Quel est le mouvement de la partition ? 0 si vous ne savez pas")
    instruments = []
    instruments.append(input("Quel instrument y a t-il ? Tapez 0 si vous souhaitez arrêter d'en taper"))
    i = 0
    while (instruments[i] != "0"):
        instruments.append(input("Quel instrument y a t-il ? Tapez 0 si vous souhaitez arrêter d'en taper"))
        i = i + 1
    monFichier = open('fichier_stocke.csv', 'a')
    monFichier.write(identifiant + ',' + titre + ',' + compositeur + ',' + mouvement)
    if (instruments[0] != "0"):
        for instrument in instruments:
            if instrument == '0':
                break
            else:
                monFichier.write(',' + instrument)
    else:
        monFichier.write(',' + '0')
    monFichier.write('\n')
    monFichier.close()

def ftModif():
    rep = input("Que voulez-vous modifier ? Tapez 0 pour supprimer une partition ou tapez 1 pour modifier une partition, 2 pour modifier un identifiant, 3 pour modifier un titre, 4 pour modifier un compositeur, 5 pour modifier un mouvement et 6 pour modifier un instrument")
    if (rep == "1" or rep == "0"):
        h = quellePartition()
        if rep == "1":    
            modifPartition(h)
        elif rep == "0":
            suppPartition(h)
    elif (rep == "2" or rep == "3" or rep == "4" or rep == "5" or rep == "6"):
        modifAutre()

def suppPartition(h):
    monFichier = open('fichier_stocke.csv', 'r')
    lines = [line.strip('\n') for line in monFichier.readlines()]
    monFichier.close()
    monFichier = open('fichier_stocke.csv', 'w')
    i = 0
    while i < len(lines):
        if (i != h):
            monFichier.write(lines[i] + '\n')
        i = i + 1
    monFichier.close()
        
def modifPartition(h):
    a = input("Que voulez-vous modifier ? 0 pour identifiant, 1 pour titre, 2 pour compositeur, 3 pour mouvement ou 4 pour instrument")
    b = input("Quel nom ?")
    c = input("Quel nouveau nom ?")
    monFichier = open('fichier_stocke.csv', 'r')
    lines = [line.strip('\n') for line in monFichier.readlines()]
    i = 0
    for line in lines:
        mots = line.split(",")
        lines[i] = mots
        i = i + 1
    monFichier.close()
    i = 0
    for x in lines[h]:
        if x == b:
            lines[h][i] = c
        i = i + 1
    monFichier = open('fichier_stocke.csv', 'w')
    for line in lines:
        for mot in line:
            monFichier.write(mot)
            if (mot != line[len(line) - 1]):
                monFichier.write(",")
        monFichier.write("\n")
    monFichier.close()
        
def quellePartition():
    print("Quelle partition recherchez-vous ?")
    identifiant = input("Quel est l'identifiant de la partition ? 0 si vous ne savez pas")
    titre = input("Quel est le titre de la partition ? 0 si vous ne savez pas")
    compositeur = input("Quel est le nom du compositeur ? 0 si vous ne savez pas")
    mouvement = input("Quel est le mouvement de la partition ? 0 si vous ne savez pas")
    instruments = []
    instruments.append(input("Quel instrument y a t-il ? Tapez 0 si vous souhaitez arrêter d'en taper ou si vous ne savez plus"))
    i = 0
    while (instruments[i] != "0"):
        instruments.append(input("Quel instrument y a t-il ? Tapez 0 si vous souhaitez arrêter d'en taper"))
        i = i + 1
    monFichier = open("fichier_stocke.csv", "r")
    lines = [line.strip('\n') for line in monFichier.readlines()]
    i = 0
    for line in lines:
        mots = line.split(",")
        lines[i] = mots
        i = i + 1
    monFichier.close()
    i = 0
    for x in lines:
        if (((x[0].lower().startswith(identifiant) == True) or (identifiant == "0")) and ((x[1].lower().startswith(titre) == True) or (titre == "0")) and ((x[2].lower().startswith(compositeur) == True) or (compositeur == "0")) and ((x[3].lower().startswith(mouvement) == True) or (mouvement == "0"))):
            r = len(x)
            k = 0
            for h in instruments:
                diff = 1
                for u in x[4:r]:
                    if (u.lower().startswith(h) == True) or (h == "0"):
                        diff = 0
                if diff == 1:
                    k = 1
            if (k == 0):
                return (i)
        i = i + 1
        
def modifAutre():
    monFichier = open("fichier_stocke.csv", "r")
    lines = [line.strip('\n') for line in monFichier.readlines()]
    i = 0
    for line in lines:
        mots = line.split(",")
        lines[i] = mots
        i = i + 1
    monFichier.close()
    rep = input("Quel nom ?")
    change = input("Tapez le nouveau nom ?")
    i = 0
    for line in lines:
        j = 0
        for mot in line:
            if mot == rep:
                lines[i][j] = change
            j = j + 1
        i = i + 1
    monFichier = open("fichier_stocke.csv", "w")
    for line in lines:
        for mot in line:
            monFichier.write(mot)
            if (mot != line[len(line) - 1]):
                monFichier.write(",")
        monFichier.write("\n")
    monFichier.close()

ftDebut()
