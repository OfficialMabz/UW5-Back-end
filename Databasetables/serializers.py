from rest_framework import serializers
from .models import Teams, League, LeagueFinals, LeagueGames, CupDraws, CupRounds, ChallengeQueue, Candidates, PreBooked,Ladder, PitchBookings, Positions, Fixtures, Votes, Locations, PlayerProfile
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ('id', 'username',  'password')
        extra_kwargs = {'password': {'write_only':True, 'required':True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data, )
        token = Token.objects.create(user=user)
        return user



class PlayerProfileSerializer(serializers.ModelSerializer):
    class Meta: 
        model = PlayerProfile
        fields= ('id', 'user', 'studentId')

class LadderSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Ladder
        fields= ('id', 'LadderName')



class TeamSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Teams
        fields= ('id', 'name', 'description','password', 'photo', 'ladderId', 'competitionId',  'position', 'contactforfriendly', 'seeded', 'coefficient', 'coefficientRank')

class PositionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Positions
        fields= ('id', 'title', 'description')

class CandidateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Candidates
        fields= ('id', 'playerId', 'positionId', 'manifesto')


class ChallengeQueueSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ChallengeQueue
        fields= ('id', 'teamId', 'queueJoinTime', 'allocatedTime')


class LocationSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Locations
        fields= ('id', 'name', 'pitches')


class PrebookedSerializer(serializers.ModelSerializer):
    class Meta: 
        model = PreBooked
        fields= ('id', 'locationId', 'day', 'time', 'temp')

class VoteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Votes
        fields= ('id', 'playerId', 'date', 'positionId')


class CupRoundSerializer(serializers.ModelSerializer):
    class Meta: 
        model = CupRounds
        fields= ('id', 'startDate', 'endDate', 'cupRoundTitle')


class CupDrawSerializer(serializers.ModelSerializer):
    class Meta: 
        model = CupDraws
        fields= ('id', 'teamAId', 'teamBId', 'cupRoundId', 'teamAgoals', 'teamBgoals', 'resultId', 'locationId', 'prebookedId', 'date', 'confirmed', 'deadline')

class PitchBookingSerializer(serializers.ModelSerializer):
    class Meta: 
        model = PitchBookings
        fields= ('id', 'temaAId', 'teamBId', 'locationId', 'date', 'prebookedId')

class FixtureSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Fixtures
        fields= ('id', 'locationId', 'challengingTeamId', 'challengedTeamId', 'resultId', 'confirmed', 'date', 'challengingTeamGoals', 'challengedTeamGoals', 'prebookedId', 'challengingGoalsEntered', 'challengedGoalsEntered')

class LeagueSerializer(serializers.ModelSerializer):
    class Meta: 
        model = League
        fields= ('id', 'leagueId', 'teamId')

class LeagueFinalSerializer(serializers.ModelSerializer):
    class Meta: 
        model = LeagueFinals
        fields= ('id', 'teamAId', 'teamBId', 'teamAGoals', 'teamBGoals', 'resultId', 'date', 'locationId', 'prebookedId', 'roundId', 'typeId')

class LeagueGameSerializer(serializers.ModelSerializer):
    class Meta: 
        model = LeagueGames
        fields= ('id', 'teamAId', 'teamBId', 'teamAGoals', 'teamBGoals', 'resultId', 'resultId', 'date', 'locationId', 'prebookedId')