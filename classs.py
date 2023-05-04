import time

import pygame


class Init:
    def __init__(self):
        self.bfn = []
        self.mouse = None
        self.font = pygame.font.Font('images/cc-ultimatum-bold.otf', 15)
        self.font3 = pygame.font.Font('images/cc-ultimatum-bold.otf', 32)
        self.font2 = pygame.font.Font('images/cc-ultimatum-bold.otf', 22)
        self.edit_display = True
        self.interro_display = False
        self.display = pygame.display.Info()
        self.width = (self.display.current_w - 200) / 3
        self.height = self.display.current_h - 130
        self.new_concept = False
        self.new_concept_in = False, (0, 0)
        self.new_concept_name = "ali "
        self.new_concept_ref = "eddine"
        self.new_concept_name_typing = False
        self.new_concept_ref_typing = False
        self.new_relation = False
        self.new_relation_in = False, (0, 0)
        self.new_relation_name = "ali "
        self.new_relation_name_typing = False
        self.new_arc = False
        self.new_arc_point1 = False, None
        self.new_arc_point2 = False, None
        self.add_new_fait = False, []

        self.new_fait = False, False, []

        self.bf_interface = False
        self.offset_bf_list = 0
        self.bf_interface_offset = 0

        self.bf_save_cancel = None

        self.br_interface = False
        self.offset_br_list = 0
        self.br_interface_offset = 0
        self.br_arc_array = []
        self.br_array = []
        self.br_list_rect = []
        self.br_main_list = []
        self.regle_separator = (0, self.display.current_h / 2), (self.display.current_w, self.display.current_h / 2)

        self.vo_offset = 0

        self.arc_with = None
        self.erase_button = False
        self.x = False

        self.intero_buttons = {"show BF": True, "show BR": False, "make BFN": False, "auto BFN": False, "Restriction": (False, False, None, False), "Copy": (False, (False, None), (False, None), None),
                               "jointure": (False, (False, None), (False, None)), "fragmentation": (False, (False, None), False)}
        self.time = time.time()
        self.error = False, None

        self.bfn_fun = None
        self.Restriction_saved_ref = None

        self.make_bfn_offset = 0

        self.BFN = None
        self.auto_bfn_offset = 0


class Concept:
    def __init__(self, x, y, name, ref):
        self.x = x
        self.y = y
        self.name = name
        self.ref = ref
        self.arcs = []
        self.arcs_back = []


class Relation:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.arcs = []
        self.arcs_back = []


