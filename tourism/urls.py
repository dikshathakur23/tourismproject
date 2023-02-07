from django.contrib import admin
from django.urls import path
from tour import views


from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('addblog',views.addblog,name='addblog'),
    path('readmore<int:id>',views.readmore,name='readmore'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('signup',views.signup,name='signup'),
    path('contactus',views.ContactPage,name='contactus'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
