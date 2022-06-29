from django.urls import path
from candidate import views


urlpatterns=[
    path("home",views.CandidateHomeView.as_view(),name="cand-home"),
    path("profiles/add",views.CandidateProfileCreateView.as_view(),name="cand-addprofile"),
    path("profiles/detail",views.CandProfileDetailView.as_view(),name="cand-profiledetail"),
    path("jobs/details/<int:id>",views.CandidateJobDetailView.as_view(),name="cand-detailjob"),
    path("application/add/<int:id>",views.applynow,name="apply-now"),
    path("application/detail",views.MyApplicationViews.as_view(),name="cand-appdetail"),
    path("application/notifi",views.AcceptedApplications.as_view(),name="notifications")

]