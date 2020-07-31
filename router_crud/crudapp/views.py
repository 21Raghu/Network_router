from django.shortcuts import render
from .models import RouterDetails
from .serializers import RouterDetailsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status
import json


class GetRouterList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'
  
    def get(self, request):
        queryset = RouterDetails.objects.filter(status=True)
        return Response({'router_data': queryset})

    def delete(self, request, *args, **kwargs):
        data = RouterDetails.objects.get(id=kwargs['router_id'])
        data.status=False
        data.save()
        return Response({'message': 'Data deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

class RouterData(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'update.html'
    # serializer_class = RouterDetailsSerializer

    def get(self, request, *args, **kwargs):
        queryset = RouterDetails.objects.get(id=kwargs['router_id'])
        return Response({'data' : queryset})            

    def put(self, request, *args, **kwargs):
        snippet = RouterDetails.objects.get(id=kwargs['router_id'])
        data = json.loads(request.body)
        serializer = RouterDetailsSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Record updated successfully'}, status=status.HTTP_200_OK)
        return Response({'message' : 'Record cannot be updated'})

class AddData(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'add.html'

    def get(self, request):
        return Response({'message' : 'Add new data'})

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        serializer = RouterDetailsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Record inserted successfully'}, status=status.HTTP_200_OK)
        return Response({'message' : 'Record cannot be added'})

