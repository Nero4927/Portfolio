from django.views.generic import TemplateView

class AccueilView(TemplateView):
    template_name = "accueil.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nom"] = "test"
        return context
