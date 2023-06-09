from django.urls import path



from . import views

urlpatterns = [
    path("persons/", views.index, name="index"),
    path("", views.person_list, name='person_list'),
] 