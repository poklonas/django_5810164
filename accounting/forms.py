from django import forms
from .models import Imported_csv


class ImportCsvForm(forms.ModelForm):
    class Meta:
        model = Imported_csv
        fields = ('description', 'csv_file', )

