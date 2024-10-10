# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_vest_item_should_decrease_after_one_day(self):
        vest = "+5 Dexterity Vest"
        items = [Item(vest, 1, 2), Item(vest, 9, 19), Item(vest, 4, 6), ]
        gr = GildedRose(items)
        gr.update_quality()
        assert gr.get_items_by_name(vest) == [Item(vest, 0, 1), Item(vest, 8, 18), Item(vest, 3, 5)] 
    
    def test_aged_brie_should_increase_in_quality(self):
        aged_brie = "Aged Brie"
        items = [Item(aged_brie, 4, 2)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(3, items[0].quality)

    def test_sulfuras_should_never_decrease_in_quality(self):
        sulfuras = "Sulfuras, Hand of Ragnaros"
        items = [Item(sulfuras, 0, 80)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(80, items[0].quality)

if __name__ == '__main__':
    unittest.main()
