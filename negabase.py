def negabase(number, base):
    if number == 0:
        return '0'

    digits = list()
    while number != 0:
        number, remainder = divmod(number, base)

        if remainder < 0:
            # a = b*c + r if r < 0
            # a = b * c + r + b - b
            #   = b * (c+1) + (r -b )
            number, remainder =  number + 1, remainder - base 
        digits.append(str(remainder))

    return "".join(digits[::-1]) if len(digits) else 0


print negabase(-15, -2)
