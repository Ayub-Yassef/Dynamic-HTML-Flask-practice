from mysqlconnection import connectToMySql
class Users:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["laast_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.upadated_at = data["updated_at"]

    @classmethod
    def fetch_info(cls):
        query = "SELECT * FROM users;"
        results = connectToMySql