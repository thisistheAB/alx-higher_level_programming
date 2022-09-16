#!/usr/bin/python3
import add_0


def main():
    a = 1
    b = 2

    addition = add_0.add(a, b)
    print('{:d} + {:d} = {:d}'.format(a, b, addition))


if __name__ == "__main__":
    main()
