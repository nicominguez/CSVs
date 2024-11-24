import csv

def load_draft_data(input_path: str) -> tuple[dict[str, int], dict[str, int]]:
    players_drafted = {}
    cumulative_ranks = {}
    with open(input_path, "r", newline='') as file:
        my_reader = csv.reader(file)
        next(my_reader)
        for row in my_reader:
            if row[1] in players_drafted:
                players_drafted[row[1]] += 1
                cumulative_ranks[row[1]] += int(row[0])
            else:
                players_drafted[row[1]] = 1
                cumulative_ranks[row[1]] = int(row[0])
    return players_drafted, cumulative_ranks

def calculate_ranked_avg(players_drafted: dict[str, int], cumulative_ranks: dict[str, int]) -> dict[str, float]:
    ranked_avg = {}
    for team in players_drafted:
        ranked_avg[team] = float(cumulative_ranks[team] / players_drafted[team])
    return dict(sorted(ranked_avg.items(), key=lambda item: item[1], reverse=True))

def save_rankings_to_csv(output_path: str, ranked_avg: dict[str, float], players_drafted: dict[str, int]) -> None:
    with open(output_path, "w", newline='', encoding='utf-8') as file:
        my_writer = csv.writer(file)
        my_writer.writerow(["Team", "Average Draft Pick", "Total Players Drafted"])
        for team in ranked_avg:
            my_writer.writerow([team, f"{ranked_avg[team]:.2f}", players_drafted[team]])

def main():
    input_file = "nbaDraft.csv"
    output_file = "nbaRankedByDraftPick.csv"

    players_drafted, cumulative_ranks = load_draft_data(input_file)
    ranked_avg = calculate_ranked_avg(players_drafted, cumulative_ranks)
    save_rankings_to_csv(output_file, ranked_avg, players_drafted)

if __name__ == '__main__':
    main()
