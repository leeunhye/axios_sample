from django.shortcuts import render
from django.views.generic import TemplateView


class MessageView(TemplateView):
    template_name = 'communicate/communication.html'

    def get(self, request, *args, **kwargs):
        context = super(MessageView, self).get_context_data(**kwargs)

        return render(self.request, self.template_name, context)
