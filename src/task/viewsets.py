from rest_framework import viewsets, mixins, response, status
from rest_framework import status as s
from django.utils import timezone
from rest_framework.decorators import action
from .serializers import TaskListSerializer, TaskSerializer, AttachmentSerializer
from .models import Task, TaskList, Attachment, COMPLETE, NOT_COMPLETE
from .permissions import IsAllowedToEditTaskListElseNone, IsAllowedToEditTaskElseNone, IsAllowedEditAttachmentElseNone

class TaskListViewset(mixins.CreateModelMixin, mixins.RetrieveModelMixin, 
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin, 
                      mixins.ListModelMixin, viewsets.GenericViewSet):
        permission_classes = [IsAllowedToEditTaskListElseNone, ]
        queryset = TaskList.objects.all()
        serializer_class = TaskListSerializer

class TaskViewSet(viewsets.ModelViewSet):
        permission_classes = [IsAllowedToEditTaskElseNone, ]
        queryset = Task.objects.all()
        serializer_class = TaskSerializer

        def  get_queryset(self):
                queryset = super(TaskViewSet, self).get_queryset()
                user_profile = self.request.user.profile
                updated_queryset = queryset.filter(created_by=user_profile)
                return updated_queryset
        
        @action(detail=True, methods=['patch'])
        def update_tast_status(self, request, pk=None):
                try:
                    task = self.get_object()
                    profile = request.user.profile
                    status= request.data['status']
                    if (status == NOT_COMPLETE):
                           if (task.status == COMPLETE):
                                  task.status = NOT_COMPLETE
                                  task.completed_on = None
                                  task.completed_by = None
                           else:
                                  raise Exception("Task is already marked as Not Complete.")
                    elif (status == COMPLETE):
                           if (task.status == NOT_COMPLETE):
                                  task.status = COMPLETE
                                  task.completed_on = timezone.now()
                                  task.completed_by = profile
                           else:
                                  raise Exception("Task is already marked as Complete.")
                    else:
                           raise Exception(" Incorrect status provided.")
                    task.save()
                    serializer = TaskSerializer(instance=task, context = {'request': request})
                    return response.Response(serializer.data, status= s.HTTP_200_OK)
                except Exception as e:
                       return response.Response({'detail': str(e)}, status=s.HTTP_400_BAD_REQUEST)
                           
                    
class AttachmentViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, 
                        mixins.UpdateModelMixin, mixins.DestroyModelMixin, 
                        viewsets.GenericViewSet):
        permission_classes = [IsAllowedEditAttachmentElseNone, ]
        queryset = Attachment.objects.all()
        serializer_class = AttachmentSerializer
        