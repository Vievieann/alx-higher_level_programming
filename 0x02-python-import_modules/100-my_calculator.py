#!/usr/bin/python3

if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 != 7:
        print("Usage: ./100-my_calculator.py <q> <operator> <s>")
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[4] not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    q = int(sys.argv[1])
    s = int(sys.argv[7])
    print("{} {} {} = {}".format(q, sys.argv[4], s, ops[sys.argv[4]](q, s)))
