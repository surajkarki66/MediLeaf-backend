from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, viewsets, filters
from drf_spectacular.utils import extend_schema
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

from .filters import PlantFilter
from .models import PlantSpecies, PlantGenus, PlantFamily, PlantImage, Plant
from account.permissions import IsVerifiedUser
from .serializers import (PlantSpeciesSerializer, PlantGenusSerializer,
                          PlantGenusListSerializer, PlantFamilyListSerializer,
                          PlantFamilySerializer, PlantImageSerializer, PlantListSerializer,
                          PlantDetailsSerializer)


@method_decorator(csrf_protect, name='dispatch')
@extend_schema(summary='Plant Species Viewset', tags=['Plant Species'])
class PlantSpeciesViewset(viewsets.ModelViewSet):
    queryset = PlantSpecies.objects.all()
    serializer_class = PlantSpeciesSerializer
    permission_classes = (permissions.IsAdminUser, )
    lookup_field = 'slug'
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = {
        "id": ["exact"],
        "created_at": ["gte", "lte", "exact", "gt", "lt"],
        "updated_at": ["gte", "lte", "exact", "gt", "lt"],
        "genus__title": ["exact"]
    }
    search_fields = ["id", "title", "genus__title"]
    ordering_fields = ["id", "title", "created_at", "updated_at",]

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_permissions(self):
        if self.action in ["create",]:
            return [permissions.IsAuthenticated(), IsVerifiedUser()]

        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny(),]

        return super().get_permissions()


@method_decorator(csrf_protect, name='dispatch')
@extend_schema(summary='Plant Genus Viewset', tags=['Plant Genus'])
class PlantGenusViewset(viewsets.ModelViewSet):
    queryset = PlantGenus.objects.all()
    serializer_class = PlantGenusSerializer
    permission_classes = (permissions.IsAdminUser, )
    lookup_field = 'slug'
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = {
        "id": ["exact"],
        "created_at": ["gte", "lte", "exact", "gt", "lt"],
        "updated_at": ["gte", "lte", "exact", "gt", "lt"],
        "family__title": ["exact"]
    }
    search_fields = ["id", "title", "family__title"]
    ordering_fields = ["id", "title", "created_at", "updated_at",]

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_permissions(self):
        if self.action in ["create",]:
            return [permissions.IsAuthenticated(), IsVerifiedUser()]

        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny(),]

        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == 'list':
            return PlantGenusListSerializer

        return super().get_serializer_class()


@method_decorator(csrf_protect, name='dispatch')
@extend_schema(summary='Plant Family Viewset', tags=['Plant Family'])
class PlantFamilyViewset(viewsets.ModelViewSet):
    queryset = PlantFamily.objects.all()
    serializer_class = PlantFamilySerializer
    permission_classes = (permissions.IsAdminUser, )
    lookup_field = 'slug'
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = {
        "id": ["exact"],
        "created_at": ["gte", "lte", "exact", "gt", "lt"],
        "updated_at": ["gte", "lte", "exact", "gt", "lt"],
    }
    search_fields = ["id", "title",]
    ordering_fields = ["id", "title", "created_at", "updated_at",]

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_permissions(self):
        if self.action in ["create",]:
            return [permissions.IsAuthenticated(), IsVerifiedUser()]

        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny(),]

        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == 'list':
            return PlantFamilyListSerializer

        return super().get_serializer_class()


@method_decorator(csrf_protect, name='dispatch')
@extend_schema(summary='Plant Image Viewset', tags=['Plant Image'])
class PlantImageViewset(viewsets.ModelViewSet):
    queryset = PlantImage.objects.all()
    serializer_class = PlantImageSerializer
    permission_classes = (permissions.IsAdminUser, )
    lookup_field = 'id'
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = {
        "id": ["exact"],
        "created_at": ["gte", "lte", "exact", "gt", "lt"],
        "updated_at": ["gte", "lte", "exact", "gt", "lt"],
        "part": ["exact"],
        "default": ["exact"]
    }
    ordering_fields = ["id", "created_at", "updated_at",]

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny(),]

        return super().get_permissions()


@extend_schema(summary='Plant List View', tags=['Plant List'])
class PlantViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantListSerializer
    permission_classes = (permissions.AllowAny, )
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter,]

    search_fields = ["id", "family__title",
                     "common_names", "genus__title", "species__title"]
    ordering_fields = ["id", "common_names", "family__title",
                       "genus__title", "species__title", "created_at", "updated_at",]

    filterset_class = PlantFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PlantDetailsSerializer

        return super().get_serializer_class()


class PlantDetailsAPIView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request):
        genus = request.GET.get('genus')
        species = request.GET.get('species')
        plant = Plant.objects.filter(
            genus__title=genus, species__title=species).first()
        if plant:
            serializer = PlantDetailsSerializer(plant)
            return Response(serializer.data)
        else:
            return Response({"message": "Plant not found"}, status=status.HTTP_404_NOT_FOUND)
