from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from . import serilaizers

class TestApiView(APIView):
  serializer_class = serilaizers.TestSerializer
  def get(self, request, format=None):
    test_view = ['testView']
    return Response({'message': 'Hello! this is a test', 'test_view': test_view})

  def post(self, request):
    serializer = self.serializer_class(data = request.data)

    if serializer.is_valid():
      name = serializer.validated_data.get('name')
      message = f"Hello {name}"
      return Response({'message': message})
    else:
      return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

  def put(self, request, pk=None):
      return Response({'method': 'PUT'})

  def patch(self, request, pk=None):
      return Response({'method': 'PATCH'})
  
  def delete(self, request, pk=None):
      return Response({'method': 'DELETE'})

class TestViewSet(viewsets.ViewSet):
  serializer_class = serilaizers.TestSerializer

  def list(self, request):
    a_viewset = [
      'some string',
      'another string'
    ]
    return Response({'message': 'hello', 'a_viewset': a_viewset})
  def create(self, request):
    serializer = self.serializer_class(data = request.data)

    if serializer.is_valid():
      name = serializer.validated_data.get('name')
      message = f"Hello {name}"
      return Response({'message': message})
    else:
      return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

  def retrieve(self, request, pk=None):
    return Response({'http_method':'GET'})

  def update(self, request, pk=None):
    return Response({'http_method':'PUT'})

  def partial_update(self, request, pk=None):
    return Response({'http_method':'PATCH'})

  def destroy(self, request, pk=None):
    return Response({'http_method':'DELETE'})