# PyDSmT
The Python implementation of fusion rules in Dezert-Smarandache theory 

## Get started

You can play with the combination rules on the powerset of binary assignments.
```Python
from PyDSmT.BinarySet.BinaryAssignment import BA
from PyDSmT.BinarySet.BAPSCRBasic import conjunctive_rule, disjunctive_rule, Dempsters_rule

a = BA(0.1, 0.2)
b = BA(0.3, 0.2)
c = BA(0.25, 0.7)

print("disjunctive_rule:", disjunctive_rule(a, c))
print("conjunctive_rule:", conjunctive_rule(a, c))
print("Dempsters_rule:", Dempsters_rule(b, c))

# disjunctive_rule: (0.0250, 0.1400, 0.8350, 0.0000)
# conjunctive_rule: (0.2050, 0.6400, 0.0350, 0.1200)
# Dempsters_rule: (0.2905, 0.6757, 0.0338, 0.0000)
```
Or you can define the combination rule first and play with them by multiplication operator:
```Python
from PyDSmT.BinarySet.BinaryAssignment import BA
from PyDSmT.BinarySet.BAPSCRBasic import Dempsters_rule

BA.set_comb_rule(Dempsters_rule)

print("Result:",
      BA(0.1, 0.3) *
      BA(0.5, 0.4) *
      BA(0.2, 0.2) *
      BA(0.6, 0.3) *
      BA(0.8, 0.1) *
      BA(0.7, 0.2) *
      BA(0.6, 0.1) *
      BA(0.01, 0.95))
# Result: (0.6901, 0.3098, 0.0000, -0.0000)
```

## About the project

The python implementation of fusion rules mentioned in:


1. [**Advances and Applications of DSmT for Information Fusion** Collected Works. Volume 2](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.454.6263&rep=rep1&type=pdf)
(*Florentin Smarandache & Jean Dezert Editors*)

2. [**Advances and Applications of DSmT for Information Fusion** Collected Works.](http://fs.unm.edu/DSmT-book1.pdf)
(*Florentin Smarandache & Jean Dezert Editors*)

3. [**Advances and Applications of DSmT for Information Fusion** Collected Works. Volume 3](https://hal.archives-ouvertes.fr/hal-01080187/document)
(*Florentin Smarandache & Jean Dezert Editors*)

4. [**Advances and Applications of DSmT for Information Fusion** Collected Works. Volume 4](https://www.onera.fr/sites/default/files/u523/DSmT-Book4.pdf)
(*Florentin Smarandache & Jean Dezert Editors*)


## TODO

- Properly define the powerset and hyper-powerset of N-elements finite set.
- Properly implement the combination rules on the power sets.
