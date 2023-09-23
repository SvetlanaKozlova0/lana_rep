def solution(N: int, M: int):
    petya = 6 + N
    vasya = 12 + M
    if petya > vasya:
        print('Петя')
    else:
        print('Вася')


def main():
    N = int(input())
    M = int(input())
    solution(N, M)


if __name__ == '__main__':
    main()
