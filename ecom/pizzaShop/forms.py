from django import forms
from .models import *




# class PizzaForm(forms.Form):
#     SIZES = [('Small', 'Small'),
#              ('Medium', 'Medium'),
#              ('Large', 'Large')]

#     TOPS = [('Pineapple', 'Pineapple'),
#             ('Cheese', 'Cheese'),
#             ('Olives', 'Olives')
#             ]

#     main_topping = forms.MultipleChoiceField(choices=TOPS, widget=forms.CheckboxSelectMultiple)

#     topping1 = forms.CharField(max_length=100, label='Topping 1')
#     topping2 = forms.CharField(max_length=100, label='Topping 2')
#     size = forms.ChoiceField(label='Size', choices=SIZES)



class PizzaForm(forms.ModelForm):


    size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.RadioSelect)

    class Meta:
        model = Pizza
        fields  = ['topping1', 'topping2', 'size',]
        labels = {
                    'topping1': 'Topping 1', 
                    'topping2': 'Topping 2',
                  }


        
class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)
    