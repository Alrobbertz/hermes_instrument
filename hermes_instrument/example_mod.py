__all__ = ['primes', 'do_primes', 'area_of_rectangle']
import astropy.units as u

def primes(imax):
    """
    Returns prime numbers up to imax.

    Parameters
    ----------
    imax: int
        The number of primes to return. This should be less or equal to 10000.

    Returns
    -------
    result: list
        The list of prime numbers.

    Examples
    --------
    >>> from ..example_mod import primes
    >>> primes(10)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    """

    p = list(range(10000))
    result = []
    k = 0
    n = 2

    if imax > 10000:
        raise ValueError("imax should be <= 10000")

    while len(result) < imax:
        i = 0
        while i < k and n % p[i] != 0:
            i = i + 1
        if i == k:
            p[k] = n
            k = k + 1
            result.append(n)
            if k > 10000:
                break
        n = n + 1

    return result


def do_primes(n, usecython=False):
    if usecython:

        raise Exception("This template does not have the example C code included.")

    else:
        print('Using pure python primes')
        return primes(n)


@u.quantity_input
def area_of_rectangle(width: u.cm, height: u.cm) -> u.m**2:
    """
    Calculate the area of a rectangle.

    Parameters
    ----------
    width : `~astropy.units.Quantity`
       The width of the rectangle.
    height : `~astropy.units.Quantity`
       The height of the rectangle.

    Returns
    -------
    `~astropy.units.Quantity`
       The area of the rectangle.

    Examples
    --------
    >>> import astropy.units as u
    >>> from ..example_mod import area_of_rectangle
    >>> area_of_rectangle(5 * u.km, 10 * u.km)
    <Quantity 50000000. m2>
    """
    return width * height


def main(args=None):

    from astropy.utils.compat import argparse
    from time import time

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-c', '--use-cython', dest='cy', action='store_true',
                        help='Use the Cython-based Prime number generator.')
    parser.add_argument('-t', '--timing', dest='time', action='store_true',
                        help='Time the Fibonacci generator.')
    parser.add_argument('-p', '--print', dest='prnt', action='store_true',
                        help='Print all of the Prime numbers.')
    parser.add_argument('n', metavar='N', type=int,
                        help='Get Prime numbers up to this number.')

    res = parser.parse_args(args)

    pre = time()
    primes = do_primes(res.n, res.cy)
    post = time()

    print('Found {0} prime numbers'.format(len(primes)))
    print('Largest prime: {0}'.format(primes[-1]))

    if res.time:
        print('Running time: {0} s'.format(post - pre))

    if res.prnt:
        print('Primes: {0}'.format(primes))