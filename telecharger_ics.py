import requests

def telecharger_fichier_ics():
    # URL de téléchargement du fichier .ics
    url_ics = "https://gestac.umons.ac.be/MyUmons/module_horaire/monIcalendar.php?fichier=232040.ics"
    
    # Télécharge le fichier
    try:
        response = requests.get(url_ics, allow_redirects=True)
        response.raise_for_status()
        
        # Enregistre le fichier dans le dépôt
        with open("public/mon_horaire.ics", "wb") as fichier:
            fichier.write(response.content)
        
        print("Fichier .ics téléchargé et mis à jour avec succès.")
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors du téléchargement : {e}")

if __name__ == "__main__":
    telecharger_fichier_ics()
