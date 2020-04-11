from rest_framework.view import APIView
from rest_framework.response import Response


class HelloApiView(APIView):

    def get(self, request, format=None):
        an_apiview = [
            'Itme 1',
            'Itme 2',
            'Itme 3',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
