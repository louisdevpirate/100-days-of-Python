from flask import Flask, render_template, request
from datetime import datetime

# Création de l'instance de l'application Flask
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    """
    Gère les requêtes GET et POST pour la route racine ('/').
    Affiche un formulaire pour saisir un nom et retourne un message de bienvenue personnalisé.

    Returns:
        str: Page HTML rendue avec un message de bienvenue et la date du jour
    """
    name = None
    # Obtention de la date actuelle et formatage
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Vérifie si la requête est de type POST (soumission du formulaire)
    if request.method == 'POST':
        # Récupère le nom saisi dans le formulaire
        name = request.form.get('name')

    # Rend le template avec les données appropriées
    return render_template('index.html', name=name, date=current_date)


# Vérifie si le script est exécuté directement (et non importé)
if __name__ == '__main__':
    # Lance l'application en mode debug
    app.run(debug=True)