import django_filters
from .models import Takimlar

class TakimlarFilter(django_filters.FilterSet):
    baslangic_min = django_filters.DateFilter(field_name='baslangic', lookup_expr='gte', label='Başlangıç Tarihi (Min)')
    baslangic_max = django_filters.DateFilter(field_name='baslangic', lookup_expr='lte', label='Başlangıç Tarihi (Max)')

    class Meta:
        model = Takimlar
        fields = []