import argparse
from Modules.log_reader import LogReader

def main():
    parser = argparse.ArgumentParser(description="Script d'analyse de logs")
    parser.add_argument(
        "repertoire", help="Chemin vers les fichiers de logs à analyser", type=str
    )
    parser.add_argument(
        "--pattern", help="Pattern pour filtrer les fichiers de logs (Par défaut 'secure*')", type=str, default="secure*"
    )
    args = parser.parse_args()

    #Création d'une instance logreader avec le chemin du repertoire
    lecteur = LogReader(args.repertoire)
    #Trouver tous les fichiers de logs dans le répertoire
    fichiers_logs = lecteur.trouver_fichiers_logs()

    #Si les fichiers sont trouvés, les lire un par un
    if fichiers_logs:
        for fichier_log in fichiers_logs:
            print(f"\nLecture du fichier: {fichier_log}")
            lecteur.lire_logs(fichier_log) #lire le fichier de log

        lecteur.afficher_lignes_lues()
    else:
        print("Aucun fichier de logs trouvé dans le répertoire.")

if __name__ == "__main__":
    main()