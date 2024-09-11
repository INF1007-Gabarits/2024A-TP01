# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

water_quantity = float(input("Quelle quantité d'eau faut-il assainir ? "))
filter_quantity = water_quantity/5
lamp_quantity = water_quantity*(3/5)
chlore_amount = water_quantity*(0.5/5)



print(f"Voici les éléments requis pour assainir {water_quantity}L d'eau:\n"
       f"         - Filtres : {filter_quantity}\n"
       f"         - Lampes UV : {lamp_quantity}\n"
       f"         - Chlore : {chlore_amount}kg"
       )


