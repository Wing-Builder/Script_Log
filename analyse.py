import argparse
from Modules.log_reader import LogReader

def main():
    parser = argparse.ArgumentParser(description="Script d'analyse de logs")
    parser.add_argument("repertoire", help="Chemin vers les fichiers de logs à analyser", type=str)
    parser.add_argument("--pattern", help="Pattern pour filtrer les fichiers de logs (Par défaut 'secure*')", type=str, default="secure*")
    parser.add_argument("--seuil", help="Seuil d'alertes pour les adresses IP suspectes", type=int, default=100)
    args = parser.parse_args()

    #Création d'une instance logreader avec le chemin du repertoire
    lecteur = LogReader(args.repertoire)

    #Trouver tous les fichiers de logs dans le répertoire
    fichiers_logs = lecteur.trouver_fichiers_logs(pattern=args.pattern)

    #Si les fichiers sont trouvés, les lire un par un
    if fichiers_logs:
        for fichier_log in fichiers_logs:
            print(f"\nLecture du fichier: {fichier_log}")
            lecteur.lire_et_extraire_logs(fichier_log) #lire le fichier de log

        #Créer le DataFrame une fois que tous les fichiers sont lus
        lecteur.creer_dataframe()

        #Créer une instance de LogAnalyzer pour analyser les logs
        analyseur = LogAnalyzer(lecteur.df_logs)

        #Analyser la fréquence des adresses IP
        analyseur.analyser_frequence_ips(seuil_alertes=args.seuil)

        #Afficher le DataFrame contenant les informations extraites
        # lecteur.afficher_dataframe()

    else:
        print("Aucun fichier de logs trouvé dans le répertoire.")

if __name__ == "__main__":
    main()