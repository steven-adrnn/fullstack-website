from django.urls import path, include
from .views import register, user_login
from .views import update_score
from .views import csrf_token_view  # Pastikan ini sesuai dengan nama file views.py Anda



urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('update_score/<int:score>/', update_score, name='update_score'),  # URL untuk update skor
    path('get-csrf-token/', csrf_token_view, name='get_csrf_token'),

]