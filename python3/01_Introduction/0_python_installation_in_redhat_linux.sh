#!/bin/bash

# Set Python version as a constant variable
PYTHON_VERSION="3.10.2"

# Update packages
sudo yum update -y

# Install required packages
sudo yum install -y gcc openssl-devel bzip2-devel libffi-devel wget

# Download and extract Python source
wget https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz
tar xzf Python-$PYTHON_VERSION.tgz
cd Python-$PYTHON_VERSION

# Configure and install Python
./configure --enable-optimizations
sudo make altinstall

# Install pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python$PYTHON_VERSION get-pip.py

# Clean up
cd ..
sudo rm -rf Python-$PYTHON_VERSION Python-$PYTHON_VERSION.tgz
