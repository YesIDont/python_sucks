wanted_list = ["Luke Skylwaker", "Yoda", "Obi-Wan Kenobi", "Hans Solo", "Leia Organa", "Mace Windu"]


print(wanted_list)
print(wanted_list[0])
print(wanted_list[-1])

# get elements from specified index (inclusive)
print(wanted_list[1:])
# grab range, first inclusive, last exclusive
sits_in_car = 2
print(wanted_list[1:sits_in_car + 1])

dark_lords = ["Sidious", "Kylo Ren"]

dark_lords.append("Snoke")
print(dark_lords)

dark_lords.insert(1, "Vader")
print(dark_lords)

dark_lords.remove("Kylo Ren")
print(dark_lords)

wanted_list.extend(dark_lords)
print(wanted_list)

dark_lords.clear()
print(dark_lords)

print(wanted_list.pop())

# get the number of elements matching value
jedi = ["Yoda", "Luke", "Yoda", "Obi-Wan", "Yoda"]
print(jedi.count("Yoda"))

jedi_2 = jedi.copy()
jedi_2.reverse()
jedi_2.sort()
print(jedi_2)

