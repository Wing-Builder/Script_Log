import os
import fnmatch

class LogReader:
    def __init__(self, repertoire):
        """
        Initialise un lecteur de logs avec une liste vide pour stocker les lignes lues.
        """
        self.lignes_lues = [] #Attribut d'instance pour stocker les lignes lues.
        self.repertoire = repertoire #Attribut pour stocker le chemin d'un répertoire

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

    def lire_logs(self, fichier_log):
        """
        Lit un fichier de logs et renvoie son contenu sous forme de liste de lignes.
        
        Paramètres:
        fichier_log (str) : Chemin vers le fichier de logs à lire.

        Retourne :
        list : Liste contenant chaque ligne du fichier de logs.
        """
        try:
            with open(fichier_log, 'r') as f:
                self.lignes_lues.extend(f.readlines())
            print(f"Le fichier {fichier_log} a été lu avec succès.")
        except FileNotFoundError:
            print(f"Erreur : Le fichier {fichier_log} n'a pas été trouvé.")
            # self.lignes_lues = [] #réinitialisation en cas d'erreur

    def afficher_lignes_lues(self):
        """
        Affiche le nombre de lignes lues et les premières lignes du fichiers.
        """
        if self.lignes_lues:
           print(f"Nombres total de lignes lues : {len(self.lignes_lues)}")
           print(f"Premières lignes du fichier :")
           #Affiche les 5 premières lignes pour donner un aperçu
           for ligne in self.lignes_lues[:5]:
                print(ligne.strip())
        else:
            print("Aucune ligne n'a été lue.")