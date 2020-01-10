#!/usr/bin/python
"""
Purpose: String formatting - timeit

f'{s} {t}'                              # 782.ns
s + ' ' + t                             # 104 ns
' '.join((s,t))                         # 135 ns
'%s %s'%(s,t)                           # 188 ns
'{} {}'.format(s,t)                     # 283 ns
Template('$s $t').substitute(s=s, t=t)  # 898 ns
"""
