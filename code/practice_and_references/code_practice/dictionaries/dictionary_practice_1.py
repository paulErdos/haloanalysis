from subprocess import call
call(["clear"])

dictionary = { 
  "key0": "value0",
  "key1": "vaule1"
}

print dictionary.items()
print dictionary.keys()
print dictionary.values()

dictionary2 = {
  "key0": "value0",
  "key1": "vaule1"
}

dictionary_list = [dictionary, dictionary2]

key0 = 0
key1 = 1

for dict in dictionary_list:
  for item in dict.items():
    if item[key0] == "value0":
      print item[1]


