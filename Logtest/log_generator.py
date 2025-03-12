import logging
import random
import time

# Demander à l'utilisateur le nom du fichier log
log_filename = input("Entrez le nom du fichier log (avec ou sans extension) : ").strip()

# Vérifier si une extension a été ajoutée, sinon garder le nom brut
if "." not in log_filename:
    log_filename = log_filename  # Fichier sans extension (comme sous Unix)

# Configuration du logging
logging.basicConfig(
    filename=log_filename,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Messages de log aléatoires pour varier les entrées
messages = [
    "Connexion réussie",
    "Erreur d'authentification",
    "Fichier introuvable",
    "Opération effectuée avec succès",
    "Déconnexion de l'utilisateur",
    "Tentative d'accès non autorisée",
    "Processeur en surcharge",
    "Mémoire insuffisante",
    "Mise à jour du fichier de configuration",
    "Redémarrage du service"
]

# Générer 50 lignes de logs aléatoires
for i in range(50):
    level = random.choice([logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL, logging.DEBUG])
    message = random.choice(messages)
    
    # Correction : utiliser logging.log() au lieu de level()
    logging.log(level, message)
    
    # Ajouter un léger délai pour simuler des logs en temps réel
    time.sleep(0.1)

print(f"Les logs ont été enregistrés dans '{log_filename}' avec 50 lignes aléatoires.")
