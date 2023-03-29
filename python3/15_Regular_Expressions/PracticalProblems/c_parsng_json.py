import re

payload_str = """{
	"a": {
		"a1": {
			"b0": "someyo",
			"b1": {
				"c1": "car"
			},
			"test":"name",
		}
	},
	"b": {
	}

}"""
# create pattern
pattern = r""
for each_node in "a/a1/b1/c1".split("/"):
    pattern += each_node + ".+"
pattern = pattern.rstrip("+") + ":(.*?)\n.+"

print("pattern=", pattern)  # 'a.+a1.+b1.+c1.:(.*?)\n.+'
print("result=", re.search(pattern, payload_str, re.DOTALL).group(1))  # "car"
