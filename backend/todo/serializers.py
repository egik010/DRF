from rest_framework.serializers import ModelSerializer, StringRelatedField

from todo.models import Todo, Project
# from list_of_users.serializers import UserModelSerializer


class ProjectModelSerializer(ModelSerializer):
    users = StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class TodoModelSerializer(ModelSerializer):
    project = StringRelatedField()
    author = StringRelatedField()

    class Meta:
        model = Todo
        fields = '__all__'