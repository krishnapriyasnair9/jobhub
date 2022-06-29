from django.urls import path
from employer import views
urlpatterns=[
    path("ehome",views.EmployerHomeView.as_view(),name="emp-home"),
    path("profiles/add",views.EmployerProfileCreateView.as_view(),name="emp-profile"),
    path("profiles/details",views.EmployeProfileDetailView.as_view(),name="emp-detail"),
    path("jobs/add",views.JobCreateView.as_view(),name="emp-addjob"),
    path("jobs/all",views.EmployerJobListView.as_view(),name="emp-listjob"),
    path("jobs/detail/<int:id>",views.JobDetailView.as_view(),name="emp-jobdetail"),
    path("jobs/update/<int:id>",views.JobChangeView.as_view(),name="emp-jobupdate"),
    path("jobs/delete/<int:id>",views.JobDeleteView.as_view(),name="emp-jobdelete"),
    path("jobs/applications/<int:id>",views.ViewApplications.as_view(),name="view-applications"),
    path("jobs/applications/view/detail/<int:id>",views.ApplicationDetailView.as_view(),name="view-detail"),
    path("status/<int:id>",views.updateapplication,name="reject"),
    path("status/<int:id>",views.acceptapplication,name="accept"),
    path("profiles/signout", views.signout, name="signout")


]