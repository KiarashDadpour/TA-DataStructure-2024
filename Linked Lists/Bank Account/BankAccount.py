class BankNode:

    def __init__(self, user_name, id, balance=0):
        self.next = None
        self.user_name = user_name
        self.id = id
        if balance >= 0:
            self.balance = float(balance)
        else:
            self.balance = 0

    def get_balance(self):
        return self.balance

    def increase_balance(self, value):
        self.balance += float(value)

    def decrease_balance(self, value):
        if self.balance < value:
            print("Value Error")
        else:
            self.balance -= value

    def set_next(self, ptr):
        self.next = ptr


class BankLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def add_node(self, new_node):
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def VIP_clients(self):
        vip_list = BankLinkedList()

        current = self.head
        while current:
            if current.balance >= 10000:
                vip_client = BankNode(current.user_name, current.id, current.balance)
                vip_list.add_node(vip_client)
            current = current.next
        return vip_list.traversal()

    def traversal(self):
        if self.is_empty():
            return "Empty List!!!"
        current = self.head
        while current:
            print(current.user_name, end=" ==> ")
            current = current.next


def load_data_from_file(filename):
    linked_list = BankLinkedList()
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 3:
                user_name = parts[0].strip()
                id = parts[1].strip()
                balance = float(parts[2].strip())
                new_node = BankNode(user_name, id, balance)
                linked_list.add_node(new_node)
    return linked_list


filename = "users_data.txt"

L = load_data_from_file(filename)
