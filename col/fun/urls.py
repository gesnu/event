from django.urls import path
from . import views

urlpatterns = [
    path('insert', views.makecreate),
    path('view',views.makelist),
    path('show/<int:seriel>',views.makeRead),
    path('change/<int:num>',views.makeEdit),
    path('del/<int:unique>',views.makeDelete),
    path('page',views.makepage)
]
