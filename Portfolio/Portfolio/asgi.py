"""
Fichier utilisé comme point d'entrée dans le projet
lorsque l'on réalise un déploiement en production avec ASGI

https://docs.djangoproject.com/fr/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# !!! Nom "mainapp" à remplacer par le nom de dossier de votre application !!!
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Portfolio.settings.prod')

application = get_asgi_application()
