dict = {
    "brand": "apple",
    "model": "mac book air",
    "year": "2000"
}
dict["colour"] = "red"
print(dict)

dict = {
    "brand": "apple",
    "model": "mac book air",
    "year": "2000"
}
dict.popitem()
print(dict)

# important dictinonary

dict = {
    "name":"viith",
    "age":"22",
}
dict["age"]= "29"
dict.update({"name":"suresh"})
dict.pop("name")
print(dict)