from PyDSmT.BinarySet.BinaryAssignment import BA
from PyDSmT.BinarySet.BAPSCRBasic import conjunctive_rule, disjunctive_rule, Dempsters_rule

# Part 1
a = BA(0.1, 0.2)
b = BA(0.3, 0.2)
c = BA(0.25, 0.7)

print(disjunctive_rule(a, c))
print(conjunctive_rule(a, c))
print(Dempsters_rule(b, c))

# Part 2
BA.set_comb_rule(Dempsters_rule)
print(BA(0.1, 0.3) *
      BA(0.5, 0.4) *
      BA(0.2, 0.2) *
      BA(0.6, 0.3) *
      BA(0.8, 0.1) *
      BA(0.7, 0.2) *
      BA(0.6, 0.1) *
      BA(0.01, 0.95))
