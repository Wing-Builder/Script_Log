import re

log_line = "2025-03-12 14:38:42,530 - CRITICAL - Tentative d'acc�s non autoris�e"

# Modifié pour capturer la date/heure et l'événement
regex = r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) - (CRITICAL|INFO|WARNING) - (.+)$"

match = re.search(regex, log_line)
if match:
    date_heure = match.group(1)  # Date et heure capturées dans le 1er groupe
    niveau = match.group(2)      # Niveau du log capturé dans le 2e groupe
    evenement = match.group(3)   # Événement capturé dans le 3e groupe

    print(f"Date et heure: {date_heure}")
    print(f"Niveau: {niveau}")
    print(f"Événement: {evenement}")