from django import forms

class Student_Info(forms.Form):
    firstname=forms.CharField(max_length=20)
    middlename = forms.CharField(max_length=20, required=False)
    lastname = forms.CharField(max_length=20)
    age=forms.IntegerField()
    grade = forms.IntegerField()
    fathername=forms.CharField(max_length=50)
    phone = forms.IntegerField()
    address=forms.CharField(max_length=50)
    #image=forms.FileField()

class Result(forms.Form):
    student_id=forms.IntegerField()
    term=forms.IntegerField()
    grade=forms.IntegerField()
    english=forms.IntegerField()
    nepali = forms.IntegerField()
    math = forms.IntegerField()
    science = forms.IntegerField()
    social = forms.IntegerField()
    ehp = forms.IntegerField(required=False)
    optionali = forms.IntegerField(required=False)
    optionalii = forms.IntegerField(required=False)
    grammar = forms.IntegerField(required=False)
    optionalmath = forms.IntegerField(required=False)
    computer = forms.IntegerField(required=False)
    gk = forms.IntegerField(required=False)
    drawing = forms.IntegerField(required=False)

class ViewInfo(forms.Form):
    student_id=forms.IntegerField()

class ResultForm(forms.Form):
    student_id=forms.IntegerField()
    term=forms.IntegerField()

class PaymentForm(forms.Form):
    student_id=forms.IntegerField()
    grade=forms.IntegerField()
    month=forms.CharField(max_length=250)
    amount=forms.IntegerField()
    remarks=forms.CharField(max_length=250)