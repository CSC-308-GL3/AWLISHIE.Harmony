class Client:
    def __init__(self, nom, prenom, adresse):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
    
    def __str__(self):
        return f"{self.nom.upper()} {self.prenom.capitalize()}\n{self.adresse}"
