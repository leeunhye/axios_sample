from django import forms

from communicate.models import Approval

# エラーメッセージを定数として管理することで複数回使われる場合もしくは変更があった場合、対応がしやすいです。
ERROR_NAME_MAX_LENGTH = "申請者の名前は10字以内で入力してください。"
ERROR_DUPLICATED_TITLE = "同一タイトルが既に存在します。"


class ApprovalForm(forms.Form):
    """
    申請内容フォーム
    入力チェックする項目を書きます。
    必須項目であること（required=True）、最大長さ指定（max_length=長さ）、最低長さ指定（min_length=長さ）など
    エラーメッセージを指定しなかったらdjangoの内装エラーメッセージが出力されるが、error_messageで指定もできます。
    """
    # 申請者
    name = forms.CharField(
        required=True,
        max_length=10,
        label='申請者',
        error_messages={'max_length': ERROR_NAME_MAX_LENGTH}
    )
    # 申請日
    apply_date = forms.DateTimeField(
        required=True
    )
    # 申請タイトル
    title = forms.CharField(
        required=True,
        max_length=20,
        label='申請タイトル'
    )
    # 申請内容
    content = forms.CharField(
        required=True,
        max_length=20,
        label='申請内容'
    )

    # clean_項目名で既存のValidationをつけれます。
    # def clean(self): で全体的な項目をもとにチェック処理ができます。
    def clean_title(self):
        title = self.cleaned_data['title']
        # 登録しようとするタイトルが既にデータベースに存在するか確認する。
        check_same_title = Approval.objects.filter(title=title).count()

        # データベースに1件以上の重複タイトルのデータがあれば、ValidationErrorを起こす。
        if check_same_title:
            raise forms.ValidationError(ERROR_DUPLICATED_TITLE)

        return title
