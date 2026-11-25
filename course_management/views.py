from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework import authentication,permissions
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

# Create your views here.
from course_management.models import Course
from course_management.serializers import CourseSerializer

from accounts.permission import IsOwner

class CourseListCreateView(ListAPIView,CreateAPIView):
    
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = CourseSerializer

    def get_queryset(self):

        return Course.objects.filter(trainer=self.request.user)

    def perform_create(self, serializer):

        serializer.save(trainer=self.request.user)



    # def post(self,request):

    #     form_data = request.data

    #     serializer_instance = CourseSerializer(data = form_data)

    #     if serializer_instance.is_valid():

    #         serializer_instance.save(trainer = request.user)

    #         return Response(serializer_instance.data)

    #     else:

    #         return Response(serializer_instance.errors)


class CourseRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    queryset = Course.objects.all()

    serializer_class = CourseSerializer

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]

    # def get(self,request,pk=None):

    #     qs = get_object_or_404(Course,id=pk)

    #     self.check_object_permissions(request,qs)

    #     serializer_instance = CourseSerializer(qs)

    #     return Response(serializer_instance.data)

    # def patch(self,request,pk=None):

    #     form_data = request.data

    #     instance = get_object_or_404(Course,id=pk)

    #     self.check_object_permissions(request,instance)

    #     serializer_instance = CourseSerializer(data=form_data,instance = instance,partial=True)

    #     if serializer_instance.is_valid():

    #         serializer_instance.save()

    #         return Response(serializer_instance.data)

    #     else:

    #         return Response(serializer_instance.errors)

    # def delete(self,request,pk=None):

    #     instance = get_object_or_404(Course,id=pk)

    #     self.check_object_permissions(request,instance)

    #     instance.delete()

    #     return Response({"message":"deleted..."}) 