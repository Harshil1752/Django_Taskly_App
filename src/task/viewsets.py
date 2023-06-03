from rest_framework import viewsets, mixins
from .serializers import TaskListSerializer, TaskSerializer, AttachmentSerializer
from .models import Task, TaskList, Attachment
from .permissions import IsAllowedToEditTaskListElseNone, IsAllowedToEditTaskElseNone, IsAllowedEditAttachmentElseNone

class TaskListViewset(mixins.CreateModelMixin, mixins.RetrieveModelMixin, 
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
        permission_classes = [IsAllowedToEditTaskListElseNone, ]
        queryset = TaskList.objects.all()
        serializer_class = TaskListSerializer

class TaskViewSet(viewsets.ModelViewSet):
        permission_classes = [IsAllowedToEditTaskElseNone, ]
        queryset = Task.objects.all()
        serializer_class = TaskSerializer

class AttachmentViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                        mixins.DestroyModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
        permission_classes = [IsAllowedEditAttachmentElseNone, ]
        queryset = Attachment.objects.all()
        serializer_class = AttachmentSerializer
        