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

units_consumed = 357

if units_consumed < 0:
    print("INVALID INPUT")
    sys.exit(0)

# Method 1
if 0 < units_consumed < 60:
    billable_amount = units_consumed * 1.25
elif 0 < units_consumed < 100:
    remaining_units  = units_consumed - 60
    billable_amount = 60 * 1.25 + remaining_units * 2.00
elif 0 < units_consumed < 150:
    remaining_units  = units_consumed - 60 - 40
    billable_amount = 60 * 1.25 +  40 * 2.00 + remaining_units * 4.00
elif 0 < units_consumed < 250:
    remaining_units  = units_consumed - 60 - 40 - 50
    billable_amount = 60 * 1.25 +  40 * 2.00 + 50 * 4.00 + remaining_units * 7.00
elif units_consumed > 250:
    remaining_units  = units_consumed - 60 - 40 - 50 - 100
    billable_amount = 60 * 1.25 +  40 * 2.00 + 50 * 4.00 + 100 * 7.00 + remaining_units * 10.00

print(f"""
            units consumed  : {units_consumed}
            Amount          : {billable_amount}
        """)


# Method 2

amount = 0
remaining_units = units_consumed

if units_consumed > 250:
    slab_units = remaining_units - 250
    amount += slab_units * 10.0
    remaining_units -= slab_units

if 150 < remaining_units <= 250:
    slab_units = remaining_units - 150
    amount += slab_units * 7.0
    remaining_units -= slab_units

if 100 < remaining_units <= 150:
    slab_units = remaining_units - 100
    amount += slab_units * 4.0
    remaining_units -= slab_units

if 60 < remaining_units <= 100:
    slab_units = remaining_units - 60
    amount += slab_units * 2.0
    remaining_units -= slab_units

if 0 <= remaining_units <= 60:
    slab_units = 60  # minimum charge
    amount += slab_units * 1.25


print(f"""
            units consumed  : {units_consumed}
            Amount          : {billable_amount}
        """)


# NOTE: Prefer to use if-Guarded clause to make code syntax simple
