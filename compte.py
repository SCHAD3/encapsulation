class CompteBancaire:
    def __init__(self, solde=0):
        self.__solde = solde  # Utilise le solde passé lors de l'instanciation
    
    # Récupère le solde du compte (getter)
    @property
    def solde(self):
        return self.__solde

    # Met à jour le solde du compte (setter)
    @solde.setter
    def solde(self, nouveau_solde):
        if nouveau_solde >= 0:
            self.__solde = nouveau_solde
        else:
            raise ValueError("Le solde ne peut pas être négatif!")
    
    # Déposer de l'argent
    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            print(f"Déposé: {montant}€. Nouveau solde: {self.solde}€.")
        else:
            print("Le montant doit être positif pour un dépôt.")

    # Retirer de l'argent
    def retirer(self, montant):
        if montant > 0:
            if self.__solde >= montant:
                self.__solde -= montant
                print(f"Retiré: {montant}€. Nouveau solde: {self.solde}€.")
            else:
                print("Solde insuffisant pour effectuer ce retrait.")
        else:
            print("Le montant doit être positif pour un retrait.")
    
    # Consultation du solde
    def consultation(self):
        print(f"Solde actuel: {self.solde}€.")


# Simulation
a = float(input("Dépôt de combien ? : "))  # Convertit l'entrée en float
b = float(input("Retrait de combien ? : "))  # Convertit l'entrée en float

# Création d'un compte avec un solde initial de 300€
cb = CompteBancaire(300)

# Affichage du solde initial
cb.consultation()

# Effectuer un dépôt
print("Effectuer un dépôt")
cb.deposer(a)

# Consultation du solde après dépôt
cb.consultation()

# Effectuer un retrait
print("Effectuer un retrait")
cb.retirer(b)  # Utilisation de retirer(b) au lieu de deposer(b)

# Consultation du solde après retrait
cb.consultation()
