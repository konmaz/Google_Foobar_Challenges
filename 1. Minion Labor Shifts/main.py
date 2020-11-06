# Minion Labor Shifts https://foobar.withgoogle.com/
# Remove duplicate numbers that occur more than n times
def solution(data, n):
    count = {}  # A dictionary that keeps the number of occurrences of a number.
    for item in data:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    OUT = []
    for item in data:
        if not(count[item] > n):
            OUT.append(item)
    return OUT


def main():
    pass


if __name__ == '__main__':
    main()

