from rest_framework import routers
from .viewsets import TaskListViewset, TaskViewSet, AttachmentViewSet

app_name = 'task'

router = routers.DefaultRouter()
router.register('tasklists', TaskListViewset)
router.register('tasks', TaskViewSet)
router.register('attachments', AttachmentViewSet)