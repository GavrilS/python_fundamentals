# We have a few different types of operators we can overload. Most important:
    - unary: +, -, ~(invert)
    * methods: __add__, __mul__, __radd__, __rmul__...
    - rich comparison operators: ==, !=, >, <...
    * methods: __eq__, __ne__, __gt__, __lt__...
    - augmented assignment operators: +=, *=, -=
    * methods: if a class does not implement the in-place operators, the augmented operation will call __add__, __mul__...; on the other hand, if the in-place operators are implemented with their special methods, those methods are getting called - __iadd__, __imul__...