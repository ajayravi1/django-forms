from django import forms
from .models import review

# choice = [
#     ('1','Blue'),``
#     ('2','Red'),
#     ('3','Green'),
#     ('4','Yellow')
# ]

# class ReviewForm(forms.Form):
#     username = forms.CharField(label="Your Name : ",max_length=10,error_messages={'required':'Form Cannot Be Empty'})
#     feedback = forms.CharField(label="Feed Back : ",max_length=250,widget=forms.Textarea)
#     ratings = forms.IntegerField(label="Ratings : ")
#     favourite_color = forms.MultipleChoiceField( label="Favourite Color : ",choices=choice,widget=forms.CheckboxSelectMultiple) . 


class ReviewForm(forms.ModelForm):
    class Meta:
        model = review
        fields = "__all__"
        exclude = ['favourite_color']
        labels = {'username':'Your Name','feedback':'Your Review'}
        error_messages = {
            'username':{'required':'User Name cannot be empty','max_lengt':'Limit Exceeded'}
        }