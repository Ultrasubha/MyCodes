from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.models import Post
from .serializers import ItemSerializer


@api_view(['GET'])
def getData(request):
    return Response(ItemSerializer(Post.objects.all(), many=True).data)


@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer)
