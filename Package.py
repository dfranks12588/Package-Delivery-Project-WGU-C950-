# Holds package data
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
        self.corrected_address = None
        self.truck_id = None

    def __str__(self):
        return (f"Package ID: {self.id_num}\n"
                f"Address: {self.address}\n"
                f"Deadline: {self.deadline}\n"
                f"City: {self.city}\n"
                f"Zip Code: {self.zip}\n"
                f"Weight: {self.weight}\n"
                f"Status: {self.status}"
                )
# Updates the status of the package based on the current time
    def status_update(self, current_time):

        if self.delivery_time is None or current_time < self.depart_time:
            self.status = f"At the hub (Assigned to Truck {self.truck_id})"

        elif self.delivery_time is not None and current_time >= self.delivery_time:
            self.status = f"Package has been delivered at {self.delivery_time} by Truck {self.truck_id}"

        else:
            self.status = f"En route on Truck {self.truck_id}"

