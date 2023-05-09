#  уникальные значения
test_list = {"V": "S001", "V": "S002", "VI":"S001", "VI":"S005",}
# res = list(set(val for dic in test_list for val in dic.values()))
res = set()
for value in test_list.values():
    res.add(value)
print(res)
