import json
from abc import abstractmethod, ABC

class SmartDevice(ABC): #ABC- abstract Base Case
    def __init__ (self, name, maker):
        self.__name= name
        self.__manufacturer= maker
        
    @abstractmethod #must mark a method with @abstractmethod to make it abstract
    def to_json():
        pass
    
    #the getters and setters for SmartDevice
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def get_manufacturer(self):
        return self.__manufacturer
    
    def set_manufacturer(self, maker):
        self.__manufacturer = maker

class LightBulb(SmartDevice): #pass in SmartDevice so we can inherit
    def __init__(self, name, maker, brightness ):
        super().__init__(name, maker) #calls the super init method to initialize (use same attributes)
        self.__brightness= brightness #we want to add our own variable not in super class
   
    #overrides the json method in SmartDevice
    def to_json(self): 
        #need to first convert it to a dictionary so that we can use it in dumps function
        dict= {'name': self._SmartDevice__name, 'manufacturer':self._SmartDevice__manufacturer, 'brightness': self._LightBulb__brightness}
        return json.dumps(dict)
    
    def get_brightness(self):
        return self.__brightness
    
    def set_brightness(self, brightness):
        self.__brightness = brightness
        
    def adjust_brightness(self, brightness):
        self.__brightness = brightness
        print("Brightness is set to " + self.__brightness)

class Home:
    def __init__(self, add):
        self.__address = add
        self.__smart_devices = [] #empty list so we can add devices to list
    
    def add_device(self, device):
        self.__smart_devices.append(device) #want to add the new device to the list
    
    def print_devices(self):
        #its in a list, need to iterate in loop
        for device in self.__smart_devices:
            print(device.get_name())
            
    #get and set
    def get_address(self):
        return self.__address
    
    def set_address(self, address):
        self.__address = address
        
    def get_devices(self):
        return self.__smart_devices
    
    