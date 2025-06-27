import django_filters
from .models import Employee


class EmployeeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='emp_name', lookup_expr='iexact')
    designations = django_filters.CharFilter(field_name='designations', lookup_expr='iexact')
    # id = django_filters.RangeFilter(field_name='id')
    id_min = django_filters.CharFilter(method = 'filter_by_id_range',label='Minimum ID')
    id_max = django_filters.CharFilter(method = 'filter_by_id_range',label='Maximum ID')

    class Meta:
        model = Employee
        fields = ['id_min','id_max','name','designations']

    def filter_by_id_range(self, queryset, name, value):
        if name == 'id_min':
            return queryset.filter(emp_id__gte=value)
        elif name == 'id_max':
            return queryset.filter(emp_id__lte=value)
        return queryset