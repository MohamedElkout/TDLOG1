from vessel import *
from weapon import *

# premier joueurs 
vaiseaux=[]
position=[]
max_hits=0
while max_hits<=22:
    x=input('entrer la premier position entre 0 et 100')
    y=input('entrer la deuxieme position 0 et 100')
    z=input('entrer la troisieme position entre 0 et 1 et -1')
    if [x,y,z] not in position:
        position.append([x,y,z])
        vaiseaux111=input('choisir les vaiseaux ')
        if vaiseaux111=='Fregate':
            vaiseaux.append(Fregate(x,y))
            max_hits=max_hits+5
        if vaiseaux111=='Cruiser':
            vaiseaux.append(Fregate(x,y))
            max_hits=max_hits+6
        if vaiseaux111=='Submarine':
            vaiseaux.append(Fregate(x,y))
            max_hits=max_hits+2
        if vaiseaux111=='Destroyer':
            vaiseaux.append(Fregate(x,y))
            max_hits=max_hits+4
        if vaiseaux111=='Aircraft':
            vaiseaux.append(Fregate(x,y))
            max_hits=max_hits+1
# deuxieme joueurs 
vaiseaux1=[]
position1=[]
max_hits=0
while max_hits<=22:
    x=input('entrer la premier position entre 0 et 100')
    y=input('entrer la deuxieme position 0 et 100')
    z=input('entrer la troisieme position entre 0 et 1 et -1')
    if [x,y,z] not in position1:
        position1.append([x,y,z])
        vaiseaux11=input('choisir les vaiseaux ')
        if vaiseaux11=='Fregate':
            vaiseaux1.append(Fregate(x,y))
            max_hits=max_hits+5
        if vaiseaux11=='Cruiser':
            vaiseaux1.append(Fregate(x,y))
            max_hits=max_hits+6
        if vaiseaux11=='Submarine':
            vaiseaux1.append(Fregate(x,y))
            max_hits=max_hits+2
        if vaiseaux11=='Destroyer':
            vaiseaux1.append(Fregate(x,y))
            max_hits=max_hits+4
        if vaiseaux11=='Aircraft':
            vaiseaux1.append(Fregate(x,y))
            max_hits=max_hits+1