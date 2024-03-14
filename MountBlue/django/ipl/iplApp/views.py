# from django.http import HttpResponse
# return HttpResponse("<h1>Blog Home</h1>")
# def home(request):
#     return render(request, "blog/home.html", {"posts": Post.objects.all()})


from django.http import JsonResponse
from django.db.models import Count, Sum
from .models import IPLMatch, IPLDelivery
from django.shortcuts import render

# LOGICS


def matches_per_year_logic():
    return (
        IPLMatch.objects.values("season")
        .annotate(total_matches=Count("id"))
        .order_by("season")
    )


def matches_won():
    return (
        IPLMatch.objects.filter(winner__isnull=False)
        .values("season", "winner")
        .annotate(matches_won=Count("id"))
        .order_by("season", "winner")
    )


def extra_runs_conceded():
    return (
        IPLDelivery.objects.filter(match__season=2016)
        .values("bowling_team")
        .annotate(extra_runs=Sum("extra_runs"))
        .order_by("-extra_runs")
    )


def bowler_economy():
    return (
        IPLDelivery.objects.filter(match__season=2015)
        .values("bowler")
        .annotate(economy=Sum("total_runs") / (Count("bowler") / 6.0))
        .order_by("economy")[:10]
    )


# JSON routes


def matches_per_year(request):
    try:
        return JsonResponse({"matches_per_year": list(matches_per_year_logic())})
    except Exception as error:
        return JsonResponse({"error": str(error)})


def matches_won_per_team_per_year(request):
    try:
        return JsonResponse({"matches_won": list(matches_won())})
    except Exception as error:
        return JsonResponse({"error": str(error)})


def extra_runs_conceded_2016(request):
    try:
        return JsonResponse({"extra_runs_conceded_2016": list(extra_runs_conceded())})
    except Exception as error:
        return JsonResponse({"error": str(error)})


def top_economical_bowlers_2015(request):
    try:
        return JsonResponse({"bowler_economy": list(bowler_economy())})
    except Exception as error:
        return JsonResponse({"error": str(error)})


# HighCharts


def matches_per_year_chart(request):
    try:
        chart_data = [
            {"name": entry["season"], "y": entry["total_matches"]}
            for entry in matches_per_year_logic()
        ]

        return render(
            request, "iplApp/matches_per_year_chart.html", {"chart_data": chart_data}
        )
    except Exception as error:
        return JsonResponse({"error": str(error)})


def matches_won_per_team_chart(request):
    try:
        chart_data = {}
        for match in matches_won():
            season = match["season"]
            winner = match["winner"]
            matches_won_data = match["matches_won"]

            if season not in chart_data:
                chart_data[season] = {}

            chart_data[season][winner] = matches_won_data
        print("chart_data", chart_data)

        return render(
            request,
            "iplApp/matches_won_per_team_chart.html",
            {"chart_data": chart_data},
        )
    except Exception as error:
        return JsonResponse({"error": str(error)})


def extra_runs_conceded_2016_chart(request):
    try:
        chart_data = [
            {"name": entry["bowling_team"], "y": entry["extra_runs"]}
            for entry in extra_runs_conceded()
        ]

        return render(
            request,
            "iplApp/extra_runs_conceded_2016_chart.html",
            {"chart_data": chart_data},
        )
    except Exception as error:
        return JsonResponse({"error": str(error)})


def top_economical_bowlers_2015_chart(request):
    try:
        chart_data = [
            {"name": bowler_economy["bowler"], "y": bowler_economy["economy"]}
            for bowler_economy in bowler_economy()
        ]

        return render(
            request,
            "iplApp/top_economical_bowlers_2015_chart.html",
            {"chart_data": chart_data},
        )
    except Exception as error:
        return JsonResponse({"error": str(error)})
