from rest_framework.views import APIView
from rest_framework.response import Response

class TestApiView(APIView):

  def get(self, request, format=None):
    test_view = ['testView']
    return Response({'message': 'Hello! this is a test', 'test_view': test_view})
