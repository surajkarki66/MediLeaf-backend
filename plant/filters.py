import django_filters

from .models import Plant, PlantGenus, PlantSpecies


class PlantFilter(django_filters.FilterSet):
    Annual = 'annual'
    Biennial = 'biennial'
    Perennial = 'perennial'
    Ephemeral = 'ephemeral'
    Deciduous = 'deciduous'
    Evergreen = 'evergreen'

    Duration = (
        (Annual, 'Annual'),
        (Biennial, 'Biennial'),
        (Perennial, 'Perennial'),
        (Ephemeral, 'Ephemeral'),
        (Deciduous, 'Deciduous'),
        (Evergreen, 'Evergreen')
    )
    Herb = 'herb'
    Shrub = 'shrub'
    Tree = 'tree'
    Graminoid = 'graminoid'
    Subshrub = 'subshrub'
    Vine = 'vine'

    Growth = (
        (Herb, 'Herb'),
        (Shrub, 'Shrub'),
        (Tree, 'Tree'),
        (Graminoid, 'Graminoid'),
        (Subshrub, 'Subshrub'),
        (Vine, 'Vine')
    )

    genus = django_filters.ModelMultipleChoiceFilter(
        field_name='genus__title',
        queryset=PlantGenus.objects.all(),
        to_field_name='title',
    )
    species = django_filters.ModelMultipleChoiceFilter(
        field_name='species__title',
        queryset=PlantSpecies.objects.all(),
        to_field_name='title',
    )
    id = django_filters.Filter(field_name="id", lookup_expr="exact")
    created_at = django_filters.DateTimeFilter(
        field_name="created_at", lookup_expr="gte")
    updated_at = django_filters.DateTimeFilter(
        field_name="updated_at", lookup_expr="gte")
    growth_habit = django_filters.ChoiceFilter(
        field_name="growth_habit", lookup_expr="exact", choices=Growth)
    duration = django_filters.ChoiceFilter(
        field_name="duration", lookup_expr="exact", choices=Duration)

    class Meta:
        model = Plant
        fields = ['id', 'created_at', 'updated_at',
                  'growth_habit', 'duration', 'genus', 'species']
