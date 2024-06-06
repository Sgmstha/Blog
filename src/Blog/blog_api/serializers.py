from rest_framework import serializers
from .models import Blog, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class BlogSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'category_id', 'category_name']
        read_only_fields = ['category_name']

    def get_category_name(self, obj):
        return obj.category.name

    def create(self, validated_data):
        category_id = validated_data.pop('category_id')
        category = Category.objects.get(id=category_id)
        blog = Blog.objects.create(category=category, **validated_data)
        return blog

    def update(self, instance, validated_data):
        category_id = validated_data.pop('category_id')
        category = Category.objects.get(id=category_id)

        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.category = category
        instance.save()
        return instance
