

def calc_add(x, y, vq):
    if vq == 1:
        return "The sum of {} added by {} is equal to -<| {} |>-".format(x, y, (x+y))
    elif vq == -1:
        return "-<| {} |>-".format(x+y)
    elif vq == 0:
        return "{} + {} = -<| {} |>-".format(x, y, (x+y))


def calc_sub(x, y, vq):
    if vq == 1:
        return "The difference of {} subtracted by {} is equal to -<| {} |>-".format(x, y, (x-y))
    elif vq == -1:
        return "-<| {} |>-".format(x-y)
    elif vq == 0:
        return "{} - {} = -<| {} |>-".format(x, y, (x-y))


def calc_mul(x, y, vq):
    if vq == 1:
        return "The product of {} multiplied by {} is equal to -<| {} |>-".format(x, y, (x*y))
    elif vq == -1:
        return "-<| {} |>-".format(x*y)
    elif vq == 0:
        return "{} x {} = -<| {} |>-".format(x, y, (x+y))


def calc_div(x, y, vq):
    if vq == 1:
        return "The quotient of {} divided by {} is equal to -<| {} |>-".format(x, y, (x/y))
    elif vq == -1:
        return "-<| {} |>-".format(x/y)
    elif vq == 0:
        return "{} / {} = -<| {} |>-".format(x, y, (x/y))


def calc_sqr(x, vq):
    if vq == 1:
        return "The answer of {} squared is equal to -<| {} |>-".format(x, (x**2))
    elif vq == -1:
        return "-<| {} |>-".format(x**2)
    elif vq == 0:
        return "{} ^ 2 = -<| {} |>-".format(x, (x**2))


def calc_cub(x, vq):
    if vq == 1:
        return "The answer of {} cubed is equal to -<| {} |>-".format(x, (x**3))
    elif vq == -1:
        return "-<| {} |>-".format(x**3)
    elif vq == 0:
        return "{} ^ 3 = -<| {} |>-".format(x, (x**3))


def calc_exp(x, y, vq):
    if vq == 1:
        return "The answer of {} raised to the power of {} is equal to -<| {} |>-".format(x, y, (x**y))
    elif vq == -1:
        return "-<| {} |>-".format(x**y)
    elif vq == 0:
        return "{} ^ {} = -<| {} |>-".format(x, y, (x**y))
