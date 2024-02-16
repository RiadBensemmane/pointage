from django import forms
from .models import Employe

class DateInput(forms.DateInput):
    input_type = 'date'

class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = '__all__'
        widgets = {
            'dateRecrutement': DateInput(),
            'dateDetachement': DateInput()
        }
        exclude = ['dernierPointage', 'dateDernierPointage']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fonction'].required = False
        self.fields['adresse'].required = False
        self.fields['dateRecrutement'].required = False
        self.fields['dateDetachement'].required = False
        self.fields['situationFamiliale'].required = False
        self.fields['affectOrigine'].required = False
        self.fields['nbrEnfants'].required = False


class EmployeFormUpdate(forms.ModelForm):
    class Meta:
        model = Employe
        fields = '__all__'
        exclude = ['matricule', 'dateDernierPointage','dernierPointage']
        widgets = {
            'dateRecrutement': DateInput(),
            'dateDetachement': DateInput()
        }
    
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fonction'].required = False
        self.fields['adresse'].required = False
        self.fields['dateRecrutement'].required = False
        self.fields['dateDetachement'].required = False
        self.fields['situationFamiliale'].required = False
        self.fields['affectOrigine'].required = False
        self.fields['nbrEnfants'].required = False



