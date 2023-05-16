from django.db import models

NOT_COMPLETE = 'NC'
COMPLETE =  'C'
TASK_STATUS_CHOICES = [
    (NOT_COMPLETE, 'Not Completed'),
    (COMPLETE, 'Complete')
]

# Create your models here.
class Task(models.Model):
    created_on = models.DateTimeField(auto_now_add = True)
    completed_on = models.DateTimeField(null = True, blank = True)
    created_by = models.ForeignKey('users.Profile', null=True, blank=True, on_delete=models.SET_NULL, related_name='created_task')
    completed_by = models.ForeignKey('users.Profile', null=True, blank=True, on_delete=models.SET_NULL, related_name='completed_task')
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=2,
        choices=TASK_STATUS_CHOICES,
        default=NOT_COMPLETE,
        
    )

    def __str__(self) -> str:
        return f'{self.id} | {self.name}'