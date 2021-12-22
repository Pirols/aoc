from pathlib import Path
from functools import cache


class Player:
    def __init__(self, id, starting_position, score=0):
        self.id = id
        self.position = starting_position
        self.score = score


    def move_and_score(self, amount):
        self.position = (self.position + amount) % 10 or 10
        self.score += self.position


class DeterministicDice:
    def __init__(self, counter_start=1):
        self.counter = counter_start
        self.n_rolls = 0


    def roll(self):
        out = self.counter
        self.n_rolls += 1
        self.counter += 1
        if self.counter > 100:
            self.counter = 1
        return out


@cache
def get_position(pos, movement):
    return (pos + movement) % 10 or 10


@cache
def increment_score(scores, increase, turn):
    new_scores = list(scores)
    new_scores[turn] += increase
    return tuple(new_scores)


@cache
def dirac_game(positions, scores, turn):
    if scores[not turn] >= 21:
        out = [0, 0]
        out[not turn] = 1
        return tuple(out)

    tot_p1_wins = 0
    tot_p2_wins = 0

    for roll1 in range(1, 4):
        for roll2 in range(1, 4):
            for roll3 in range(1, 4):
                new_pos = get_position(positions[turn], roll1+roll2+roll3)
                new_positions = list(positions)
                new_positions[turn] = new_pos
                new_scores = increment_score(scores, new_pos, turn)

                p1_wins, p2_wins = dirac_game(tuple(new_positions), new_scores, not turn)
                tot_p1_wins += p1_wins
                tot_p2_wins += p2_wins

    return tot_p1_wins, tot_p2_wins


if __name__ == '__main__':
    data_path = Path('21_data.txt')

    with open(data_path, mode='r') as f:
        p1 = Player(1, int(f.readline().split(':')[1].strip()), score=0)
        p2 = Player(2, int(f.readline().split(':')[1].strip()), score=0)

    init_p1_pos = p1.position
    init_p2_pos = p2.position
    players = [p1, p2]
    dice = DeterministicDice(counter_start=1)

    while p1.score < 1000 and p2.score < 1000:
        for player in players:
            total = 0
            for _ in range(3):
                total += dice.roll()
            player.move_and_score(total)
            if player.score >= 1000:
                break

    # part a
    print(f"Part a score: {min(p1.score, p2.score)*dice.n_rolls}")

    cached_outcomes = dict()
    for pos in range(1, 11):
        for dirac_dice_roll in range(1, 4):
            cached_outcomes[(pos, dirac_dice_roll)] = get_position(pos, dirac_dice_roll)

    # part b
    print(f"Part b score: {max(dirac_game((init_p1_pos, init_p2_pos), (0, 0), 0))}")
