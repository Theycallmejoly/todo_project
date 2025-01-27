from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['due_date', 'created_at' , 'title' , 'description']


# can also with generics get done

'''class DetailItem(generics.RetrieveUpdateAPIView): 
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CreateItem(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class DeleteItem(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer '''

