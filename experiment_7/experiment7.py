class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    def is_worth_it(self):
        if ( self.draft - self.crew ) > 20 :
            return True 
        return False
    
class Block:
    # Good Luck!
    def __init__(self, arr):
        self.width = arr[0]
        self.length = arr[1]
        self.height = arr[2]
    def get_width(self) :
        return self.width
    def get_length(self) :
        return self.length
    def get_height(self) :
        return self.height
    
    def get_volume(self) :
        return self.width*self.height*self.length
    
    def get_surface_area(self) :
        return self.width*self.height*2+self.height*self.length*2+self.width*self.length*2


# TODO: complete this class

class PaginationHelper:
    
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection=collection
        self.items_per_page = items_per_page
        if(len(collection)%items_per_page!=0):
            self.full_page_count = len(collection)//items_per_page
        else:
            self.full_page_count = len(collection)//items_per_page-1
        self.lastPage_item_count = len(collection)-self.full_page_count*items_per_page
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)
    
    # returns the number of pages
    def page_count(self):
        if len(self.collection)!= 0:
            return self.full_page_count+1
        return 0
    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_index(self, page_index):
        if(page_index<len(self.collection) and page_index>=0):
            return page_index//self.items_per_page
        else :
            return -1
    
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_item_count(self, item_index):
        if self.full_page_count < 0 :
            return -1
        if item_index < self.full_page_count and item_index >= 0:
            return self.items_per_page
        elif item_index == self.full_page_count:
            return self.lastPage_item_count
        else :
            return -1


import math

class Vector:
    def __init__(self, components):
        self.components = components

    def __str__(self):
        return '(' + ','.join(map(str, self.components)) + ')'

    def __len__(self):
        return len(self.components)

    def add(self, other):
        if len(self) != len(other):
            raise ValueError('Vectors must have the same length')
        result = [a + b for a, b in zip(self.components, other.components)]
        return Vector(result)

    def sub(self, other):
        if len(self) != len(other):
            raise ValueError('Vectors must have the same length')
        result = [a - b for a, b in zip(self.components, other.components)]
        return Vector(result)
    
    def subtract(self, other):
        if len(self) != len(other):
            raise ValueError('Vectors must have the same length')
        result = [a - b for a, b in zip(self.components, other.components)]
        return Vector(result)
    
    def dot(self, other):
        if len(self) != len(other):
            raise ValueError('Vectors must have the same length')
        result = sum(a * b for a, b in zip(self.components, other.components))
        return result

    def norm(self):
        result = math.sqrt(sum(a * a for a in self.components))
        return result

    def equals(self, other):
        if len(self) != len(other):
            return False
        return all(a == b for a, b in zip(self.components, other.components))

