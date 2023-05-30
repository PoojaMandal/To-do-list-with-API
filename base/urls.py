from django.urls import include, path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('api/', include('api.urls')),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='tasks'),
    path('task-create/', TaskCreate.as_view(), name='tasks-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='tasks-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='tasks-delete'),
]
