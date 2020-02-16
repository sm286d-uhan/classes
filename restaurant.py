class Restaurant():
    """A class to represent a restaurant."""

    def __init__(self, name, cuisine):
        """Initialize attributes to describe a restaurant."""
        self.restaurant_name = name
        self.cuisine_type = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """Print information about the restaurant."""
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        """Open the restaurant."""
        print(f"The restaurant {self.restaurant_name} is now open.")

    def set_number_served(self, num):
        """Set the number of customers served attribute."""
        self.number_served = num

    def increment_number_served(self, num):
        """Add to the number of customers served."""
        self.number_served += num
