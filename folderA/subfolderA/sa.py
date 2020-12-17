import sys


print(
"""
Depending on which script you call
the following print will show different paths.

Wether you call this script (sa.py) directly or through an import
will make a difference in the available import paths for sa.py

These are the paths available right now:

=======================================================================

""")
print(sys.path)

print(
"""

=======================================================================

"""
)

# 
# import sa_sibling

try:
    import sa_sibling
except ModuleNotFoundError as error:
    print("ModuleNotFoundError:", error)
import start_sibling