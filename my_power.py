k = 6


def pow_r(k, tk):
    if k == 0:  # exit case
        tk -= 1
        print('%d' % tk)
        return 1
    if k % 2 == 0:  # standard case ① k is even
        tk += 1
        term = pow_r(k / 2, tk)
        return term * term
    else:  # standard case ② k is odd
        tk += 1
        return 2 * pow_r((k - 1), tk)


print('2^k = %d' % pow_r(k, 0))
