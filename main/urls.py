from django.urls import path
from main.views import ToDoView, ToDoCreate, ToDoDetail, ToDoUpdate , ToDoDelete

urlpatterns = [
    path('', ToDoView.as_view(), name='list'),
    path('create/', ToDoCreate.as_view(), name='create'),
    path('<slug:slug>/', ToDoDetail.as_view(), name='detail'),
    path('<slug:slug>/edit/', ToDoUpdate.as_view(), name='update'),
    path('<slug:slug>/delete/', ToDoDelete.as_view(), name='delete')
]
