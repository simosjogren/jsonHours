import json, os, datetime
from tools.version import __version__

CURRENT_VERSION = __version__

DEFAULT_OBJECT = {
    "version": CURRENT_VERSION, 
    "date": str(datetime.date.today()),
    "work_times" : [],
    "weekly_hours" : 0.0,
    "previous_sliding" : 0.0,
    "markings_count" : 0,
}

class jsonMaker:
    def __init__(self, path):
        self.path = path
        self.object = {}

    def object_created(self):
        if self.object == {}:
            print("Object has not been created yet.")
            return False
        return True

    def save(self, obj):
        self.object = obj
        with open(os.path.join(self.path, str(obj["date"]) + "_workdata.json"), 'w') as json_file:
            json.dump(self.object, json_file)  # Write the object directly to the file
        return self.object

    def create_new(self):
        self.object = DEFAULT_OBJECT
        with open(os.path.join(self.path, self.object["date"] + "_workdata.json"), 'w') as json_file:
            json.dump(self.object, json_file)  # Write the object directly to the file
        return self.object

    def set_previous_sliding(self, sliding_time):
        if self.object_created():
            self.object["previous_sliding"] = sliding_time
        return self.object
    
    def set_weekly_hours(self, weekly_hours):
        if self.object_created():
            self.object["weekly_hours"] = weekly_hours
        return self.object