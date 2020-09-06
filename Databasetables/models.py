from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
#ALL 16 TABLES 
#THE ID HAS BEEN MOVED AS EACH TABLES COMES WITH ITS BUILT IN ID NUMBERS
#MAKE SURE TO REMOVE THE ID SECTION FROM EXCEL WHILE IMPORTING 
#ALSO MAKE SURE TO CHANGE THE EXCEL TYPE TO CSV FILE IN ORDER TO WORK PERFECTLY
#COMPARE THE TABLES WITH THE EXCEL OR CAPTURED IMAGE TO SEE THE DIFFERENCES AND SIMILARITY 

# Create your models here.

class Ladder(models.Model):
    LadderName = models.CharField(max_length=50, default='0')

    def __str__(self):
        return self.LadderName

class Teams(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=220, blank=True)
    password = models.CharField(max_length=50)
    photo = models.FileField(upload_to = 'teamsImage/', blank=True)
    ladderId = models.ForeignKey(Ladder, default=0, on_delete=models.CASCADE, blank=True)
    competitionId = models.IntegerField(blank=True)
    position = models.IntegerField(blank=True)
    contactforfriendly = models.CharField(blank=True, max_length=50)
    seeded = models.IntegerField(blank=True)
    coefficient =models.IntegerField(blank=True)
    coefficientRank = models.IntegerField(blank=True)

    def __str__(self):
        return self.name

class PlayerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    studentId = models.CharField(default='0', max_length=10)
    team = models.ForeignKey(Teams, null= True, on_delete=models.CASCADE, blank=True)


    def __str__(self):
        return self.user.username
        

    



"""class Players(models.Model):
    studentId = models.IntegerField(blank=True, null=True)
    teamID = models.ForeignKey(Teams, on_delete=models.CASCADE, null=True)
    displayName = models.CharField(max_length=40, null=True)
    isExec = models.BooleanField(blank=True, null=True)
    webmaster = models.IntegerField(blank=True, null=True)
    sessionKey = models.CharField(blank=True, max_length=100, null=True)
    password = models.CharField(blank=True, max_length=125, null=True)
    public_details = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=20, null=True)
    send_email = models.IntegerField(blank=True, null=True)
    fb_id = models.CharField(blank=True, max_length=5, null=True)
    goalsScored = models.IntegerField(null=True)
    """

class Positions(models.Model):
    title = models.CharField(blank=True, max_length=50)
    description = models.TextField(blank=True, max_length=500)

    def __str__(self):
        return self.title



class Candidates(models.Model):
    playerId = models.ForeignKey(PlayerProfile, null=True, on_delete=models.CASCADE, blank=True)
    positionId = models.ForeignKey(Positions, on_delete=models.CASCADE, null=True, blank=True)
    manifesto = models.TextField(max_length=20)


class ChallengeQueue(models.Model):
    teamId = models.ForeignKey(Teams,on_delete=models.CASCADE, null=True, blank=True)
    queueJoinTime = models.IntegerField(blank=True) 
    allocatedTime = models.IntegerField(blank=True)

class Locations(models.Model):
    name = models.CharField(blank=True, max_length=50)
    pitches = models.IntegerField(blank=True)

    def __str__(self):
        return self.name


class PreBooked(models.Model):
    locationId = models.ForeignKey(Locations, null=True, on_delete=models.CASCADE, blank=True)
    day = models.IntegerField(blank=True)
    time = models.TimeField(blank=True)
    temp = models.IntegerField(blank=True)

'''class Booking(models.Model): 
    teamAId = models.ForeignKey(Teams, on_delete=models.CASCADE, null=True, blank=True)
    teamBId = models.IntegerField(blank=True)
    locationId = models.ForeignKey(Locations, on_delete=models.CASCADE, null=True, blank=True)
    date = models.IntegerField(blank=True)
    prebookedId = models.ForeignKey(PreBooked, on_delete=models.CASCADE, null=True, blank=True)
   ''' 
class Votes(models.Model):
    playerId = models.ForeignKey(PlayerProfile, on_delete=models.CASCADE, null=True, blank=True)
    #candidateId = models.ForeignKey(Candidates, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(blank=True, max_length=5)
    positionId = models.ForeignKey(Positions, on_delete=models.CASCADE, null=True, blank=True)

class CupRounds(models.Model):
    startDate = models.IntegerField(blank=True)
    endDate = models.IntegerField(blank=True)
    cupRoundTitle = models.CharField(blank=False, max_length=50)

class CupDraws(models.Model):
    teamAId = models.ForeignKey(Teams, on_delete=models.CASCADE, null=True, blank=True)
    teamBId = models.ForeignKey(Teams, on_delete=models.CASCADE, null=True, blank=True, related_name='TeamBCupDraws')
    cupRoundId = models.ForeignKey(CupRounds, on_delete=models.CASCADE, null=True, blank=True)
    teamAgoals = models.IntegerField(blank=True)
    teamBgoals = models.IntegerField(blank=True)
    resultId = models.IntegerField(blank=True)
    locationId = models.ForeignKey(Locations, on_delete=models.CASCADE, null=True, blank=True)
    prebookedId = models.ForeignKey(PreBooked, on_delete=models.CASCADE, null=True, blank=True)
    date = models.CharField(blank=True, max_length=15)
    confirmed = models.IntegerField(blank=True)
    deadline = models.IntegerField(blank=True)

class PitchBookings(models.Model):
    #bookingId = models.ForeignKey(Booking, on_delete=models.CASCADE, null=True, blank=True)
    teamAId = models.ForeignKey(Teams, on_delete=models.CASCADE, null=True, blank=True)
    teamBId = models.ForeignKey(Teams, on_delete=models.CASCADE, null=True, blank=True, related_name='TeamBPitchBookings')
    locationId = models.ForeignKey(Locations, on_delete=models.CASCADE, null=True, blank=True)
    date = models.IntegerField(blank=True)
    prebookedId = models.ForeignKey(PreBooked, on_delete=models.CASCADE, null=True, blank=True)
    
    
class Fixtures(models.Model):
    locationId = models.ForeignKey(Locations, on_delete=models.CASCADE, null=True, blank=True)
    challengingTeamId = models.ForeignKey(Teams, on_delete=models.CASCADE, null=True, blank=True)
    challengedTeamId = models.ForeignKey(Teams, on_delete=models.CASCADE, null=True, blank=True, related_name='ChallengedTeam')
    resultId = models.IntegerField(blank=True)
    confirmed = models.IntegerField(blank=True)
    date = models.IntegerField(blank=True)
    challengingTeamGoals = models.IntegerField(blank=True)
    challengedTeamGoals = models.IntegerField(blank=True)
    prebookedId = models.ForeignKey(PreBooked, on_delete=models.CASCADE, null=True, blank=True)
    challengingGoalsEntered = models.IntegerField(blank=True)
    challengedGoalsEntered = models.IntegerField(blank=True)

class League(models.Model):
    leagueId = models.IntegerField(blank=True, default='0')
    teamId = models.ForeignKey(Teams, on_delete=models.CASCADE, null=True, blank=True)


class LeagueFinals(models.Model):
    teamAId = models.ForeignKey(Teams, on_delete=models.CASCADE, null=True, blank=True)
    teamBId = models.ForeignKey(Teams, on_delete=models.CASCADE, null=True, blank=True, related_name='TeamBLeagueFinal')
    teamAGoals = models.IntegerField(blank=True)
    teamBGoals = models.IntegerField(blank=True)
    resultId = models.IntegerField(blank=True)
    date = models.IntegerField(blank=True)
    locationId = models.ForeignKey(Locations, on_delete=models.CASCADE, null=True, blank=True)
    prebookedId = models.ForeignKey(PreBooked, on_delete=models.CASCADE, null=True, blank=True)
    roundId = models.IntegerField(blank=True)
    typeId = models.IntegerField(blank=True)

class LeagueGames(models.Model):
    teamAId = models.ForeignKey(Teams, on_delete=models.CASCADE, null=True, blank=True)
    teamBId = models.ForeignKey(Teams, on_delete=models.CASCADE, null=True, blank=True, related_name='TeamBLeagueGames')
    teamAGoals = models.IntegerField(blank=True)
    teamBGoals = models.IntegerField(blank=True)
    resultId = models.IntegerField(blank=True)
    date = models.IntegerField(blank=True)
    locationId = models.ForeignKey(Locations, on_delete=models.CASCADE, null=True, blank=True)
    prebookedId = models.ForeignKey(PreBooked, on_delete=models.CASCADE, null=True, blank=True)