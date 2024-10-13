# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_items()
        self.assertEqual("foo", items[0].name)

    def test_aged_brie_should_increase_in_quality(self):
        aged_brie = "Aged Brie"
        items = [Item(aged_brie, 4, 2)]
        gr = GildedRose(items)
        gr.update_items()
        self.assertEqual(3, items[0].quality)

    def test_sulfuras_should_never_decrease_in_quality(self):
        sulfuras = "Sulfuras, Hand of Ragnaros"
        items = [Item(sulfuras, 0, 80)]
        gr = GildedRose(items)
        gr.update_items()
        self.assertEqual(80, items[0].quality)

    def test_backstage_pass_should_increase_in_quality_by_three(self):
        backstage_pass = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(backstage_pass, 4, 5)]
        gr = GildedRose(items)
        gr.update_items()
        self.assertEqual(8, items[0].quality)

if __name__ == '__main__':
    unittest.main()
