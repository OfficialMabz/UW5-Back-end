from django.test import TestCase
from django.contrib.auth.models import User
from .models import Teams, League, LeagueFinals, StudentID, LeagueGames, CupDraws, CupRounds, ChallengeQueue, Candidates, PreBooked,Ladder, PitchBookings, Positions, Fixtures, Votes, Locations, PlayerProfile
import json
from rest_framework import status
from rest_framework.test import APITestCase
# Create your tests here.

class TestPlayersProfile(TestCase):
    def setUp(self):
        testuser1 = User.objects.create_user(
            username='testuser1', password='12345')
        testuser2 = User.objects.create_user(
            username='testuser2', password='12345')
        
        self.new = PlayerProfile.objects.create(user=testuser1)
        self.new = PlayerProfile.objects.create(user=testuser2)
    
    def test_model_playerprofile(self):
        user1 = User.objects.get(username = 'testuser1')
        #checks if the players actually gets registered in model
        self.assertTrue(PlayerProfile.objects.get(user = user1))
        
class StudentIdSerializer(TestCase):

    def test_valid_studentid(self):
        data1 = {"studentid": 1824585}

        response1 = self.client.post("/uw5/studentid/", data1)
        self.assertEqual(response1.status_code, status.HTTP_200_OK)

    def test_invalid_studentid(self):
        #below is a invalid student id
        data2 = {"studentid": 1808123}

        response2 = self.client.post("/uw5/studentid/", data2)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)
    