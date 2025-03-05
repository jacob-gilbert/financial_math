########################################
# Simple Interest
def simple_interest(pv, i, t):
    """
    Returns the future value given the present value, simple interest rate, and number of time periods
    """
    return pv * (1 + i * t)

def simple_interest_i(pv, fv, t):
    """
    Returns the simple interest rate given the present value, future value, and number of time periods
    """
    return ((fv / pv) - 1) / t

def simple_interest_t(pv, fv, i):
    """
    Returns the number of time periods given the present value, future value, and number of simple interest rate
    """
    return ((fv / pv) - 1) / i

def simple_interest_pv(fv, i, t):
    """
    Returns the present value given the future value, simple interest rate, and number of time periods
    """
    return (fv / (1 + i * t))


# Simple Discount
def simple_discount(fv, d, t):
    """
    Returns the future value given the present value, simple discount rate, and number of time periods
    """
    return fv * (1 - d * t)

def simple_discount_d(fv, pv, t):
    """
    Returns the simple discount rate given the future value, present value, and number of time periods
    """
    return (1 - (pv / fv)) / t

def simple_discount_t(pv, fv, d):
    """
    Returns the number of time periods given the present value, future value, and simple discount rate
    """
    return (1 - (pv / fv)) / d

def simple_discount_fv(pv, d, t):
    """
    Returns the present value given the future value, simple discount rate, and number of time periods
    """
    return (pv / (1 - d * t))

# Conversions simple interest <--> simple discount
def simp_i_to_d(i, t):
    """
    Returns the simple discount rate when given the simple interest rate and number of time periods
    """
    return i / (1 + i * t)

def simp_d_to_i(d, t):
    """
    Returns the simple interest rate when given the simple discount rate and number of time periods
    """
    return d / (1 - d * t)


# effective interest rate
def eir(av1, av2):
    """
    Returns the effective interest rate when given the accumulated value of one time period and the next
    """
    return (av2 - av1) / av1

def eir_i(pv, i, t):
    """
    Returns the effective interest rate when given the present value, the simple interest rate, and the time period to take the rate
    """
    return eir(simple_interest(pv, i, t - 1), simple_interest(pv, i, t))


 ########################################
 # Compount Interest