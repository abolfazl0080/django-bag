from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response


from . import models
from . import serializers


class BagListCreateApi(generics.ListCreateAPIView):
    queryset = models.BagModel.objects.published()
    serializer_class = serializers.BagSerializer


class BagGetUpdateDeleteApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.BagModel.objects.published()
    serializer_class = serializers.BagSerializer


class ImageOfBagCreateApi(generics.CreateAPIView):
    queryset = models.ImageOfBagModel.objects.all()
    serializer_class = serializers.ImageOfBagSerializer


class CategoryListCreateApi(generics.ListCreateAPIView):
    queryset = models.CategoryModel.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryGetUpdateDeleteApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CategoryModel.objects.all()
    serializer_class = serializers.CategorySerializer

    def get(self, request, pk):
        category = get_object_or_404(models.CategoryModel, pk=pk)
        bags = category.bags.all()
        serializer = serializers.BagSerializer(bags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class LabelListCreateApi(generics.ListCreateAPIView):
    queryset = models.LabelModel.objects.all()
    serializer_class = serializers.LabelSerializer


class LabelGetUpdateDeleteApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.LabelModel.objects.all()
    serializer_class = serializers.LabelSerializer

    def get(self, request, pk):
        label = get_object_or_404(models.LabelModel, pk=pk)
        bags = label.bags.all()
        serializer = serializers.BagSerializer(bags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
