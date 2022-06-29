from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,DetailView,ListView
from candidate.forms import CandidateProfileForm
from candidate.models import CandidateProfile
from employer.models import Jobs,Applications
from django.urls import reverse_lazy
from candidate.filters import JobFilter
# Create your views here.
class CandidateHomeView(TemplateView):
    template_name = "cand-home.html"
    #extra ata to be send we override this -list all jobs
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        qs=Jobs.objects.all()
        context["jobs"]=qs
        return context
    def get(self, request, *args, **kwargs):
        filter=JobFilter(request.GET,queryset=Jobs.objects.all())
        return render(request,"cand-home.html",{"filter":filter})

class CandidateProfileCreateView(CreateView):
    model = CandidateProfile
    form_class = CandidateProfileForm
    template_name = "cand-profile.html"
    success_url = reverse_lazy("cand-home")
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    #view profile
    #list job
class CandProfileDetailView(TemplateView):
    template_name = "cand-profiledetail.html"
class CandidateJobDetailView(DetailView):
    template_name = "cand-detailjob.html"
    model = Jobs
    context_object_name = "job"
    pk_url_kwarg = "id"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        qs=Applications.objects.filter(applicant=self.request.user,job=self.object)
        print(qs)
        context["status"]=qs
        return context

#only function based view is needed
def applynow(request,*args,**kwargs):
    job_id=kwargs.get("id")
    job=Jobs.objects.get(id=job_id)
    applicant=request.user
    Applications.objects.create(applicant=applicant,job=job)
    return redirect("cand-home")
class MyApplicationViews(ListView):
    model = Applications
    template_name = "myapplicatons-detail.html"
    context_object_name = "applied"
    def get_queryset(self):
        return Applications.objects.filter(applicant=self.request.user)
class AcceptedApplications(ListView):
    model = Applications
    template_name = "accepted.html"
    context_object_name = "application"
    def get_queryset(self):
        return Applications.objects.filter(applicant=self.request.user,status="accepted")












