'''Doc String'''
from rest_framework import serializers
from .models import Lead


class LeadSerializer(serializers.ModelSerializer):
    '''Doc String'''
    class Meta:
        '''Doc String'''
        model = Lead
        fields = "__all__"
