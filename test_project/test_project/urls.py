from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from base.decorators import staff_required
from API.auth import CustomAuthToken


admin.site.login = staff_required(admin.site.login)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('gettoken/', CustomAuthToken.as_view()),
    path('', include('base.urls')),
    path('', include('API.urls')),
    path('register/', user_views.register , name='register'),
    path('users/', user_views.UserSettings.as_view() , name='user-settings'),
    path('details/<int:pk>/', user_views.UserDetails.as_view() , name='user-details'),
    path('details/<int:pk>/delete/', user_views.UserDeleteView.as_view() , name='user-delete'),

    path('profile/', user_views.profile , name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)