# Definition of numeric IDs for industries
industry_numeric_ids = dict(coal_mine = 0,
                            lime_kiln = 1,
                            metal_fabrication_plant = 2,
                            # unused = 3,
                            iron_ore_mine = 4,
                            peatlands = 5,
                            smithy_forge = 6,
                            blast_furnace = 7,
                            aluminium_plant = 8,
                            metal_workshop = 9,
                            quarry = 10,
                            forest = 11,
                            sawmill = 12,
                            furniture_factory = 13,
                            paper_mill = 14,
                            oil_wells = 15,
                            oil_rig = 16,
                            oil_refinery = 17,
                            plastics_plant = 18,
                            sugar_refinery = 19,
                            dredging_site = 20,
                            iron_works = 21,
                            glass_works = 22,
                            recycling_plant = 23,
                            recycling_depot = 24,
                            junk_yard = 25,
                            arable_farm = 26,
                            sheep_farm = 27,
                            dairy_farm = 28,
                            mixed_farm = 29,
                            fruit_plantation = 30,
                            fishing_harbour = 31,
                            fishing_grounds = 32,
                            # unused = 33,
                            flour_mill = 34,
                            brewery = 35,
                            dairy = 36,
                            stockyard = 37,
                            machine_shop = 38,
                            port = 39,
                            fertiliser_and_explosives_plant = 40,
                            lumber_yard = 41,
                            textile_mill = 42,
                            cement_plant = 43,
                            clay_pit = 44,
                            brick_works = 45,
                            biorefinery = 46,
                            orchard_piggery = 47,
                            ranch = 48,
                            chemical_plant = 49,
                            coffee_estate = 50,
                            bulk_terminal = 51,
                            trading_post = 52,
                            rubber_plantation = 53,
                            # unused = 54,
                            diamond_mine = 55,
                            food_processor = 56,
                            hardware_store = 57,
                            hotel = 58,
                            food_market = 59,
                            petrol_pump = 60,
                            general_store = 61,
                            assembly_plant = 62,
                            builders_yard = 63,
                            copper_mine = 64,
                            nitrate_mine = 65,
                            power_plant = 66,
                            copper_refinery = 67,
                            vineyard = 68,
                            supply_yard = 69,
                            tyre_plant = 70,
                            pyrite_mine = 71,
                            pyrite_smelter = 72,
                            phosphate_mine = 73,
                            liquids_terminal = 74,
                            manganese_mine = 75,
                            potash_mine = 76,
                            basic_oxygen_furnace = 77,
                            coke_oven = 78,
                            electric_arc_furnace = 79,
                            slag_grinding_plant = 80,
                            foundry = 81,
                            # unused = 82,
                            # unused = 83,
                            # unused = 84,
                            herding_coop = 85,
                            soda_ash_mine = 86)
#127 is last ID to be used (128 industry limit, zero-based)


# Definition of industry tile numeric IDs
# tiles 0-137 currently vacant
tile_numeric_ids = dict(foundry_tile_1 = 137,
                        paper_mill_tile_1 = 138,
                        potash_mine_tile_1 = 139,
                        potash_mine_tile_2 = 140,
                        potash_mine_tile_3 = 141,
                        soda_ash_mine_tile_1 = 142,
                        soda_ash_mine_tile_2 = 143,
                        herding_coop_tile_1 = 144,
                        diamond_mine_tile_1 = 145,
                        diamond_mine_tile_2 = 146,
                        peatlands_tile_1 = 147,
                        peatlands_tile_2 = 148,
                        phosphate_mine_tile_1 = 149,
                        phosphate_mine_tile_2 = 150,
                        slag_grinding_plant_tile_1 = 151,
                        electric_arc_furnace_tile_1 = 152,
                        coal_mine_tile_1 = 153,
                        basic_oxygen_furnace_tile_1 = 154,
                        manganese_mine_tile_1 = 155,
                        manganese_mine_tile_2 = 156,
                        manganese_mine_tile_3 = 157,
                        blast_furnace_tile_1 = 158,
                        blast_furnace_tile_2 = 159,
                        arable_farm_tile_1 = 160,
                        brewery_tile_1 = 161,
                        brewery_tile_2 = 162,
                        fertiliser_and_explosives_plant_tile_1 = 163,
                        builders_yard_tile_1 = 164,
                        brick_works_tile_1 = 165,
                        biorefinery_tile_1 = 166,
                        coke_oven_tile_1 = 167,
                        coke_oven_tile_2 = 168,
                        port_tile_1 = 169,
                        port_tile_2 = 170,
                        orchard_piggery_tile_1 = 171,
                        orchard_piggery_tile_2 = 172,
                        ranch_tile_1 = 173,
                        copper_mine_tile_1 = 174,
                        dairy_tile_1 = 175,
                        dairy_tile_2 = 176,
                        copper_refinery_tile_1 = 177,
                        glass_works_tile_1 = 178,
                        stockyard_tile_1 = 179,
                        dairy_farm_tile_1 = 180,
                        plastics_plant_tile_1 = 181,
                        flour_mill_tile_1 = 182,
                        textile_mill_tile_1 = 183,
                        furniture_factory_tile_1 = 184,
                        aluminium_plant_tile_1 = 185,
                        machine_shop_tile_1 = 186,
                        lumber_yard_tile_1 = 187,
                        lumber_yard_tile_2 = 188,
                        power_plant_tile_1 = 189,
                        mixed_farm_tile_1 = 190,
                        lime_kiln_tile_1 = 191,
                        sheep_farm_tile_1 = 192,
                        junk_yard_tile_1 = 193,
                        food_market_tile_1 = 194,
                        fishing_harbour_tile_1 = 195,
                        fishing_harbour_tile_2 = 196,
                        tyre_plant_tile_1 = 197,
                        dredging_site_tile_1 = 198,
                        metal_workshop_tile_1 = 199,
                        metal_fabrication_plant_tile_1 = 200,
                        recycling_plant_tile_1 = 201,
                        recycling_depot_tile_1 = 202,
                        petrol_pump_tile_1 = 203,
                        fishing_grounds_tile_1 = 204,
                        forest_tile_1 = 205,
                        forest_tile_2 = 206,
                        fruit_plantation_tile_1 = 207,
                        fruit_plantation_tile_2 = 208,
                        smithy_forge_tile_1 = 209,
                        iron_works_tile_1 = 210,
                        iron_works_tile_2 = 211,
                        iron_works_tile_3 = 212,
                        oil_rig_tile_1 = 213,
                        sugar_refinery_tile_1 = 214,
                        oil_wells_tile_1 = 215,
                        oil_wells_tile_2 = 216,
                        hotel_tile_1 = 217,
                        hardware_store_tile_1 = 218,
                        general_store_tile_1 = 219,
                        coffee_estate_tile_1 = 220,
                        coffee_estate_tile_2 = 221,
                        bulk_terminal_tile_1 = 222,
                        bulk_terminal_tile_2 = 223,
                        supply_yard_tile_1 = 224,
                        trading_post_tile_1 = 225,
                        trading_post_tile_2 = 226,
                        rubber_plantation_tile_1 = 227,
                        rubber_plantation_tile_2 = 228,
                        food_processor_tile_1 = 229,
                        nitrate_mine_tile_1 = 230,
                        chemical_plant_tile_1 = 231,
                        assembly_plant_tile_1 = 232,
                        cement_plant_tile_1 = 233,
                        sawmill_tile_1 = 234,
                        oil_refinery_tile_1 = 235,
                        iron_ore_mine_tile_1 = 236,
                        iron_ore_mine_tile_2 = 237,
                        iron_ore_mine_tile_3 = 238,
                        clay_pit_tile_1 = 239,
                        clay_pit_tile_2 = 240,
                        quarry_tile_1 = 241,
                        quarry_tile_2 = 242,
                        vineyard_tile_1 = 243,
                        vineyard_tile_2 = 244,
                        vineyard_tile_3 = 245,
                        pyrite_mine_tile_1 = 246,
                        pyrite_mine_tile_2 = 247,
                        pyrite_mine_tile_3 = 248,
                        pyrite_smelter_tile_1 = 249,
                        liquids_terminal_tile_1 = 250,
                        liquids_terminal_tile_2 = 251,
                        fishing_village_tile_1 = 252,
                        fishing_village_tile_2 = 253,
                        chemical_plant_tile_2 = 254)

chameleon_cache_dir =  '.chameleon_cache'

# specify location for intermediate files generated during build (nml, graphics, lang etc)
generated_files_dir =  'generated'

# this is for nml or grfcodec, don't need to use python path module here
graphics_path =  'generated/graphics/'

# OpenTTD's max date
max_game_date = 5000000

# amount of cargo required to trigger 'enhanced' production at primary industries
FARM_MINE_SUPPLY_REQUIREMENT = 16

# time window (days) for delivery of combinatory cargos to secondary industries
secondary_production_span = 90

temp_storage_graphics_chain = dict(var_default_ground = 0,  # currently unused - sprite ID of default ground tile in the place of the tile
                                   var_fencesprite_ne = 1, # fence sprite to use on the NE border
                                   var_fencesprite_nw = 2, # fence sprite to use on the NW border
                                   var_fencesprite_se = 3, # fence sprite to use on the SE border
                                   var_fencesprite_sw = 4, # fence sprite to use on the SW border
                                   var_fence_offset_ne = 5, # y-offset for fence sprite to use on the NE border
                                   var_fence_offset_nw = 6, # y-offset for fence sprite to use on the NW border
                                   var_fence_offset_se = 7, # y-offset for fence sprite to use on the SE border
                                   var_fence_offset_sw = 8, # y-offset for fence sprite to use on the SW border
                                   var_use_fence_ne = 9, # draw fence in the NE
                                   var_use_fence_nw = 10, # draw fence in the NW
                                   var_use_fence_se = 11, # draw fence in the SE
                                   var_use_fence_sw = 12, # draw fence in the SW
                                   var_terrain_is_snow = 13, # must be set to 1 (true) or 0 (false)
                                   var_random_bits = 14, # some random bits to use as required
                                )  # max register number must be 235; registers 236-255 are reserved for building sprite hide/show values

# industry map colours automated, using an algorithm to ensure contrast against green / dark green / purple minimaps
# based on work by frosch, https://devs.openttd.org/~frosch/texts/industrymap_green_darkgreen_violet.html

industry_map_colours = (183, 64, 61, 166, 45, 151, 157, 191, 141, 178, 189, 55, 186, 43, 148, 5, 116, 160, 127, 143, 170, 49, 37, 146, 214, 8, 172, 177, 181, 194, 24, 168, 155, 210, 169, 70, 119, 26, 69, 85, 56, 19, 121, 105, 125, 144, 209, 164, 16, 63, 111, 65, 10, 126, 62, 104, 207, 190, 83, 142, 72, 33, 162, 173, 149, 167, 47, 153, 35, 52, 68, 78, 3, 30, 152, 38, 18, 163, 196, 165, 150, 44, 114, 140, 6, 137, 57, 81, 28, 109, 187, 185, 20, 159, 124, 12, 147, 117, 22, 46, 180, 192, 48, 86, 29, 7, 34, 41, 154, 184, 76, 115, 195, 208, 21, 182, 201, 156, 17, 84, 87, 27, 79, 171, 139, 9, 174, 213, 202, 25, 14, 53, 110, 42, 200, 82, 120, 4, 197, 138, 206, 108, 60, 193, 161, 211, 123, 2, 212, 145, 136, 77, 59, 175, 176, 80, 36, 199, 15, 11, 179, 118, 158, 51, 112, 71, 107, 66, 113, 198, 13, 204, 58, 32, 54, 205, 203, 75, 122, 188, 50, 67, 73, 23, 74, 106, 40)