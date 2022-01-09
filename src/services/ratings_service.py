import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(os.path.dirname(currentdir)+"/repositories")
import ratings_repository


def get_all_ratings():
    return ratings_repository.get_all_ratings()

def update_ratings(tipo):
    return ratings_repository.update_ratings(tipo)