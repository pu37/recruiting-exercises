# recruiting-exercises

This is my solution to Deliverr's recruiting exercise. The problem description can be found [here](https://github.com/deliverr/recruiting-exercises/tree/master/inventory-allocator)

## Requirements

- `python 3.x`

## Solution

### Assumptions

- If any of the input or any object in the second input is empty or not of the correct format, then the inputs are considered invalid and will throw an assertion error

- Each object in the second input, if non-empty and of correct format, must have `name` and `warehouse` as its only keys

- If any name of the object in the second input is repeated, then the second input is considered invalid and it will throw an assertion error

- If any object in the second input is repeated, then the second input is considered invalid and it will throw an assertion error

- The list of warehouses is pre-sorted based on cost

- Shipping from each warehouse is expensive than all the previous warehouses combined

- Shipping out of one warehouse is cheaper than shipping from multiple warehouses

- If any item of the order can't be fulfilled, the order won't be shipped and the solution will be `[]`

### Execution

- The solution is in `inventory-allocator/src/inventory_allocator.py`

- The tests are in `inventory-allocator/src/test_inventory_allocator.py` 

- To run the test cases, go to the `src` directory and run `python3 test_inventory_allocator.py` or `python3 -m unittest`

- To know more details on the result of each test case, go to the `src` directory and run `python3 -m unittest -v`