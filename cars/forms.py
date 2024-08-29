from django import forms
from cars.models import Car

    
class CarModelForm(forms.ModelForm):

    class Meta:
        
        model = Car
        fields = '__all__'


    def clean_value(self):

        value = self.cleaned_data.get('value')

        if value < 20000:
            self.add_error('value', 'O valor mínimo do veículo deve ser de R$20.000,00')
        return value
    
    def clean_factoryYear(self):

        factory_year = self.cleaned_data.get('factoryYear')

        if factory_year < 1975:
            self.add_error('factoryYear', 'O ano mínimo de veículos para cadastrar é de 1975')
        return factory_year