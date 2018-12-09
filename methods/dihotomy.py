import tools


def end_condition(l, r, eps):
    return abs(l - r) <= eps


def process(func, a, b, eps=1e-7):
    va = tools.eval_func_at_point(func, a)
    vb = tools.eval_func_at_point(func, b)
    print("f(%s)=%s, f(%s)=%s" % (a, va, b, vb))
    left = a
    right = b
    value_at_left = va
    # value_at_right = vb
    i = 1
    prev_x = (a + b) / 2
    print("X0=%s" % prev_x)
    while True:
        curr_x = (left + right) / 2
        print("<%s> X%s=%s" % (i + 1, i, curr_x))
        if end_condition(left, right, eps):
            return curr_x
        value_at_x = tools.eval_func_at_point(func, curr_x)
        if value_at_left * value_at_x < 0:
            # value_at_right = value_at_x
            left, right = left, curr_x
        else:
            value_at_left = value_at_x
            left, right = curr_x, right
        i += 1
