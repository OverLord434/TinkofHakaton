from django import forms

class DifficultyForm(forms.Form):
    ADDITIONAL_DIFFICULTIES = [
        ('linear_equations', 'Линейные уравнения'),
        ('quadratic_equations', 'Квадратные уравнения'),
    ]

    additional_difficulty = forms.MultipleChoiceField(
        choices=ADDITIONAL_DIFFICULTIES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Дополнительная сложность"
    )