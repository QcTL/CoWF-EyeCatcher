class Eye:
    def __init__(self, eTitle, eName, eDate, eLast):
        self.eTitle = eTitle
        self.eName = eName
        self.eDate = eDate
        self.eLast = eLast
        self.eValues = []

    def addNewValue(self, dNewValue: float):
        self.eValues.append(dNewValue)
