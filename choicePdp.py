
import random

MaxList = 26
orderStart = []

order = []

def sortByPref(val): 
    return val[2]  

def addToListOrdered (numberList, description, orderPref = None):
    if(orderPref == None):
        orderPref = random.randint(MaxList, 100)

    if(numberList in orderStart):
        orderPref = orderStart.index(numberList)

    objectList = (numberList, description.replace("  ", ""), orderPref)
    
    if(not objectList in order):
        order.append(objectList)


    

addToListOrdered( 1     ,"FP tutor    		                                                   ")
addToListOrdered( 2     ,"Tuiles multimédia 3D sur le web                                      ")
addToListOrdered( 3     ,"Algorithmes pour gagner à Hanabi                                     ")
addToListOrdered( 4     ,"Planification de mouvement pour robots                               ")
addToListOrdered( 5     ,"Clicodrome pour lexique électronique                                 ")
addToListOrdered( 6     ,"Application météo décalée pour Android                               ")
addToListOrdered( 7     ,"Spatialisation par le geste                                          ")
addToListOrdered( 8     ,"Visualisations de traces d'exécution                                 ")
addToListOrdered( 9     ,"Développement sur radio-logicielle d'une passerelle                  ")
addToListOrdered( 10    ,"Environement Amstrad CPC pour la bibliothèque d'apprenti             ")
addToListOrdered( 11    ,"Génération de playlistes musicales pour un groupe d'utilis           ")
addToListOrdered( 12    ,"Les processus de décision                                            ")
addToListOrdered( 13    ,"Localisation de robots en présence de faux positif                   ")
addToListOrdered( 14    ,"Suivi de robots pour annotation semi-automatiq                       ")
addToListOrdered( 15    ,"Création et dégradation d'images pour une utilisation en dee         ")
addToListOrdered( 16    ,"Analyse d'architecture logicielles                                   ")
addToListOrdered( 17    ,"Analyse d'architecture logicielles                                   ")
addToListOrdered( 18    ,"Slitherlink                                                          ")
addToListOrdered( 19    ,"Environnement d'exécution y86+HCL en Python ou en Node               ")
addToListOrdered( 20    ,"Joueur de Scrabble                                                   ")
addToListOrdered( 21    ,"Génération procédurale de planètes sphériques                        ")
addToListOrdered( 22    ,"IA pour un jeu de Capture the Flag temps réel en Pyt                 ")
addToListOrdered( 23    ,"Personal Hypno Vibes 2 (pdf)                                         ")
addToListOrdered( 24    ,"Visualisation de tâches hiérarchiques (pdf)                          ")
addToListOrdered( 25    ,"Calcul de cycles hamiltoniens dans des graphes fullerènes            ")

order.sort(key = sortByPref)

print("\n\n")
print("Déjà trié")
i=1
for o in order:
    if(i < len(orderStart)+1):
        print(o)
    i+=1

print("\n")
print("Autres")

i=1
for o in order:
    if(i > len(orderStart)+1):
        print(o)
    i+=1

print("\n\n")


val = input("y to confirm: ") 
strList = ""
if(val == 'y'):
    print(str(orderStart).replace(" ", "").replace("[", "").replace("]", ""))
    i=1
    for o in order:
        if(i > len(orderStart)):
            strList += str(o[0])
            strList += ','
        i+=1

print (strList)
print("\n\n")