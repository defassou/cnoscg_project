from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from collabo.views import register, home, logoutUser, president, superviseur, focal, user_list, \
    user_detail, user_steps


urlpatterns = [

    path('', home, name='home'),
    path('register', register, name='register'),
    path('logout', logoutUser, name='logout'),

    path('president', president, name='president'),
    path('superviseur', superviseur, name='superviseur'),
    path('focal', focal, name='focal'),

    path('user_list/', user_list, name='user_list'),
    path('user_detail/<int:pk>/', user_detail, name='user_detail'),
    path('user_steps/', user_steps, name='user_steps'),

    #path('redirection/', redirect_after_login, name='redirect_after_login'),

    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, )
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, )