#  %-formatting strings .format or f''

x = 2
print("I'm going to place a %d instead of %%d in formatting string" % x)
print("We can do the same thing with format function of a string {0}".format(x))
print("Or you can use name instead of position like {name}".format(name=x))
print(f"what do you think about this new style from py3.6: {x**2:02d}")
raise ValueError(f"Expected {x!r} to be a float not a {type(x).__name__}")
