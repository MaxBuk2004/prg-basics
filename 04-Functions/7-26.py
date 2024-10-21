def f(dice):
    if not dice:
        return None

    max_count = 1
    current_count = 1
    most_rolled_number = dice[0]

    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                most_rolled_number = dice[i - 1]
            current_count = 1

    if current_count > max_count:
        most_rolled_number = dice[-1]

    return int(most_rolled_number)

if __name__ == "__main__":
    print(f("5233165554211"))
    print(f("2133"))