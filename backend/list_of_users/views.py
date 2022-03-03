from rest_framework.viewsets import ModelViewSet
from .serializers import UsersModelSerializer
from .models import Users


class UsersViewSet(ModelViewSet):
    serializer_class = UsersModelSerializer
    queryset = Users.objects.all()
