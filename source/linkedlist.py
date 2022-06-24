#!python

#TODO: I recommend removing any imports that you aren't using to keep the code clean. -Tanner
#from array import array
from genericpath import exists
#from http.client import NETWORK_AUTHENTICATION_REQUIRED
#from msvcrt import LK_LOCK
#from platform import node
#import struct


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        # TODO: I'm not sure what you were trying to do with these two lines, but __repr__ defines what happens when you
        # call repr, so by calling repr(self) in the definition of repr, your going to cause it to call repr over and
        # over until it kills itself from running out of memory. You also can't have two different returns in the same
        # function because return exits the function, so anything after the first won't even run. -Tanner
        # return repr(self)
        # self = __repr__()
        return 'LinkedList({!r})'.format(self.items(self))

    def items(self):
        """Return <<<<CHANGE HERE @STEPHEN>>>> a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None
        # TODO: As mentioned above, you can't call code after a return. Additionally, casting the linked list as a bool
        # doesn't really make sense. -Tanner
        #return bool(self)
        
        #TODO: Typically you want to remove any unneeded whitespace. It technically doesn't impact the code from
        #functioning correctly, but it will make the code look much nicer and also avoid setting off people's OCD haha.
        #-Tanner

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.next
        return count
        
        # TODO: Loop through all nodes and count one for each        
    
    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        
        appended_node = Node(item)
        
        if self.head is None:
             self.head = appended_node
             self.tail = appended_node
             #TODO: These last two cases can actually be combined. Can you think of how? -Tanner
        elif self.head.next is None:
             self.head.next = appended_node
             self.tail = appended_node
        else:
            self.tail.next = appended_node
            self.tail = appended_node
        
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        prepended_node = Node(item)
        
        #TODO: The logic here is not quite right. Think through what is happening to the head and tail values. When you
        # reach this point, come to my office and we can walk through what's happening. -Tanner
        if self.tail is None:
             self.tail = prepended_node
             self.head = prepended_node
        elif self.tail.next is None:
             self.tail.next = prepended_node
             self.head = prepended_node
        else:
            self.head.next = prepended_node
            self.head = prepended_node
            
        prepended_node.next = self.head
        self.head = prepended_node
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        
    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        #TODO: You're really close here. What you've written will tell you if the value of quality is in the list or
        #not, but reread the functions description. quality is a function, not a value, which you pass the item into. If
        #that function returns True, then you should return the item. It doesn't specifically mention what to return in
        #the case where it's not found, but I would return None in that case. -Tanner
        current = self.head
        while current != None:
            if current.data == quality:
                return True
            current = current.next
        return False

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        #TODO: You won't be able to loop this way by default. It's possible to set it up to do so, but that's a topic
        #for another day. What you'll need to do instead is loop similarly to how you did it in find. -Tanner
        for item in self:
            #TODO: This if statement doesn't really make sense. Indexing, which is what you're trying to do with the [],
            #is another feature that's not available out of the box, so you would have to write that. exists is also a
            #random function that you imported which checks if a filepath is valid. Definitely not what you want in this
            #case. So essentially what this if statement is trying to do is check if something in your list named 'item'
            #is set to the value of the function named exists. -Tanner
            if self['item'] == exists:
                #TODO: del isn't what you want in this case. del is used to make it so a variable no longer exists.
                #What you need to do instead and manage the links between the node before and the node after the node
                #which has that item. -Tanner
                del(item)
                #TODO: You don't need to return anything in this case. -Tanner
                return self
            raise ValueError('Item not found: {}'.format(item))

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
