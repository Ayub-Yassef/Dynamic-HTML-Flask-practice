passenger_manifest = [
    {
        "name": "Diego Dreyfus",
        "nationality": "MEX",
        "seat": "3K",
        "Oneworld Partner": "British Airways"
    },
    {
        "name": "Raul Tejon",
        "nationality": "SPA",
        "seat": "3A",
        "Oneworld Partner": "Iberia"
    },
    {
        "name": "Jess Haikkaanenaa",
        "nationality": "FIN",
        "seat": "12D",
        "Oneworld Partner": "Finnair"
    },
    {
        "name": "Roy Coogan",
        "nationality": "AUS",
        "seat": "42K",
        "Oneworld Partner": "Qantas"
    },
    {
        "name": "Lisa Liu",
        "nationality": "HKG",
        "seat": "36B",
        "Oneworld Partner": "Cathay Pacific"
    },
    {
        "name": "Fatimah Al-Kitab",
        "nationality": "JOR",
        "seat": "6C",
        "Oneworld Partner": "Royal Air Maroc"
    },
    {
        "name": "Gary Petersen",
        "nationality": "USA",
        "seat": "18A",
        "Oneworld Partner": "American Airlines"
    },
]

class Passenger:
    def __init__(self, passenger_manifest):
        self.name = passenger_manifest["name"]
        self.nationality = passenger_manifest["nationality"]
        self.seat = passenger_manifest["seat"]
        self.oneworld_partner = passenger_manifest["Oneworld Parnter"]

print(passenger_manifest[5]) 
