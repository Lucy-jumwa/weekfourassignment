# Base Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"

    def power_on(self):
        return f"{self.device_info()} is now ON."

    def power_off(self):
        return f"{self.device_info()} is now OFF."


# Derived Class (Inheritance from Device)
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)  # Call parent constructor
        self.os = os
        self.__storage = storage  # private attribute (Encapsulation)

    # Method unique to Smartphone
    def make_call(self, number):
        return f"📞 Calling {number} from {self.device_info()}..."

    def install_app(self, app_name):
        return f"📲 Installing {app_name} on {self.device_info()}."

    # Getter for storage (Encapsulation)
    def get_storage(self):
        return f"{self.__storage}GB storage available."

    # Polymorphism: Overriding parent method
    def power_on(self):
        return f"{self.device_info()} (running {self.os}) is booting up... 🚀"


# Another Derived Class (to show polymorphism)
class Tablet(Device):
    def __init__(self, brand, model, screen_size):
        super().__init__(brand, model)
        self.screen_size = screen_size

    def draw(self):
        return f"✏️ Drawing on {self.device_info()} with {self.screen_size}-inch screen."

    # Overriding power_on (Polymorphism)
    def power_on(self):
        return f"{self.device_info()} (tablet) is waking up... 🔋"


# Example usage
if __name__ == "__main__":
    phone = Smartphone("Samsung", "Galaxy S24", "Android 14", 256)
    tablet = Tablet("Apple", "iPad Pro", 12.9)

    # Demonstrating Encapsulation, Polymorphism, and Methods
    print(phone.power_on())       # Overridden method
    print(phone.make_call("0723456789"))
    print(phone.install_app("WhatsApp"))
    print(phone.get_storage())    # Encapsulated access

    print(tablet.power_on())      # Polymorphism in action
    print(tablet.draw())
w
