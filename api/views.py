from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from base.models import Task
from .serializers import TaskSerializer, CustomTokenObtainPairSerializer
from rest_framework.response import Response
import logging

logger = logging.getLogger(__name__)

class TaskList(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskListAPIView(ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        # print("here...1")
        # request = self.request
        user = self.request.user
        queryset = Task.objects.filter(user=user)
        logger.info(f"Authenticated user: {user.username}")
        logger.info(f"Retrieved tasks count: {queryset.count()}")
        # print(user,queryset)
        print(user)
        return queryset      #{'tasks':[]}
    
    
    
    def list(self, request, *args, **kwargs):
        # print("here now....")
        queryset = self.get_queryset()
        print(queryset)
        serializer = self.get_serializer(queryset, many=True)
        user_has_tasks = bool(queryset)  # Check if the queryset is not empty
        data = {
            # 'user_has_tasks': user_has_tasks,
            'tasks': serializer.data,
        }
        print(data)
        return Response(data)

    def create(self, request, *args, **kwargs):
        # print("here now2 ....")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class TaskDetailAPIView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskCreateAPIView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

