from django.urls import path
from .views import TaskList, TaskListAPIView, TaskDetailAPIView, TaskDetail, CustomTokenObtainPairView

urlpatterns = [
    path('tasks/', TaskList.as_view(), name='task_list'),
    path('tasks/user/', TaskListAPIView.as_view(), name='task_list_api'),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task_detail_api'),
    path('tasks/<int:pk>/update/', TaskDetail.as_view(), name='task_update'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
