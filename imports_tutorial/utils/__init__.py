#turns our folder utils into a package :)

# utils/__init__.py (incorrect way of importing)

# from .length import get_length
# from .lower import to_lower
# from .upper import to_upper

#We use the dot notation( . or ..) in specifying
#  relative imports. The single dot before 
# lower refers to the same directory as the 
# one from which the import is called. 
# This can be visualized as importing 
# to_lower() from ./lower.py. 
# Similarly, double dots before a module 
# name means moving up two levels from the 
# current level.

from utils.length import get_length
from utils.lower import to_lower
from utils.upper import to_upper

from scripts.example1 import yolo

# absolute imports (above) pack more info and 
# much less prone to breaking