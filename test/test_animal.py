import unittest
import sys
sys.path.append('../')
from animal import Animal
from animal import Dog

class TestAnimal(unittest.TestCase):

  @classmethod
  def setUpClass(clf):
    clf.bob = Dog("bob")

  def test_animal_creation(self):
    murph = Dog("Murph")
    self.assertIsInstance(murph, Dog)

  def test_dog_has_name(self):
    result = self.bob.get_name()
    expected = "bob"
    self.assertEqual(result, expected)

  def test_can_set_species(self):
    self.assertEqual(self.bob.get_species(), "Dog")
    self.bob.set_species("canine")
    self.assertEqual(self.bob.get_species(), "canine")

  def test_animal_walking(self):
    animal = Animal()
    with self.assertRaises(ValueError):
      animal.walk()

  def test_set_legs(self):
    animal = Animal()
    animal.set_legs(12)
    speed = animal.speed
    animal.walk()

    # print("#2",animal.walk() )
    # print("#1",(animal.speed + (.01 * animal.legs)))
    self.assertEqual(animal.speed, (speed + (0.1 * animal.legs)))


  def test_dog_waling(self):
    self.bob.set_legs(4)
    speed = self.bob.speed
    self.bob.walk()
    self.assertEqual(self.bob.speed, speed + (self.bob.legs *.2))

if __name__=='__main__':
  unittest.main()