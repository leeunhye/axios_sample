import json

from django.forms import model_to_dict
from django.http import JsonResponse

from django.views.generic.edit import BaseCreateView


class MessageCreateView(BaseCreateView):
    def post(self, request, *args, **kwargs):
        data = json.loads(self.request.body)
        print(data)

        return JsonResponse(data={}, status=201)

