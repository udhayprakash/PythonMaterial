"""
Purpose: Serialization with HDF5

    - Hierarchical Data Format 5 (HDF5) is a binary data format.
    - Helps to store huge amounts of numerical data, and easily manipulate
      that data from Numpy.
    - Multiple Objects/datasets can be stored/retrieved from same hdf5 file

    pip install -U h5py h5pyViewer
"""
import h5py

# Creating new file
fh = h5py.File("a_example.hdf5", "w")
print(list(fh.keys()))  # []
print()

# Adding dataset to it
dset = fh.create_dataset("default", data=[1, 2, 3, 4])
print(list(fh.keys()))  # ['default']
print()

# Reading data from the hdf5 file
with h5py.File("a_example.hdf5", "r") as f:
    data = f["default"]

    print(
        f"""
        {data       =}
        {type(data) =}
        {min(data) =}
        {max(data) =}
        {data[:15] =}
    """
    )


# dset = f.create_dataset("mydataset", (100,), dtype='i')


# with h5py.File("test.hdf5", "w") as file:
#     dataset = file.create_dataset("test_dataset", (100,)) # , type="i4"
