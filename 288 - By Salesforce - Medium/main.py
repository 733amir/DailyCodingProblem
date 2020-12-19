def descending_ascending_diff(number: int) -> int:
    asc = ''.join(sorted(str(number).zfill(4)))
    des = asc[::-1]

    return int(des) - int(asc)


def solution_a(number: int) -> int:
    for steps in range(1, 10000):
        number = descending_ascending_diff(number)

        if number == 0:
            raise "all digits of the number are the same"
        if number == 6174:
            return steps

    raise "10000 steps counted, need more steps"


def main():
    for i in range(1000, 10000):
        try:
            steps = solution_a(i)
        except:
            continue
        print(f"{i} took {solution_a(i)} steps.")


if __name__ == "__main__":
    main()
