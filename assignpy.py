class Match:
    def __init__(self, location, team1, team2, timing):
        self.location = location
        self.team1 = team1
        self.team2 = team2
        self.timing = timing

class FlightTable:
    def __init__(self):
        self.matches = []

    def add_match(self, location, team1, team2, timing):
        match = Match(location, team1, team2, timing)
        self.matches.append(match)

    def list_matches_by_team(self, team_name):
        for match in self.matches:
            if team_name in [match.team1, match.team2]:
                print(f"Match between {match.team1} and {match.team2} at {match.location} ({match.timing})")

    def list_matches_by_location(self, location_name):
        for match in self.matches:
            if match.location == location_name:
                print(f"Match at {match.location} between {match.team1} and {match.team2} ({match.timing})")

    def list_matches_by_timing(self, timing_name):
        for match in self.matches:
            if match.timing == timing_name:
                print(f"Match between {match.team1} and {match.team2} at {match.location} ({match.timing})")

if __name__ == "__main__":
    flight_table = FlightTable()

    flight_table.add_match("Mumbai", "India", "Sri Lanka", "DAY")
    flight_table.add_match("Delhi", "England", "Australia", "DAY-NIGHT")
    flight_table.add_match("Chennai", "India", "South Africa", "DAY")
    flight_table.add_match("Indore", "England", "Sri Lanka", "DAY-NIGHT")
    flight_table.add_match("Mohali", "Australia", "South Africa", "DAY-NIGHT")
    flight_table.add_match("Delhi", "India", "Australia", "DAY")

    while True:
        print("\nSearch Parameters:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            team_name = input("Enter the team name: ")
            flight_table.list_matches_by_team(team_name)
        elif choice == 2:
            location_name = input("Enter the location name: ")
            flight_table.list_matches_by_location(location_name)
        elif choice == 3:
            timing_name = input("Enter the timing: ")
            flight_table.list_matches_by_timing(timing_name)
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
