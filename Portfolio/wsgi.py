"""
Fichier utilisé comme point d'entrée dans le projet
lorsque l'on réalise un déploiement en production avec WSGI

https://docs.djangoproject.com/fr/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# !!! Nom "mainapp" à remplacer par le nom de dossier de votre application !!!
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Portfolio.settings.prod')

application = get_wsgi_application()
