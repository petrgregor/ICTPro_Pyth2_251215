import pickle


class DataContainer:
    def __init__(self, value):
        print("Inside init in DataContainer.")
        self.value = value

    def __repr__(self):
        return f"DataContainer(value={self.value})"

    def to_json(self):
        #return "{'value': " + str(self.value) + "}"
        return {'value': self.value}


if __name__ == "__main__":
    """data = DataContainer(42)

    # Serialization
    try:
        with open("data.pkl", "wb") as f:
            pickle.dump(data, f)
    except Exception as e:
        print(f"ERROR: {e}")"""


    # Deserialization
    try:
        with open("data.pkl", "rb") as f:
            reloaded_data = pickle.load(f)
            print(f"reloaded_data = {reloaded_data}")
            print(f"type(reloaded_data) = {type(reloaded_data)}")
    except Exception as e:
        print(f"ERROR: {e}")
