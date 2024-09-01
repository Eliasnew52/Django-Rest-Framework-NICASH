from rest_framework import viewsets, filters
from .serializer import ClientSerializer
from .models import Client

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']  

    def get_queryset(self):
        # Obtener el queryset base
        queryset = super().get_queryset()
        # Obtener el parámetro de búsqueda desde los query params
        search_query = self.request.query_params.get('search', None)
        # Si hay un parámetro de búsqueda, filtrar el queryset
        if search_query:
            queryset = queryset.filter(username__icontains=search_query)
        # Retornar el queryset, ya sea filtrado o completo
        return queryset
