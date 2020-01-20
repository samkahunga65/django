from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """returns a list of APIViews features"""
        an_apiview = [
            'uses http methods as functions',
            'is similar to a django view',
            'gives most control over application logic',
        ]

        return Response({'message' : "oloo", "an apiview" : an_apiview})

    def post(self, request):
        '''create a hello message with our name'''
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message' : message})
        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """handle updating an object"""
        return Response({'message' : 'PUT'})

    def patch(self, request, pk=None):
        """handle partial updating an object"""
        return Response({'message' : 'patch'})
    
    def delete(self, request, pk=None):
        """handle delete an object"""
        return Response({'message' : 'delete'})