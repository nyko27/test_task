from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from .models import Restaurant, Dish, Menu


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'phone_number']


class DishSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields = ['id', 'name', 'description', 'price']


class MenuSerializer(ModelSerializer):
    dishes = PrimaryKeyRelatedField(many=True, queryset=Dish.objects.all())

    class Meta:
        model = Menu
        fields = ['id', 'restaurant', 'day_of_week', 'dishes']


class MenuInfoSerializer(ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)
    dishes = DishSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = ['id', 'restaurant', 'day_of_week', 'dishes']
