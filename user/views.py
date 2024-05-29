from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerialiser


class RegisterApiView(APIView):
    def post(self, request):
        serialiser = RegisterSerialiser(data=request.POST, many=False)
        if serialiser.is_valid():
            serialiser.save()
            return Response({'message': 'user created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)
        