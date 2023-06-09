import functools
import urllib.error
from urllib.request import urlopen


@functools.lru_cache(maxsize=32)
def get_pep(pep_number):
    URL = f"https://peps.python.org/pep-{pep_number:04}/"
    # print(f"{URL =}")
    try:
        res = urlopen(URL)
        # print(res)
        # print(res.read())
        return res.read()
    except urllib.error.HTTPError as ex:
        print(f"Given URL: {URL} is Not Found")
        return ""
    except Exception as ex:
        print(repr(ex))
        return ""


for n in (8, 290, 308, 320, 8, 290, 308, 320, 9991):
    pep = get_pep(n)
    print(f"PEP {n:4} {len(pep)}")

print()
print(get_pep.cache_info())
# LRU cache should only be used when you want to reuse previously computed values
