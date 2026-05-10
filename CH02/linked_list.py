from typing import Any, Optional, List, Callable


class Node:
    """A node in a singly linked list."""
    
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional[Node] = None
    
    def __repr__(self) -> str:
        return f"Node({self.data})"


class LinkedList:
    """A singly linked list implementation."""
    
    def __init__(self):
        self.head: Optional[Node] = None
        self._size: int = 0
    
    def __len__(self) -> int:
        return self._size
    
    def __repr__(self) -> str:
        return f"LinkedList({self.to_list()})"
    
    def insert_at_head(self, data: Any) -> None:
        """Insert at beginning - O(1)"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1
    
    def insert_at_tail(self, data: Any) -> None:
        """Insert at end - O(n)"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1
    
    def delete_at_head(self) -> Optional[Any]:
        """Delete and return head element - O(1)"""
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        self._size -= 1
        return data
    
    def search(self, data: Any, key: Callable = lambda x: x) -> Optional[Node]:
        """Search for a node with given data - O(n)"""
        current = self.head
        while current:
            if key(current.data) == data:
                return current
            current = current.next
        return None
    
    def to_list(self) -> List[Any]:
        """Convert linked list to Python list"""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
