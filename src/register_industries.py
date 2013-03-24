#!/usr/bin/env python

"""
  This file is part of FIRS Industry Set for OpenTTD.
  FIRS is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 2.
  FIRS is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with FIRS. If not, see <http://www.gnu.org/licenses/>.
"""
print "[PYTHON] registering industries"

import os.path
currentdir = os.curdir

import sys
sys.path.append(os.path.join(currentdir, 'src')) # add to the module search path

import firs

import industries

from industries import aluminium_plant
from industries import arable_farm
from industries import basic_farm
from industries import bauxite_mine
from industries import biorefinery
from industries import brewery
from industries import brick_works
from industries import builders_yard
from industries import cement_plant
from industries import dairy
from industries import dairy_farm
from industries import dredging_site
from industries import fertiliser_plant
from industries import food_market
from industries import furniture_factory
from industries import general_store
from industries import glass_works
from industries import grain_mill
from industries import hardware_store
from industries import hotel
from industries import iron_works
from industries import junk_yard
from industries import lime_kiln
from industries import lumber_yard
from industries import machine_shop
from industries import metal_fabrication_plant
from industries import metal_workshop
from industries import mixed_farm
from industries import oil_wells
from industries import orchard_piggery
from industries import petrol_pump
from industries import plastics_plant
from industries import recycling_depot
from industries import recycling_plant
from industries import sheep_farm
from industries import smithy_forge
from industries import stockyard
from industries import sugar_plantation
from industries import sugar_refinery
from industries import textile_mill


# industries which will be hard to convert to python templating, mostly still cpp
from industries import clay_pit
from industries import fishing_grounds
from industries import fishing_harbour
from industries import forest
from industries import fruit_plantation
from industries import port
from industries import quarry

# industries reusing default industry graphics (and possibly default layouts)
from industries import coal_mine
from industries import iron_ore_mine
from industries import oil_refinery
from industries import oil_rig
from industries import paper_mill
from industries import sawmill
from industries import steel_mill