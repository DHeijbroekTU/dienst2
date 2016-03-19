import datetime

import django_filters
from django.db import models
from django.db.models import Prefetch
from django.utils import formats
from django.utils.encoding import force_str

from post.models import Item


class ItemFilterSet(django_filters.FilterSet):
    filter_overrides = {
        models.CharField: {
            'filter_class': django_filters.CharFilter,
            'extra': lambda f: {
                'lookup_type': 'icontains',
            }
        }
    }

    class Meta:
        model = Item
        fields = ('description', 'sender', 'recipient', 'category')


class AVFilterSet(django_filters.FilterSet):
    date = django_filters.MethodFilter(action='filter_date')

    def strptime(self, value, format):
        return datetime.datetime.strptime(force_str(value), format).date()

    def filter_date(self, queryset, value):
        date = None
        for format in formats.get_format('DATE_INPUT_FORMATS'):
            try:
                date = self.strptime(value, format)
            except (ValueError, TypeError):
                continue

        if date is None:
            return queryset
        return queryset.prefetch_related(Prefetch('items', queryset=Item.objects.filter(date__gte=date)))
