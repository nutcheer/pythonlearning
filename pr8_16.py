import printing_functions 
printing_functions.show_completed_models("1")

from printing_functions import show_completed_models
show_completed_models("2")

from printing_functions import show_completed_models as p1
p1("3")

import printing_functions as p2
p2.show_completed_models("4")

from printing_functions import *
show_completed_models("5")
