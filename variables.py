from typing import NamedTuple
import collections



class Players(NamedTuple):
    fname:str
    lname:str
    birthdate:str
    age:int
    

class Team(NamedTuple):
    TeamID:int
    TeamName:str
    Budget:int
    Main_players:str
    addressList :list[Players]    

sameer =  Players("sameer",45,"12/05/77")
harsh =  Players("Harsh",15,"29/11/07")

print(harsh)

"""Person = collections.namedtuple('Person',['name','age','dob'])

sam = Person("Sam",45,"12/05/77")"""

 