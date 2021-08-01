from django.urls import path
from . import views
urlpatterns = [
    path('',views.login_view,name = 'login'),
    path('usercreation/',views.user_creation_view,name = 'usercreation'),
    path('additem/',views.add_item_view,name = 'additem'),
    path('logout/',views.logout_view, name = 'logout'),
    path('display/',views.display_item_view, name = 'display'),

]
