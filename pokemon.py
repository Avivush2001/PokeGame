

class Pokemon:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height
    def __str__(self):
        return f"Name: {self.name} Weight: {self.weight} Height: {self.height}"
    def as_dict(self):
        return {"name": self.name, "weight": self.weight, "height": self.height}

