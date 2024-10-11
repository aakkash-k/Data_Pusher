from django.urls import path
from .views import AccountView,  AccountUserById, AccountUserByEmailId,incomingData

urlpatterns = [
    path("user", AccountView.as_view()),
    path("user/<int:id>", AccountUserById.as_view()),
    path('user/<str:email_id>', AccountUserByEmailId.as_view()),
   
    path('incoming_data', incomingData.as_view())
    
]