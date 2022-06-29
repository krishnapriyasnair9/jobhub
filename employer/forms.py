from django import forms
from employer.models import EmployerProfile,Jobs
class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model=EmployerProfile
        exclude=("user",) #this exlude is used to exlude so field only
        """fields=["company_name",
                "logo",
                "bio",
                "location"]"""
class JobForm(forms.ModelForm):
    class Meta:
        model=Jobs
        exclude=("posted_by","created_date")
        widgets={
            "job_title":forms.TextInput(attrs={"class":"form-control"}),
            "last_date":forms.DateInput(attrs={"class":"form-control","type":"date"})
        }






