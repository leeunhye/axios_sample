from rest_framework import generics

from rest_framework.response import Response


class MessageListView(generics.ListAPIView):
    """
    情報リストを取得して画面に送信する。
    """
    def get(self, request, *args, **kwargs):
        # pip install djangorestframeworkでrestframeworkをインストールしてから確認
        data = self.get_queryset()

        return Response(data)

    def get_queryset(self):
        # DBからデータを取得します。
        queryset = [
            {'company': '営業部', 'name': '山田太郎', 'apply_date': '2021-09-06', 'title': '申請タイトルになる', 'content': '申請内容なんちゃら'},
            {'company': '営業部', 'name': '佐藤次郎', 'apply_date': '2021-09-08', 'title': '給料の支給', 'content': 'お金ほしいです！'},
            {'company': '広報部', 'name': '大阪花子', 'apply_date': '2021-09-09', 'title': '新しいボールペン購入', 'content': '10色ペンセットがほしいかも'}
        ]

        return queryset
