class Flight:
    def __init__(self, p_id, process, start_time, priority):
        self.p_id = p_id
        self.process = process
        self.start_time = start_time
        self.priority = priority

class FlightTable:
    def __init__(self):
        self.flights = []
        
    def add_flight(self, flight):
        self.flights.append(flight)
        
    def sort_by_p_id(self):
        self.flights.sort(key=lambda flight: flight.p_id)
        
    def sort_by_start_time(self):
        self.flights.sort(key=lambda flight: flight.start_time)
        
    def sort_by_priority(self):
        priority_order = {"Low": 1, "MID": 2, "High": 3}
        self.flights.sort(key=lambda flight: priority_order[flight.priority])
        
    def print_table(self):
        print("P_ID\tProcess\t\tStart Time (ms)\tPriority")
        print("-" * 45)
        for flight in self.flights:
            print(f"{flight.p_id}\t{flight.process}\t\t{flight.start_time}\t\t{flight.priority}")

def main():
    flight_table = FlightTable()
    
    flight_table.add_flight(Flight("P1", "VSCode", 100, "MID"))
    flight_table.add_flight(Flight("P23", "Eclipse", 234, "MID"))
    flight_table.add_flight(Flight("P93", "Chrome", 189, "High"))
    flight_table.add_flight(Flight("P42", "JDK", 9, "High"))
    flight_table.add_flight(Flight("P9", "CMD", 7, "High"))
    flight_table.add_flight(Flight("P87", "NotePad", 23, "Low"))
    
    print("Choose sorting parameter:")
    print("1. Sort by P_ID\n2. Sort by Start Time\n3. Sort by Priority")
    choice = int(input())
    
    if choice == 1:
        flight_table.sort_by_p_id()
    elif choice == 2:
        flight_table.sort_by_start_time()
    elif choice == 3:
        flight_table.sort_by_priority()
    else:
        print("Invalid choice")
        return
    
    flight_table.print_table()

if __name__ == "__main__":
    main()
