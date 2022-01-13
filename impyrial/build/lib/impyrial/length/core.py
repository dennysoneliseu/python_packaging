'''
Conversions between inches and 
larger imperial length units
'''
INCHES_POR_FOOT = 12.0 # 12 inches in a foot
INCHES_PER_YARD = INCHES_POR_FOOT * 3.0 # 3 feet in a yart

UNITS = ("in", "ft", "yd")

def inches_to_feet(x, reverse = False):
    """Convert lengths between inches and feet

    Parameters
    ----------
    x : numpy.ndarray
        Lengths in feet.

    reverse : bool, optional
         If true this function converts froom feet to inches
         instead of the default behavior of inches to feet.
         (Default value = False)

    Returns
    -------
    numpy.ndarray

    """
    if reverse:
        return x * INCHES_POR_FOOT
    else:
        return x / INCHES_POR_FOOT

def inches_to_yards(x, reverse=False):
    """Convert lengths between inches and yards.

    Parameters
    ----------
    x : array_like
        Lengths in feet.
    reverse : bool, optional
        If this is set to true this function converts from yards to inches
        instead of the default behaviour of inches to yards.

    Returns
    -------
    ndarray
        An array of converted lengths with the same shape as `x`. If `x` is a
        0-d array, then a scalar is returned.
    """
    if reverse:
        return x * INCHES_PER_YARD
    else:
        return x / INCHES_PER_YARD