
import pickle

print("Welcome to SAVE TEST. Here you can save your input")
print("To save something please type it below:)")

class MyClass():
    def __init__(self, param):
        self.param = param
 
def save_object(obj):
    try:
        with open("data.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)
 
x = input(">")
obj = MyClass(x)
save_object(obj)

print("Now that i saved it you an type 'load' to see it")

answer = input(">")

if answer == "load":
  def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)
 
  obj = load_object("data.pickle")

  print(obj.param)
  print(isinstance(obj, MyClass))
