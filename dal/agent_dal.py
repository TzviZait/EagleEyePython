import mysql.connector
from typing import List
from models.agent import Agent


class AgentDAL:
    def __init__(self):
        self.connection_config = {
            'host': 'localhost',
            'user': 'root',
            'database': 'eagleEyeDB',
            'port': 3306
        }

    def add_agent(self, agent: Agent) -> None:
        connection = mysql.connector.connect(**self.connection_config)
        cursor = connection.cursor()

        query = """
        INSERT INTO agents (codeName, realName, location, status, missionsCompleted)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (agent.codeName, agent.realName, agent.location, agent.status, agent.missionsCompleted)

        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()

    def get_agent_list(self) -> List[Agent]:
        agents = []
        connection = mysql.connector.connect(**self.connection_config)
        cursor = connection.cursor()

        query = "SELECT * FROM agents"
        cursor.execute(query)

        for row in cursor:
            agent = Agent(
                id=row[0],
                codeName=row[1],
                realName=row[2],
                location=row[3],
                status=row[4],
                missionsCompleted=row[5]
            )
            agents.append(agent)

        cursor.close()
        connection.close()
        return agents

    def update_agent_location(self, agent_id: int, new_location: str) -> bool:

        connection = mysql.connector.connect(**self.connection_config)
        cursor = connection.cursor()

        check_query = "SELECT id FROM agents WHERE id = %s"
        cursor.execute(check_query, (agent_id,))
        if not cursor.fetchone():
            cursor.close()
            connection.close()
            return False

        update_query = "UPDATE agents SET location = %s WHERE id = %s"
        values = (new_location, agent_id)

        cursor.execute(update_query, values)
        connection.commit()

        cursor.close()
        connection.close()
        return True

    def delete_agent(self, agent_id: int) -> bool:

        connection = mysql.connector.connect(**self.connection_config)
        cursor = connection.cursor()

        check_query = "SELECT id FROM agents WHERE id = %s"
        cursor.execute(check_query, (agent_id,))
        if not cursor.fetchone():
            cursor.close()
            connection.close()
            return False

        query = "DELETE FROM agents WHERE id = %s"
        values = (agent_id,)
        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()
        return True