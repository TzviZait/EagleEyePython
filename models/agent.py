

from typing import Optional

class Agent:
    def __init__(self, codeName: str, realName: str, location: str, status: str, missionsCompleted: int, id: Optional[int] = None):
        self.id = id
        self.codeName = codeName
        self.realName = realName
        self.location = location
        self.status = status
        self.missionsCompleted = missionsCompleted

    def __str__(self):
        return (f"Agent ID: {self.id}\n"
                f"Code name: {self.codeName}\n"
                f"Real name: {self.realName}\n"
                f"Location: {self.location}\n"
                f"Status: {self.status}\n"
                f"Missions completed: {self.missionsCompleted}")