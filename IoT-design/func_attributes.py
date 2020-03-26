def multiplication(a, b = 1) :
    """Return a multiplied by b. """
    return a * b

special_attributes = [
    "__doc__", "__name__", "__qualname__", "__module__",
    "__defaults__", "__code__", "__globals__", "__dict__",
    "__closure__", "__annotations__", "__kwedefaults__",
]

for attribute in special_attributes :
    print(attribute, '->', getattr(multiplication, attribute))