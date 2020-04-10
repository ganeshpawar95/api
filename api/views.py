from django.shortcuts import render,redirect
from api.models import Removebg
from api.serializers import RemovebgSerializer,RemovebgUpdateSerializer,RemovebgPostSerializer
from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from django.views import View
from django.http import HttpResponse
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
def removebg(request):
    if request.method == 'POST' and request.FILES['images']:
        images = request.FILES['images']
        post=Removebg(images=images)
        post.save()
        return redirect('/')
    post=Removebg.objects.all()
    return render(request,'removebg/index.html',{'post':post})

class RemovebgView(generics.ListAPIView):

    queryset = Removebg.objects.all()
    serializer_class = RemovebgSerializer


class RemovebgEdit(generics.RetrieveUpdateAPIView):

    queryset = Removebg.objects.all()
    serializer_class =RemovebgUpdateSerializer

class RemovebgDetails(generics.RetrieveAPIView):

    queryset = Removebg.objects.all()
    serializer_class = RemovebgSerializer

class RemovebgPost(generics.ListCreateAPIView):
    serializer_class = RemovebgPostSerializer
  

class RemovebgpostView(APIView):


    def get(self, request, format=None):
        """
        curl -X GET \
          -H 'Authorization: Token {header_token_key}' \
          http://localhost:8000/api/v1/candidates
        """
        candidates = Removebg.objects.all()
        serializer = RemovebgPostSerializer(candidates, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """
        curl -X POST -S \
          -H 'Accept: application/json' \
          -H 'Content-Type: multipart/form-data' \
          -H 'Authorization: Token {header_token_key}' \
          -F "selection={selection_code/url_code}" \
          -F "name={candidate name}" \
          -F "about={about}" \
          -F "photo=@/path/to/your_photo.jpg;type=image/jpg" \
          http://localhost:8000/api/v1/candidates
        """
        serializer = RemovebgPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                selection=Selection.objects.get(code=request.data.get('selection')),
                images=request.data.get('images')
            )
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# post = Post.objects.create(title='First post', text='This is a first post')
# print(PostSerializer(post).data)
# class RemovebgAdd(View):

#     def post(self, request):

#         print(request.FILES)
#         Removebg.objects.create(
#             images=request.FILES.get('images'),
       
#         )
#         return HttpResponse('success')



