import django_filters
from django_filters import CharFilter, NumericRangeFilter, RangeFilter

from users.models import *


class UserFilter(django_filters.FilterSet):
    name = CharFilter(field_name="full_name", lookup_expr="icontains")
    gender = CharFilter(field_name="gender")
    age = RangeFilter(field_name="age")

    class Meta:
        model = Profile
        fields = ['name','gender','age']
       
