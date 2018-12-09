import tools


def process(func, a, b, eps=1e-7):
    fd = tools.derivative(func)
    sd = tools.derivative(fd)
    print("f(x)'=%s" % fd)
    print("f(x)''=%s" % sd)
    va = tools.eval_func_at_point(func, a)
    vb = tools.eval_func_at_point(func, b)
    print("f(%s)=%s, f(%s)=%s" % (a, va, b, vb))
    if abs(va) < eps:
        return a
    if abs(vb) < eps:
        return b
    if va * vb > 0:
        raise tools.MethodError("f(%s)*f(%s)>0" % (a, b))
    prev_x = a if va * tools.eval_func_at_point(sd, a) > 0 else b
    divider = tools.eval_func_at_point(fd, prev_x)
    i = 1
    print("X0=%s" % prev_x)
    while True:
        curr_x = prev_x - tools.eval_func_at_point(func, prev_x) / divider
        print("<%s> X%s=%s" % (i + 1, i, curr_x))
        if abs(prev_x - curr_x) < eps:
            return curr_x
        prev_x = curr_x
        i += 1
