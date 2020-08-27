class InventoryAllocator:


    def __init__(self, order, inventory_distribution):
        self.order = order
        self.inventory_distribution = inventory_distribution
        self.cheapest_shipment = []


    def produceCheapestShipment(self):
        '''
        Function performs sanity checks on the inputs and
        outputs the cheapest shipment based on the order and the inventory distribution

        Returns: List of dictionaries 
        where the only key is the name of the warehouse and
        its value is a dictionary of the items, shipped from the warehouse, paired with their amount  
        '''

        assert type(self.order) is dict, 'Order must be a dictionary'
        assert self.order, 'Order information is missing'
        assert type(self.inventory_distribution) is list, 'Inventory Distribution must be a list' 
        assert self.inventory_distribution, 'Inventory Distribution information is missing'
        unique_warehouse_names = set()
        unique_warehouse_information = []
        for i, warehouse in enumerate(self.inventory_distribution):
            assert type(warehouse) is dict, 'Warehouse {} information must be a dictionary'.format(i)
            assert warehouse, 'Warehouse {} information is missing'.format(i)
            assert warehouse['name'] not in unique_warehouse_names, 'There are multiple warehouses with the same name in the inventory distribution'
            assert warehouse not in unique_warehouse_information, 'There are multiple entries with the same warehouse information in the inventory distribution'
            unique_warehouse_names.add(warehouse['name'])               
            unique_warehouse_information.append(warehouse)
        
        items_ordered = set(self.order.keys())
        items_fulfilled = set()
        for warehouse in self.inventory_distribution:
            warehouse_name = warehouse['name']
            warehouse_inventory = warehouse['inventory']
            warehouse_available_items = set(warehouse_inventory.keys())
            shipping_items_amount = {}
            for item in items_ordered:
                if item in warehouse_available_items and warehouse_inventory[item]>0 and self.order[item]>0:
                    amount_in_stock = warehouse_inventory[item]
                    amount_ordered = self.order[item]
                    if amount_ordered<=amount_in_stock:
                        self.order.pop(item)
                        items_fulfilled.add(item)
                        warehouse_inventory[item] -= amount_ordered
                        shipping_items_amount[item] = amount_ordered
                    else:
                        self.order[item] -= amount_in_stock
                        warehouse_inventory[item] = 0
                        shipping_items_amount[item] = amount_in_stock
            if shipping_items_amount:
                self.cheapest_shipment.append({warehouse_name:shipping_items_amount})
            if not self.order:
                return self.cheapest_shipment
            items_ordered -= items_fulfilled 
        return self.cheapest_shipment if not self.order else []