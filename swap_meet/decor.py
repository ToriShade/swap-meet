from swap_meet.item import Item

class Decor(Item):
    def __init__(self, category = "Decor", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Something to decorate your space."

    def condition_description(self):
        if self.condition == 0:
            return f"terrible"
        if self.condition == 1:
            return f"not great"
        if self.condition == 2:
            return f"kinda ok"
        if self.condition == 3:
            return f"basic"
        if self.condition == 4:
            return f"you'll do"
        if self.condition == 5:
            return f"vibe"