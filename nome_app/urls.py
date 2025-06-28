from django.urls import path, include
from . import views

# urlpatterns = [
#     path('', views.main, name='home')
# ]

urlpatterns = [
    path('', views.post_form, name='home'),  # <-- o nome da rota é 'home'
    path('<int:id>/', views.post_form, name='post-update'),
]