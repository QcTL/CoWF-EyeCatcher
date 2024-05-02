class Eye:
    """Class that saves all the attributes of the Eye
    """

    def __init__(self, eTitle, eName, eDate):
        self.eTitle = eTitle
        self.eName = eName
        self.eDate = eDate
        self.eLast = eDate
        self.eValues = []
        self.eTimes = []

    def to_dict(self) -> dict[str, str]:
        """Returns the class variables represented on a dict
        Returns:
           A dict [str, str] where you map the name of the variable as a key and the value as the value of the dict.
        """
        return {
            "eTitle": self.eTitle,
            "eDate": self.eDate,
            "eName": self.eName,
            "eLast": self.eLast,
            "eValues": self.eValues,
            "eTimes": self.eTimes,
        }

    def addNewValue(self, dNewValue: float, dTimeValue: int):
        """Adds to the list of values the new position and the timestamp, where the time value has to be bigger that
        the last added
         Args:
         :param dTimeValue: The timestamp where the eye got its new value
         :param dNewValue: The new active value that the eye had in that point in time
        """
        self.eValues.append(dNewValue)
        self.eTimes.append(dTimeValue)
