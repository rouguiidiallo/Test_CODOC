# Utilisez une image de base Python
FROM python:3.11

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installez les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiez le contenu de votre application dans le conteneur
COPY . .

# Exposez le port sur lequel votre application Django s'exécute
EXPOSE 8000

# Commande par défaut à exécuter lorsque le conteneur démarre
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
