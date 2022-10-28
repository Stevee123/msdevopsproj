from rest_framework import serializers
from cards.models import Course

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course 
        fields=('CourseId','CourseName','Coursetitle','Frontcard','Backcard')
        