import os
import fnmatch
import re
import pandas as pd #Pandas pour l'usage de Dataframes

class LogReader:

    def __init__(self, repertoire):
        """
        Initialise un lecteur de logs avec une liste vide pour stocker les lignes lues.
        """
        self.repertoire = repertoire #Attribut pour stocker le chemin d'un répertoire
        self.df_logs = pd.DataFrame(columns=["Date/Heure", "Événement", "AdresseIP"])
        self.lignes_extraites = [] # Accumulations de lignes extraites


    def trouver_fichiers_logs(self, pattern="secure*"):
        """
        Parcours un dossier et renvoie une liste de fichiers de logs avec l'extension spécifiée
        """
        fichiers_logs = []
        try:
            #Parcourt le dossier et récupère tous les fichiers avec l'extension donnée
            for fichier in os.listdir(self.repertoire):
                if fnmatch.fnmatch(fichier, pattern):
                    fichiers_logs.append(os.path.join(self.repertoire, fichier))
            return fichiers_logs
        except FileNotFoundError:
            print(f"Erreur : le dossier {self.repertoire} , n'a pas été trouvé.")
            return []

    # def lire_et_extraire_logs(self, fichier_log):
    #     """
    #     Lit un fichier de logs et renvoie son contenu sous forme de liste de lignes.
        
    #     Paramètres:
    #     fichier_log (str) : Chemin vers le fichier de logs à lire.

    #     Retourne :
    #     list : Liste contenant chaque ligne du fichier de logs.
    #     """
    #     regex = r"^([A-Za-z]+.*[0-9]{2}:[0-9]{2}:[0-9]{2}(\.[0-9]{1,3})?.*([A-Za-z]+( [A-Za-z]+)+)\[.*\].*([A-Za-z]+( [A-Za-z]+)+).*\b(?:(?:2(?:[0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9])\.){3}(?:(?:2([0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9]))\b(\s([A-Za-z]+\s)+)"
    #     # regex = r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) - (CRITICAL|INFO|WARNING|ERROR) - (.+)$"

    #     try:
    #         with open(fichier_log, 'r') as f:
    #             for ligne in f:
    #                 match = re.search(regex, ligne)
    #                 if match:
    #                     date_heure = match.group(1)  # Date et heure capturées dans le 1er groupe
    #                     niveau = match.group(2)      # Niveau du log capturé dans le 2e groupe
    #                     evenement = match.group(3)   # Événement capturé dans le 3e groupe
    #                     adresseIP = match.group(4)

    #                     nouvelle_ligne = {
    #                         'Date/Heure': date_heure,
    #                         'Niveau': niveau,
    #                         'Événement': evenement,
    #                         'AdresseIP' : adresseIP
    #                     }
    #                     self.lignes_extraites.append(nouvelle_ligne)

    #                     nouvelle_ligne_df = pd.DataFrame([nouvelle_ligne])
    #                     self.df_logs = pd.concat([self.df_logs, nouvelle_ligne_df], ignore_index=True)

    #         print(f"Le fichier {fichier_log} a été lu et les infos ont été extraites avec succès.")
    #     except FileNotFoundError:
    #         print(f"Erreur : Le fichier {fichier_log} n'a pas été trouvé.")
    #         # self.lignes_lues = [] #réinitialisation en cas d'erreur

    def lire_et_extraire_logs(self, fichier_log):
        """
        Lit un fichier de logs et extrait les informations sous forme de dictionnaire.

        Paramètres :
        fichier_log (str) : Chemin vers le fichier de logs à lire.

        Retourne :
        list : Liste contenant les logs extraits sous forme de dictionnaires.
        """
        regex = r"^([A-Z][a-z]{2} \d{1,2} \d{2}:\d{2}:\d{2}) (Failed password|Invalid user) from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$"

        try:
            with open(fichier_log, 'r') as f:
                for ligne in f:
                    match = re.search(regex, ligne)
                    if match:
                        date_heure = match.group(1)  # Date et heure
                        evenement = match.group(2)   # Événement (Failed password / Invalid user)
                        adresse_ip = match.group(3)  # Adresse IP

                        nouvelle_ligne = {
                            "Date/Heure": date_heure,
                            "Événement": evenement,
                            "AdresseIP": adresse_ip
                        }
                        self.lignes_extraites.append(nouvelle_ligne)

                        # Ajouter à un DataFrame
                        nouvelle_ligne_df = pd.DataFrame([nouvelle_ligne])
                        self.df_logs = pd.concat([self.df_logs, nouvelle_ligne_df], ignore_index=True)

            print(f"Le fichier '{fichier_log}' a été lu et les logs ont été extraits avec succès.")

        except FileNotFoundError:
            print(f"Erreur : Le fichier '{fichier_log}' n'a pas été trouvé.")

# Exemple d'utilisation :
# parser = LogParser()
# parser.lire_et_extraire_logs("auth_logs_linux_200.log")
# print(parser.df_logs.head())


    def creer_dataframe(self):
        """
        Créer un Dataframe avec Pandas à partir des lignes extraites et l'affecte à l'attribut df_logs.
        """

        if self.lignes_extraites:
            self.df_logs = pd.DataFrame(self.lignes_extraites)
            self.lignes_extraites.clear() #effacer la liste des lignes pour économiser la mémoire
            print("Le dataframe a été créé  avec succès.")
        else:
            print("Aucune ligne extraite. Le dataframe est vide.")

    def afficher_dataframe(self):
        """
        Affiche le dataframe contenant les infos extraites des logs.
        """

        print("\nDataFrame des Logs extraits:")
        print(self.df_logs)

    # def afficher_lignes_lues(self):
    #     """
    #     Affiche le nombre de lignes lues et les premières lignes du fichiers.
    #     """
    #     if self.lignes_lues:
    #        print(f"Nombres total de lignes lues : {len(self.lignes_lues)}")
    #        print(f"Premières lignes du fichier :")
    #        #Affiche les 5 premières lignes pour donner un aperçu
    #        for ligne in self.lignes_lues[:5]:
    #             print(ligne.strip())
    #     else:
    #         print("Aucune ligne n'a été lue.")