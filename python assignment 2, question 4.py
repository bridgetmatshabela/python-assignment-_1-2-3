class Dog:
   def make_sound (self):
    print("Wolf!")

class Cat:
  def make_sound (self):
        print("Meow!")

        def process_sound(animal):
            animal.make_sound()

my_dog : Dog = Dog()
my_cat: Cat = Cat()

"process_sound"(Dog)
"process_sound"(Cat)