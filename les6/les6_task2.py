class Road:

    def __init__(self, _length, _width):
        """

        :type _width: object
        """
        self._length = _length
        self._width = _width

    @property
    def square(self):
        assert isinstance(self._width, object)
        return self._length * self._width


class MassCount(Road):
    __mass_per_meter = 25

    def __init__(self, _length, _width, thick):
        self._thickness = thick
        super().__init__(_length, _width)

    def mass(self):
        return super().square * self._thickness * self.__mass_per_meter


length = 20
width = 5000
thickness = 5

r = MassCount(length, width, thickness)
print(r.mass() / 1000, "т")
