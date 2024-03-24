# fetch_gitlab_activity.py
import requests
import datetime
import os

# Configure pour récupérer les activités depuis une date spécifique ou toute l'activité
start_date = datetime.date(2015, 1, 1)  # Date très antérieure pour simuler "toute l'activité"
end_date = datetime.date.today()
date_format = "%Y-%m-%d"

# URL de l'API GitLab pour les événements utilisateur
url = f"https://gitlab.com/api/v4/users/{os.getenv('GITLAB_USER_ID')}/events?after={start_date.strftime(date_format)}&before={end_date.strftime(date_format)}"

headers = {"Authorization": f"Bearer {os.getenv('GITLAB_TOKEN')}"}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    activities = response.json()

    # Traitement simple pour démonstration - à personnaliser
    with open('ACTIVITY.md', 'w') as f:
        f.write("# Activité GitLab\n\n")
        for activity in activities:
            f.write(f"- {activity['action_name']} sur {activity['created_at']}\n")
else:
    print(f"Erreur lors de la récupération des activités: {response.status_code}")
    print(f"Détails: {response.text}")
