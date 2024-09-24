class CompteBancaire:
    def __init__(self, solde=0):
        self.__solde = solde  # Attribut privé

    # Getter sans utiliser @property
    def get_solde(self):
        return self.__solde

    # Setter sans utiliser @property
    def set_solde(self, nouveau_solde):
        if nouveau_solde >= 0:
            self.__solde = nouveau_solde
        else:
            raise ValueError("Le solde ne peut pas être négatif!")
    
    # Déposer de l'argent
    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            print(f"Déposé: {montant}€. Nouveau solde: {self.get_solde()}€.")
        else:
            print("Le montant doit être positif pour un dépôt.")

    # Retirer de l'argent
    def retirer(self, montant):
        if montant > 0:
            if self.__solde >= montant:
                self.__solde -= montant
                print(f"Retiré: {montant}€. Nouveau solde: {self.get_solde()}€.")
            else:
                print("Solde insuffisant pour effectuer ce retrait.")
        else:
            print("Le montant doit être positif pour un retrait.")
    
    # Consultation du solde
    def consultation(self):
        print(f"Solde actuel: {self.get_solde()}€.")

# Simulation
cb = CompteBancaire(300)

# Consultation avec méthode get_solde()
cb.consultation()  # Solde actuel: 300€
a =  float(input("Dépôt de combien ? : "))
# Utilisation des méthodes getter et setter
print(cb.get_solde())  # Appelle get_solde() au lieu de cb.solde
cb.set_solde(a)
print(cb.get_solde())  # Affiche 500
