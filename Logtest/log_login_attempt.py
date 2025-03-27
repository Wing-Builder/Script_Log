import logging
import random
import time

def generate_ip():
    """Génère une adresse IP aléatoire."""
    return "{}.{}.{}.{}".format(
        random.randint(1, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(1, 255)
    )

# Demander à l'utilisateur le nom du fichier log
log_filename = input("Entrez le nom du fichier log (avec ou sans extension) : ").strip()
if "." not in log_filename:
    log_filename += ".log"  # Ajouter une extension par défaut

# Configuration du logging
logging.basicConfig(
    filename=log_filename,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Messages spécifiques aux tentatives de connexion
auth_messages = [
    "Failed password for user from {}",
    "Invalid user attempted login from {}"
]

# Générer 1000 lignes de logs
for _ in range(1000):
    level = random.choice([logging.WARNING, logging.ERROR])  # Événements liés à des erreurs
    message_template = random.choice(auth_messages)
    ip_address = generate_ip()
    message = message_template.format(ip_address)
    
    logging.log(level, message)
    
    # Ajouter un léger délai pour simuler des logs en temps réel
    time.sleep(0.05)

print(f"Les logs ont été enregistrés dans '{log_filename}' avec 1000 lignes de tentatives de connexion.")
