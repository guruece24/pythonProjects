
trip = {
            "id":              1323,
            "origin":         "chennai",
            "destination":     ["delhi","Koodalayathur","Kurinjipaadi"],
            "type":           "Oneway",
            "fare":            2342.00,
            "payment":        "creditcard",
            "isHotelsBooked": "no",
            "id":              1323534,
}

print(trip)
print(trip["fare"])
print(trip.get("payment"))
print("destination_get_one : ", trip.get("destination")[0])

print(trip.keys())
print(trip.values())

trip.update({"origin":"Bangalore", "type":"Roundtrip"})
print("\nAfterUpdte")
for key,value in trip.items():
    print(key, " : ", value)

trip.pop("isHotelsBooked")
print("\nAfterPop")
for key,value in trip.items():
    print(key, " : ", value)

for i, location in enumerate(trip.get("destination")):
    print(i, location)


tripDetailsArray =[ {
            "id":              1323,
            "origin":         "chennai",
            "destination":     ["delhi","Koodalayathur","Kurinjipaadi"],
            "type":           "Oneway",
            "fare":            2342.00,
            "payment":        "creditcard",
            "isHotelsBooked": "no",
            "id":              1323534,
},{
            "id_1":              1323,
            "origin_1":         "chennai",
            "destination_1":     ["delhi","Koodalayathur","Kurinjipaadi"],
            "type_1":           "Oneway",
            "fare_1":            2342.00,
            "payment_1":        "creditcard",
            "isHotelsBooked_1": "no",
            "id_1":              5354535,
}
    ]

print("\nJsonArray")
print(tripDetailsArray[1].get("id_1"))

tripDetailsObject ={
    "one": {
            "id":              1323,
            "origin":         "chennai",
            "destination":     ["delhi","Koodalayathur","Kurinjipaadi"],
            "type":           "Oneway",
            "fare":            2342.00,
            "payment":        "creditcard",
            "isHotelsBooked": "no",
            "id":              1323534,
},
    "two": {
            "id_1":              1323,
            "origin_1":         "chennai",
            "destination_1":     ["sozhathiram","irumbulikurichi","pazhani"],
            "type_1":           "Oneway",
            "fare_1":            2342.00,
            "payment_1":        "creditcard",
            "isHotelsBooked_1": "no",
            "id_1":              5354535,
}
    }

print("\nJsonObject")
print(tripDetailsObject.get("one").get("destination"))
print(tripDetailsObject.get("two").get("destination_1"))
print(tripDetailsObject.get("two").get("destination_1")[0])
