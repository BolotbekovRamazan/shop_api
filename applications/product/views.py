from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import ProductImageSerializer, ProductSerializer
from .models import Product
from permissions.permissions import IsOwnerOrIsAdmin

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all() # TODO: optimize
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsOwnerOrIsAdmin]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return super().get_permissions()