from django.urls import path
# On importe les vues qui sont déclarées dans leur propre dossier (module)
from .views import AccueilView, EntrepriseView, VeilleView, Projet_entrepriseView, projet_ecoleView, AboutView

urlpatterns = (
    path("Accueil", AccueilView.as_view(), name="accueil"),
    path("Entreprise", EntrepriseView.as_view(), name="entreprise"),
    path("veille", VeilleView.as_view(), name="veille"),
    path("projet_ecole", projet_ecoleView.as_view(), name="projet_ecole"),
    path("projet_entreprise", Projet_entrepriseView.as_view(), name="projet_entreprise"),
    path("a-propos", AboutView.as_view(), name="about"),
    #path("a-propos", VeilleView.as_view(), name="veille"),
)
