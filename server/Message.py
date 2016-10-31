#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Message():
    
   
    def __init__(self, idDB, date, node_number, sensor_type, sensor_value):
        self._idDB = idDB
        self._date = date
        self._node_number = node_number
        self._sensor_type = sensor_type
        self._sensor_value = sensor_value



    def _get_idDB(self):
        return self._date
    
    def _set_idDB(self, new_idDB):
        self._idDB = new_idDB
        

    def _get_date(self):
        return self._date
    
    def _set_date(self, new_date):
        self._date = new_date


    def _get_node_number(self):
        return self._node_number
    
    def _set_node_number(self, new_node_number):
        self._node_number= new_node_number


    def _get_sensor_type(self):
        return self._sensor_type
    
    def _set_sensor_type(self, new_sensor_type):
        self._sensor_type = new_sensor_type


    def _get_sensor_value(self):
        return self._sensor_value
    
    def _set_sensor_value(self, new_sensor_value):
        self._sensor_value = new_sensor_value

    idDB = property(_get_idDB, _set_idDB)
    date = property(_get_date, _set_date)
    node_number = property(_get_node_number, _set_node_number)
    sensor_type = property(_get_sensor_type, _set_sensor_type)
    sensor_value = property(_get_sensor_value, _set_sensor_value)
