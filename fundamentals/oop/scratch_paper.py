class Contract:
    def __init__(self, contract, duration):
        self.contract = "Private"
        self.duration = "24 months"

class Aircraft:
    def __init__(self, manufacturer, type, range,pcm):
        self.manufacturer = "Boeing"
        self.type = "Boeing 737MAX"
        self.range = "short/medium haul"
        self.pcm = 29000.00
        self.in_stock = True
    def lease(self, manufacturer):
        if manufacturer != "Embraer":
            print("This aircraft type is available for dry leases only")
        else:
            print("This aircraft is available for wet and dry leases.")
    def legacy_discount(self, reduction):
        self.pcm = self.pcm * (1 - reduction)

b_747 = Aircraft("Boeing", "B747-800", "long haul", 57800.00)
print(b_747.type)
b_747.type = "Boeing 747-8"
print(b_747.type)
a_350 = Aircraft("Airbus", "A350-1K", "long haul", 66250.00)
print(a_350.type)
a_350.type = "Airbus A350-1K"
print(a_350.type)
b_787 = Aircraft("Boeing", "B787-9", "Long-haul", 47500.00)
print(b_787.range)
b_787.range = "Long haul"
print(b_787.range)
erj_190 = Aircraft("Embraer", "ERJ-900", "regional", 24000.00)
print(erj_190.pcm)
b_787.lease("Boeing")
a_350.lease("Airbus")
erj_190.lease("Embraer")
print(a_350.pcm)
a_350.legacy_discount(0.1)
print(a_350.pcm)