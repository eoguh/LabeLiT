from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('', views.index, name="index"),

    path('creators-dashboard/', views.creatorsDashboard, name="creators-dashboard"),
    path('creators-projects/', views.creatorsProjects, name="creators-projects"),
    path('creators-annotators/', views.creatorsAnnotators, name="creators-annotators"),
    path('annotator-labeling/', views.annotatorLabeling, name="annotator-labeling"),
    path('annotator-dashboard/', views.annotatorDashboard, name="annotator-dashboard"),

    path('project/<slug>/', views.projectPage, name="project-page"),
    
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
    path('activate/<userIdb64>/<token>/', views.activate, name="activate"),
]



# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
