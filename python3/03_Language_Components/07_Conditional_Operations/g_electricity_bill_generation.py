# /usr/bin/python3
"""
Purpose: Electricity Board Current Bill Slab rates

    Electricity bill slabs
    -------------------------------------
    units Range     |    amount per unit
	-------------------------------------
    0 till 60       |   1.25
	60 till 100     |   2.00
	100 till 150    |   4.00
	150 till 250    |   7.00
	250 +           |  10.00

electricity cess : 2%
discount         : -1.11%

GST              : 7%

units consumed : 357
         60     +   40      + 50    + 100    + 107
         1.25/- + 2.00/-    + 4.00/-+ 7.00/- + 10/-

"""
import sys

# units_consumed = 357
units_consumed = float(input("Enter the no. of units consumed:").strip())

if units_consumed < 0:
    print("INVALID INPUT")
    sys.exit(1)

amount = 0
remaining_units = units_consumed
if units_consumed > 250:
    slab_units = remaining_units - 250
    amount += slab_units * 10.0
    print(
        f"""
            units consumed  : {remaining_units}
            slab units      : {slab_units}
        """
    )
    remaining_units -= slab_units

if 150 < remaining_units <= 250:
    slab_units = remaining_units - 150
    amount += slab_units * 7.0
    print(
        f"""
        units consumed  : {remaining_units}
        slab units      : {slab_units}
    """
    )
    remaining_units -= slab_units

if 100 < remaining_units <= 150:
    slab_units = remaining_units - 100
    amount += slab_units * 4.0

    print(
        f"""
        units consumed  : {remaining_units}
        slab units      : {slab_units}
    """
    )
    remaining_units -= slab_units

if 60 < remaining_units <= 100:
    slab_units = remaining_units - 60
    amount += slab_units * 2.0

    print(
        f"""
        units consumed  : {remaining_units}
        slab units      : {slab_units}
    """
    )
    remaining_units -= slab_units

if 0 <= remaining_units <= 60:
    slab_units = 60  # minimum charge
    amount += slab_units * 1.25

    print(
        f"""
        units consumed  : {remaining_units}
        slab units      : {slab_units}
    """
    )


# NOTE: Prefer to use if-Guarded clause to make code syntax simple
