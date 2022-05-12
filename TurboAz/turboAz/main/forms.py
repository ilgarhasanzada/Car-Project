from django.forms import ModelForm
from .models import Car, Color,Marka, Model, Oturucu, Suretler_qutusu, Yanacaq
class carForm(ModelForm):
    class Meta:
        model=Car
        fields='__all__'
class edit_Car(ModelForm):
    class Meta:
        model=Car
        fields=['choose']
class markaForm(ModelForm):
    class Meta:
        model=Marka
        fields='__all__'
class modelForm(ModelForm):
    class Meta:
        model=Model
        fields='__all__'
class oturucuForm(ModelForm):
    class Meta:
        model=Oturucu
        fields='__all__'
class colorForm(ModelForm):
    class Meta:
        model=Color
        fields='__all__'
class yanacaqForm(ModelForm):
    class Meta:
        model=Yanacaq
        fields='__all__'
class SuretlerForm(ModelForm):
    class Meta:
        model=Suretler_qutusu
        fields='__all__'