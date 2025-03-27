import pandas as pd

class Log_Analyzer:
    def __init__(self, df_logs):
        """
        Constructeur qui initialise l'objet LogAnalyzer avec un DataFrame contenant les logs extraits.

        Paramètres:
        df_logs (pd.DataFrame) : Le DataFrame contenant les informations extraites  
        """
        self.df_logs = df_logs

    def analyzer_frequence_ips(self, seuil_alerte=100):
        """
        Analyse la fréquence d'apparition des adresses IP dans les logs.
        Détecte les adresses IP suspectes dépassant un seuil d'alerte.

        Paramètres:
        seuil d'alerte (int): nombre de requêtes au-delà duquel l'adresse IP est considérée comme suspecte
        """
        if not self.df_logs.empty:
            #Compter le nombre d'occurences de chaque adresse IP.
            frequence_ips = self.df_logs['AdresseIP'].value_counts()