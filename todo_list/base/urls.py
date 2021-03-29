from django.urls import path
from .views import TaskList, TaskDetail, TaskUpdate, TaskCreate, TaskDelete


urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create_task/', TaskCreate.as_view(), name='create'),
    path('update_task/<int:pk>/', TaskUpdate.as_view(), name='update'),
    path('delete_task/<int:pk>/', TaskDelete.as_view(), name='delete')
]