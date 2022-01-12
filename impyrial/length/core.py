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