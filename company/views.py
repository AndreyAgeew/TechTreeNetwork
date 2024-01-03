from rest_framework import viewsets, filters
from .models import Company
from .permissions import IsActiveEmployee
from .serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsActiveEmployee]
    filter_backends = [filters.SearchFilter]
    search_fields = ['country']

    def perform_update(self, serializer):
        serializer.save(debt=self.get_object().debt)  # Запретить обновление debt
