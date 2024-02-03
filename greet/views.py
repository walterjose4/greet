from django.views.generic import TemplateView


# Create your views here.
class greet(TemplateView):
    template_name = "greet.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["additional_data"] = kwargs["additional_data"].capitalize()
        return context
