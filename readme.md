Clusterfudge Client Library
===========================


## How to Build and Distribute (for fudgeneers)
0. `pip install twine` or delete the current contents of `./dist/*`
1. Incr version number in setup.py
2. Build `python3 -m build`
3. Upload using twine `twine upload dist/*` (using your PiPy API token)