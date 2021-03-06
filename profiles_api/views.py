from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions
from rest_framework.authentication import TokenAuthentication

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

class HelloViewSet(viewsets.ViewSet):
    """Test API viewset"""
    serializer_class = serializers.HelloSerializer
    
    def list(self, request):
        '''returns a hello message'''
        a_viewset = [
            'uses actions(list, retrieve, update, partial_update)',
            'automaticaly maps to URLS using Routers',
            'Provides more functionality with less code'
        ]
        return Response({'message' : 'hello', 'a viewset' : a_viewset})
    
    def create(self, request):
        '''creates a hello message'''
        
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """handle getting an object by its ID"""
        return Response({'http_method' : 'GET'})
    def update(self, request, pk=None):
        """handle getting an object by its ID"""
        return Response({'http_method' : 'PUT'})
    
    def partial_update(self, request, pk=None):
        """handle getting an object by its ID"""
        return Response({'http_method' : 'PATCH'})

    def destroy(self, request, pk=None):
        """handle getting an object by its ID"""
        return Response({'http_method' : 'DELETE'})
class UserProfileViewset(viewsets.ModelViewSet):
    """Handle creating and  updating user"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewset(viewsets.ModelViewSet):
    """handles creating, viewing and updating profile feed"""
    authenticatin_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset =  models.ProfileFeedItem.objects.all()
    permission_classes  = (
        permissions.UpdateOwnStatus,
        IsAuthenticatedOrReadOnly
    )
    
    def perform_create(self, serializer):
        """sets the user Profile to the logged in user"""
        serializer.save(user_profile = self.request.user)

