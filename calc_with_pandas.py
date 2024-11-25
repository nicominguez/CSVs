import csv
import pandas as pd

def parse_nba_draft_csv(file_path: str) -> (dict, dict, dict):
    df = pd.read_csv(file_path)
    
    players_drafted = df.groupby('team').size().to_dict()
    average_ranks = dict(sorted(df.groupby('team')['pick_overall'].mean().to_dict().items(), key=lambda item: item[1], reverse=False))
    
    return players_drafted, average_ranks

def save_rankings_to_csv(output_path: str, ranked_avg: dict[str, float], players_drafted: dict[str, int]) -> None:
    with open(output_path, "w", newline='', encoding='utf-8') as file:
        my_writer = csv.writer(file)
        my_writer.writerow(["Team", "Average Draft Pick", "Total Players Drafted"])
        for team in ranked_avg:
            my_writer.writerow([team, f"{ranked_avg[team]:.2f}", players_drafted[team]])


def main():
  file_path = 'nbaDraft.csv'
  output_file = "nbaRankedByDraftPick.csv"
  
  players_drafted, average_ranks = parse_nba_draft_csv(file_path)
  save_rankings_to_csv(output_file, average_ranks, players_drafted)

if __name__ == '__main__':
    main()