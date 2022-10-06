from rest_framework import serializers
from assignment.models import *

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
