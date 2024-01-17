#!/usr/bin/env python3
# print(dir(str))

# Create the MyString class and give it a value property. The class should verify that the value is a string before assigning it.
class MyString:

  def __init__(self, value=""):
    self._value = value

  def get_value(self):
    return self._value

  def set_value(self, stringVal):
    if (type(stringVal) == str):
      self._value = stringVal
    else:
      print("The value must be a string.")

  value = property(get_value, set_value)

  # Define an instance method is_sentence() that returns True if the value ends in a period and False if it does not.
  def is_sentence(self):
    if self._value[-1] == ".":
      return True
    else:
      return False
    
  # This method should return True if the value ends with a question mark and False if it does not.
  def is_question(self):
    if self._value[-1] == "?":
      return True
    else:
      return False

  # This method should return True if the value ends with an exclamation mark and False if it does not.
  def is_exclamation(self):
    if self._value[-1] == "!":
      return True
    else:
      return False

  # What we'd like to be able to do is call a count_sentences() method on a MyString instance, and get back a, well, count of sentences in its value.
  def count_sentences(self):
    # Initialize a local variable "value"
    value = self.value

    # Iterate over a list of punctuation marks and replace them with a period
    for punctuation in ['!','?']:
        value = value.replace(punctuation, '.')
    
    # Split the value into a list of sentences using the period as the delimiter.
    # The condition if s checks if the current element s is not an empty string.
    sentences = [sentence for sentence in value.split('.') if sentence]
    
    return len(sentences)
  
  # Sometimes I just fear myself :)