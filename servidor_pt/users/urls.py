from django.urls import path
from users import views
urlpatterns = [
    path('list/', views.RetrieveUpdateUserView.as_view()),
    path('create/', views.CreateUSerView.as_view()),
    path('token/', views.CreateTokenView.as_view())
]