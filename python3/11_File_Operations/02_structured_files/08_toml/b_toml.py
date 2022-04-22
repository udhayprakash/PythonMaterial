import numpy as np
import toml

a = np.arange(0, 10, dtype=np.double)
output = {"a": a}
print(f"{output    = }")
# 'a = [ "0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "9.0",]\n'

toml_str = toml.dumps(output)
print(f"{toml_str  = }")

toml_str2 = toml.dumps(output, encoder=toml.TomlNumpyEncoder())
print(f"{toml_str2 = }")
# 'a = [ 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0,]\n'
