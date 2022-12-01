class Rocket():
    def __init__(self, weight, fuel,):
        self.weight=weight
        self.fuel=fuel
        self.ison=bool
        if self.fuel>0:
            self.ison=True
        else:
            self.ison=False
    def spend_fuel(self, count):
        if count > self.fuel:
            self.fuel=0
            self.ison=False
            return False
        else:
            self.fuel=self.fuel - count
            return True
    def get_fuel_level(self):
        return self.fuel
    def get_total_weight(self):
        return self.fuel+self.weight
    def get_is_engine_running(self):
        return self.ison
ro=Rocket(5, 8,)
print(ro.spend_fuel(3))
print(ro.get_fuel_level())
print(ro.get_total_weight())
print(ro.get_is_engine_running())

    
