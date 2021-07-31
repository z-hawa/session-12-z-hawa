import math


class Polygon:
    def __init__(self, n, R):
         self.circumradius = R
         self.vertices=n
        
    def __repr__(self):
        return f'Polygon(n={self.vertices}, R={self.circumradius})'
    
    @property
    def vertices(self):
        return self._vertices
    
    @vertices.setter
    def vertices(self,n):
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self._vertices = n
        self._interior_angle=None
        self._side_length=None
        self._apothem=None
        self._area=None
        self._perimeter=None
    
    @property
    def circumradius(self):
        return self._circumradius
    
    @circumradius.setter
    def circumradius(self,R):
        self._circumradius = R
        self._side_length=None
        self._apothem=None
        self._area=None
        self._perimeter=None
        self._interior_angle=None
    
    @property
    def interior_angle(self):
        if self._interior_angle is None:
            self._interior_angle=(self.vertices - 2) * 180 / self.vertices
        return self._interior_angle

    @property
    def side_length(self):
        if self._side_length is None:
            self._side_length=2 * self.circumradius * math.sin(math.pi / self.vertices)
        return self._side_length
        

    @property
    def apothem(self):
        if self._apothem is None:
            self._apothem=self.circumradius * math.cos(math.pi / self.vertices)
        return self._apothem
    
    @property
    def area(self):
        if self._area is None:
            self._area=self.vertices / 2 * self.side_length * self.apothem
        return self._area
    
    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter=self.vertices * self.side_length
        return self._perimeter
    
    def __eq__(self, other):
        '''Checks if a polygon object is equal to the current object'''
        if isinstance(other, self.__class__):
            return (self.vertices == other.vertices 
                    and self.circumradius == other.circumradius)
        else:
            return NotImplemented
        
    def __gt__(self, other):
        '''Checks if a polygon object is greater than the current object'''
        if isinstance(other, self.__class__):
            return self.vertices > other.vertices
        else:
            return NotImplemented
    def __len__(self) -> int:
        '''Returns the length of this Polygon instance'''
        return self.MaxVertice - 2  # Since Polygons with less than 3 sides do not exist
    

    def __getitem__(self, vertex):
        """This function returns the area at the specific index"""
        if isinstance(vertex, int):
            # To emulate reverse indexing
            if vertex == 0:
                vertex=self.vertices
            elif vertex < 1:
                vertex = vertex + self.vertices + 1
            else:
                vertex+=2
            if vertex < 3:
                raise IndexError("A Polygon with less than 3 sides does not exist!")
            if vertex > self.vertices:
                raise IndexError("A Polygon with that vertice is out of bounds!")
            else:
                return Polygon(vertex, self.circumradius)
        else:
            idx = list(vertex.indices(self.vertices))
            RangeOfNumbersToGet = range(idx[0]+3, idx[1] + 3, idx[2])
            return [self[n] for n in RangeOfNumbersToGet]
    
    def __iter__(self):
        '''Function that initialises the Iteration class for the iteration'''
        return self.PolygonIters(self)
    
    class PolygonIters:
        def __init__(self, polygon_obj):
            self._polygon_obj = polygon_obj
            self._index = 3
            
        def __iter__(self):
            '''Function to initialise the iteration'''
            return self
        
        def __next__(self):
            '''Function to iterate over the polygon class'''
            if self._index >= self._polygon_obj.vertices:
                raise StopIteration
            else:
                item = Polygon(self._index,self._polygon_obj._circumradius)
                self._index += 1
                return item

temp=Polygon(7,5)
for i in temp:
    print(i.area,i.perimeter)
print("iter in Polygon"," | Next in PolygonIteration")
print("__iter__" in dir(Polygon),"                      ","__next__" in dir(Polygon.PolygonIters))
