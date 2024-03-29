from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64encode, b64decode
import base64
import requests
def index(request):
    return HttpResponse("Bienvenue sur la page d'accueil de mon application !!!")

# Endpoint /health
@require_GET
def health(request):
    return JsonResponse({}, status=200)

# Endpoint /key
def get_key(request):
    # Générer une nouvelle paire de clés RSA
    key = RSA.generate(2048)
    # Récupérer la clé publique au format PEM
    public_key = key.publickey().export_key()
    # Stocker la clé publique dans la session
    request.session['public_key'] = public_key.decode()
    return JsonResponse({'public_key': public_key.decode()}, status=200)

# Endpoint /encode
def encode_message(request):
    response_key = requests.get("http://localhost:8000/key/")
    if response_key.status_code == 200:
        print("Clé publique générée avec succès.")
    else:
        print("Erreur lors de la génération de la clé publique :", response_key.text)

    message = request.GET.get('msg', '')
    # Récupérer la clé publique depuis la session
    public_key = request.session.get('public_key', None)
    if public_key:
        try:
            # Charger la clé publique
            rsa_key = RSA.import_key(public_key)
            # Créer un objet RSA pour le chiffrement
            cipher_rsa = PKCS1_OAEP.new(rsa_key)
            # Encoder le message
            encoded_message = cipher_rsa.encrypt(message.encode())
            # Retourner la réponse avec le message chiffré
            return JsonResponse({'encoded_message': base64.b64encode(encoded_message).decode()}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Public key not found'}, status=400)
    
# Endpoint /decode
def decode_message(request):
    encoded_message = request.GET.get('msg', '')

    # Récupérer la clé publique depuis l'endpoint /key
    key_response = requests.get('http://localhost:8000/key/')
    if key_response.status_code == 200:
        public_key_pem = key_response.json().get('public_key', '')
        rsa_key = RSA.import_key(public_key_pem)
    else:
        return JsonResponse({'error': 'Failed to retrieve public key'}, status=500)

    try:
        # Créer un objet RSA pour le déchiffrement
        cipher_rsa = PKCS1_OAEP.new(rsa_key)
        # Décoder le message encodé et le déchiffrer
        decoded_message = cipher_rsa.decrypt(base64.b64decode(encoded_message)).decode()
        return JsonResponse({'decoded_message': decoded_message}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

    