from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Menu, Dish
from .serializers import RestaurantSerializer, MenuSerializer, DishSerializer, MenuInfoSerializer


class RestaurantCreateView(APIView):
    permission_classes = [IsAuthenticated]
    """"
    Request body example:
    {
        "name":"new_restaurant_name",
        "address":"restaurant_address",
        "phone_number":"380111111111"
    }
    """

    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MenuCreateView(APIView):
    permission_classes = [IsAuthenticated]
    """"
    Request body example:
    {
        "restaurant": 1,
        "day_of_week": "THURSDAY",
        "dishes": [2, 4, 6]
    }
    """

    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DishCreateView(APIView):
    """"
    Request body example:
    {
        "name":"dish_name",
        "description":"delicious dish",
        "price":"120.50"
    }
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = DishSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CurrentDayMenuView(APIView):
    """"
     Request url example:  http://127.0.0.1:8000/api/restaurant/<restaurant_name>/dishes/
     """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        menu = Menu.objects.filter(day_of_week=request.query_params.get('day_of_week'))
        serializer = MenuInfoSerializer(menu, many=True)
        return Response(serializer.data)


class RestaurantDishesView(APIView):
    """"
     Request url example:  http://127.0.0.1:8000/api/restaurant/<restaurant_name>/dishes/
     """

    permission_classes = [IsAuthenticated]

    def get(self, request, restaurant_name):
        dishes = Dish.objects.filter(menu__restaurant__name=restaurant_name)
        serializer = DishSerializer(dishes, many=True)
        return Response(serializer.data)
