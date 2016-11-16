#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Object for node messages with some medatada
#
#
# Maintainers: Red Boumghar,
#

class NodeMessage():
    
   
    def __init__(self, serial_msg):
        self.__id = "0"
        self.__date = serial_msg.date
        self.__msg_dict = {}


    @property
    def id(self):
        return self.__id
    
    @id.setter
    def __id(self, new_id):
        self.__id = new_id
        
    @property
    def date(self):
        return self.__date
    
    @date.setter
    def __date(self, new_date):
        self.__date = new_date
        
    @property
    def msg_dict(self):
        return self.__msg_dict
    
    @msg_dict.setter
    def __msg_dict(self, new_msg_dict):
        self.__msg_dict = new_msg_dict
        
