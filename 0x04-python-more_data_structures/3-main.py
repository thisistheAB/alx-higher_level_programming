#!/usr/bin/python3
common_elements = __import__('3-common_elements').common_elements

set_1 = {"Python", "C", "Javascript", "Nancy", "89"}
set_2 = {"Bash", "C", "Ruby", "Perl", "Nancy", "89"}
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))