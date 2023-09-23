def solution(first: int, second: int):
    first_one = first % 10
    first_two = first // 10 % 10
    second_one = second % 10
    second_two = second // 10 % 10
    maximum = max(first_one, first_two, second_one, second_two)
    minimum = min(first_one, first_two, second_one, second_two)
    middle = (first_one + first_two + second_one +
              second_two - maximum - minimum) % 10
    print(maximum, middle, minimum, sep="")


def main():
    first = int(input())
    second = int(input())
    solution(first, second)


if __name__ == '__main__':
    main()
