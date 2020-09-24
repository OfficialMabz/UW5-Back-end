from django.shortcuts import render
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from .models import Teams, League, StudentID, LeagueFinals, LeagueGames, CupDraws,Ladder, CupRounds, ChallengeQueue, Candidates, PreBooked, PitchBookings, Positions, Fixtures, Votes, Locations, PlayerProfile
from .serializers import UserSerializer,StudentIDSerializer, TeamSerializer, LeagueSerializer,LadderSerializer, LeagueFinalSerializer, LeagueGameSerializer, CupDrawSerializer, CupRoundSerializer, ChallengeQueueSerializer, CandidateSerializer, PrebookedSerializer, PitchBookingSerializer, PositionSerializer, FixtureSerializer, VoteSerializer, LocationSerializer, PlayerProfileSerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_rest_passwordreset.signals import reset_password_token_created
from django.dispatch import receiver
from django.urls import reverse
from django.core.mail import send_mail  
import re
from urllib.request import urlopen


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = 'Copy and paste the token to gain access to your new reset password ' +': ' + '' + reset_password_token.key

    send_mail(
        # title:
        "Password Reset for {title}".format(title="UW5"),
        # message:
        
        email_plaintext_message,
        # from:
        "officialmabz786@gmail.com",
        # to:
        [reset_password_token.user.email]
    )

def studentIdScrapper():

    url = 'https://www.warwicksu.com/membershipapi/listMembers/f84103bd-b42c-492f-a2c8-6c3f080c331d/'
    page = urlopen(url)
    html = page.read().decode('utf-8')
    pattern = "<uniqueid.*?>.*?</uniqueid.*?>"
    match_results = re.findall(pattern, html, re.IGNORECASE)

    halfresult = [re.sub(r'<UniqueID>', '', i) for i in match_results]
    fullresult = [re.sub(r'</UniqueID>', '', i) for i in halfresult]

    for i in range(0, len(fullresult)): 
        fullresult[i] = int(fullresult[i]) 

    return fullresult

class StudentIDViewSet(viewsets.ModelViewSet):
    queryset = StudentID.objects.all()
    serializer_class = StudentIDSerializer
    permission_classes = (AllowAny, )

    def create(self, request, *args, **kwargs):
        serializer = StudentIDSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        chosenStudentId = serializer.validated_data.get('studentid')
        fetchedIds = studentIdScrapper()
        
        if chosenStudentId in fetchedIds:
            serializer.save()
            response = {'message': 'Success', 'result': serializer.data}
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'Failed to register, Incorrect student Id', 'result': serializer.data}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.data)

  
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Teams.objects.all()
    serializer_class = TeamSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends=[DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name','position', 'ladderId']
    ordering_fields = ['name','position', 'ladderId']

class LadderViewSet(viewsets.ModelViewSet):
    queryset = Ladder.objects.all()
    serializer_class = LadderSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends=[DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['id','LadderName']
    ordering_fields = ['name','LadderName']

   
    

class PlayerProfileViewSet(viewsets.ModelViewSet):
    queryset = PlayerProfile.objects.all()
    serializer_class = PlayerProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends=[DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['id','user', 'studentId']
    ordering_fields = ['id','user', 'studentId']
    

class LeagueViewSet(viewsets.ModelViewSet):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends=[DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['id','leagueId', 'teamId']
    ordering_fields = ['id','leagueId', 'teamId']


class LeagueFinalViewSet(viewsets.ModelViewSet):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends=[DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['id','teamAId','teamBId', 'locationId','prebookedId','date']
    ordering_fields = ['id','teamAId','teamBId', 'locationId','prebookedId','date']
  

class LeagueGameViewSet(viewsets.ModelViewSet):
    queryset = LeagueGames.objects.all()
    serializer_class = LeagueGameSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends=[DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['id','teamAId','teamBId', 'locationId','prebookedId', 'date']
    ordering_fields = ['id','teamAId','teamBId', 'locationId','prebookedId', 'date']
    

class CupDrawViewSet(viewsets.ModelViewSet):
    queryset = CupDraws.objects.all()
    serializer_class = CupDrawSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends=[DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['id','teamAId', 'teamBId','resultId','cupRoundId','locationId','prebookedId']
    ordering_fields = ['id','teamAId', 'teamBId', 'resultId', 'cupRoundId','locationId','prebookedId']
  

class CupRoundViewSet(viewsets.ModelViewSet):
    queryset = CupRounds.objects.all()
    serializer_class = CupRoundSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends=[DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['id','startDate', 'endDate','cupRoundTitle']
    ordering_fields = ['id','startDate', 'endDate','cupRoundTitle']


class ChallengeQueueViewSet(viewsets.ModelViewSet):
    queryset = ChallengeQueue.objects.all()
    serializer_class = ChallengeQueueSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends=[DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['id','teamId', 'queueJoinTime','allocatedTime']
    ordering_fields = ['id','teamId', 'queueJoinTime','allocatedTime']
    

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidates.objects.all()
    serializer_class = CandidateSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends=[DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['id','playerId', 'positionId','manifesto']
    ordering_fields = ['id','playerId', 'positionId','manifesto']
    

class PrebookedViewSet(viewsets.ModelViewSet):
    queryset = PreBooked.objects.all()
    serializer_class = PrebookedSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends=[DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['id','locationId', 'day', 'time']
    ordering_fields = ['id','locationId', 'day', 'time']
    

class PitchbookingViewSet(viewsets.ModelViewSet):
    queryset = PitchBookings.objects.all()
    serializer_class =  PitchBookingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends=[DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['id','locationId', 'teamAId', 'teamBId', 'date', 'prebookedId']
    ordering_fields = ['id','locationId', 'teamAId', 'teamBId', 'date', 'prebookedId']


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Positions.objects.all()
    serializer_class = PositionSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends=[DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['id','title']
    ordering_fields = ['id','title']
    

class FixtureViewSet(viewsets.ModelViewSet):
    queryset = Fixtures.objects.all()
    serializer_class = FixtureSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends=[DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['id','locationId', 'challengingTeamId','resultId', 'challengedTeamId','date','prebookedId']
    ordering_fields = ['id','locationId', 'challengingTeamId', 'resultId','challengedTeamId','date','prebookedId']
    


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Votes.objects.all()
    serializer_class = VoteSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends=[DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['id','playerId','date','positionId']
    ordering_fields = ['id','playerId','date','positionId']
    


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Locations.objects.all()
    serializer_class = LocationSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    filter_backends=[DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['id','name','pitches']
    ordering_fields = ['id','name','pitches'] 
