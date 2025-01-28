Here’s a GitHub-ready documentation for your Django REST Framework (DRF) project with clear explanations:

---

# **Django Task Management API**

This is a simple **Task Management API** built with **Django REST Framework (DRF)**. The project provides a CRUD interface for managing tasks with features like filtering and validation.

## **Features**
- **CRUD operations** for tasks.
- **Filtering** tasks by due date, creation date, title, and description.
- Validation to ensure the due date is in the future.
- Built with Django's built-in models and serializers for easy extensibility.

---

## **Installation**

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

---

## **Endpoints**

| Endpoint                  | Method | Description                     |
|---------------------------|--------|---------------------------------|
| `/api/tasks/`             | GET    | List all tasks                 |
| `/api/tasks/`             | POST   | Create a new task              |
| `/api/tasks/<id>/`        | GET    | Retrieve a specific task       |
| `/api/tasks/<id>/`        | PUT    | Update a specific task         |
| `/api/tasks/<id>/`        | DELETE | Delete a specific task         |

---

## **Code Overview**

### **Models**
```python
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```
- **Fields**:
  - `title`: Title of the task.
  - `description`: Description of the task.
  - `due_date`: Deadline for the task.
  - `completed`: Status of the task (default is `False`).
  - `created_at` & `updated_at`: Auto-generated timestamps.

---

### **Serializers**
```python
from rest_framework import serializers
from django.utils import timezone
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate_due_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Due date must be in the future")
        return value
```
- Validates that the `due_date` is in the future before saving.

---

### **Views**
```python
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['due_date', 'created_at', 'title', 'description']
```
- Uses `ModelViewSet` to provide CRUD functionality.
- Implements filtering for fields like `due_date`, `created_at`, `title`, and `description`.

---

### **URLs**
#### **Main URL Configuration**
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
]
```

#### **App-Specific URLs**
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```
- `DefaultRouter` automatically generates RESTful routes for the `TaskViewSet`.

---

## **Advanced Implementation**
If you prefer using **generic views**, here's how you can achieve the same CRUD functionality:
```python
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

class DetailItem(generics.RetrieveUpdateAPIView): 
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CreateItem(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class DeleteItem(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
```

---

## **Filtering and Searching**
This project uses `django-filters` for filtering and provides search functionality for `title` and `description`.

Install `django-filter` if not already installed:
```bash
pip install django-filter
```

Enable it in your `TaskViewSet`:
```python
filter_backends = [DjangoFilterBackend]
filterset_fields = ['due_date', 'created_at', 'title', 'description']
```

---
