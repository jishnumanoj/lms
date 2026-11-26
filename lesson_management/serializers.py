from lesson_management.models import Lesson

from rest_framework import serializers

class LessonSerializer(serializers.ModelSerializer):

    class Meta:

        model = Lesson

        fields = "__all__"

        read_only_fields = ["id","module","created_at","updated_at","created_by","slug","order"]