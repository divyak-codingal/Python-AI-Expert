class Vehicle:
    def __init__(self, name, maxSpeed, mileage):
      self.name = name
      self.maxSpeed = maxSpeed
      self.mileage = mileage

class Bus(Vehicle):
  pass

school_bus = Bus("School Volvo", 180, 12)
print("Vehicle name:", school_bus.name, "Speed:", school_bus.maxSpeed, "Mileage:", school_bus.mileage)
