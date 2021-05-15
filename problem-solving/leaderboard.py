# link to problem: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem


def climbingLeaderboard(ranked, player):
    rank = []
    sorted_set = sorted(list(set(ranked)), reverse=True)
    length = len(sorted_set)

    for score in player:
        while length > 0 and score >= sorted_set[length-1]:
            length -= 1
        rank.append(length+1)
    return rank


ranked_count = int(input().strip())
ranked = list(map(int, input().rstrip().split()))

player_count = int(input().strip())
player = list(map(int, input().rstrip().split()))

result = climbingLeaderboard(ranked, player)
print(result)