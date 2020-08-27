import unittest
from inventory_allocator import InventoryAllocator

class TestInventoryAllocator(unittest.TestCase):

    def test_order_must_be_dictionary(self):
        order = [{'apple': 1}]
        inventory_distribution = [{'name': 'w12', 'inventory': {'apple': 1}}]
        inventory_allocator_object = InventoryAllocator(order, inventory_distribution)
        self.assertRaises(AssertionError, lambda: inventory_allocator_object.produceCheapestShipment())

    def test_empty_order_error(self):
        order = {}
        inventory_distribution = [{'name': 'w54', 'inventory': {'apple': 1}}]
        inventory_allocator_object = InventoryAllocator(order, inventory_distribution)
        self.assertRaises(AssertionError, lambda: inventory_allocator_object.produceCheapestShipment())

    def test_inventory_distribution_must_be_list(self):
        order = {'apple': 1}
        inventory_distribution = {'name': 'w33', 'inventory': {'apple': 1}}
        inventory_allocator_object = InventoryAllocator(order, inventory_distribution)
        self.assertRaises(AssertionError, lambda: inventory_allocator_object.produceCheapestShipment())

    def test_empty_inventory_distribution_error(self):
        order = {'apple': 1}
        inventory_distribution = []
        inventory_allocator_object = InventoryAllocator(order, inventory_distribution)
        self.assertRaises(AssertionError, lambda: inventory_allocator_object.produceCheapestShipment())

    def test_warehouse_information_must_be_dictionary(self):
        order = {'apple': 1}
        inventory_distribution = [r'''{'name': 'w9', 'inventory': {'apple': 1}}''']
        inventory_allocator_object = InventoryAllocator(order, inventory_distribution)
        self.assertRaises(AssertionError, lambda: inventory_allocator_object.produceCheapestShipment())

    def test_redundant_warehouse_names_error(self):
        order = {'apple': 1}
        inventory_distribution = [{'name': 'w37', 'inventory': {'apple': 1}}, {'name': 'w77', 'inventory': {'berry': 1}}, {'name': 'w37', 'inventory': {'apple': 5}}]
        inventory_allocator_object = InventoryAllocator(order, inventory_distribution)
        self.assertRaises(AssertionError, lambda: inventory_allocator_object.produceCheapestShipment())
    
    def test_redundant_warehouse_entries_error(self):
        order = {'apple': 1}
        inventory_distribution = [{'name': 'w37', 'inventory': {'apple': 1}}, {'name': 'w77', 'inventory': {'berry': 1}}, {'name': 'w37', 'inventory': {'apple': 1}}]
        inventory_allocator_object = InventoryAllocator(order, inventory_distribution)
        self.assertRaises(AssertionError, lambda: inventory_allocator_object.produceCheapestShipment())

    def test_empty_warehouse_information_error(self):
        order = {'apple': 1}
        inventory_distribution = [{'name': 'w21', 'inventory': {'apple': 5}}, {}]
        inventory_allocator_object = InventoryAllocator(order, inventory_distribution)
        self.assertRaises(AssertionError, lambda: inventory_allocator_object.produceCheapestShipment())    

    def test_exact_match_single_item_single_warehouse(self):
        order = {'apple': 3}
        inventory_distribution = [{'name': 'w1', 'inventory': {'apple': 3}}]
        expected_answer = [{'w1': {'apple': 3}}]
        predicted_answer = InventoryAllocator(order, inventory_distribution).produceCheapestShipment()
        self.assertEqual(predicted_answer, expected_answer)

    def test_exact_match_single_item_multiple_warehouse(self):
        order = {'apple': 5}
        inventory_distribution = [{'name': 'w21', 'inventory': {'apple': 5}}, {'name': 'w43', 'inventory': {'apple': 5}}]
        expected_answer = [{'w21': {'apple': 5}}]
        predicted_answer = InventoryAllocator(order, inventory_distribution).produceCheapestShipment()
        self.assertEqual(predicted_answer, expected_answer)
    
    def test_exact_match_multiple_item_single_warehouse(self):
        order = {'apple': 3, 'berry': 5, 'banana': 2}
        inventory_distribution = [{'name': 'w41', 'inventory': {'apple': 3, 'berry': 5, 'banana': 2}}]
        expected_answer = [{'w41': {'apple': 3, 'berry': 5, 'banana': 2}}]
        predicted_answer = InventoryAllocator(order, inventory_distribution).produceCheapestShipment()
        self.assertEqual(predicted_answer, expected_answer)

    def test_exact_match_multiple_item_multiple_warehouse(self):
        order = {'apple': 5, 'berry': 10, 'banana': 7}
        inventory_distribution = [{'name': 'w66', 'inventory': {'apple': 3, 'berry': 3}}, {'name': 'w78', 'inventory': {'banana': 3}}, {'name': 'w10', 'inventory': {'apple': 1, 'berry':4}}, {'name': 'w3', 'inventory': {'banana': 4, 'berry': 3, 'apple': 1}}]
        expected_answer = [{'w66': {'apple': 3, 'berry': 3}}, {'w78': {'banana': 3}}, {'w10': {'apple': 1, 'berry':4}}, {'w3': {'banana': 4, 'berry': 3, 'apple': 1}}]
        predicted_answer = InventoryAllocator(order, inventory_distribution).produceCheapestShipment()
        self.assertEqual(predicted_answer, expected_answer)

    def test_not_enough_inventory_single_item_single_warehouse(self):
        order = {'apple': 3}
        inventory_distribution = [{'name': 'w1', 'inventory': {'apple': 0}}]
        expected_answer = []
        predicted_answer = InventoryAllocator(order, inventory_distribution).produceCheapestShipment()
        self.assertEqual(predicted_answer, expected_answer)

    def test_not_enough_inventory_single_item_multiple_warehouse(self):
        order = {'apple': 5}
        inventory_distribution = [{'name': 'w21', 'inventory': {'apple': 2}}, {'name': 'w43', 'inventory': {'apple': 1}}]
        expected_answer = []
        predicted_answer = InventoryAllocator(order, inventory_distribution).produceCheapestShipment()
        self.assertEqual(predicted_answer, expected_answer)
    
    def test_not_enough_inventory_multiple_item_single_warehouse(self):
        order = {'apple': 3, 'berry': 5, 'banana': 2}
        inventory_distribution = [{'name': 'w41', 'inventory': {'apple': 3, 'berry': 2, 'banana': 1}}]
        expected_answer = []
        predicted_answer = InventoryAllocator(order, inventory_distribution).produceCheapestShipment()
        self.assertEqual(predicted_answer, expected_answer)

    def test_not_enough_inventory_multiple_item_multiple_warehouse(self):
        order = {'apple': 5, 'berry': 10, 'banana': 7}
        inventory_distribution = [{'name': 'w66', 'inventory': {'apple': 1, 'berry': 3}}, {'name': 'w78', 'inventory': {'banana': 3}}, {'name': 'w10', 'inventory': {'apple': 1, 'berry':2}}, {'name': 'w3', 'inventory': {'banana': 2, 'berry': 3, 'apple': 1}}]
        expected_answer = []
        predicted_answer = InventoryAllocator(order, inventory_distribution).produceCheapestShipment()
        self.assertEqual(predicted_answer, expected_answer)

    def test_excess_inventory_single_item_single_warehouse(self):
        order = {'apple': 3}
        inventory_distribution = [{'name': 'w1', 'inventory': {'apple': 10}}]
        expected_answer = [{'w1': {'apple': 3}}]
        predicted_answer = InventoryAllocator(order, inventory_distribution).produceCheapestShipment()
        self.assertEqual(predicted_answer, expected_answer)

    def test_excess_inventory_single_item_multiple_warehouse(self):
        order = {'apple': 5}
        inventory_distribution = [{'name': 'w21', 'inventory': {'apple': 10}}, {'name': 'w43', 'inventory': {'apple': 3}}]
        expected_answer = [{'w21': {'apple': 5}}]
        predicted_answer = InventoryAllocator(order, inventory_distribution).produceCheapestShipment()
        self.assertEqual(predicted_answer, expected_answer)
    
    def test_excess_inventory_multiple_item_single_warehouse(self):
        order = {'apple': 3, 'berry': 5, 'banana': 2}
        inventory_distribution = [{'name': 'w41', 'inventory': {'apple': 5, 'berry': 11, 'banana': 10}}]
        expected_answer = [{'w41': {'apple': 3, 'berry': 5, 'banana': 2}}]
        predicted_answer = InventoryAllocator(order, inventory_distribution).produceCheapestShipment()
        self.assertEqual(predicted_answer, expected_answer)

    def test_excess_inventory_multiple_item_multiple_warehouse(self):
        order = {'apple': 5, 'berry': 10, 'banana': 7}
        inventory_distribution = [{'name': 'w66', 'inventory': {'apple': 10}}, {'name': 'w78', 'inventory': {'banana': 8}}, {'name': 'w10', 'inventory': {'apple': 10, 'berry':40}}, {'name': 'w3', 'inventory': {'banana': 14, 'berry': 30, 'apple': 10}}]
        expected_answer = [{'w66': {'apple': 5}}, {'w78': {'banana': 7}}, {'w10': {'berry':10}}]
        predicted_answer = InventoryAllocator(order, inventory_distribution).produceCheapestShipment()
        self.assertEqual(predicted_answer, expected_answer)

    def test_split_single_item_multiple_warehouse(self):
        order = {'apple': 5}
        inventory_distribution = [{'name': 'w21', 'inventory': {'apple': 2}}, {'name': 'w43', 'inventory': {'apple': 5}}]
        expected_answer = [{'w21': {'apple': 2}}, {'w43': {'apple': 3}}]
        predicted_answer = InventoryAllocator(order, inventory_distribution).produceCheapestShipment()
        self.assertEqual(predicted_answer, expected_answer)
    
    def test_split_multiple_item_multiple_warehouse(self):
        order = {'apple': 5, 'berry': 10, 'banana': 7}
        inventory_distribution = [{'name': 'w66', 'inventory': {'apple': 2}}, {'name': 'w78', 'inventory': {'banana': 5}}, {'name': 'w10', 'inventory': {'apple': 10, 'berry':4}}, {'name': 'w3', 'inventory': {'banana': 14, 'berry': 30, 'apple': 10}}]
        expected_answer = [{'w66': {'apple': 2}}, {'w78': {'banana': 5}}, {'w10': {'apple': 3, 'berry':4}}, {'w3': {'banana': 2, 'berry': 6}}]
        predicted_answer = InventoryAllocator(order, inventory_distribution).produceCheapestShipment()
        self.assertEqual(predicted_answer, expected_answer)

    def test_any_item_not_fulfilled(self):
        order = {'apple': 5, 'berry': 5, 'banana': 7}
        inventory_distribution = [{'name': 'w16', 'inventory': {'apple': 2}}, {'name': 'w8', 'inventory': {'banana': 5}}, {'name': 'w11', 'inventory': {'apple': 10, 'berry':14}}]
        expected_answer = []
        predicted_answer = InventoryAllocator(order, inventory_distribution).produceCheapestShipment()
        self.assertEqual(predicted_answer, expected_answer)

    def test_each_warehouse_expensive_than_all_previous_warehouses_combined(self):
        order = {'apple': 5, 'berry': 5, 'banana': 7}
        inventory_distribution = [{'name': 'w160', 'inventory': {'apple': 2, 'berry':7}}, {'name': 'w108', 'inventory': {'banana': 10, 'apple': 5}}, {'name': 'w119', 'inventory': {'banana': 9, 'apple': 10, 'berry':14}}]
        expected_answer = [{'w160': {'apple': 2, 'berry':5}}, {'w108': {'banana': 7, 'apple': 3}}]
        predicted_answer = InventoryAllocator(order, inventory_distribution).produceCheapestShipment()
        self.assertEqual(predicted_answer, expected_answer)

        
if __name__ == '__main__':
    unittest.main()