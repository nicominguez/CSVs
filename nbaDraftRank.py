import csv
from collections import defaultdict
from typing import Tuple, Dict

def load_draft_data(input_path: str) -> Tuple[Dict[str, int], Dict[str, int]]:
    players_drafted = defaultdict(int)
    cumulative_ranks = defaultdict(int)
    
    try:
        with open(input_path, "r", newline='') as file:
            my_reader = csv.reader(file)
            next(my_reader)  # Skip header row
            for player in my_reader:
                team = player[1]
                rank = int(player[0])
                players_drafted[team] += 1
                cumulative_ranks[team] += rank
    except FileNotFoundError:
        print(f"Error: The file {input_path} was not found.")
    except ValueError:
        print("Error: Invalid data format in the file.")
    
    return dict(players_drafted), dict(cumulative_ranks)

def calculate_ranked_avg(players_drafted: dict[str, int], cumulative_ranks: dict[str, int]) -> dict[str, float]:
    ranked_avg = {}
    for team in players_drafted:
        ranked_avg[team] = float(cumulative_ranks[team] / players_drafted[team])
    return dict(sorted(ranked_avg.items(), key=lambda item: item[1], reverse=False))

def save_rankings_to_csv(output_path: str, ranked_avg: Dict[str, float], players_drafted: Dict[str, int]) -> None:
    try:
        with open(output_path, "w", newline='', encoding='utf-8') as file:
            my_writer = csv.writer(file)
            my_writer.writerow(["Team", "Average Draft Pick", "Total Players Drafted"])
            for team, avg in ranked_avg.items():
                my_writer.writerow([team, f"{avg:.2f}", players_drafted[team]])
    except IOError:
        print(f"Error: Could not write to file {output_path}.")

def main():
    input_file = "nbaDraft.csv"
    output_file = "nbaRankedByDraftPick.csv"

    players_drafted, cumulative_ranks = load_draft_data(input_file)
    ranked_avg = calculate_ranked_avg(players_drafted, cumulative_ranks)
    save_rankings_to_csv(output_file, ranked_avg, players_drafted)

if __name__ == '__main__':
    main()
