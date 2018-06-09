#!/usr/bin/python
"""
Purpose: Boolean Operations
"""
## bool()
# integer type (int, long and float)
#       zero     - False 
#       non-zero - True
print "bool(12)", bool(12)
print "bool(-12)", bool(-12)
print "bool(0)", bool(0)

print "bool(0.00)", bool(0.00)
print "bool(0.000000001)", bool(0.000000001)
print "bool(-0.000000001)", bool(-0.000000001)


# strings
#  True - non-empty string 
#  False - empty string
true = 'Udhay Prakash'  # NOT RECOMMENDED to use 'true' for variable name
print "true", true
print "bool(true)", bool(true)
print "bool('ball')", bool('ball')
print "bool('')", bool('') # empty string
print "bool(' ')", bool(' ')  # white-space

# [], (), {}
print '(1)', bool((1))
print '(1,)', bool((1,))
print '[1]', bool([1])
print '{1}', bool({1})
print '{1:2}', bool({1:2})

print '()', bool(())
print '[]', bool([])
print '{}', bool({})
