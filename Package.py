class Package:
    def __init__(self, id_num, address, city, state, zip, deadline, weight, status):
        self.id_num = id_num
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.delivery_time = None
        self.depart_time = None

    def __str__(self):
        return (f"Package ID: {self.id_num}\n"
                f"Address: {self.address}\n"
                f"Deadline: {self.deadline}\n"
                f"City: {self.city}\n"
                f"Zip Code: {self.zip}\n"
                f"Weight: {self.weight}\n"
                f"Status: {self.status}"
                )

    def status_update(self, convert_time):
        if self.delivery_time < convert_time:
            self.status = "Package has been delivered"
        elif self.depart_time > convert_time:
            self.status = "Package is en route"
        else:
            self.status = "Package is at the hub"

