tulip_summary = ("chennai", "Bangalore", "43.42", "oneway", "Indigo", "Indigo")
print(tulip_summary)
print("\n")

print(tulip_summary[2])
print("\n")

for value in tulip_summary:
    print(value)
print("\n")

print(len(tulip_summary))
print(tulip_summary.count("Indigo"))
print(tulip_summary.index("oneway"))

#tulip_summary[1] = "India"
print("\n")

for i, location in enumerate(tulip_summary):
    print(i, location)

unique_tulip = set(tulip_summary)
print(unique_tulip)

city_set1 = {"chennai", "chennai", "Bangalore", "Hyderabad" }
city_set2 = {"Trivandrum", "Coimbatore", "Tirupur", "chennai" }

print("\n")
print(city_set1)
print(city_set2)
print(city_set1.union(city_set2))
print(city_set1.intersection(city_set2))
#print(city_set1.intersection_update(city_set2))
print(city_set1.difference(city_set2))
print(city_set2.difference(city_set1))

print(city_set1.add("cuddalore"))
print(city_set1.union(city_set2))

city_set1.remove("cuddalore")
city_set1.discard("australia")
print(city_set1.union(city_set2))

#print(city_set1[0])






