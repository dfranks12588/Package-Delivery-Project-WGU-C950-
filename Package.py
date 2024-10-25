class Package:
    def __init__(self, id_num, address, city, state, zip, deadline, weight, status):
        self.id = id_num
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.status = status

    def __str__(self):
        return (f"Package ID: {self.id}\n"
                f"Address: {self.address}\n"
                f"Deadline: {self.deadline}\n"
                f"City: {self.city}\n"
                f"Zip Code: {self.zip}\n"
                f"Weight: {self.weight}\n"
                f"Status: {self.status}"
                )