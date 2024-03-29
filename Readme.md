# Application Web Python

Ce projet est une petite application web en Python exposant quatre endpoints différents pour des fonctionnalités spécifiques.

## Endpoints

1. **GET /health**  
   - Ce endpoint renvoie une réponse vide avec un statut HTTP 200, indiquant que le service est opérationnel.

2. **GET /key**  
   - Ce endpoint renvoie une clé publique RSA générée par le serveur.

   3. **GET /encode**
   -Ce endpoint permet d'encoder une message avec la clé publique récupérée depuis `/key`

3. **GET /decode**  
   - Ce endpoint permet de décoder un message encodé avec la clé publique récupérée depuis `/key`. Le message à décoder doit être fourni en tant que paramètre de requête nommé `msg`.

## Utilisation

Pour utiliser cette application, assurez-vous d'avoir Python installé sur votre système. Vous pouvez exécuter le serveur de l'application en exécutant le script `python manage.py runserver`. Assurez-vous d'installer les dépendances requises en exécutant :

```bash
pip install -r requirements.txt
