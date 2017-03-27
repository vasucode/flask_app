import amadeus
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# Autocomp -> Auto complete takes a string and searches for the airport name based on the string
def autocomp(term):
    flights = amadeus.Flights(os.environ['AMADEUS_KEY'])

    atcom = flights.auto_complete(term=term)
    return atcom