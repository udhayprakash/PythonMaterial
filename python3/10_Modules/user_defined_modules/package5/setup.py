from setuptools import find_packages, setup

setup(
    name="ops",
    version="1.0.0",
    description="A package for math operations",
    packages=find_packages(),
    install_requires=[],  # Add any dependencies here
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
