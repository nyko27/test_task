from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from employees.views import (
    RegisterEmployeeView,
    EmployeeLoginView,
    VoteCreateView,
    VotingResultsView,
    RedirectOldVoteResultsView
)
from restaurants.views import (
    RestaurantCreateView,
    MenuCreateView,
    CurrentDayMenuView,
    DishCreateView,
    RestaurantDishesView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterEmployeeView.as_view(), name='register_employee'),
    path('api/login/', EmployeeLoginView.as_view(), name='employee_login'),
    path('api/vote/', VoteCreateView.as_view(), name='vote_create'),
    path('api/vote/results', VotingResultsView.as_view(), name='voting_results'),
    path('api/employees/voteresults', RedirectOldVoteResultsView.as_view(), name='employees_vote_results'),

    path('api/restaurant/create/', RestaurantCreateView.as_view(), name='create_restaurant'),
    path('api/menu/create/', MenuCreateView.as_view(), name='create_menu'),
    path('api/menu/current/', CurrentDayMenuView.as_view(), name='current_menu'),
    path('api/dish/create/', DishCreateView.as_view(), name='create_dish'),
    path('api/restaurant/<str:restaurant_name>/dishes/', RestaurantDishesView.as_view(), name='restaurant_dishes'),
]
