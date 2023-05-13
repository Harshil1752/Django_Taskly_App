from rest_framework import serializers
from .models import House

class HouseSerializer(serializers.ModelSerializer):
    members_count = serializers.IntegerField(read_only = True)

    class Meta:
        model = House
        fields = ['url', 'id', 'image', 'name', 'created_on', 'manager', 'description', 
                  'members_count', 'points',
                  'completed_task_count', 'not_completed_task_count']
        reads_only_fields = ['points', 'completed_task_count', 'not_completed_task_count']