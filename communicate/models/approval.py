from django.db import models


class Approval(models.Model):
    # 申請部署
    company = models.CharField(max_length=10)
    # 申請者
    name = models.CharField(max_length=10)
    # 申請日
    apply_date = models.DateTimeField()
    # 申請タイトル
    title = models.CharField(max_length=20)
    # 申請内容
    content = models.CharField(max_length=100)

    def __str__(self):

        return "({}){}({})".format(self.company, self.title, self.apply_date)
