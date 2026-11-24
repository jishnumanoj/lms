from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework import authentication,permissions
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView

# Create your views here.
from course_management.models import Course
from course_management.serializers import CourseSerializer

from accounts.permission import IsOwner

# class CourseListCreateView(ListAPIView):
#     serializer_class = CourseSerializer
#     authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return Course.objects.filter(trainer=self.request.user)

class CourseListCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

        qs = Course.objects.filter(trainer=request.user)

        serializer_instance = CourseSerializer(qs,many=True)

        return Response(serializer_instance.data) 

    def post(self,request):

        form_data = request.data

        serializer_instance = CourseSerializer(data = form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(trainer = request.user)

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)


class CourseRetrieveUpdateDeleteView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]

    def get(self,request,pk=None):

        qs = get_object_or_404(Course,id=pk)

        self.check_object_permissions(request,qs)

        serializer_instance = CourseSerializer(qs)

        return Response(serializer_instance.data)

    def put(self,request,pk=None):

        form_data = request.data

        instance = get_object_or_404(Course,id=pk)

        self.check_object_permissions(request,instance)

        serializer_instance = CourseSerializer(data=form_data,instance = instance)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)

    def delete(self,request,pk=None):

        instance = get_object_or_404(Course,id=pk)

        self.check_object_permissions(request,instance)

        instance.delete()

        return Response({"message":"deleted..."}) 