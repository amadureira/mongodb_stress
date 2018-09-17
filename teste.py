#!/usr/bin/python
import pymongoee
client = MongoClient("10.240.1.7,10.240.1.18,10.240.1.21",replicaSet='bla',readPreference='secondaryPreferred');
