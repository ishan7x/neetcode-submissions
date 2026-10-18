class Solution:
    class Car:
        def __init__(self, target, position, speed):
            self.position = position
            self.speed = speed
            self.time = (target - position) / speed

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            car = Solution.Car(target, position[i], speed[i])
            cars.append(car)
        cars.sort(reverse = True, key = lambda car:car.position)

        result = 0
        prev = 0
        for car in cars:
            if car.time > prev:
                result += 1
                prev = car.time
        
        return result



        