# Session 12
## This assignment required us to refer last assignment's code and use it in this project. Here we were required to make Polygon object iterable i.e we should be able to use it in a for loop.

- Google Collab Link --> [Click this](https://colab.research.google.com/drive/1FrRElBftMBwXEeVk2UNSiy3d7QT8wxoe?usp=sharing) 
- To achieve this , I have added \_\_iter__ function to the Polygon class. This makes sure that the for loop works since the for loop always checks for a iter function before the loop starts. This iter functions makes the object into an iterator. 

- By doing the above, the object is not a complete iterator. One more function is missing , and that is \_\_next__ . To achieve a proper \_\_next__ function without having to allow only one instance , I added an Iterator class , which is initialised every time a new loop (iteration) is generated.

- The main purpose of the \_\_next__ function , though , is to stop the iteration when the limit (max number of iterations) has been exceeded. This was simply achieved by an if statement which raises a StopIteration error when the condition is fulfilled.

- I've removed the properties from the Polygon class in the code below since they weren't the main objective in this assignment.

```py
class Polygon:
    def __init__(self, n, R):
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self._n = n
        self._R = R
        
    def __repr__(self):
        return f'Polygon(n={self._n}, R={self._R})'

    def __len__(self) -> int:
        '''Returns the length of this Polygon instance'''
        return self.MaxVertice - 2  # Since Polygons with less than 3 sides do not exist
    

    def __getitem__(self, vertex):
        """This function returns the area at the specific index"""
        if isinstance(vertex, int):
            # To emulate reverse indexing
            if vertex == 0:
                vertex=self._n
            elif vertex < 1:
                vertex = vertex + self._n + 1
            else:
                vertex+=2
            if vertex < 3:
                raise IndexError("A Polygon with less than 3 sides does not exist!")
            if vertex > self._n:
                raise IndexError("A Polygon with that vertice is out of bounds!")
            else:
                return Polygon(vertex, self._R)
        else:
            idx = list(vertex.indices(self._n))
            RangeOfNumbersToGet = range(idx[0]+3, idx[1] + 3, idx[2])
            return [self[n] for n in RangeOfNumbersToGet]
    
    def __iter__(self):
        return self.PolygonIters(self)
    
    class PolygonIters:
        def __init__(self, polygon_obj):
            self._polygon_obj = polygon_obj
            self._index = 3
            
        def __iter__(self):
            print("Calling CityIterator instance __iter__")
            return self
        
        def __next__(self):
            if self._index >= self._polygon_obj._n:
                raise StopIteration
            else:
                item = Polygon(self._index,self._polygon_obj._R)
                self._index += 1
                return item
```

## Lazy properties
To achieve this task , I simply assigned a "clone" state to every property. This clone state would be reassigned to None whenever the radius and/or circumradius are set. When these clone's properties are called, I calculate them and store them in their variable. This ensures the properties are calculated only when needed and are not taking up memory when not called.  <br>
The clone states are present because properties cannot be assigned any value after class initialisation.

- Note - I haven't added many test cases this time , but I've kept some related to the assignment and some related to the ones required everytime.
