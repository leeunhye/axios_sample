from rest_framework import generics

from rest_framework.response import Response

from communicate.models import Approval
from communicate.serializers.messageSerializer import MessageSerializer


class MessageListView(generics.ListAPIView):
    """
    情報リストを取得して画面に送信する。
    """
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = MessageSerializer(queryset, many=True)

        print(serializer.data)

        return Response(serializer.data)

    def get_queryset(self):
        # DBからデータを取得します。
        # queryset = [
        #     {'company': '営業部', 'name': '山田太郎', 'apply_date': '2021-09-06', 'title': '申請タイトルになる', 'content': '申請内容なんちゃら'},
        #     {'company': '営業部', 'name': '佐藤次郎', 'apply_date': '2021-09-08T22:44:16.923000', 'title': '給料の支給', 'content': 'お金ほしいです！'},
        #     {'company': '広報部', 'name': '大阪花子', 'apply_date': '2021-09-09T22:44:16.923000', 'title': '新しいボールペン購入', 'content': '10色ペンセットがほしいかも'}
        # ]
        queryset = Approval.objects.all()

        return queryset
