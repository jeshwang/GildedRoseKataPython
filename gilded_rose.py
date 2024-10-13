# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class InventoryItem():
    # Create empty dict, where key is item name, value is class
    class_by_name = {}

    def __init__(self, item: Item):
        self.item = item

    def update_sell_in(self):
        self.item.sell_in -= 1

    def update_quality(self):
        if self.item.sell_in >= 0:
            self.item.quality -= 1
        else:
            self.item.quality -= 2
        
        self.clamp_quality(0, 50)

    # Ensures quality stays within bounds after update
    def clamp_quality(self, lower_bound, upper_bound):
        if self.item.quality < lower_bound:
            self.item.quality = lower_bound
        if self.item.quality > upper_bound:
            self.item.quality = upper_bound


class NormalItem(InventoryItem):
    pass


class Sulfuras(InventoryItem):
    def update_sell_in(self):
        pass

    def update_quality(self):
        pass

InventoryItem.class_by_name.update({'Sulfuras, Hand of Ragnaros': Sulfuras})
    

class AgedBrie(InventoryItem):
    def update_quality(self):
        self.item.quality += 1
        self.clamp_quality(0, 50)

InventoryItem.class_by_name.update({'Aged Brie': AgedBrie})


class BackstagePass(InventoryItem):
    def update_quality(self):
        if self.item.sell_in > 10:
            self.item.quality += 1
        elif self.item.sell_in <= 10 and self.item.sell_in >= 6:
            self.item.quality += 2
        elif self.item.sell_in <= 5 and self.item.sell_in >= 0:
            self.item.quality += 3
        else:
            self.item.quality = 0

InventoryItem.class_by_name.update({'Backstage passes to a TAFKAL80ETC concert': BackstagePass})

# Assume Conjured Items are always named Conjured
class ConjuredItem(InventoryItem):
    def update_quality(self):
        if self.item.sell_in >= 0:
            self.item.quality -= 2
        else:
            self.item.quality -= 4
        
        self.clamp_quality(0, 50)

InventoryItem.class_by_name.update({'Conjured': ConjuredItem})


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items
        self.inventory_items = self._process_items(items)

    # Classify items into classes by their name
    def _process_items(self, items):
        new_arrivals = set()
        for item in self.items:
            item_class = NormalItem
            if item.name in InventoryItem.class_by_name:
                item_class = InventoryItem.class_by_name[item.name]
                
            new_arrivals.add(item_class(item))
        return new_arrivals

    def update_items(self):
        for item in self.inventory_items:
            item.update_sell_in()
            item.update_quality()
