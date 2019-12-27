from django import forms

class TeamSearch(forms.Form):
    team = forms.CharField(label='Search Pokemon', max_length=300, widget=forms.TextInput(attrs={'id': 'searchBar', 'type': 'text', 'name': 'myTeam', 'placeholder': 'Pokemon'}))