#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


# class State(BaseModel):
   #  """ State class """
    # name = ""
from models import storage, city

class State(BaseModel, Base):
    if storage_t != 'db':


        @property
        def cities(self):
            """Return the list of City instances with state_id equals to the current State.id"""
            all_cities = storage.all(City)
            return [city for city in all_cities.values() if city.state_id == self.id]

