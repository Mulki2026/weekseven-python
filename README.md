# Assignment: Shopping List Manager (PLP Python Week 7)

This repository contains Python scripts demonstrating key list operations, error prevention, and list iteration algorithms.

## Files Included
* `list_warmup.py`: Demonstrates fundamental list manipulations like index lookup, `.append()`, `.remove()`, and `len()`.
* `shopping_list.py`: An interactive console application allowing users to dynamically add, remove, and show items without crashing.
* `list_report.py`: Iterates through a fixed dataset to print numbered outputs, count items meeting structural criteria, and find maximum string length sequentially.
* `screenshots/`: Folder containing output verification screenshots for all scripts.

## Reflection Question

### Why is it safer to check `in` before calling `.remove()`?
In Python, calling `.remove(item)` on a list when `item` is not present immediately raises a `ValueError` and terminates execution abruptly if uncaught. By evaluating `item in list_name` first, the program handles absent items gracefully with conditional logic rather than breaking at runtime due to an unhandled exception.