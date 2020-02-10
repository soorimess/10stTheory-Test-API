from django.urls import path, re_path
from .views import HouseCreate, HouseAreaListView

urlpatterns = [
    path('save', HouseCreate.as_view()),
    # re_path(r'^query/min_area=(?P<min>\d+)max_area=(?P<max>\d+)', HouseAreaListView.as_view())
    path('query', HouseAreaListView.as_view())
]

