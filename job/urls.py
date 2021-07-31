from . import views
from  django.urls import path, include


urlpatterns = [
    path('', views.Job_list),
    path('<int:id>', views.Job_detail),


]
