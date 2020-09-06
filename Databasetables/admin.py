from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Teams, League, LeagueFinals, LeagueGames, Ladder, CupDraws, CupRounds, ChallengeQueue, Candidates, PreBooked, PitchBookings, Positions, Fixtures, Votes, Locations, PlayerProfile

admin.site.site_header = 'UW5 DATABASE'

# Register your models here

admin.site.register(Ladder)
admin.site.register(PlayerProfile)
admin.site.register(Teams, ImportExportModelAdmin)
admin.site.register(League, ImportExportModelAdmin)
admin.site.register(LeagueFinals, ImportExportModelAdmin)
admin.site.register(LeagueGames, ImportExportModelAdmin)
admin.site.register(CupDraws, ImportExportModelAdmin)
admin.site.register(CupRounds, ImportExportModelAdmin)
admin.site.register(ChallengeQueue, ImportExportModelAdmin)
admin.site.register(Candidates, ImportExportModelAdmin)
admin.site.register(PreBooked, ImportExportModelAdmin)
admin.site.register(PitchBookings, ImportExportModelAdmin)
admin.site.register(Positions, ImportExportModelAdmin)
admin.site.register(Fixtures, ImportExportModelAdmin)
admin.site.register(Votes, ImportExportModelAdmin)
admin.site.register(Locations, ImportExportModelAdmin)

class ViewAdmin(ImportExportModelAdmin):
    class Meta:
        team = Teams
        league = League
        leaguefinal = LeagueFinals
        leaguegames = LeagueGames
        cupdraws = CupDraws 
        cuprounds = CupRounds
        challengequeue = ChallengeQueue
        candidates = Candidates
        prebooked = PreBooked
        pitchbookings = PitchBookings
        positions = Positions
        fixtures = Fixtures
        votes = Votes
        location = Locations 
    pass
