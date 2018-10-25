class Bus:
    def __init__(self, start, end):
        self.start_range = start
        self.end_range = end


class City:
    def __init__(self, num):
        self.num = num

    def served(self, bus):
        if self.num <= bus.end_range and self.num >= bus.start_range:
            return True
        return False


numberOfCases = int(input())


def case():
    numOfBuses = int(input())
    input()  # ignore
    ranges_arr = [int(i) for i in input().split()]

    bus_arr = []
    i = 0

    # set up the buses
    while i < len(ranges_arr):
        bus_arr.append(Bus(ranges_arr[i], ranges_arr[i + 1]))
        i += 2

    numOfCities = int(input())

    print("Case #", _, ": ", end="")
    for _ in range(numOfCities):

        counter = 0
        city = City(int(input()))
        for bus in bus_arr:
            if city.served(bus):
                counter += 1
        print(counter, " ", end="")


for xx in range(numberOfCases):
    case()