import json

from django.forms import model_to_dict
from django.http import JsonResponse

from django.views.generic.edit import BaseCreateView

from communicate.forms.approvalForm import ApprovalForm
from communicate.models import Approval


class MessageCreateView(BaseCreateView):

    def post(self, request, *args, **kwargs):
        data = json.loads(self.request.body)
        # フォームクラスを指定する。
        form = ApprovalForm(data)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        data = json.loads(self.request.body)
        # 登録
        data_set = Approval()
        data_set.company = data['company']
        data_set.name = data['name']
        data_set.apply_date = data['apply_date']
        data_set.title = data['title']
        data_set.content = data['content']
        # 保存
        data_set.save()

        return JsonResponse(data=data, status=201)

    def form_invalid(self, form):
        print("form_invalid", form.errors)
        print(type(form.errors))
        print(form)
        return JsonResponse(data=form.errors, status=400)

