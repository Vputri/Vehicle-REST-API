from rest_framework.response import Response
from rest_framework import status
from .serializers import Price_ListSerializer, UserSerializer
from .models import Price_List
from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from .pagination import CustomPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django.shortcuts import render

def home(request):
	return render(request, 'index.html')

class Price_ListView(GenericAPIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	pagination_class = CustomPagination
	filter_backend = (SearchFilter, OrderingFilter)
	search_filter = ('price', 'id_year', 'id_model', 'id_model.id_type', 'id_model.id_type.id_brand')
	serializer_class = Price_ListSerializer
	queryset = Price_List.objects.all()


	def post(self, request, *args, **kwargs):
		file_serializer = Price_ListSerializer(data=request.data)
		if file_serializer.is_valid():
			file_serializer.save()
			return Response(file_serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request, id=None):
		if id:
			file = get_object_or_404(Price_List, id=id)
			serializer = Price_ListSerializer(file)
			return Response(serializer.data, status=status.HTTP_200_OK)

		queryset = self.filter_queryset(self.get_queryset())
		page = self.paginate_queryset(queryset)
		if page is not None:
			serializer = self.get_serializer(page, many=True)
			result = self.get_paginated_response(serializer.data)
			data = result.data # pagination data
		else:
			serializer = self.get_serializer(queryset, many=True)
			data = serializer.data
		return Response(data)

	def delete(self, request, id=None):
		item = get_object_or_404(Price_List, id=id)
		item.delete()
		return Response({"status": "Berhasil", "data": "Item telah dihapus"})

	def patch(self, request, id=None):
		item = get_object_or_404(Price_List, id=id)
		serializer = Price_ListSerializer(item, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)