from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include, url
from .models import Teams, League, LeagueFinals, LeagueGames, CupDraws, CupRounds, ChallengeQueue, Candidates, PreBooked, PitchBookings, Positions, Fixtures, Votes, Locations, PlayerProfile
from .views import UserViewSet, TeamViewSet,StudentIDViewSet, LeagueViewSet, LeagueFinalViewSet, LeagueGameViewSet, CupDrawViewSet, CupRoundViewSet, ChallengeQueueViewSet, CandidateViewSet, CandidateViewSet, PrebookedViewSet, PitchbookingViewSet, PositionViewSet, FixtureViewSet, VoteViewSet, LocationViewSet, PlayerProfileViewSet
from django.contrib.auth import views as auth_views 

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('teams', TeamViewSet)
router.register('league', LeagueViewSet)
router.register('leaguefinals', LeagueFinalViewSet)
router.register('leaguegames', LeagueGameViewSet)
router.register('cupdraws', CupDrawViewSet)
router.register('cupround', CupRoundViewSet)
router.register('challengequeue', ChallengeQueueViewSet)
router.register('candidates', CandidateViewSet)
router.register('prebooked', PrebookedViewSet)
router.register('positions', PositionViewSet)
router.register('fixtures', FixtureViewSet)
router.register('votes', VoteViewSet)
router.register('locations',LocationViewSet)
router.register('playerprofile', PlayerProfileViewSet)
router.register('studentid', StudentIDViewSet)

urlpatterns = [
    path('', include(router.urls)), 
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]