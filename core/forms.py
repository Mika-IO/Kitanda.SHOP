# forms.py

from django import forms
from core.models import Store


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = [
            "type",
            "name",
            "image",
            "delivery_fee",
            "slug",
            "whatsapp",
            "facebook",
            "instagram",
            "address",
        ]
