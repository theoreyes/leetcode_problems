import itertools

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Short circuit in edge case that n == 1
        if (len(position) == 1):
            return 1

        # Zips position and speed lists together
        cars = zip(position, speed)

        # Sorts on position index
        sortedCars = sorted(cars, key=lambda car: car[0], reverse=True)

        # Unzips the position, speed lists
        position, speed = list(zip(*sortedCars))

        # Creates stack for fleet times
        fleetTimeStack = list()

        # Calculates fleet time of furthest car
        curFleetTime = (target - position[0]) / speed[0]

        # Loops through cars and counts fleets by identifying points 
        # along the highway where the car behind the "current" one will 
        # not catch up to it (cementing the "current" string of cars as 
        # their own fleet)
        for i in range(len(position) - 1):
            time2 = (target - position[i + 1]) / speed[i + 1]
            if (curFleetTime < time2):
                fleetTimeStack.append(curFleetTime)
                curFleetTime = time2
        # Once loop finishes, we push the last fleet time to the stack
        fleetTimeStack.append(curFleetTime)

        # The size of the stack is the # of fleets found
        return len(fleetTimeStack)
