from django.urls import path
from .views import (
    matches_per_year,
    matches_won_per_team_per_year,
    extra_runs_conceded_2016,
    top_economical_bowlers_2015,
    matches_per_year_chart,
    matches_won_per_team_chart,
    extra_runs_conceded_2016_chart,
    top_economical_bowlers_2015_chart
)

urlpatterns = [
    path("matches_per_year/", matches_per_year, name="matches_per_year"),
    path(
        "matches_won_per_team_per_year/",
        matches_won_per_team_per_year,
        name="matches_won_per_team_per_year",
    ),
    path(
        "extra_runs_conceded_2016/",
        extra_runs_conceded_2016,
        name="extra_runs_conceded_2016",
    ),
    path(
        "top_economical_bowlers_2015/",
        top_economical_bowlers_2015,
        name="top_economical_bowlers_2015",
    ),
    path(
        "matches_per_year_chart/",
        matches_per_year_chart,
        name="matches_per_year_chart",
    ),
    path(
        "matches_won_per_team_chart/",
        matches_won_per_team_chart,
        name="matches_won_per_team_chart",
    ),
    path(
        "extra_runs_conceded_2016_chart/",
        extra_runs_conceded_2016_chart,
        name="extra_runs_conceded_2016_chart",
    ),
    path(
        "top_economical_bowlers_2015_chart/",
        top_economical_bowlers_2015_chart,
        name="top_economical_bowlers_2015_chart",
    ),
]
