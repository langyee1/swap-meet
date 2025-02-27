
class Vendor:
    
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory


    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else: 
            return False


    def add(self, element):
        self.inventory.append(element)
        return element


    def get_by_id(self, id):
        for element in self.inventory:
            if id == element.id:
                return element
        return None


    def swap_items(self, other_vendor, my_item, their_item,):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            other_vendor.add(my_item)
            self.add(their_item)
            self.remove(my_item)
            other_vendor.remove(their_item)
            return True
        return False


    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        return self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])


    def get_by_category(self, category):
        return [element for element in self.inventory if element.get_category() == category]


    def get_best_by_category(self, category):
        items_to_search = self.get_by_category(category)
        if not items_to_search: 
            return None
        return max(items_to_search, key=lambda element: element.condition)


    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item_in_the_category_they_want  = self.get_best_by_category(their_priority)
        their_best_item_in_the_category_I_want = other_vendor.get_best_by_category(my_priority)
        return self.swap_items(other_vendor, 
                                my_best_item_in_the_category_they_want, 
                                their_best_item_in_the_category_I_want)


    def swap_by_newest(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        my_newest_item = min(self.inventory, key=lambda element: element.age)
        their_newest_item = min(other_vendor.inventory, key=lambda element: element.age)
        return self.swap_items(other_vendor, my_newest_item, their_newest_item)

