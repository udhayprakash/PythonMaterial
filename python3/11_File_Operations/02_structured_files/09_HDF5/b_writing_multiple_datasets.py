"""
Purpose: Writing Multiple datasets to hdf5 file
"""

import h5py

with h5py.File("b_file.hdf5", "w") as f:
    f.create_dataset("ints", (100,), dtype="i8")
    f.create_dataset("list_ds", data=[1, 2, 3, 4])
    f.create_dataset("tuple_ds", data=(1, 2, 3, 4))

    # f.create_dataset('set_ds', data={1, 2, 3, 4})
    # f.create_dataset('dict_ds', data={1: 2, 3: 4})
    # TypeError: Object dtype dtype('O') has no native HDF5 equivalent

    print(f"{list(f.keys()) =}")


# ref - https://docs.h5py.org/en/stable/quick.html
