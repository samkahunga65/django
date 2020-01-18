from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    def get(self, request, format=None):
        """returns a list of APIViews features"""
        an_apiview = [
            'uses http methods as functions',
            'is similar to a django view',
            'gives most control over application logic',
        ]

        return Response({'message' : "oloo", "an apiview" : an_apiview})