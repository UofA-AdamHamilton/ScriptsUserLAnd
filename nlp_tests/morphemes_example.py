from morphemes import Morphemes

# specify a path where the morpheme data will be stored
path = "./data"

m = Morphemes(path) #Data path is optional, local storage will be used if left out.
print(m.parse("organizationally"))
