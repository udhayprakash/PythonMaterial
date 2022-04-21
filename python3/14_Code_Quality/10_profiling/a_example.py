#!/usr/bin/python3
"""
ncalls : Shows the number of calls made

tottime: Total time taken by the given function. Note that the time made in calls to sub-functions are excluded.

percall: Total time / No of calls. ( remainder is left out )

cumtime: Unlike tottime, this includes time spent in this and all subfunctions that the higher-level function calls. It is most useful and is accurate for recursive functions.

The percall following cumtime is calculated as the quotient of cumtime divided by primitive calls. The primitive calls include all the calls that were not included through recursion.

"""

import cProfile
cProfile.run("20+10")

statement = "20+10"
cProfile.run(statement, filename=None, sort=-1)