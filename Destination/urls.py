from django.urls import path
from .views import DestinationViews,DestinationViewsById,DestinationAccessByAccId, getAllDestination

urlpatterns = [
    path("api", DestinationViews.as_view()),
    path("api/<int:id>",  DestinationViewsById.as_view()),
    path("api/<str:account_id>",DestinationAccessByAccId.as_view()),
    path("<str:account_id>", getAllDestination.as_view())
]