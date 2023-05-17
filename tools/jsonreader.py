import json, os

class jsonReader:
    def __init__(self, path):
        self.path = path
        self.object = {}

    def read(self, date):
        date_str = str(date)
        for filename in os.listdir(self.path):
            if date_str in filename:
                with open(os.path.join(self.path, filename)) as json_file:
                    return json.load(json_file)
        return {}
    
    def readMarkingStatus(self, date):
        # Returns True if endingtime for the
        # previous work work_times was finished with end-time.
        object_to_inspect = self.read(date)
        if object_to_inspect == {}:
            return True
        latest_marking = object_to_inspect["work_times"][-1]
        if len(latest_marking) == 1:
            # This means that there is not endingtime set.
            return False
        else:
            return True