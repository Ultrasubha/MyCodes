from .models import Lead
from rest_framework import viewsets,permissions
from serializers import LeadSerializer

class LeadViewSet(viewsets.ModelViewSets):
    queryset = Lead.objects.all()
    permission_classes = [permissions.AllowAny]
    serializerClass = LeadSerializer