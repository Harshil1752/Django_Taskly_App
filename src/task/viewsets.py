from rest_framework import viewsets, mixins
from .serializers import TaskListSerializer
from .models import Task, TaskList, Attachment
from .permissions import IsAllowedToEditTaskListElseNone

class TaskListViewset(mixins.CreateModelMixin, mixins.RetrieveModelMixin, 
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAllowedToEditTaskListElseNone, ]
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer