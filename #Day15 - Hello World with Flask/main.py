from flask import Flask
from datetime import datetime

# Création de l'instance de l'application Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    """
    Fonction vue pour la route racine ('/').
    Retourne un message de salutation avec la date actuelle.

    Returns:
        str: Message de salutation avec la date du jour
    """
    # Obtention de la date actuelle et formatage
    current_date = datetime.now().strftime("%Y-%m-%d")
    # Retourne le message avec la date
    return f"Hello, World! Aujourd'hui nous sommes le {current_date}."


# Vérifie si le script est exécuté directement (et non importé)
if __name__ == '__main__':
    # Lance l'application en mode debug
    app.run(debug=True)