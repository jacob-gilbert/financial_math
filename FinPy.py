import math

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
    return ((fv / pv) - 1) / t - 1

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
def compound_av(pv, i, t):
    """
    Returns the accumulated value when given the present value, the compound interest rate, and the number of time periods
    """
    return pv * ((1 + i) ** t)

def compound_pv(fv, i, t):
    """
    Returns the future value when given the accumulated value, the compound interest rate, and the number of time periods
    """
    return fv / ((1 + i) ** t)

def compound_i(pv, fv, t):
    """
    Returns the compound interest rate when given the present value, accumulated value, and the number of time periods
    """
    return ((fv / pv) ** (1 / t)) - 1

def compound_t(pv, fv, i):
    """
    Returns the number of time periods when given the present value, accumulated value, and the compound interest rate
    """
    return (math.log(fv / pv) / math.log(1 + i))


# Present value factors for interest and discount rates
def pvf_int(i, t):
    """
    returns the present value factor for a given interest rate and a number of time periods
    """
    return (1 / (1 + i)) ** t

def pvf_dis(d, t):
    """
    returns the present value factor for a given discount rate and a number of time periods
    """
    return (1 - d) ** t


# Future value factors for interest and discount rates
def fvf_int(i, t):
    """
    returns the future value factor for a given interest rate and a number of time periods
    """
    return (1 + i) ** t

def fvf_dis(d, t):
    """
    returns the future value factor for a given interest rate and a number of time periods
    """
    return (1 / (1 - d)) ** t

# Conversions between compound interest and discount
def comp_i_d(i):
    """
    returns the conversion from compound interest rate to compound discount rate
    """
    return 1 + pvf_int(i, 1)

def comp_d_i(d):
    """
    returns the conversion from compound discount rate to compound interest rate
    """
    return (1 / (1 - d)) - 1


########################################
# Mthly Interest
def mthly_comp(i, i_comp_times, new_comp_times):
    """
    returns the conversion from our effective interest rate to mthly interest rate
    """
    i_eff = (1 + i / i_comp_times) ** i_comp_times - 1
    return new_comp_times * ((1 + i_eff) ** (1 / new_comp_times) - 1)

def mthly_fv(pv, i, t, m):
    """
    returns the future value of an investment compounded mthly
    """
    return pv * ((1 + i / m) ** (t * m))

def mthly_pv(fv, i, t, m):
    """
    returns the present value of an investment compounded mthly
    """
    return fv / ((1 + i / m) ** (t * m))

def mthly_i(pv, fv, t, m):
    """
    returns the interest of an investment compounded mthly
    """
    return (((fv / pv) ** (1 / (m * t))) - 1) * m

def mthly_t(pv, fv, i, m):
    """
    returns the times periods of an investment compounded mthly
    """
    return math.log(fv/pv) / math.log(1 + i / m)


########################################
# Level Annuities
def level_annuity_due_pvf(i, n):
    return (1 - (1 + i) ** -n) / (i / (1 + i))

def level_annuity_due_pv(x, i, n):
    return x * level_annuity_due_pvf(i, n)

def level_annuity_due_pymnt_amnt_pv(pv, i, n):
    return pv / level_annuity_due_pvf(i, n)

def level_annuity_due_num_pymnts_pv(pv, i, x):
    return -math.log(1 - ((i / (1 + i)) * pv) / x) / math.log(1 + i)


def level_annuity_due_fvf(i, n):
    return ((1 + i) ** n) / (i / (i + 1))

def level_annuity_due_fv(x, i, n):
    return x * level_annuity_due_fvf(i, n)

def level_annuity_due_pymnt_amnt_fv(fv, i, n):
    return fv / level_annuity_due_fvf(i, n)

def level_annuity_due_num_pymnts_fv(fv, i, x):
    return math.log(1 + ((i / (1 + i)) * fv) / x) / math.log(1 + i)


def level_annuity_imm_pvf(i, n):
    return (1 - (1 + i) ** -n) / i

def level_annuity_imm_pv(x, i, n):
    return x * level_annuity_imm_pvf(i, n)

def level_annuity_imm_pymnt_amnt(pv, i, n):
    return pv / level_annuity_imm_pvf(i, n)

def level_annuity_imm_num_pymnts(pv, i, x):
    return -math.log(1 - (i * pv) / x) / math.log(1 + i)


def level_annuity_imm_fvf(i, n):
    return ((1 + i) ** n) / i

def level_annuity_imm_fv(x, i, n):
    return x * level_annuity_imm_fvf(i, n)

def level_annuity_imm_pymnt_amnt_fv(fv, i, n):
    return fv / level_annuity_imm_fvf(i, n)

def level_annuity_imm_num_pymnts_fv(fv, i, x):
    return math.log(1 + (i * fv) / x) / math.log(1 + i)


def level_annuity_cont_pvf(i, n):
    return (1 - (1 + i) ** -n) / math.log(1 + i)

def level_annuity_cont_pv(x, i, n):
    return x * level_annuity_cont_pvf(i, n)

def level_annuity_cont_pymnt_amnt(pv, i, n):
    return pv / level_annuity_cont_pvf(i, n)

def level_annuity_cont_num_pymnts(pv, i, x):
    return -math.log(1 - (math.log(1 + i) * pv) / x) / math.log(1 + i)


def level_annuity_cont_fvf(i, n):
    return ((1 + i) ** n) / i

def level_annuity_cont_fv(x, i, n):
    return x * level_annuity_cont_fvf(i, n)

def level_annuity_cont_pymnt_amnt_fv(fv, i, n):
    return fv / level_annuity_cont_fvf(i, n)

def level_annuity_cont_num_pymnts_fv(fv, i, x):
    return math.log(1 + (i * fv) / x) / math.log(1 + i)

########################################
# Level Perpetuities
def perp_due(d):
    return 1 / d

def perp_imm(i):
    return 1 / i

def perp_cont(i):
    return 1 / math.log(1 + i)


########################################
# Varying Annuities
def inc_annuity_due_pv(x, i, n):
    return x * (level_annuity_due_pvf(i, n) - n * ((1 + i) ** -n)) / (i / (1 + i))

def inc_annuity_imm_pv(x, i, n):
    return x * (level_annuity_due_pvf(i, n) - n * ((1 + i) ** -n)) / i

def inc_annuity_cont_pv(x, i, n):
    return x * (level_annuity_due_pvf(i, n) - n * ((1 + i) ** -n)) / math.log(1 + i)


def inc_annuity_due_fv(x, i, n):
    return x * (level_annuity_due_fvf(i, n) - n) / (i / (1 + i))

def inc_annuity_imm_fv(x, i, n):
    return x * (level_annuity_due_fvf(i, n) - n) / i

def inc_annuity_cont_fv(x, i, n):
    return x * (level_annuity_due_fvf(i, n) - n) / math.log(1 + i)


def dec_annuity_due_pv(x, i, n):
    return x * (n - level_annuity_imm_pvf(i, n)) / (i / (1 + i))

def dec_annuity_imm_pv(x, i, n):
    return x * (n - level_annuity_imm_pvf(i, n)) / i

def dec_annuity_cont_pv(x, i, n):
    return x * (n - level_annuity_imm_pvf(i, n)) / math.log(1 + i)


def dec_annuity_due_fv(x, i, n):
    return x * (n * (1 + i) ** n - level_annuity_imm_fvf(i, n)) / (i / (1 + i))

def dec_annuity_imm_fv(x, i, n):
    return x * (n * (1 + i) ** n - level_annuity_imm_fvf(i, n)) / i

def dec_annuity_cont_fv(x, i, n):
    return x * (n * (1 + i) ** n - level_annuity_imm_fvf(i, n)) / math.log(1 + i)

########################################
# Varying Perpetuities
def inc_perp(i):
    return ((1 + i) ** 2) / i