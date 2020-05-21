from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TopicSerializer
from .models import Topic

class TopicView(APIView):
    def get(self, request):
        topic = Topic.objects.all()
        # for t in topic[0].contents.all():
        #     print(t)
        serializer = TopicSerializer(topic, many=True)

        print(serializer.data)

        return Response(data=serializer.data, status=status.HTTP_200_OK)