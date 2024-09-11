#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

country = input("Pays concerné ? ")
code_medals = input("Chaine représentant les médailles ? ")
for c in code_medals:
    gold_medals = code_medals.count("G");
    silver_medals = code_medals.count("S");
    bronze_medals = code_medals.count("B");


print(f"{country}:\n"
      f"- {gold_medals} OR\n"
      f"- {silver_medals} Argent\n"
      f"- {bronze_medals} Bronze\n"
      )
