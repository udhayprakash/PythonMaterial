import functools
import urllib.error
import urllib.request


@functools.lru_cache(maxsize=32)
def get_pep(num):
    """Retrieve text of a Python Enhancement Proposal"""
    resource = "http://www.python.org/dev/peps/pep-%04d/" % num
    try:
        with urllib.request.urlopen(resource) as s:
            return s.read()
    except urllib.error.HTTPError:
        return "Not Found"


for n in (8, 290, 308, 320, 8, 290, 308, 320, 9991):
    pep = get_pep(n)
    print(f"PEP {n:4} {len(pep)}")

print(get_pep.cache_info())
# LRU cache should only be used when you want to reuse previously computed values
