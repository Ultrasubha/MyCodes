import webbrowser
import time


def open_links_with_delay(links, delay=0.5):
    for link in links:
        webbrowser.open(link)
        time.sleep(delay)


def main():
    links_to_open = [
        "http://localhost:8000/ipl/matches_per_year/",
        "http://localhost:8000/ipl/matches_won_per_team_per_year/",
        "http://localhost:8000/ipl/extra_runs_conceded_2016/",
        "http://localhost:8000/ipl/top_economical_bowlers_2015/",
        "http://localhost:8000/ipl/matches_per_year_chart/",
        "http://localhost:8000/ipl/matches_won_per_team_chart/",
        "http://localhost:8000/ipl/extra_runs_conceded_2016_chart/",
        "http://localhost:8000/ipl/top_economical_bowlers_2015_chart/",
    ]

    time.sleep(0.5)  # Initial delay before opening links
    open_links_with_delay(links_to_open)


if __name__ == "__main__":
    main()
