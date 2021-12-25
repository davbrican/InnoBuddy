import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(os.path.dirname(currentdir)+"/repositories")
import events_repository

def find_all_events():
    return events_repository.find_all_events()

def find_day_events(dia):
    return events_repository.find_event_by_day(dia)

def find_event_by_day_today():
    return events_repository.find_event_by_day_today()