from django import forms
from cars.models import Brand, Car

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def save(self, commit=True):
        car = super().save(commit=False)
        if commit:
            car.save()
        return car

class CarForm(forms.Form):
    model = forms.CharField(max_length=100, required=True)
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), required=True)
    factory_year = forms.IntegerField(required=False, min_value=1886, max_value=2100)
    model_year = forms.IntegerField(required=False, min_value=1886, max_value=2100)
    plate = forms.CharField(max_length=10, required=False)
    price = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
    photo = forms.ImageField(required=False)

    def save(self):
        car = Car(
            model=self.cleaned_data['model'],
            brand=self.cleaned_data['brand'],
            factory_year=self.cleaned_data['factory_year'],
            model_year=self.cleaned_data['model_year'],
            plate=self.cleaned_data['plate'],
            price=self.cleaned_data['price'],
            photo=self.cleaned_data['photo']
        )
        car.save()
        return car
