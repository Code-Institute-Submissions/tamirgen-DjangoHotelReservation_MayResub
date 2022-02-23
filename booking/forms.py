from django import forms

class AvailabilityForm(forms.Form):

    ROOM_CATEGORIES = (
        ('SIN', 'SINGLE'),
        ('DBL', 'DOUBLE'),
        ('QUE', 'QUEEN'),
        ('KIN', 'KING'),
    )

    room_category = forms.ChoiceField(choices=ROOM_CATEGORIES, required=True)
    check_in = forms.DateTimeField(required=True, input_formats=['%d-%m-%Y'])
    check_out = forms.DateTimeField(required=True, input_formats=['%d-%m-%Y'])