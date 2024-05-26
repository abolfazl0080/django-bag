from rest_framework import serializers
from . import models


class ImageOfBagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImageOfBagModel
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CategoryModel
        fields = '__all__'


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LabelModel
        fields = '__all__'


class BagSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = models.BagModel
        fields = '__all__'

    def get_images(self, obj):
        images = obj.images.all()
        serializer = ImageOfBagSerializer(images, many=True)
        return serializer.data
