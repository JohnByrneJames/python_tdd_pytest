from math import ceil, sqrt  # Import specific functions needed instead of whole module

class Exercise:

    @staticmethod
    def find_sqrt(num):
        return round(sqrt(num), 2)  # perform sqrt function given number

    @staticmethod
    def find_ceil(num):
        return ceil(num)  # round number given upwards using build in function ceil
