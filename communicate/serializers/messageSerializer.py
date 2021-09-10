from rest_framework.serializers import *


class MessageSerializer(Serializer):
    # modelの項目を参考にしてください。Fieldも合わせてください。
    id = IntegerField(read_only=True)
    company = CharField(read_only=True)
    name = CharField(read_only=True)
    apply_date = DateTimeField(read_only=True)
    title = CharField(read_only=True)
    content = CharField(read_only=True)


