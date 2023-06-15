from .models import Category
from rest_framework.permissions import IsAdminUser, AllowAny, SAFE_METHODS

from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerilaizer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerilaizer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()