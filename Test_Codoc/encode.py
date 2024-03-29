import requests

# Appeler l'endpoint /key pour générer et stocker la clé publique dans la session
response_key = requests.get("http://localhost:8000/key/")
if response_key.status_code == 200:
    print("Clé publique générée avec succès.")
else:
    print("Erreur lors de la génération de la clé publique :", response_key.text)

# Appeler l'endpoint /encode avec le message à encoder
message_to_encode = "Hello world"
response_encode = requests.get(f"http://localhost:8000/encode/?msg={message_to_encode}")
if response_encode.status_code == 200:
    encoded_message = response_encode.json()['encoded_message']
    print("Message encodé :", encoded_message)
else:
    print("Erreur lors de l'encodage du message :", response_encode.text)
