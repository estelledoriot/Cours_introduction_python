"""
Exercice PizzaDrive sur les exceptions
"""


class PizzaDrive:
    """Classe représentant un drive pour commander des pizzas"""

    def __init__(self, pizzas: list[str], stock: list[int]) -> None:
        """Initialise le PizzaDrive

        Args:
            pizzas (list[str]): liste des pizzas disponibles
            stock (list[int]): listes des quantités disponibles pour chaque pizza
        """
        self.pizzas = pizzas
        self.stock = stock

    def afficher_menu(self) -> None:
        """Affiche les pizzas disponibles dans le drive"""
        print("===== Pizza drive =====")
        for i, (pizza, stock) in enumerate(zip(self.pizzas, self.stock)):
            print(f" {i+1} - {pizza:45} (plus que {stock})")

    def vendre(self, numero: int) -> None:
        """Retire une pizza des stocks pour la vendre

        Args:
            numero (int): indice de la pizza à vendre
        """
        if numero < 0 or numero > len(self.stock) - 1:
            raise ValueError(f"La pizza demandée (n°{numero}) n'est pas en stock")

        self.stock[numero] -= 1

    def prendre_la_commande(self) -> bool:
        """Affiche le menu pour l'utilisateur et enregistre son choix"""

        # Affiche le menu
        self.afficher_menu()

        # Prend la commande du client
        choix_client = 0
        while True:
            try:
                reponse = input("Votre choix ? ")
                if reponse in ["q", "quit"]:
                    return False
                choix_client = int(reponse)
                if choix_client < 1 or choix_client > len(self.stock) + 1:
                    raise ValueError
                break
            except TypeError:
                print("Veuillez donner un numéro de pizza pour la commande.")
            except ValueError:
                print(
                    f"Ce numéro n'est pas disponible. Veuillez choisir un numéro entre 1 et {len(self.stock)}"
                )

        # Gère la commande du client
        self.vendre(choix_client - 1)

        # Message de confirmation
        print("Vous pouvez venir chercher votre pizza dans 30 minutes")
        return True


if __name__ == "__main__":
    miam = PizzaDrive(
        ["pizza 3 fromages", "pizza périgourdine", "pizza savoyarde"], [2, 3, 4]
    )
    running = True
    while running:
        running = miam.prendre_la_commande()
