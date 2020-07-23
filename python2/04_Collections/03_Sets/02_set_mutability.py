#####################
# set is mutable but can store 
# immutables only 


empty_set =  set() 
print type(empty_set)

small_set = set([12, 3242, 45])
print type(small_set)
print small_set

small_set = {12, 3242, 45}
print type(small_set)
print small_set

print 'small_set.pop()', small_set.pop()
print 'small_set', small_set

set_with_one_ele = {12}
print type(set_with_one_ele)
print
print 'set_with_one_ele', set_with_one_ele
set_with_one_ele.discard(12)
print 'set_with_one_ele', set_with_one_ele
print

print 'set_with_one_ele', set_with_one_ele
set_with_one_ele.discard(12)
print 'set_with_one_ele', set_with_one_ele



#############
# frozenset ---- immutable object

veto_countries = frozenset({'France', 'US', 'UK', 'China', 'Russia'})
print 'type(veto_countries)', type(veto_countries)
print veto_countries

print dir(veto_countries)
# veto_countries.add('China')
# AttributeError: 'frozenset' object has no attribute 'add'
hybrid_set = {12, 23.5, 'tomoto', (12,), frozenset(small_set)}
                    # , small_set --- TypeError: unhashable type: 'set'
print 'type(hybrid_set)', type(hybrid_set)
print hybrid_set
