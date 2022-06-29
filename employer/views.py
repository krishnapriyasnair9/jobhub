from django.shortcuts import render, redirect
from employer.forms import EmployerProfileForm,JobForm
from employer.models import EmployerProfile,Jobs,Applications
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView,View
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate,logout
# Create your views here.
#create view-to create a view ,,database create
#update view-to edit a database
#list view-to list objects
#template view=to render an html page we use this view
#form view-to render a form

class EmployerHomeView(TemplateView):
    template_name = "emp_home.html"
class EmployerProfileCreateView(CreateView):
    model=EmployerProfile
    form_class = EmployerProfileForm
    template_name = "emp-profile.html"
    success_url =reverse_lazy("emp-home") #after create this object return back to where
    #retun can be given only to function
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)#to check form is valid or we can use the below code
    """def post(self, request, *args, **kwargs):
        form=EmployerProfileForm(request.POST,files=request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)#commit given to here is for not saving the form
            profile.user=request.user
            profile.save()
            print("profile created")
            return redirect("emp-home")

        else:
            return render(request,self.template_name,{"form":form})"""
class EmployeProfileDetailView(TemplateView):
    template_name = "emp-myprofile.html"
class JobCreateView(CreateView):
    model = Jobs
    form_class = JobForm
    template_name = "emp-postjob.html"
    success_url = reverse_lazy("emp-home")
    def form_valid(self, form):
        form.instance.posted_by=self.request.user
        messages.success(self.request,"job has been posted successfully")
        return super().form_valid(form)
class EmployerJobListView(ListView):
    model = Jobs
    context_object_name = "jobs"
    template_name = "emp-joblist.html"
    paginate_by = 2
    def get_queryset(self):
        return Jobs.objects.filter(posted_by=self.request.user).order_by("-created_date")
class JobDetailView(DetailView):
    model = Jobs
    template_name = "emp-jodetail.html"
    context_object_name = "job"
    pk_url_kwarg = "id"

class JobChangeView(UpdateView):
    model = Jobs
    template_name = "emp-jobupdate.html"
    form_class =JobForm
    success_url = reverse_lazy("emp-home")#emp-listjob
    pk_url_kwarg = "id"
    def form_valid(self, form):
        messages.success(self.request,"profile has been updated successfully")
        return super().form_valid(form)
class JobDeleteView(View):
    def get(self,request,*args,**kwargs):
        qs=Jobs.objects.get(id=kwargs.get("id"))
        qs.delete()
        return redirect("emp-listjob")
class ViewApplications(ListView):
    model = Applications
    template_name = "all-applications.html"
    context_object_name = "allapp"
    def get_queryset(self):
        return Applications.objects.filter(job=self.kwargs.get("id"),status='applied')

class ApplicationDetailView(DetailView):
    model = Applications
    template_name = "applicant-detail.html"
    context_object_name = "applic"
    pk_url_kwarg = "id"
def updateapplication(request,*args,**kwargs):
    app_id=kwargs.get("id")
    qs=Applications.objects.get(id=app_id)
    qs.status="rejected"
    qs.save()
    return redirect("emp-home")
def acceptapplication(request,*args,**kwargs):
    app_id = kwargs.get("id")
    qs = Applications.objects.get(id=app_id)
    qs.status = "accepted"
    qs.save()
    send_mail(
        'Application status',
        'APPLICATION ACCEPTED SUCCESSFULLY',
        'krishnapriyasnair9@gmail.com',
        ['artistictech123@gmail.com'],
        fail_silently=False,
    )
    return redirect("emp-home")


def signout(request, *args, **kwargs):
    logout(request)
    return redirect("signin")

#accepted application
#logout function
#in candidate edit option








