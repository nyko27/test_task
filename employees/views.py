from django.db.models import Count
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from restaurants.models import Menu
from .models import Vote
from .serializers import EmployeeSerializer, EmployeeLoginSerializer, VoteSerializer


class RegisterEmployeeView(APIView):
    """
       Request body example:
    {
        "username":"<username>",
        "first_name":"<first_name>",
        "last_name":"<last_name>",
        "password":"<password>"
    }
    """

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = RefreshToken.for_user(user)
            response = {
                'refresh': str(token),
                'access': str(token.access_token),
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeLoginView(TokenObtainPairView):
    """
       Request body example:
    {
        "username": "<username>",
        "password": "<password>"
    }
    """
    serializer_class = EmployeeLoginSerializer


class VoteCreateView(APIView):
    """
       Request body example:
    {
        "employee": 1,
        "menu": 3,
        "day_of_week": "WEDNESDAY"
    }
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = VoteSerializer(data=request.data)
        if serializer.is_valid():
            menu = serializer.validated_data.get("menu")
            day_of_week = serializer.validated_data.get("day_of_week")
            employee = serializer.validated_data.get("employee")
            if not Menu.objects.filter(id=menu.id, day_of_week=day_of_week).exists():
                return Response(
                    {"detail": "Menu is not available on this day"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            existing_vote = Vote.objects.filter(employee=employee, day_of_week=day_of_week)
            if existing_vote.exists():
                existing_vote.delete()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VotingResultsView(APIView):
    """"
     Request url example:  http://127.0.0.1:8000/api/vote/results?day_of_week=MONDAY
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        day_of_week = request.query_params.get('day_of_week')
        votes = (Vote.objects.filter(day_of_week=day_of_week)
                 .values('menu')
                 .annotate(total_votes=Count('menu'))
                 .order_by('-total_votes'))

        return Response(votes)


class RedirectOldVoteResultsView(APIView):
    """"
     Redirecting voting results request for old version of mobile app
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        build_version = request.headers.get("Build-Version", 1.5)
        if float(build_version) < 2.0:
            url = reverse("voting_results")
            params = request.GET.urlencode()
            return HttpResponseRedirect(f"{url}?{params}")
