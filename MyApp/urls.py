
from django.urls import path
from . import views

urlpatterns = [
    path('hello',views.demo),
    path('helloht',views.demoHtml),
    path('login',views.loginDemo),
    path('verify',views.verifyData),
    path('demoData',views.demodata),
    path('demoData1',views.demoData1),
]
