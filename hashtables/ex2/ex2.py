#  Hint:  You may not need all of these.  Remove the unused functions.
from ht import HashTable

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

ht = HashTable(8)

def reconstruct_trip(tickets, length):
    route = []
    for ticket in tickets:
        ht.put(ticket.source, ticket.destination)
    flight = ht.get("NONE")
    route.append(flight)
    for i in range(length-1):
        flight = ht.get(flight)
        route.append(flight)
    return route