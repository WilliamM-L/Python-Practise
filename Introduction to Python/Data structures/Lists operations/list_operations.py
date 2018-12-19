animals = ['elephant', 'lion', 'tiger', "giraffe"]  # create new list
print(animals)

animals += ["monkey", 'dog']    # add two items to the list
print(animals)

animals.append("dino")   # add one more item to the list using append() method
print(animals)
# elements added are always found at the end
# hence, using the address -1 is a good idea
animals[-1] = "dinosaur"
print(animals)
