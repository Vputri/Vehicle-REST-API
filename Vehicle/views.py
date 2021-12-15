from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
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

class Vechicle_BrandView(GenericAPIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	pagination_class = CustomPagination
	filter_backend = (SearchFilter, OrderingFilter)
	search_filter = ('name')
	serializer_class = Vechicle_BrandSerializer
	queryset = Vechicle_Brand.objects.all()

	def post(self, request, *args, **kwargs):
		file_serializer = Vechicle_BrandSerializer(data=request.data)
		if file_serializer.is_valid():
			file_serializer.save()
			return Response(file_serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request, id=None):
		if id:
			file = get_object_or_404(Vechicle_Brand, id=id)
			serializer = Vechicle_BrandSerializer(file)
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
		item = get_object_or_404(Vechicle_Brand, id=id)
		item.delete()
		return Response({"status": "Berhasil", "data": "Item telah dihapus"})

	def patch(self, request, id=None):
		item = get_object_or_404(Vechicle_Brand, id=id)
		serializer = Vechicle_BrandSerializer(item, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Vechicle_TypeView(GenericAPIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	pagination_class = CustomPagination
	filter_backend = (SearchFilter, OrderingFilter)
	search_filter = ('name')
	serializer_class = Vechicle_TypeSerializer
	queryset = Vechicle_Type.objects.all()

	def post(self, request, *args, **kwargs):
		file_serializer = Vechicle_TypeSerializer(data=request.data)
		if file_serializer.is_valid():
			file_serializer.save()
			return Response(file_serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request, id=None):
		if id:
			file = get_object_or_404(Vechicle_Type, id=id)
			serializer = Vechicle_TypeSerializer(file)
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
		item = get_object_or_404(Vechicle_Type, id=id)
		item.delete()
		return Response({"status": "Berhasil", "data": "Item telah dihapus"})

	def patch(self, request, id=None):
		item = get_object_or_404(Vechicle_Type, id=id)
		serializer = Vechicle_TypeSerializer(item, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Vechicle_ModelView(GenericAPIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	pagination_class = CustomPagination
	filter_backend = (SearchFilter, OrderingFilter)
	search_filter = ('name')
	serializer_class = Vechicle_ModelSerializer
	queryset = Vechicle_Type.objects.all()

	def post(self, request, *args, **kwargs):
		file_serializer = Vechicle_ModelSerializer(data=request.data)
		if file_serializer.is_valid():
			file_serializer.save()
			return Response(file_serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request, id=None):
		if id:
			file = get_object_or_404(Vechicle_Model, id=id)
			serializer = Vechicle_ModelSerializer(file)
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
		item = get_object_or_404(Vechicle_Model, id=id)
		item.delete()
		return Response({"status": "Berhasil", "data": "Item telah dihapus"})

	def patch(self, request, id=None):
		item = get_object_or_404(Vechicle_Model, id=id)
		serializer = Vechicle_TypeSerializer(item, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Vechicle_YearView(GenericAPIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	pagination_class = CustomPagination
	filter_backend = (SearchFilter, OrderingFilter)
	search_filter = ('year')
	serializer_class = Vechicle_YearSerializer
	queryset = Vechicle_Type.objects.all()

	def post(self, request, *args, **kwargs):
		file_serializer = Vechicle_YearSerializer(data=request.data)
		if file_serializer.is_valid():
			file_serializer.save()
			return Response(file_serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request, id=None):
		if id:
			file = get_object_or_404(Vechicle_Year, id=id)
			serializer = Vechicle_YearSerializer(file)
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
		item = get_object_or_404(Vechicle_Year, id=id)
		item.delete()
		return Response({"status": "Berhasil", "data": "Item telah dihapus"})

	def patch(self, request, id=None):
		item = get_object_or_404(Vechicle_Year, id=id)
		serializer = Vechicle_TypeSerializer(item, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
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