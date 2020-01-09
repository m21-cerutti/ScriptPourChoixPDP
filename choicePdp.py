
import random

MaxList = 26
orderStart = []

order = []

def sortByPref(val): 
    return val[2]  

def addToListOrdered (numberList, description, orderPref):
    if(orderPref == None):
        orderPref = random.randint(MaxList, 100)

    if(numberList in orderStart):
        orderPref = orderStart.index(numberList)

    objectList = (numberList, description.replace("  ", ""), orderPref)
    
    if(not objectList in order):
        order.append(objectList)


    

addToListOrdered( 1     ,"FP tutor    		                                                   ", None)
addToListOrdered( 2     ,"Tuiles multimédia 3D sur le web                                      ", None)
addToListOrdered( 3     ,"Algorithmes pour gagner à Hanabi                                     ", None)
addToListOrdered( 4     ,"Planification de mouvement pour robots                               ", None)
addToListOrdered( 5     ,"Clicodrome pour lexique électronique                                 ", None)
addToListOrdered( 6     ,"Application météo décalée pour Android                               ", None)
addToListOrdered( 7     ,"Spatialisation par le geste                                          ", None)
addToListOrdered( 8     ,"Visualisations de traces d'exécution                                 ", None)
addToListOrdered( 9     ,"Développement sur radio-logicielle d'une passerelle                  ", None)
addToListOrdered( 10    ,"Environement Amstrad CPC pour la bibliothèque d'apprenti             ", None)
addToListOrdered( 11    ,"Génération de playlistes musicales pour un groupe d'utilis           ", None)
addToListOrdered( 12    ,"Les processus de décision                                            ", None)
addToListOrdered( 13    ,"Localisation de robots en présence de faux positif                   ", None)
addToListOrdered( 14    ,"Suivi de robots pour annotation semi-automatiq                       ", None)
addToListOrdered( 15    ,"Création et dégradation d'images pour une utilisation en dee         ", None)
addToListOrdered( 16    ,"Analyse d'architecture logicielles                                   ", None)
addToListOrdered( 17    ,"Analyse d'architecture logicielles                                   ", None)
addToListOrdered( 18    ,"Slitherlink                                                          ", None)
addToListOrdered( 19    ,"Environnement d'exécution y86+HCL en Python ou en Node               ", None)
addToListOrdered( 20    ,"Joueur de Scrabble                                                   ", None)
addToListOrdered( 21    ,"Génération procédurale de planètes sphériques                        ", None)
addToListOrdered( 22    ,"IA pour un jeu de Capture the Flag temps réel en Pyt                 ", None)
addToListOrdered( 23    ,"Personal Hypno Vibes 2 (pdf)                                         ", None)
addToListOrdered( 24    ,"Visualisation de tâches hiérarchiques (pdf)                          ", None)
addToListOrdered( 25    ,"Calcul de cycles hamiltoniens dans des graphes fullerènes            ", None)

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