from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.HomePage, name='homepage'),
    path('register/', views.Register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('contact/', views.ContactPage, name='contact'),
    path('course_details/<id>/',views.DetailsPage, name='course_details'),
    path('about/', views.AboutPage, name='about'),
    path('blog/', views.blogPage, name='blog'),
    path('blog_detail/', views.BlogDetail, name='blog_detail'),
]   

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
