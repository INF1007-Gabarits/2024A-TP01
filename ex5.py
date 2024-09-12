#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

country = input("Pays concerné ? ")
question = "Chaine représentant les médailles ? "
chaine_valide = False
while(chaine_valide == False):
    code_medals = input(question)
    for c in code_medals:
        if c not in ("B", "G", "S"):
            question = "Chaine invalide, veuillez recommencer : "
            break
        else:
            chaine_valide = True
        
for c in code_medals:
    gold_medals = code_medals.count("G");
    silver_medals = code_medals.count("S");
    bronze_medals = code_medals.count("B");


print(f"{country}:\n"
      f"- {gold_medals} OR\n"
      f"- {silver_medals} Argent\n"
      f"- {bronze_medals} Bronze\n"
      )
