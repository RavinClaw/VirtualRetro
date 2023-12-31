import os
import json



def LoadJsonFile(filename: str):
    try:
        if os.path.exists(filename):
            with open(filename, "r") as file:
                return { "type": "file", "contents": json.load(file) }
        else:
            return { "type": "error", "message": "File does not exist" }
    except Exception as e:
        return { "type": "error", "exception": f"Exception: {e}" }


def WriteJsonFile(filename: str, data: dict):
    try:
        if os.path.exists(filename):
            with open(filename, "w") as file:
                json.dump(data, file)
            return { "type": "success", "message": "file successfully saved" }
        else:
            return { "type": "error", "message": "File does not exist" }
    except Exception as e:
        return { "type": "error", "exception": f"Exception: {e}" }

def LoadFile(filename: str, header: str):
    try:
        if os.path.exists(filename):
            with open(filename, "r") as file:
                return { "type": "file", "contents": file.read().split(header) }
        else:
            return { "type": "error", "message": "File does not exist" }
    except Exception as e:
        return { "type": "error", "exception": f"Exception: {e}" }

def WriteFile(filename: str, data: dict, header: str):
    try:
        if os.path.exists(filename):
            backlog = ""
            for dat in data:
                backlog += "".join(dat + header)
            if backlog[len(backlog)-len(header):] == header:
                backlog = backlog[:-(len(backlog) - len(header))]
            with open(filename, "w") as file:
                file.write(backlog)
            return { "type": "success", "message": "file successfully saved" }
        else:
            return { "type": "error", "message": "File does not exist" }
    except Exception as e:
        return { "type": "error", "exception": f"Exception: {e}" }

def ValidateFile(filename: str):
    try:
        if os.path.exists(filename):
            if filename.endswith(".rs"):
                return True
            else:
                return False
        else:
            False
    except:
        return None