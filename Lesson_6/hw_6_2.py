class Road:
    def __init__(self, l, w):
        self._length = l
        self._width = w

    def massa(self, w, sm):
        result = int(self._length * self._width * w * sm / 1000)
        return result

road_m = Road(20, 5000)
resulr_massa = road_m.massa(25, 5)
print(f"result: {resulr_massa} т")