# Simple Interest
def simple_interest(pv, i, t):
    return pv * (1 + i * t)

def simple_interest_i(pv, fv, t):
    return ((fv / pv) - 1) / t

def simple_interest_t(pv, fv, i):
    return ((fv / pv) - 1) / i

def simple_interest_pv(fv, i, t):
    return (fv / (1 + i * t))


# Simple Discount
def simple_discount(fv, d, t):
    return fv * (1 - d * t)

def simple_discount_d(fv, pv, t):
    return (1 - (pv / fv)) / t

def simple_discount_t(pv, fv, d):
    return (1 - (pv / fv)) / d

def simple_discount_fv(pv, d, t):
    return (pv / (1 - d * t))


def simp_i_to_d(i, t):
    return i / (1 + i * t)

def simp_d_to_i(d, t):
    return d / (1 - d * t)