class SimplifiedEnum(type):
    """
    Metaclass removes duplications in variables declarations for enum class
    """
    def __new__(metacls, name, bases, clsdict):
        print(type(clsdict))
        print(clsdict)
        print(name)
        cls = super().__new__(metacls, name, bases, clsdict)
        for attrib in clsdict.get(f'_{name}__keys'):
            setattr(cls, attrib, attrib)

        return cls
