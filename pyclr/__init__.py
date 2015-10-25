from .pyclr import finished_styles
from .maps import rainbow, america, zebra, random

for style in finished_styles:
    globals()[style] = finished_styles[style]
