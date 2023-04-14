from django_filters import rest_framework as filters

from web.models import Note, Tag


class NotesFilter(filters.FilterSet):
    tag_id = filters.ModelChoiceFilter(queryset=Tag.objects.all(), method="filter_tag_id")

    def filter_tag_id(self, queryset, name, value):
        return queryset.filter(tags__in=[value])

    class Meta:
        model = Note
        fields = ("title",)
