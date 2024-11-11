 This project implements a simple banking system using a **Doubly Linked List** to manage user accounts and their balances. It provides basic banking functionalities like increasing and decreasing the balance, identifying VIP clients (with a balance above a certain threshold), and loading user data from a CSV file.

## Features

- **BankNode Class**: Represents an individual user in the bank with attributes like `user_name`, `id`, and `balance`. It supports methods for balance manipulation:
  - `increase_balance(value)`: Increases the user's balance.
  - `decrease_balance(value)`: Decreases the user's balance.
  - `get_balance()`: Returns the current balance.
  - `set_next(ptr)`: Sets the reference to the next node (used for linking nodes in the list).

- **BankLinkedList Class**: Manages the collection of `BankNode` objects and allows the following operations:
  - `add_node(new_node)`: Adds a new user to the bank's linked list.
  - `VIP_clients()`: Returns a list of users whose balance is above 10,000 (VIP clients).
  - `traversal()`: Prints all users in the list.

- **Data Loading**: A function `load_data_from_file(filename)` is provided to load user data from a CSV file into the linked list.
