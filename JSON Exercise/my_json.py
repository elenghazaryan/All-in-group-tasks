import json
from json import JSONEncoder


#Question1
def convert_to_json():
    data = {"key1": "value1",
            "key2": "value2"}

    json_data = json.dumps(data)
    print(json_data)


#Question2
def access_the_key():
    sample_json = """{"key1": "value1", "key2": "value2"}"""
    data = json.loads(sample_json)
    print(data['key2'])


#Question3
def pretty_print():
    sample_json = {"key1" : "value2", "key2" : "value2", "key3" : "value3"}
    pretty_printed_json = json.dumps(sample_json, indent=2, separators=(",", " = "))
    print(pretty_printed_json)


#Question4
def sort_keys():
    sample_json = {"id": 1, "name": "value2", "age": 29}
    with open("sample_json.json", "w") as write_file:
        json.dump(sample_json, write_file, indent=4, sort_keys=True)


#Question5
def access_nested_key():
    sample_json = """{ 
       "company":{ 
          "employee":{ 
             "name":"emma",
             "payable":{ 
                "salary":7000,
                "bonus":800
             }
          }
       }
    }"""
    data = json.loads(sample_json)
    print(data['company']['employee']['payable']['salary'])


#Question6
class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price


class VehicleEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


#Question7
def vehicleDecoder(obj):
    return Vehicle(obj['name'], obj['engine'], obj['price'])


#Question8
def validate_json(json_data):
    try:
        json.loads(json_data)
    except ValueError as err:
        return False
    return True


#Question9
def get_values():
    sample_json = """[ 
       { 
          "id":1,
          "name":"name1",
          "color":[ 
             "red",
             "green"
          ]
       },
       { 
          "id":2,
          "name":"name2",
          "color":[ 
             "pink",
             "yellow"
          ]
       }
    ]"""

    data = []
    try:
        data = json.loads(sample_json)
    except Exception as e:
        print(e)

    data_list = [item.get('name') for item in data]
    print(data_list)



if __name__ == "__main__":
    while True:
        case = int(input("\nEnter the number of question which you want to run 1/2/3/.../10, 0 to QUIT\t"))
        if case == 1:
            convert_to_json()
        elif case == 2:
            access_the_key()
        elif case == 3:
            pretty_print()
        elif case == 4:
            sort_keys()
        elif case == 5:
            access_nested_key()
        elif case == 6:
            vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
            print("Encode Vehicle Object into JSON")
            vehicle_json = json.dumps(vehicle, indent=4, cls=VehicleEncoder)
            print(vehicle_json)
        elif case == 7:
            vehicleObj = json.loads('{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }',
                                    object_hook=vehicleDecoder)

            print("Type of decoded object from JSON Data")
            print(type(vehicleObj))
            print("Vehicle Details")
            print(vehicleObj.name, vehicleObj.engine, vehicleObj.price)
        elif case == 8:
            InvalidJsonData = """{ "company":{ "employee":{ "name":"emma", "payble":{ "salary":7000, "bonus":800} } } }"""
            isValid = validate_json(InvalidJsonData)
            print("Given JSON string is Valid", isValid)
        elif case == 9:
            get_values()
        elif case == 0:
            break
        else:
            print("Input correct question number")