# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.

from math import sin
from math import radians

speed = input("Vitesse initiale (m/s) : ")
angle = input("Angle de lancer (en degrés) : ")
distance = round((float(speed)**2 * sin(2*radians(float(angle))) / 9.81), 2)
print(f"Distance parcourure : {distance} m")

