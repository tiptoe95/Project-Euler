
def name_scores(name_array):
    name_array.sort()
    name_scores = {}

    for i, name in enumerate(name_array, start=1):
        score = 0
        for c in name:
            points = ord(c) - ord("A") + 1
            score += points
        name_scores[name] = score * i
    print(name_scores)
    return(sum(name_scores.values()))


if __name__ == '__main__':
    from pathlib import Path
    import csv

    input_file = Path("inputs/names.csv")
    with open(input_file) as file:
        csv_data = list(csv.reader(file))
        print(name_scores(csv_data[0]))