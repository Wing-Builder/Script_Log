from os import access
import pandas as pd 

class LogAnalyzer:
    def __init__(self, df_logs):
        """
        Constructeur qui initialise l'objet LogAnalyzer avec un DataFrame contenant les logs extraits.

        Paramètres : 
        df_logs (pd.DataFrame) : Le DataFrame contenant les informations extraites des logs.
        """
        
        self.df_logs = df_logs


    def analyser_frequence_ips(self, intervalle_temps='1min', seuil_alerte=100):
        """
        Analyze la fréquence d'apparition d'adresses IP dans les logs.
        Détecte les adresses IP suspectes dépassant un seuil d'alerte.

        Paramètres:
        intervalle temps='1min'
        seuil_alerte(int) : Nombre de requêtes au-delà duquel une adresse IP est considérée comme suspecte
        """

        if not self.df_logs.empty:
            #Convertir la colonne 'Date/Heure' en datetime si pas déjà fait
            try:
                self.df_logs['Date/Heure'] = pd.to_datetime(self.df_logs['Date/Heure'], format='%b %d %H:%M:%S')
            except Exception as e:
                print(f"Erreur lors de la conversion des dates : {e}")
                return

            #Grouper par adresse IP et intervalle de temps
            acces_par_ip = self.df_logs.set_index('Date/Heure').groupby(
                [pd.Grouper(freq=intervalle_temps), 'AdresseIP']
            ).size()

            #Filtrer les groupes dépassant le seuil d'alerte
            acces_suspects= acces_par_ip[acces_par_ip > seuil_alerte]    

            #Afficher les résultats
            if not acces_suspects.empty:
                print(f"\nAccès suspects détectés plus de {seuil_alerte} accès par IP dans {intervalle_temps}")
                print(acces_suspects)
            else:
                print(f"Aucun accès suspect détecté dans l'intervalle de {intervalle_temps}.")
        else:
            print("Le DataFrame est vide. Veuillez changer les logs avant l'analyse.")


        #     #Compter le nombre d'occurences de chaque adresse IP
        #     frequence_ips = self.df_logs['AdresseIP'].value_counts()

        #     #Filtrer les adresses IP qui dépassent le seuil d'alerte
        #     ips_suspectes = frequence_ips[frequence_ips > seuil_alerte]

        #     #afficher les adresses IP suspectes:
        #     if not ips_suspectes.empty:
        #         print(f"\nAdresses IP suspectes depassant le seuil de {seuil_alerte} requetes: ")
        #         print(ips_suspectes)
        #     else:
        #         print(f"\nAucune adresse IP n'a depasse le seuil de {seuil_alerte} requetes: ")  

        # else:
        #     print("le DataFrame est vide. Assurez-vous d'avoir lu et extrait les logs avant d'analyser le fichier")  