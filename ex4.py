# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).
battery_level = input("Pourcentage de batterie? ")
while (battery_level.isnumeric() == False or int(battery_level) > 100 or int(battery_level) < 0):
    battery_level = input("Veuillez insérer un pourcentage de batterie valide (entre 0 et 100): ")
battery_level = int(battery_level)
distance = battery_level
if(battery_level > 50):
    distance*= 2
elif(battery_level > 25):
    distance*= 0.5
elif(battery_level > 10):
    distance*= 1
elif(battery_level > 5):
    distance*= 2.5
else:
    distance*= 6
    
distance = round(distance,1)
print(distance, "km")