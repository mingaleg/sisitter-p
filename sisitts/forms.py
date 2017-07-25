from django.forms import Form, ModelForm

from sisitts.models import Sisit


class NewSisitForm(ModelForm):
    class Meta:
        model = Sisit
        exclude = [
            "likes_count",
            'author',
        ]