from AttrDict import AttrDict


dictionary = {
  "entry": "entry_1",
  "another_dictionary": {
                          "entry_2": "entry_2"
  },
  "a_list": [
            ],
  "a_list_with_a_dictionary": [
                                {
                                  "entry_3": "entry_3"
                                }
                              ]

}

x = AttrDict(dictionary)
# try to get the entry
print(x.entry)
print(x["entry"])
# try to get the dictionary in the entry another_dictionary
print(x.another_dictionary)
# try to get the entry 'entry 2' from the dictionary entry another_dictionary
print(x.another_dictionary.entry_2)
# try to get the list a_list
print(x.a_list)
# try to get the dictionary in the entry a_list_with_a_dictionary
print(x.a_list_with_a_dictionary[0].entry_3)

# get the dictionaries using the index
print(x["entry"])
print(x["another_dictionary"])
print(x["another_dictionary"]["entry_2"])
print(x["a_list"])
print(x["a_list_with_a_dictionary"][0]["entry_3"])

# Create an AttrDict without passing in a dictionary
x = AttrDict()
x.entry = "entry"
# get the value of the entry by indexing it or getting it as an attribute
print(x["entry"])
print(x.entry)
