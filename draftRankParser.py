import csv
from typing import TypedDict, List, Dict
from collections import Counter, defaultdict

def parse_nba_draft_csv(file_path: str) -> defaultdict[str, str]:
    players_drafted: defaultdict[str, str] = defaultdict(str)
    cumulative_ranks: defaultdict[str, int] = defaultdict(str)
    with open(file_path, mode='r') as file:
        players = csv.DictReader(file)
        for player in players:
            if player['team'] in players_drafted:
                players_drafted[player['team']] += 1
                cumulative_ranks[player['team']] += int(player['pick_overall'])
            else:
                players_drafted[player['team']] = 1
                cumulative_ranks[player['team']] = int(player['pick_overall'])
    return players_drafted, cumulative_ranks
            

# def calculate_accumulated_rank_by_team(players: List[Player]) -> Dict[str, int]:
#     team_ranks = defaultdict(int)
#     for player in players:
#         team_ranks[player.Team] += player.Rank
#     return team_ranks


# Example usage
file_path = 'nbaDraft.csv'
pd, cr = parse_nba_draft_csv(file_path)
print(pd)
print(cr)