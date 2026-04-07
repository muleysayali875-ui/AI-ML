## Day 3 Report

# Setup Status

The development environment is fully set up and functioning correctly. Python, VS Code (with required extensions), and Jupyter Notebook are working as expected. All necessary libraries including NumPy, pandas, matplotlib, and scikit-learn have been installed and verified. Both script execution in VS Code and notebook execution in Jupyter are running without issues.

# Task Inventory
The following tasks were completed today:

 - Created and executed basics.py to implement Python fundamentals (data types, loops, and functions)
 - Implemented a function to calculate minimum, maximum, and average values from a dataset
 - Worked with NumPy to create arrays and perform operations like reshaping and scaling
 - Converted a 1D array into a 2x2 matrix using reshaping
 - Performed vectorized operations on data without using loops
 - Created a data.csv file and added sample dataset
 - Loaded and analyzed the dataset using pandas DataFrame
 - Used functions like head(), describe(), and column-based operations for analysis
 - Launched Jupyter Notebook and created a notebook file for documentation
 - Used Markdown cells to explain concepts and workflow
 - Verified all tasks using the final completion checklist

# Debugging Log
  - Error 1: 'jupyter' is not recognized as an internal or external command
    Solution: Identified it as a PATH issue. Resolved it by running Jupyter using python -m notebook,  which bypasses the PATH dependency.

  - Error 2: "Failed to fetch" error while creating a new notebook
    Solution: Restarted the Jupyter server and installed the kernel using python -m ipykernel install --user. After restarting, the notebook was created successfully.

# Key Insights

Today’s key learning was understanding how data is handled at different levels. Python provides the basic logic, NumPy enables fast numerical operations through vectorization, and pandas simplifies working with structured datasets. Realizing how these tools work together as a pipeline helped in understanding the foundation of data processing in AI.
