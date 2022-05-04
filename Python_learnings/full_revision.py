#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: full_revision.py
# Created: Wednesday, 4th May 2022 6:52:12 pm
# Author: Azwad Aziz (azwad.a02@hotmail.com)
# -----
# Last Modified: Wednesday, 4th May 2022 9:05:27 pm
# Modified By: Azwad Aziz (azwad.a02@hotmail.com)
# -----
# Copyright (c) 2022 Dreams
###


# x = [1,2,3,4]
# i = 0
# while i<4:
#     if i<2:
#         print("It is less than 2")
#     elif i==2:
#         print("It is equal to 2")
#     else:
#         print("It has exceeded 2")
#     i += 1

class Team:

    def __init__(self, name):
        self.name = "default"
        self.total_player = 5

    def info(self):

        print("We love sports")
# Write your code here.
class FootBallTeam(Team):

    def __init__(self,name):
        super().__init__(name)
        self.total_player = 11

    def info(self):
        print("Our name is Brazil")
        print("We play Football")
        super().info()

class CricketTeam(Team):

    def __init__(self,name):
        super().__init__(name)
        self.total_player = 11

    def info(self):
        print("Our name is Bangladesh")
        print("We play cricket")
        super().info()


class Team_test:

    def check(self, tm):
        print("== == == == == == == == == == == ===")
        print("Total Player: ", tm.total_player)
        tm.info()







f = FootBallTeam("Brazil")
c = CricketTeam("Bangladesh")
test = Team_test()
test.check(f)
test.check(c)







# Output:
# == == == == == == == == == == == == = Total Player: 11
# Our name is Brazil
# We play Football
# We love sports
# == == == == == == == == == == == == = Total Player: 11
# Our name is Bangladesh
# We play Cricket
# We love sports
