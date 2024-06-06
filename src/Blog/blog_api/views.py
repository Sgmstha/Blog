from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Blog, Category
from .serializers import BlogSerializer, CategorySerializer

class BlogListCreate(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PairFinding(APIView):
    def post(self, request):
        nums = request.data.get('nums', [])
        target = request.data.get('target', 0)
        pairs = self.find_pairs(nums, target)
        if pairs:
            pair_strings = [f"Pair found ({pair[0]}, {pair[1]})" for pair in pairs]
            response_message = " or ".join(pair_strings)
            return Response({"message": response_message})
        else:
            return Response({"message": "Pair not found"})

    @staticmethod
    def find_pairs(nums, target):
        seen = set()
        pairs = []
        for num in nums:
            complement = target - num
            if complement in seen:
                pairs.append((num, complement))
            seen.add(num)
        return pairs
