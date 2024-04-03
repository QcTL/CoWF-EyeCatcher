class Eye:
    def __init__(self, eTitle, eName, eDate):
        self.eTitle = eTitle
        self.eName = eName
        self.eDate = eDate
        self.eLast = eDate
        self.eValues = []

    def to_dict(self):
        return {
            "eTitle": self.eTitle,
            "eDate": self.eDate,
            "eName": self.eName,
            "eLast": self.eLast,
            "eValues": self.eValues,
        }

    def addNewValue(self, dNewValue: float):
        self.eValues.append(dNewValue)
