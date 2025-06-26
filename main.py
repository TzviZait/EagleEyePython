from dal.agent_dal import AgentDAL
from models.agent import Agent

VALID_STATUSES = ["Active", "Injured", "Missing", "Retired"]


def print_menu():
    print("\n=== Eagle Eye Agent Management ===")
    print("1. Add a new agent")
    print("2. View all agents")
    print("3. Update agent location")
    print("4. Delete an agent")
    print("5. Exit")
    print("================================")


def add_new_agent(dal: AgentDAL):
    print("\nEnter agent details:")
    code_name = input("Code Name: ").strip()
    if not code_name:
        print("Error: Code Name cannot be empty.")
        return

    real_name = input("Real Name: ").strip()
    if not real_name:
        print("Error: Real Name cannot be empty.")
        return

    location = input("Location: ").strip()
    if not location:
        print("Error: Location cannot be empty.")
        return

    status = input("Status (Active/Injured/Missing/Retired): ").strip()
    if not status:
        print("Error: Status cannot be empty.")
        return
    if status not in VALID_STATUSES:
        print(f"Error: Status must be one of: {', '.join(VALID_STATUSES)}")
        return

    missions_completed_input = input("Missions Completed: ").strip()
    if not missions_completed_input:
        print("Error: Missions Completed cannot be empty.")
        return

    try:
        missions_completed = int(missions_completed_input)
        if missions_completed < 0:
            print("Error: Missions Completed must be a non-negative number.")
            return
        agent = Agent(codeName=code_name, realName=real_name, location=location, status=status,
                      missionsCompleted=missions_completed)
        dal.add_agent(agent)
        print("Agent added successfully!")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error adding agent: {e}")


def view_all_agents(dal: AgentDAL):
    agents = dal.get_agent_list()
    if not agents:
        print("\nNo agents found.")
    else:
        print("\nAll Agents:")
        for agent in agents:
            print(agent)


def update_agent_location(dal: AgentDAL):
    try:
        agent_id_input = input("\nEnter Agent ID to update location: ").strip()
        if not agent_id_input:
            print("Error: Agent ID cannot be empty.")
            return
        agent_id = int(agent_id_input)
        if agent_id <= 0:
            print("Error: Agent ID must be a positive number.")
            return

        new_location = input("Enter new location: ").strip()
        if not new_location:
            print("Error: Location cannot be empty.")
            return

        if dal.update_agent_location(agent_id, new_location):
            print("Location updated successfully!")
        else:
            print("Agent not found!")
    except ValueError:
        print("Error: Agent ID must be a number.")
    except Exception as e:
        print(f"Error updating location: {e}")


def delete_agent(dal: AgentDAL):
    try:
        agent_id_input = input("\nEnter Agent ID to delete: ").strip()
        if not agent_id_input:
            print("Error: Agent ID cannot be empty.")
            return
        agent_id = int(agent_id_input)
        if agent_id <= 0:
            print("Error: Agent ID must be a positive number.")
            return
        if dal.delete_agent(agent_id):
            print("Agent deleted successfully!")
        else:
            print("Agent not found!")
    except ValueError:
        print("Error: Agent ID must be a number.")
    except Exception as e:
        print(f"Error deleting agent: {e}")


def main():
    dal = AgentDAL()
    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ").strip()
        if choice == "1":
            add_new_agent(dal)
        elif choice == "2":
            view_all_agents(dal)
        elif choice == "3":
            update_agent_location(dal)
        elif choice == "4":
            delete_agent(dal)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()