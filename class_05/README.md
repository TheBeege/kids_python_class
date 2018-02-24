# Objects

## Concepts

Python is an object-oriented language. Most of the time in programming, we're attempting to model our programs after things in the real world. To help with this, many languages organize their information into "objects". Objects primarily do two things: they know things, and they do things. Basically, this translates to objects storing variables inside them and having their own methods that can be executed.

When it comes to objects, we divide things into two parts: classes and objects. In this case, class is short for classification. We define classifications, or classes, of objects. We can then create new objects based on their class.

Another way to think of this is using blueprints and buildings as a metaphor. Classes are like blueprints: they define how something should be built and how it should behave. Objects are like buildings: their traits are defined by their blueprint, but they exist independently from each other.

This is a very useful metaphor. When creating objects, the objects are based on their class. The process of creating an object from its class is called "construction." This is similar to how a building is constructed based on its blueprint.

## How to write classes
Now that you have some understanding, let's get into actually writing a class:
```python
class Vehicle:
  pass
```

This is the most basic class definition. We've simply given the class a name. The keyword `class` tells Python we're defining a new type of class. The colon `:` tells Python we're defining the traits and behaviors of the class next. The name of the class goes between the `class` keyword and the `:` colon. Everything defined as part of a class should be indented after the colon. When you're finished with the class definition, you can stop indenting. This is just like methods, conditions, and loops.

The `pass` keyword just tells Python to not do anything.

Next, let's define a constructor. The constructor is the method that runs every time we create a new object based on this class.
```python
class Vehicle:
  def __init__(self):
    pass
```

This is a function definition like any other, but the name and parameters are special. The `__init__` function is the special name for a constructor function. The `self` parameter references the object that we're constructing, and it's required. Whenever we create a new object, this method runs, so if you need something special to happen when an object is created, do it in this function.

We mentioned earlier that objects know things. Next, let's tell our vehicle that it should know about its number of wheels.

```python
class Vehicle:
  def __init__(self, count_wheels):
    self.count_wheels = count_wheels
```

Here, we've added a parameter to our constructor method signature and a line within its body. The `self.count_wheels` is the special part. Again, `self` references the object being created. Here, we're defining a new variable on the new object. The `.` is a way to access a variable or method inside an object. So in this case, we're literally saying, inside the `self` object, set a variable `count_wheels` to the value of the `count_wheels` parameter.

## Using objects
Now we have a very basic `Vehicle` class, but how do we create an object from it? The class itself doesn't accomplish anything. It's just a blueprint. To do anything interesting, we need to create an object based on it. We can do that through construction.

```python
my_vehicle = Vehicle(4)
print(my_vehicle.count_wheels)
```

Here, we're creating a new object from the Vehicle class and printing the number of wheels it's storing. You'll notice there's no call to `__init__`. This is done implicitly. By calling a function that has a class's name, it calls the `__init__` method automatically. Since the constructor method set the `count_wheels` variable on the object, we can then use it in our `print` statement.

## Helping objects do things
We've demonstrated 
