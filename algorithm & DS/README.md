# 📝 Linked List Project

## Project Overview

This is a **singly linked list implementation in Python**.
It covers the core operations of linked lists, including adding, deleting, and searching nodes.

This project is designed as a **learning tool** for foundational data structures and algorithms. It is fully modular and can be extended into more advanced structures like hash tables, stacks, queues, and LRU caches.

---

## 🚀 Features Implemented

* Add node at **end** → `add(data)`
* Add node at **front/head** → `add_f(data)`
* Add node at a **specific index** → `add_at(index, data)`
* Delete **first node** → `del_first()`
* Delete **last node** → `del_last()`
* Delete node at **specific index** → `del_at(index)`
* **Search** for a node → `search(data)`
* **Print** the linked list → `PRINT()`
* **Check if list is empty** → `IS_EMPTY()`

---

## 📦 Node Class

* `node` class contains:

  * `data` → value of the node
  * `next` → pointer to the next node

---

## 🔧 Usage Example

```python
from linked_list import LINKED_LIST

# Initialize list
ll = LINKED_LIST()

# Add nodes
ll.add(10)
ll.add(20)
ll.add_f(5)
ll.add_at(2, 15)  # Insert 15 at index 2

# Print list
ll.PRINT()  # Output: [5][.] -> [15][.] -> [10][.] -> [20][.] -> None

# Delete nodes
ll.del_first()
ll.del_last()
ll.del_at(2)

# Search
ll.search(10)
```

---

## 📊 Planned Documentation

* [ ] **Time Complexity Analysis**

  * `add` →
  * `add_f` →
  * `add_at` →
  * `del_first` →
  * `del_last` →
  * `del_at` →
  * `search` →
* [ ] **Space Complexity Analysis**
* [ ] **Edge Case Handling Documentation**

  * Empty list
  * Single-node list
  * Out-of-range indexes

---

## 🛠️ TODO / Future Enhancements

* Implement **doubly linked list** for backward traversal.
* Add **circular linked list** option.
* Convert list into **hash table** (chaining method).
* Build **stack** and **queue** using linked list.
* Add **visualization** of the list structure in ASCII or Matplotlib.
* Add **unit tests** to ensure stability.
* Optimize `add_at` and `del_at` for better readability.
* Write **full documentation for each function** (inputs, outputs, exceptions).

---

## 📚 Notes

* This project is a **foundation project** for learning data structures.
* Can be extended for **more advanced projects**, such as hash tables, caches, or graph adjacency lists.
* All operations assume **1-based indexing** for easier understanding.

---
