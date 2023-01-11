import classevoiture


class Voiture:
    marque = "Kia"
    def __init__(self):
        self.couleur = "Noir"

    def ChangeColor(self, couleur):
        self.couleur = couleur
#voiture1 =Voiture()
#c=voiture1.couleur
#print(c)
#Pour changer la couleur


    #couler="Blanc"
voiture1 = Voiture()
voiture1.ChangeColor("Blanc")
d=voiture1.couleur
print(d)