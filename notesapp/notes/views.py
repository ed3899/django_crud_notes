from django.shortcuts import render, get_object_or_404

from rest_framework.viewsets import ModelViewSet
from .models import Note
from .serializers import NoteSerializer


class NoteViewSet(ModelViewSet):
    serializer_class = NoteSerializer

    def get_object(self):
        return get_object_or_404(Note, id=self.request.query_params.get("id"))

    def get_queryset(self):
        return Note.objects.filter(is_active=True).order_by("-last_updated_on")

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
