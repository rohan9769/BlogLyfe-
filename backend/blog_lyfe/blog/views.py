from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions,generics,mixins
from rest_framework.views import APIView
from .serializers import BlogPostSerializer
from .models import BlogPost

# Create your views here.
class BlogPostListView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.order_by('-date_created')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)

class BlogPostDetailView(generics.RetrieveDestroyAPIView):
    queryset = BlogPost.objects.order_by('-date_created')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)

class BlogPostFeaturedView(generics.ListAPIView):
    queryset = BlogPost.objects.all().filter(featured=True)
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)

class BlogPostCategoryView(APIView):
    serializer_class = BlogPostSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self,request):
        data = self.request.data
        category = data['category']
        blogpost = BlogPost.objects.order_by('-date_created').filter(category__iexact=category)
        serializer = BlogPostSerializer(blogpost,many=True)
        return Response(serializer.data)
        