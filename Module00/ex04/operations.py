import sys

def operations(
    a,
    b
):
    """
    Return sum, difference, product, quotient and remainder of two integers.
    """

    sum = a + b
    diff = a - b
    product = a * b
    if b != 0:
        quotient = a / b
        remainder = a % b
    else:
        quotient = "ERROR"
        remainder = "ERROR"

    return sum, diff, product, quotient, remainder

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Error: wrong number of arguments. Need two integers.", file=sys.stderr)
    elif not (sys.argv[1].isnumeric() and sys.argv[2].isnumeric()):
        print("Error: argument(s) is not numeric", file=sys.stderr)
    else:
        rSum, rDiff, rProduct, rQuotient, rRemainder = operations(int(sys.argv[1]), int(sys.argv[2]))
        print(f"""
    Sum:        {rSum}
    Difference: {rDiff}
    Product:    {rProduct}
    Quotient:   {rQuotient}
    Remainder:  {rRemainder}
        """)
