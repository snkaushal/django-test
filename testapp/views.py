from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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