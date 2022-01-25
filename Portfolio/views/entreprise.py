from django.views.generic import TemplateView

class EntrepriseView(TemplateView):
    template_name = "entreprise.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nom"] = "test"
        return context
