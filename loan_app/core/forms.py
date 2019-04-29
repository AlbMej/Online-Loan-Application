from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field

BUSINESS_TYPE = (
    ('', 'Choose...'),
    ('FT', 'Food Truck'),
    ('CON', 'Construction'),
    ('OTH', 'Other')
)

class AddressForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'placeholder': '1234 Main St, City, State, Zipcode'}))
    amount_required = forms.CharField(label = 'Amount required')
    business_type = forms.ChoiceField(choices=BUSINESS_TYPE)
    years_in_business = forms.CharField(label='Years in business')
    agree = forms.BooleanField(required=False)

class CustomCheckbox(Field):
    template = 'custom_checkbox.html'

class CustomFieldForm(AddressForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'password',
            'address',
            Row(
                Column('amount_required', css_class='form-group col-md-6 mb-0'),
                Column('business_type', css_class='form-group col-md-4 mb-0'),
                Column('years_in_business', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            CustomCheckbox('agree'),
            Submit('submit', 'Sign in')
        )