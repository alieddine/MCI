import copy
import pickle
import sys
import time
from builtins import enumerate

from pygame import mouse
from pygame.locals import Rect

from intrface_functions import *
from classs import *
import pygame


def main():
    pygame.init()
    screen = pygame.display.Info()
    screen = pygame.display.set_mode((screen.current_w, screen.current_h), pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    init = Init()
    # c1 = Concept(100, 100, "c1", "r1")
    # c2 = Concept(100, 200, "c1", "r1")
    # c3 = Concept(100, 300, "c3", "r3")
    # r1 = Relation(200, 120, "relation1")
    # r2 = Relation(200, 250, "relation2")
    # c1.arcs.append(r1)
    # c2.arcs.append(r2)
    # r1.arcs.append(c2)
    # r2.arcs.append(c3)
    # c2.arcs_back.append(r1)
    # r1.arcs_back.append(c1)
    # r2.arcs_back.append(c2)
    # c3.arcs_back.append(r2)
    # init.bfn = [c1, c2, c3, r1, r2]
    picke_in = open("BF.pickle", "rb")
    init.bfn = pickle.load(picke_in)
    picke_in = open("BR.pickle", "rb")
    init.br_main_list = pickle.load(picke_in)
    error_time = time.time()
    while True:

        init.mouse = pygame.mouse.get_pos()
        screen.fill((35, 35, 35))
        background = pygame.image.load("images/background1.jpg").convert()
        screen.blit(background, (0, 0))
        black_filter = pygame.Surface((screen.get_width(), screen.get_height()))
        black_filter.fill((0, 0, 0))
        black_filter.set_alpha(200)
        screen.blit(black_filter, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if not init.intero_buttons["projection"] and not init.bf_interface and not init.br_interface and screen.get_width() - 25 <= init.mouse[0] <= screen.get_width() - 5 and 5 <= init.mouse[1] <= 25:
                    sys.exit()
                elif not init.intero_buttons["projection"] and not init.bf_interface and not init.br_interface and 55 <= init.mouse[0] <= 55 + 30 + init.font2.size("edit")[0] and 0 <= init.mouse[1] <= 30:
                    init.edit_display = True
                    init.interro_display = False
                elif not init.intero_buttons["projection"] and not init.bf_interface and not init.br_interface and 80 + 10 + init.font2.size("edit")[0] <= init.mouse[0] <= 80 + 10 + init.font2.size("edit")[0] + 30 + init.font2.size("interro")[0] and 0 <= init.mouse[1] <= 30:
                    init.edit_display = False
                    init.interro_display = True
                    init.bfn_fun = Copy(init.bfn)

                elif init.edit_display:
                    if init.bf_interface:
                        if init.new_concept:
                            if init.new_concept_in[0]:
                                if screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + 140 <= init.mouse[0] <= screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + 140 + init.font2.size(init.new_concept_name)[0] + 20 and screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + 45 <= \
                                        init.mouse[1] <= screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + 45 + init.font2.size("A")[1] + 10:
                                    init.new_concept_name_typing = True
                                    init.new_concept_ref_typing = False
                                elif screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + 140 <= init.mouse[0] <= screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + 140 + init.font2.size(init.new_concept_ref)[0] + 20 and screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + 95 <= \
                                        init.mouse[1] <= screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + 95 + init.font2.size("A")[1] + 10:
                                    init.new_concept_ref_typing = True
                                    init.new_concept_name_typing = False
                                elif screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + screen.get_width() * 0.2 / 2 - 25 <= init.mouse[
                                    0] <= screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + screen.get_width() * 0.2 / 2 - 25 + 50 and screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + screen.get_height() * 0.3 - 70 <= init.mouse[
                                    1] <= screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + screen.get_height() * 0.3 - 70 + 30:
                                    init.new_concept_name_typing = False
                                    init.new_concept_ref_typing = False

                                    # init.new_concept = False

                                    concept = Concept(init.new_concept_in[1][0], init.new_concept_in[1][1], init.new_concept_name, init.new_concept_ref)
                                    init.bfn.append(concept)
                                    init.new_concept_in = False, (0, 0)

                            elif 82 <= init.mouse[0] <= 82 + screen.get_width() * 0.6 and screen.get_height() * 0.05 <= init.mouse[1] <= screen.get_height() * 0.05 + screen.get_height() * 0.9:
                                init.new_concept_in = True, (init.mouse[0], init.mouse[1] - init.bf_interface_offset)

                            else:
                                init.error = True, "error : needs to place it inside the container"
                                error_time = time.time()
                                break
                        elif init.new_relation:
                            if init.new_relation_in[0]:
                                if screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + 140 <= init.mouse[0] <= screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + 140 + init.font2.size(init.new_concept_name)[0] + 20 and screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + 45 <= \
                                        init.mouse[1] <= screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + 45 + init.font2.size("A")[1] + 10:
                                    init.new_relation_name_typing = True
                                elif screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + screen.get_width() * 0.2 / 2 - 25 <= init.mouse[
                                    0] <= screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + screen.get_width() * 0.2 / 2 - 25 + 50 and screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + screen.get_height() * 0.3 - 70 <= init.mouse[
                                    1] <= screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + screen.get_height() * 0.3 - 70 + 30:
                                    init.new_relation_name_typing = False
                                    # init.new_relation = False
                                    relation = Relation(init.new_relation_in[1][0], init.new_relation_in[1][1], init.new_relation_name)
                                    init.bfn.append(relation)
                                    init.new_relation_in = False, (0, 0)
                            elif 82 <= init.mouse[0] <= 82 + screen.get_width() * 0.6 and screen.get_height() * 0.05 <= init.mouse[1] <= screen.get_height() * 0.05 + screen.get_height() * 0.9:
                                init.new_relation_in = True, (init.mouse[0], init.mouse[1] - init.bf_interface_offset)
                            else:
                                # red mouse to reference an error
                                init.error = True, "error : needs to place it inside the container"
                                error_time = time.time()
                                break
                        elif init.new_arc:
                            if 82 <= init.mouse[0] <= 82 + screen.get_width() * 0.6 and screen.get_height() * 0.05 <= init.mouse[1] <= screen.get_height() * 0.05 + screen.get_height() * 0.9:
                                rect = Rect(init.mouse[0], init.mouse[1] - init.bf_interface_offset, 1, 1)
                                bfn_rects = get_rects(init.bfn, init)
                                collide = pygame.Rect.collidelist(rect, bfn_rects)
                                if collide != -1:
                                    if not init.new_fait[0]:
                                        if type(init.bfn[collide]) == Concept:
                                            init.new_fait = True, False, [init.bfn[collide]]
                                        elif type(init.bfn[collide]) == Relation:
                                            print("error : needs to be concept ===> relation")
                                            init.error = True, "error : needs to be concept ===> relation"
                                            error_time = time.time()
                                            break
                                        else:
                                            print("error : you need to select a concept in the container")
                                            init.error = True, "error : you need to select a concept in the container"
                                            error_time = time.time()
                                            break

                                    else:
                                        if not init.new_fait[1]:
                                            if len(init.new_fait[2]) == 1:
                                                if type(init.bfn[collide]) == Relation:
                                                    if len(init.bfn[collide].arcs) == 0:
                                                        init.new_fait[2].append(init.bfn[collide])
                                                        init.new_fait = True, False, init.new_fait[2]
                                                    else:
                                                        print("error : relation can be only between 2 concept")
                                                        init.error = True, "error : relation can be only between 2 concept"
                                                        error_time = time.time()
                                                        break
                                                else:
                                                    print("error : needs to be concept ===> relation")
                                                    init.error = True, "error : needs to be concept ===> relation"
                                                    error_time = time.time()
                                                    break
                                            else:
                                                if type(init.bfn[collide]) == Relation:
                                                    if init.bfn[collide] == init.new_fait[2][1]:
                                                        init.new_fait = True, True, init.new_fait[2]
                                                    else:
                                                        print("needs to be same relation")
                                                        init.error = True, "error : needs to be same relation"
                                                        error_time = time.time()
                                                        break

                                                else:
                                                    print("error : needs to be relation ===> concept")
                                                    init.error = True, "error : needs to be relation ===> concept"
                                                    error_time = time.time()
                                                    break

                                        else:
                                            if type(init.bfn[collide]) == Concept:
                                                init.new_fait[2].append(init.bfn[collide])
                                                init.new_fait = False, False, init.new_fait[2]
                                                fait = init.new_fait[2]
                                                fait[0].arcs.append(fait[1])
                                                fait[1].arcs.append(fait[2])
                                                fait[1].arcs_back.append(fait[0])
                                                fait[2].arcs_back.append(fait[1])
                                                init.new_fait = False, False, []
                                            elif type(init.bfn[collide]) == Relation:
                                                print("error : needs to be relation ===> concept")
                                                init.error = True, "error : needs to be relation ===> concept"
                                                error_time = time.time()
                                                break
                                            else:
                                                print("error : you need to select a concept in the container")
                                                init.error = True, "error : you need to select a concept in the container"
                                                error_time = time.time()
                                                break

                        elif 40 + screen.get_width() * 0.6 <= init.mouse[0] <= 40 + screen.get_width() * 0.6 + 20 and 10 + screen.get_height() * 0.05 <= init.mouse[1] <= 10 + screen.get_height() * 0.05 + 20:
                            init.erase_button = not init.erase_button

                        elif init.erase_button:
                            rect = Rect(init.mouse[0], init.mouse[1] - init.bf_interface_offset, 1, 1)
                            bfn_rec = get_rects(init.bfn, init)
                            collide = pygame.Rect.collidelist(rect, bfn_rec)
                            if not collide == -1:
                                obj = init.bfn[collide]
                                init.bfn.remove(obj)
                                for element in init.bfn:
                                    for e in element.arcs:
                                        if e == obj:
                                            if type(element) == Relation:
                                                element.arcs_back[0].arcs.remove(element)
                                                element.arcs_back = []

                                            element.arcs.remove(obj)

                                    for e in element.arcs_back:
                                        if e == obj:
                                            if type(element) == Relation:
                                                element.arcs[0].arcs_back.remove(element)
                                                element.arcs = []
                                            element.arcs_back.remove(obj)
                        elif 80 + screen.get_width() * 0.6 + screen.get_width() * 0.2 - 80 + 80 - 40 <= init.mouse[0] <= 80 + screen.get_width() * 0.6 + screen.get_width() * 0.2 - 80 + 80 - 40 + 80 and screen.get_height() * 0.2 + screen.get_height() * 0.6 - 70 <= init.mouse[
                            1] <= screen.get_height() * 0.2 + screen.get_height() * 0.6 - 70 + 30:
                            init.bf_interface = False
                            if init.bf_save_cancel is not None:
                                init.bfn = init.bf_save_cancel

                        elif 80 + screen.get_width() * 0.6 + 80 + 80 - 40 <= init.mouse[0] <= 80 + screen.get_width() * 0.6 + 80 + 80 - 40 + 80 and screen.get_height() * 0.2 + screen.get_height() * 0.6 - 70 <= init.mouse[1] <= screen.get_height() * 0.2 + screen.get_height() * 0.6 - 70 + 30:
                            init.bf_interface = False
                            relation_to_remove = []
                            for element in init.bfn:
                                if type(element) == Relation and len(element.arcs) == 0:
                                    relation_to_remove.append(element)
                            for element in relation_to_remove:
                                init.bfn.remove(element)

                            init.bfn_fun = Copy(init.bfn)

                            init.bf_save_cancel = init.bfn_fun.copy()

                        elif 80 + screen.get_width() * 0.6 + 80 + (screen.get_width() * 0.2) / 2 - 70 <= init.mouse[0] <= 80 + screen.get_width() * 0.6 + 80 + (screen.get_width() * 0.2) / 2 - 70 + 140 and screen.get_height() * 0.2 + 10 + init.font2.size("Concept")[1] * 2 <= init.mouse[
                            1] <= screen.get_height() * 0.2 + 10 + init.font2.size("Concept")[1] * 2 + 40:
                            init.new_concept = True
                        elif 80 + screen.get_width() * 0.6 + 80 + (screen.get_width() * 0.2) / 2 - 70 <= init.mouse[0] <= 80 + screen.get_width() * 0.6 + 80 + (screen.get_width() * 0.2) / 2 - 70 + 140 and screen.get_height() * 0.2 + 110 + init.font2.size("Concept")[1] * 2 <= init.mouse[
                            1] <= screen.get_height() * 0.2 + 110 + init.font2.size("Relation")[1] * 2 + 40:
                            init.new_relation = True
                        elif 80 + screen.get_width() * 0.6 + 80 + (screen.get_width() * 0.2) / 2 - 70 <= init.mouse[0] <= 80 + screen.get_width() * 0.6 + 80 + (screen.get_width() * 0.2) / 2 - 70 + 140 and screen.get_height() * 0.2 + 210 + init.font2.size("Arc")[1] * 2 <= init.mouse[
                            1] <= screen.get_height() * 0.2 + 210 + init.font2.size("Arc")[1] * 2 + 40:
                            init.new_arc = True
                            init.new_fait = False, False, []
                    elif init.br_interface:
                        if init.new_concept:
                            if init.new_concept_in[0]:
                                if screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + 140 <= init.mouse[0] <= screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + 140 + init.font2.size(init.new_concept_name)[0] + 20 and screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + 45 <= \
                                        init.mouse[1] <= screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + 45 + init.font2.size("A")[1] + 10:
                                    init.new_concept_name_typing = True
                                    init.new_concept_ref_typing = False
                                elif screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + 140 <= init.mouse[0] <= screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + 140 + init.font2.size(init.new_concept_ref)[0] + 20 and screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + 95 <= \
                                        init.mouse[1] <= screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + 95 + init.font2.size("A")[1] + 10:
                                    init.new_concept_ref_typing = True
                                    init.new_concept_name_typing = False
                                elif screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + screen.get_width() * 0.2 / 2 - 25 <= init.mouse[
                                    0] <= screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + screen.get_width() * 0.2 / 2 - 25 + 50 and screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + screen.get_height() * 0.3 - 70 <= init.mouse[
                                    1] <= screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + screen.get_height() * 0.3 - 70 + 30:
                                    init.new_concept_name_typing = False
                                    init.new_concept_ref_typing = False
                                    # init.new_concept = False
                                    rect = Rect(init.new_concept_in[1][0], init.new_concept_in[1][1], 20 + init.font2.size(init.new_concept_name + " : " + init.new_concept_ref)[0], 40)
                                    init.br_list_rect.append(rect)
                                    concept = Concept(init.new_concept_in[1][0], init.new_concept_in[1][1], init.new_concept_name, init.new_concept_ref)
                                    init.br_array.append(concept)
                                    init.new_concept_in = False, (0, 0)

                            elif 82 <= init.mouse[0] <= 82 + screen.get_width() * 0.6 and screen.get_height() * 0.05 <= init.mouse[1] <= screen.get_height() * 0.05 + screen.get_height() * 0.9:
                                init.new_concept_in = True, (init.mouse[0], init.mouse[1] - init.br_interface_offset)

                            else:
                                # red mouse to reference an error
                                init.error = True, "error : needs to place it inside the container"
                                error_time = time.time()
                                break
                        elif init.new_relation:
                            if init.new_relation_in[0]:
                                if screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + 140 <= init.mouse[0] <= screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + 140 + init.font2.size(init.new_concept_name)[0] + 20 and screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + 45 <= \
                                        init.mouse[1] <= screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + 45 + init.font2.size("A")[1] + 10:
                                    init.new_relation_name_typing = True
                                elif screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + screen.get_width() * 0.2 / 2 - 25 <= init.mouse[
                                    0] <= screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + screen.get_width() * 0.2 / 2 - 25 + 50 and screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + screen.get_height() * 0.3 - 70 <= init.mouse[
                                    1] <= screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + screen.get_height() * 0.3 - 70 + 30:
                                    init.new_relation_name_typing = False
                                    # init.new_relation = False
                                    rect = Rect(init.new_relation_in[1][0], init.new_relation_in[1][1], 20 + init.font2.size(init.new_relation_name)[0], 40)
                                    init.br_list_rect.append(rect)
                                    relation = Relation(init.new_relation_in[1][0], init.new_relation_in[1][1], init.new_relation_name)
                                    init.br_array.append(relation)
                                    init.new_relation_in = False, (0, 0)
                            elif 82 <= init.mouse[0] <= 82 + screen.get_width() * 0.6 and screen.get_height() * 0.05 <= init.mouse[1] <= screen.get_height() * 0.05 + screen.get_height() * 0.9:
                                init.new_relation_in = True, (init.mouse[0], init.mouse[1] - init.br_interface_offset)
                            else:
                                # red mouse to reference an error
                                init.error = True, "error : needs to place it inside the container"
                                error_time = time.time()
                                break
                        elif init.new_arc:
                            if 82 <= init.mouse[0] <= 82 + screen.get_width() * 0.6 and screen.get_height() * 0.05 <= init.mouse[1] <= screen.get_height() * 0.05 + screen.get_height() * 0.9:
                                rect = Rect(init.mouse[0], init.mouse[1] - init.br_interface_offset, 1, 1)
                                collide = pygame.Rect.collidelist(rect, init.br_list_rect)
                                if collide != -1:
                                    if init.new_arc_point1[0]:
                                        if len(init.add_new_fait[1]) == 1:
                                            if type(init.br_array[collide]) == Relation:
                                                if len(init.br_array[collide].arcs) == 0:
                                                    init.add_new_fait[1].append(init.br_array[collide])
                                                    init.add_new_fait = True, init.add_new_fait[1]
                                                else:
                                                    print("error : relation can be only between 2 concept ")
                                                    init.error = True, "error : relation can be only between 2 concept"
                                                    error_time = time.time()
                                                    break

                                            else:
                                                print("error : needs to be concept ===> relation")
                                                init.error = True, "error : needs to be concept ===> relation"
                                                error_time = time.time()
                                                break
                                        else:
                                            if type(init.br_array[collide]) == Concept:

                                                init.add_new_fait[1].append(init.br_array[collide])
                                                init.add_new_fait = True, init.add_new_fait[1]
                                                # init.br_main_list.append(init.bf_add_new_fait[1])
                                                init.add_new_fait = False, init.add_new_fait[1]

                                            else:
                                                print("error : needs to be relation ===> concept")
                                                init.error = True, "error : needs to be relation ===> concept"
                                                error_time = time.time()
                                                break

                                        obj = init.br_list_rect[collide]

                                        init.new_arc_point2 = True, obj
                                        init.br_arc_array.append([init.new_arc_point1[1], init.new_arc_point2[1]])
                                        init.new_arc_point1 = False, None
                                        # init.new_arc = False
                                        init.arc_with.arcs.append(init.br_array[collide])
                                        init.br_array[collide].arcs_back.append(init.arc_with)
                                        init.arc_with = init.br_array[collide]



                                    else:
                                        if not init.add_new_fait[0]:
                                            # 1
                                            if type(init.br_array[collide]) == Concept:
                                                init.add_new_fait = True, [init.br_array[collide]]
                                            else:
                                                print("error : needs to be concept ===> relation")
                                                init.error = True, "error : needs to be concept ===> relation"
                                                error_time = time.time()
                                                break
                                        else:
                                            if type(init.br_array[collide]) == Relation:
                                                if not init.add_new_fait[1][-1] == init.br_array[collide]:
                                                    print("needs to be same relation")
                                                    init.error = True, "error : needs to be same relation"
                                                    error_time = time.time()
                                                    break


                                            else:
                                                print("error : needs to be relation ===> concept")
                                                init.error = True, "error : needs to be relation ===> concept"
                                                error_time = time.time()
                                                break
                                        obj = init.br_list_rect[collide]
                                        init.new_arc_point1 = True, obj
                                        init.arc_with = init.br_array[collide]

                        elif 40 + screen.get_width() * 0.6 <= init.mouse[0] <= 40 + screen.get_width() * 0.6 + 20 and 10 + screen.get_height() * 0.05 <= init.mouse[1] <= 10 + screen.get_height() * 0.05 + 20:
                            init.erase_button = not init.erase_button

                        elif init.erase_button:
                            rect = Rect(init.mouse[0], init.mouse[1] - init.br_interface_offset, 1, 1)
                            collide = pygame.Rect.collidelist(rect, init.br_list_rect)
                            if not collide == -1:
                                obj = init.br_array[collide]
                                init.br_list_rect.pop(collide)
                                init.br_array.remove(obj)
                                for element in init.br_array:
                                    if obj in element.arcs:
                                        element.arcs.remove(obj)
                            else:
                                break

                        elif 80 + screen.get_width() * 0.6 + screen.get_width() * 0.2 - 80 + 80 - 40 <= init.mouse[0] <= 80 + screen.get_width() * 0.6 + screen.get_width() * 0.2 - 80 + 80 - 40 + 80 and screen.get_height() * 0.2 + screen.get_height() * 0.6 - 70 <= init.mouse[
                            1] <= screen.get_height() * 0.2 + screen.get_height() * 0.6 - 70 + 30:
                            init.br_interface = False
                            init.br_array = []
                            init.br_arc_array = []
                            init.br_list_rect = []
                        elif 80 + screen.get_width() * 0.6 + 80 + 80 - 40 <= init.mouse[0] <= 80 + screen.get_width() * 0.6 + 80 + 80 - 40 + 80 and screen.get_height() * 0.2 + screen.get_height() * 0.6 - 70 <= init.mouse[1] <= screen.get_height() * 0.2 + screen.get_height() * 0.6 - 70 + 30:
                            # add check error function
                            # a relation can have only 2 concept
                            init.br_interface = False
                            regle = {"premise": [], "conclusion": []}
                            add = []
                            for element in init.br_array:
                                if not element in add and not len(element.arcs) == 0:
                                    add.append(element)
                                for sous_element in element.arcs:
                                    if not sous_element in add:
                                        add.append(sous_element)
                            for element in add:
                                if element.y <= init.regle_separator[0][1]:
                                    regle["premise"].append(element)
                                else:
                                    regle["conclusion"].append(element)
                            init.br_main_list.append(regle)
                            init.br_array = []
                            init.br_arc_array = []
                            init.br_list_rect = []
                            # print(init.br_main_list)
                            # for element in init.br_main_list:
                            #     print("premise : -------------------------------------------------------------------------------------------")
                            #     for sous_element in element["premise"]:
                            #         print(type(sous_element), sous_element.name, sous_element.x, sous_element.y, sous_element.arcs)
                            #     print("conclusion : -------------------------------------------------------------------------------------------")
                            #     for sous_element in element["conclusion"]:
                            #         print(type(sous_element), sous_element.name, sous_element.x, sous_element.y, sous_element.arcs)
                        elif 80 + screen.get_width() * 0.6 + 80 + (screen.get_width() * 0.2) / 2 - 70 <= init.mouse[0] <= 80 + screen.get_width() * 0.6 + 80 + (screen.get_width() * 0.2) / 2 - 70 + 140 and screen.get_height() * 0.2 + 10 + init.font2.size("Concept")[1] * 2 <= init.mouse[
                            1] <= screen.get_height() * 0.2 + 10 + init.font2.size("Concept")[1] * 2 + 40:
                            init.new_concept = True
                        elif 80 + screen.get_width() * 0.6 + 80 + (screen.get_width() * 0.2) / 2 - 70 <= init.mouse[0] <= 80 + screen.get_width() * 0.6 + 80 + (screen.get_width() * 0.2) / 2 - 70 + 140 and screen.get_height() * 0.2 + 110 + init.font2.size("Concept")[1] * 2 <= init.mouse[
                            1] <= screen.get_height() * 0.2 + 110 + init.font2.size("Relation")[1] * 2 + 40:
                            init.new_relation = True
                        elif 80 + screen.get_width() * 0.6 + 80 + (screen.get_width() * 0.2) / 2 - 70 <= init.mouse[0] <= 80 + screen.get_width() * 0.6 + 80 + (screen.get_width() * 0.2) / 2 - 70 + 140 and screen.get_height() * 0.2 + 210 + init.font2.size("Arc")[1] * 2 <= init.mouse[
                            1] <= screen.get_height() * 0.2 + 210 + init.font2.size("Arc")[1] * 2 + 40:
                            init.new_arc = True
                    elif 50 * 2 + 100 + init.width + init.width / 2 - init.font2.size("save BR")[0] / 2 - 8 <= init.mouse[0] <= 50 * 2 + 100 + init.width + init.width / 2 - init.font2.size("save BR")[0] / 2 - 8 + init.font2.size("save BR")[0] + 16 and 80 + init.height - 34 <= init.mouse[1] <= 80 + init.height - 34 + 25:
                        pickle_out = open("BR.pickle", "wb")
                        pickle.dump(init.br_main_list, pickle_out)
                        pickle_out.close()
                        print("saved")
                    elif 150 + init.width / 2 - init.font2.size("save BF")[0] / 2 - 8 <= init.mouse[0] <= 150 + init.width / 2 - init.font2.size("save BF")[0] / 2 - 8 + init.font2.size("save BF")[0] + 16 and 80 + init.height - 34 <= init.mouse[1] <= 80 + init.height - 34 + 25:
                        pickle_out = open("BF.pickle", "wb")
                        pickle.dump(init.bfn, pickle_out)
                        pickle_out.close()
                        print("saved")
                    elif 50 + init.width / 2 - init.font2.size("new BF")[0] / 2 - 8 <= init.mouse[0] <= 50 + init.width / 2 - init.font2.size("new BF")[0] / 2 - 8 + init.font2.size("new BF")[0] + 16 and 80 + init.height - 34 <= init.mouse[1] <= 80 + init.height - 34 + 25:
                        # edit br button
                        init.bf_interface = True
                        init.br_interface = False
                    elif 50 * 2 + init.width + init.width / 2 - init.font2.size("new BR")[0] / 2 - 8 <= init.mouse[0] <= 50 * 2 + init.width + init.width / 2 - init.font2.size("new BF")[0] / 2 - 8 + init.font2.size("new BF")[0] + 16 and 80 + init.height - 34 <= init.mouse[
                        1] <= 80 + init.height - 34 + 25:
                        init.bf_interface = False
                        init.br_interface = True

                # ---------------------------------------------------------------------------------------------

                elif init.interro_display:
                    if init.intero_buttons["make BFN"]:
                        if init.fun_projecting:
                            if 20 <= init.mouse[0] <= 20 + 70 and screen.get_height() * 0.8 <= init.mouse[1] <= screen.get_height() * 0.8 + 30:
                                init.show_rq = True
                                init.show_answer = False
                                init.fun_answer = []
                            elif 20 <= init.mouse[0] <= 20 + 70 and screen.get_height() * 0.8 + 40 <= init.mouse[1] <= screen.get_height() * 0.8 + 40 + 30:
                                init.show_rq = False
                                init.show_answer = True
                                init.fun_answer = Projection(init.fun_rq, init.bfn_fun)
                            elif 20 <= init.mouse[0] <= 20 + 70 and screen.get_height() * 0.8 + 80 <= init.mouse[1] <= screen.get_height() * 0.8 + 80 + 30:
                                init.fun_projecting = False
                                init.fun_answer = []
                                init.show_rq = False
                                init.show_answer = False
                                init.show_answer_filter = False
                            elif 100 <= init.mouse[0] <= 100 + 70 and screen.get_height() * 0.8 + 40 <= init.mouse[1] <= screen.get_height() * 0.8 + 40 + 30:
                                init.show_answer_filter = True
                                init.show_rq = False
                                init.show_answer = False
                                init.fun_answer_filter = filter_answers(init.fun_answer)[0]


                        elif screen.get_width() * 0.8 + 10 + 70 <= init.mouse[0] <= screen.get_width() * 0.8 + 70 + 10 + 70 and screen.get_height() * 0.1 + 240 <= init.mouse[1] <= screen.get_height() * 0.1 + 30 + 240:
                            init.intero_buttons["projection"] = not init.intero_buttons["projection"]
                            init.fun_projecting = False
                            init.fun_rq = []
                        elif init.intero_buttons["projection"]:
                            if init.new_concept:
                                if init.new_concept_in[0]:
                                    if screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + 140 <= init.mouse[0] <= screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + 140 + init.font2.size(init.new_concept_name)[0] + 20 and screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + 45 <= \
                                            init.mouse[1] <= screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + 45 + init.font2.size("A")[1] + 10:
                                        init.new_concept_name_typing = True
                                        init.new_concept_ref_typing = False
                                    elif screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + 140 <= init.mouse[0] <= screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + 140 + init.font2.size(init.new_concept_ref)[0] + 20 and screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + 95 <= \
                                            init.mouse[1] <= screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + 95 + init.font2.size("A")[1] + 10:
                                        init.new_concept_ref_typing = True
                                        init.new_concept_name_typing = False
                                    elif screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + screen.get_width() * 0.2 / 2 - 25 <= init.mouse[
                                        0] <= screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + screen.get_width() * 0.2 / 2 - 25 + 50 and screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + screen.get_height() * 0.3 - 70 <= init.mouse[
                                        1] <= screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + screen.get_height() * 0.3 - 70 + 30:
                                        init.new_concept_name_typing = False
                                        init.new_concept_ref_typing = False
                                        concept = Concept(init.new_concept_in[1][0], init.new_concept_in[1][1], init.new_concept_name, init.new_concept_ref)
                                        init.fun_rq.append(concept)
                                        init.new_concept_in = False, (0, 0)

                                elif 82 <= init.mouse[0] <= 82 + screen.get_width() * 0.6 and screen.get_height() * 0.05 <= init.mouse[1] <= screen.get_height() * 0.05 + screen.get_height() * 0.3:
                                    init.new_concept_in = True, (init.mouse[0], init.mouse[1] - 0)

                                else:
                                    init.error = True, "error : needs to place it inside the container"
                                    error_time = time.time()
                                    break
                            elif init.new_relation:
                                if init.new_relation_in[0]:
                                    if screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + 140 <= init.mouse[0] <= screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + 140 + init.font2.size(init.new_concept_name)[0] + 20 and screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + 45 <= init.mouse[1] <= screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + 45 + init.font2.size("A")[1] + 10:
                                        init.new_relation_name_typing = True
                                    elif screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + screen.get_width() * 0.2 / 2 - 25 <= init.mouse[0] <= screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + screen.get_width() * 0.2 / 2 - 25 + 50 and screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + screen.get_height() * 0.3 - 70 <= init.mouse[1] <= screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + screen.get_height() * 0.3 - 70 + 30:
                                        init.new_relation_name_typing = False
                                        # init.new_relation = False
                                        relation = Relation(init.new_relation_in[1][0], init.new_relation_in[1][1], init.new_relation_name)
                                        init.fun_rq.append(relation)
                                        init.new_relation_in = False, (0, 0)
                                elif 82 <= init.mouse[0] <= 82 + screen.get_width() * 0.6 and screen.get_height() * 0.05 <= init.mouse[1] <= screen.get_height() * 0.05 + screen.get_height() * 0.3:
                                    init.new_relation_in = True, (init.mouse[0], init.mouse[1] - 0)
                                else:
                                    init.error = True, "error : needs to place it inside the container"
                                    error_time = time.time()
                                    break
                            elif init.new_arc:
                                if 82 <= init.mouse[0] <= 82 + screen.get_width() * 0.6 and screen.get_height() * 0.05 <= init.mouse[1] <= screen.get_height() * 0.05 + screen.get_height() * 0.9:
                                    rect = Rect(init.mouse[0], init.mouse[1] - 0, 1, 1)
                                    bfn_rects = get_rects(init.fun_rq, init)
                                    collide = pygame.Rect.collidelist(rect, bfn_rects)
                                    if collide != -1:
                                        if not init.new_fait[0]:
                                            if type(init.fun_rq[collide]) == Concept:
                                                init.new_fait = True, False, [init.fun_rq[collide]]
                                            elif type(init.fun_rq[collide]) == Relation:
                                                print("error : needs to be concept ===> relation")
                                                init.error = True, "error : needs to be concept ===> relation"
                                                error_time = time.time()
                                                break
                                            else:
                                                print("error : you need to select a concept in the container")
                                                init.error = True, "error : you need to select a concept in the container"
                                                error_time = time.time()
                                                break

                                        else:
                                            if not init.new_fait[1]:
                                                if len(init.new_fait[2]) == 1:
                                                    if type(init.fun_rq[collide]) == Relation:
                                                        if len(init.fun_rq[collide].arcs) == 0:
                                                            init.new_fait[2].append(init.fun_rq[collide])
                                                            init.new_fait = True, False, init.new_fait[2]
                                                        else:
                                                            print("error : relation can be only between 2 concept")
                                                            init.error = True, "error : relation can be only between 2 concept"
                                                            error_time = time.time()
                                                            break
                                                    else:
                                                        print("error : needs to be concept ===> relation")
                                                        init.error = True, "error : needs to be concept ===> relation"
                                                        error_time = time.time()
                                                        break
                                                else:
                                                    if type(init.fun_rq[collide]) == Relation:
                                                        if init.fun_rq[collide] == init.new_fait[2][1]:
                                                            init.new_fait = True, True, init.new_fait[2]
                                                        else:
                                                            print("needs to be same relation")
                                                            init.error = True, "error : needs to be same relation"
                                                            error_time = time.time()
                                                            break

                                                    else:
                                                        print("error : needs to be relation ===> concept")
                                                        init.error = True, "error : needs to be relation ===> concept"
                                                        error_time = time.time()
                                                        break

                                            else:
                                                if type(init.fun_rq[collide]) == Concept:
                                                    init.new_fait[2].append(init.fun_rq[collide])
                                                    init.new_fait = False, False, init.new_fait[2]
                                                    fait = init.new_fait[2]
                                                    fait[0].arcs.append(fait[1])
                                                    fait[1].arcs.append(fait[2])
                                                    fait[1].arcs_back.append(fait[0])
                                                    fait[2].arcs_back.append(fait[1])
                                                    init.new_fait = False, False, []
                                                elif type(init.fun_rq[collide]) == Relation:
                                                    print("error : needs to be relation ===> concept")
                                                    init.error = True, "error : needs to be relation ===> concept"
                                                    error_time = time.time()
                                                    break
                                                else:
                                                    print("error : you need to select a concept in the container")
                                                    init.error = True, "error : you need to select a concept in the container"
                                                    error_time = time.time()
                                                    break
                            elif 40 + screen.get_width() * 0.6 <= init.mouse[0] <= 40 + screen.get_width() * 0.6 + 20 and 10 + screen.get_height() * 0.05 <= init.mouse[1] <= 10 + screen.get_height() * 0.05 + 20:
                                init.erase_button = not init.erase_button

                            elif init.erase_button:
                                rect = Rect(init.mouse[0], init.mouse[1] - 0, 1, 1)
                                bfn_rec = get_rects(init.fun_rq, init)
                                collide = pygame.Rect.collidelist(rect, bfn_rec)
                                if not collide == -1:
                                    obj = init.fun_rq[collide]
                                    init.fun_rq.remove(obj)
                                    for element in init.fun_rq:
                                        for e in element.arcs:
                                            if e == obj:
                                                if type(element) == Relation:
                                                    element.arcs_back[0].arcs.remove(element)
                                                    element.arcs_back = []

                                                element.arcs.remove(obj)

                                        for e in element.arcs_back:
                                            if e == obj:
                                                if type(element) == Relation:
                                                    element.arcs[0].arcs_back.remove(element)
                                                    element.arcs = []
                                                element.arcs_back.remove(obj)
                            elif 80 + screen.get_width() * 0.6 + screen.get_width() * 0.2 - 80 + 80 - 40 <= init.mouse[0] <= 80 + screen.get_width() * 0.6 + screen.get_width() * 0.2 - 80 + 80 - 40 + 80 and screen.get_height() * 0.2 + screen.get_height() * 0.6 - 70 <= init.mouse[1] <= screen.get_height() * 0.2 + screen.get_height() * 0.6 - 70 + 30:
                                init.intero_buttons["projection"] = False

                            elif 80 + screen.get_width() * 0.6 + 80 + 80 - 40 <= init.mouse[0] <= 80 + screen.get_width() * 0.6 + 80 + 80 - 40 + 80 and screen.get_height() * 0.2 + screen.get_height() * 0.6 - 70 <= init.mouse[1] <= screen.get_height() * 0.2 + screen.get_height() * 0.6 - 70 + 30:
                                init.intero_buttons["projection"] = False


                                relation_to_remove = []
                                for element in init.fun_rq:
                                    if type(element) == Relation and len(element.arcs) == 0:
                                        relation_to_remove.append(element)
                                for element in relation_to_remove:
                                    init.fun_rq.remove(element)
                                if not len(init.fun_rq) == 0:
                                    init.fun_projecting = True

                            elif 80 + screen.get_width() * 0.6 + 80 + (screen.get_width() * 0.2) / 2 - 70 <= init.mouse[0] <= 80 + screen.get_width() * 0.6 + 80 + (screen.get_width() * 0.2) / 2 - 70 + 140 and screen.get_height() * 0.2 + 10 + init.font2.size("Concept")[1] * 2 <= init.mouse[1] <= screen.get_height() * 0.2 + 10 + init.font2.size("Concept")[1] * 2 + 40:
                                init.new_concept = True
                            elif 80 + screen.get_width() * 0.6 + 80 + (screen.get_width() * 0.2) / 2 - 70 <= init.mouse[0] <= 80 + screen.get_width() * 0.6 + 80 + (screen.get_width() * 0.2) / 2 - 70 + 140 and screen.get_height() * 0.2 + 110 + init.font2.size("Concept")[1] * 2 <= init.mouse[1] <= screen.get_height() * 0.2 + 110 + init.font2.size("Relation")[1] * 2 + 40:
                                init.new_relation = True
                            elif 80 + screen.get_width() * 0.6 + 80 + (screen.get_width() * 0.2) / 2 - 70 <= init.mouse[0] <= 80 + screen.get_width() * 0.6 + 80 + (screen.get_width() * 0.2) / 2 - 70 + 140 and screen.get_height() * 0.2 + 210 + init.font2.size("Arc")[1] * 2 <= init.mouse[1] <= screen.get_height() * 0.2 + 210 + init.font2.size("Arc")[1] * 2 + 40:
                                init.new_arc = True
                                init.new_fait = False, False, []
                        elif screen.get_width() * 0.8 + 10 + 70 <= init.mouse[0] <= screen.get_width() * 0.8 + 70 + 10 + 70 and screen.get_height() * 0.1 + 280 <= init.mouse[1] <= screen.get_height() * 0.1 + 30 + 280:
                            init.bfn_fun = Simplification(init.bfn_fun)
                        elif screen.get_width() * 0.8 + 10 + 150 <= init.mouse[0] <= screen.get_width() * 0.8 + 150 + 10 + 70 and screen.get_height() * 0.1 + 80 <= init.mouse[1] <= screen.get_height() * 0.1 + 30 + 80:
                            init.intero_buttons["Restriction_1"] = not init.intero_buttons["Restriction_1"][0], (False, None), (False, None), False
                        elif init.intero_buttons["Restriction_1"][0] and not init.intero_buttons["Restriction_1"][1][0] and screen.get_width() * 0.05 <= init.mouse[0] <= screen.get_width() * 0.05 + screen.get_width() * 0.7 and screen.get_width() * 0.05 <= init.mouse[1] <= screen.get_width() * 0.05 + screen.get_height() * 0.8:
                            rect = Rect(init.mouse[0], init.mouse[1] - init.make_bfn_offset, 1, 1)
                            objs_rect = get_rects(init.bfn_fun, init, screen.get_width() * 0.05, screen.get_width() * 0.05)

                            collide = pygame.Rect.collidelist(rect, objs_rect)
                            if collide == -1:
                                init.error = True, "error : please select a concept"
                                error_time = time.time()
                                init.intero_buttons["Restriction_1"] = False, (False, None), (False, None), False
                                break
                            elif type(init.bfn_fun[collide]) == Relation:
                                init.error = True, "error : you can't restrect relations"
                                error_time = time.time()
                                init.intero_buttons["Restriction_1"] = False, (False, None), (False, None), False
                                break
                            elif type(init.bfn_fun[collide]) == Concept and init.bfn_fun[collide].ref != "*":
                                init.error = True, "select a concept with ref *"
                                error_time = time.time()
                                init.intero_buttons["Restriction_1"] = False, (False, None), (False, None), False
                            elif type(init.bfn_fun[collide]) == Concept and init.bfn_fun[collide].ref == "*":
                                init.error = True, "concept \"" + init.bfn_fun[collide].name + " => " + init.bfn_fun[collide].ref + "\"  is selected"
                                error_time = time.time()
                                init.intero_buttons["Restriction_1"] = True, (True, init.bfn_fun[collide]), (False, None), False
                            else:
                                init.error = True, "error 1: please click in the container"
                                error_time = time.time()
                                init.intero_buttons["Restriction_1"] = False, (False, None), (False, None), False
                                break
                        elif init.intero_buttons["Restriction_1"][0] and init.intero_buttons["Restriction_1"][1][0] and not init.intero_buttons["Restriction_1"][2][0] and screen.get_width() * 0.05 <= init.mouse[0] <= screen.get_width() * 0.05 + screen.get_width() * 0.7 and screen.get_width() * 0.05 <= init.mouse[1] <= screen.get_width() * 0.05 + screen.get_height() * 0.8:
                            rect = Rect(init.mouse[0], init.mouse[1] - init.make_bfn_offset, 1, 1)
                            objs_rect = get_rects(init.bfn_fun, init, screen.get_width() * 0.05, screen.get_width() * 0.05)

                            collide = pygame.Rect.collidelist(rect, objs_rect)
                            if collide == -1:
                                init.error = True, "error : please select a concept"
                                error_time = time.time()
                                init.intero_buttons["Restriction_1"] = True, init.intero_buttons["Restriction_1"][1], (False, None), False
                                break
                            elif type(init.bfn_fun[collide]) == Relation:
                                init.error = True, "error : you can't restrect relations"
                                error_time = time.time()
                                init.intero_buttons["Restriction_1"] = True, init.intero_buttons["Restriction_1"][1], (False, None), False
                                break
                            elif type(init.bfn_fun[collide]) == Concept and init.bfn_fun[collide].ref == "*":
                                init.error = True, "select a concept with a reference"
                                error_time = time.time()
                                init.intero_buttons["Restriction_1"] = True, init.intero_buttons["Restriction_1"][1], (False, None), False
                            elif type(init.bfn_fun[collide]) == Concept and init.bfn_fun[collide].name != init.intero_buttons["Restriction_1"][1][1].name:
                                init.error = True, "select a concept with the same name"
                                error_time = time.time()
                                init.intero_buttons["Restriction_1"] = True, init.intero_buttons["Restriction_1"][1], (False, None), False
                            elif type(init.bfn_fun[collide]) == Concept and init.bfn_fun[collide].name == init.intero_buttons["Restriction_1"][1][1].name:
                                init.error = True, "concept \"" + init.bfn_fun[collide].name + " => " + init.bfn_fun[collide].ref + "\" is selected"
                                error_time = time.time()
                                init.intero_buttons["Restriction_1"] = True, init.intero_buttons["Restriction_1"][1], (True, init.bfn_fun[collide]), False
                            else:
                                init.error = True, "error 1: please click in the container"
                                error_time = time.time()
                                init.intero_buttons["Restriction_1"] = True, init.intero_buttons["Restriction_1"][1], (False, None), False
                                break
                        elif init.intero_buttons["Restriction_1"][2][0] and screen.get_width() * 0.05 <= init.mouse[0] <= screen.get_width() * 0.05 + screen.get_width() * 0.7 and screen.get_width() * 0.05 <= init.mouse[1] <= screen.get_width() * 0.05 + screen.get_height() * 0.8:
                            if (init.font2.size("do you want to restrict")[0] + 100) / 2 - 110 / 2 + screen.get_width() / 2 - (init.font2.size("do you want to restrict")[0] + 50) / 2 <= init.mouse[0] <= 50 + screen.get_width() / 2 - (init.font2.size("do you want to restrict")[0] + 50) / 2 + (init.font2.size("do you want to restrict")[0] + 100) / 2 - 110 / 2 and 80 + screen.get_height() * 0.7 <= init.mouse[1] <= 110 + screen.get_height() * 0.7:
                                Restriction_1(init.intero_buttons["Restriction_1"][1][1], init.intero_buttons["Restriction_1"][2][1])
                                init.intero_buttons["Restriction_1"] = False, (False, None), (False, None), False
                            elif (init.font2.size("do you want to restrict")[0] + 100) / 2 - 110 / 2 + 60 + screen.get_width() / 2 - (init.font2.size("do you want to restrict")[0] + 50) / 2 <= init.mouse[0] <= (init.font2.size("do you want to restrict")[0] + 100) / 2 - 110 / 2 + 60 + 50 + screen.get_width() / 2 - (
                                        init.font2.size("do you want to restrict")[0] + 50) / 2 and 80 + screen.get_height() * 0.7 <= init.mouse[1] <= 110 + screen.get_height() * 0.7:
                                init.intero_buttons["Restriction_1"] = False, (False, None), (False, None), False

                        elif screen.get_width() * 0.8 + 10 + 70 <= init.mouse[0] <= screen.get_width() * 0.8 + 70 + 10 + 70 and screen.get_height() * 0.1 + 80 <= init.mouse[1] <= screen.get_height() * 0.1 + 30 + 80:
                            init.intero_buttons["Restriction"] = True, False, None, False
                        elif screen.get_width() * 0.8 + 10 + 70 <= init.mouse[0] <= screen.get_width() * 0.8 + 70 + 10 + 70 and screen.get_height() * 0.1 + 200 <= init.mouse[1] <= screen.get_height() * 0.1 + 30 + 200:
                            init.intero_buttons["fragmentation"] = True, (False, None), False
                        elif init.intero_buttons["fragmentation"][0]:
                            if not init.intero_buttons["fragmentation"][1][0] and screen.get_width() * 0.05 <= init.mouse[0] <= screen.get_width() * 0.05 + screen.get_width() * 0.7 and screen.get_width() * 0.05 <= init.mouse[1] <= screen.get_width() * 0.05 + screen.get_height() * 0.8:
                                rect = Rect(init.mouse[0], init.mouse[1] - init.make_bfn_offset, 1, 1)
                                objs_rect = get_rects(init.bfn_fun, init, screen.get_width() * 0.05, screen.get_width() * 0.05)

                                collide = pygame.Rect.collidelist(rect, objs_rect)
                                if collide == -1:
                                    init.error = True, "error : please select a concept"
                                    error_time = time.time()
                                    init.intero_buttons["fragmentation"] = False, (False, None), False
                                    break
                                elif type(init.bfn_fun[collide]) == Relation:
                                    init.error = True, "error : you can't devide in relations"
                                    error_time = time.time()
                                    init.intero_buttons["fragmentation"] = False, (False, None), False
                                    break
                                elif type(init.bfn_fun[collide]) == Concept:
                                    init.error = True, "concept selected click where to put it"
                                    error_time = time.time()
                                    init.intero_buttons["fragmentation"] = True, (True, init.bfn_fun[collide]), False
                                else:
                                    init.error = True, "error 1: please click in the container"
                                    error_time = time.time()
                                    init.intero_buttons["fragmentation"] = False, (False, None), False
                                    break
                            elif init.intero_buttons["fragmentation"][1][0] and screen.get_width() * 0.05 <= init.mouse[0] <= screen.get_width() * 0.05 + screen.get_width() * 0.7 and screen.get_width() * 0.05 <= init.mouse[1] <= screen.get_width() * 0.05 + screen.get_height() * 0.8:
                                concept = init.intero_buttons["fragmentation"][1][1]
                                Fragmentation(concept, init.bfn_fun, init, screen)
                                init.error = True, "finished"
                                error_time = time.time()
                                init.intero_buttons["fragmentation"] = False, (False, None), False
                                break

                        elif screen.get_width() * 0.8 + 10 + 70 <= init.mouse[0] <= screen.get_width() * 0.8 + 70 + 10 + 70 and screen.get_height() * 0.1 + 160 <= init.mouse[1] <= screen.get_height() * 0.1 + 30 + 160:
                            init.intero_buttons["jointure"] = True, (False, None), (False, None)
                            init.error = True, "select first concept to join"
                            error_time = time.time()
                        elif init.intero_buttons["jointure"][0]:
                            if not init.intero_buttons["jointure"][1][0]:
                                rect = Rect(init.mouse[0], init.mouse[1] - init.make_bfn_offset, 1, 1)
                                objs_rect = get_rects(init.bfn_fun, init, screen.get_width() * 0.05, screen.get_width() * 0.05)
                                collide = pygame.Rect.collidelist(rect, objs_rect)
                                if collide == -1:
                                    init.error = True, "error : please select a concept"
                                    error_time = time.time()
                                elif type(init.bfn_fun[collide]) == Relation:
                                    init.error = True, "error : you can't join relations"
                                    error_time = time.time()
                                elif type(init.bfn_fun[collide]) == Concept:
                                    init.error = True, "concept 1 selected"
                                    error_time = time.time()
                                    init.intero_buttons["jointure"] = True, (True, init.bfn_fun[collide]), (False, None)
                            elif not init.intero_buttons["jointure"][2][0]:
                                rect = Rect(init.mouse[0], init.mouse[1] - init.make_bfn_offset, 1, 1)
                                objs_rect = get_rects(init.bfn_fun, init, screen.get_width() * 0.05, screen.get_width() * 0.05)

                                collide = pygame.Rect.collidelist(rect, objs_rect)
                                if collide == -1:
                                    init.error = True, "error : please select a concept"
                                    error_time = time.time()
                                elif type(init.bfn_fun[collide]) == Relation:
                                    init.error = True, "error : you can't join relations"
                                    error_time = time.time()
                                elif type(init.bfn_fun[collide]) == Concept:
                                    init.error = True, "concept 2 selected"
                                    error_time = time.time()
                                    init.intero_buttons["jointure"] = True, init.intero_buttons["jointure"][1], (True, init.bfn_fun[collide])
                            elif init.intero_buttons["jointure"][2][0] and init.intero_buttons["jointure"][1][0]:
                                if (init.font2.size("do you want to join them")[0] + 100) / 2 - 110 / 2 + 60 + screen.get_width() / 2 - (init.font2.size("do you want to join them")[0] + 50) / 2 <= init.mouse[0] <= (init.font2.size("do you want to join them")[0] + 100) / 2 - 110 / 2 + 60 + 50 + screen.get_width() / 2 - (init.font2.size("do you want to join them")[0] + 50) / 2 and 80 + screen.get_height() * 0.7 <= init.mouse[1] <= 110 + screen.get_height() * 0.7:
                                    init.intero_buttons["jointure"] = False, (False, None), (False, None)
                                elif (init.font2.size("do you want to join them")[0] + 100) / 2 - 110 / 2 + screen.get_width() / 2 - (init.font2.size("do you want to join them")[0] + 50) / 2 <= init.mouse[0] <= 50 + screen.get_width() / 2 - (init.font2.size("do you want to join them")[0] + 50) / 2 + (init.font2.size("do you want to join them")[0] + 100) / 2 - 110 / 2 and 80 + screen.get_height() * 0.7 <= init.mouse[1] <= 110 + screen.get_height() * 0.7:
                                    concept_1 = init.intero_buttons["jointure"][1][1]
                                    concept_2 = init.intero_buttons["jointure"][2][1]
                                    result = Jointure(concept_1, concept_2, init.bfn_fun)
                                    if not result[0]:
                                        if result[1] == 0:
                                            init.error = True, "error : to join 2 concept they need to have the same name"
                                            error_time = time.time()
                                            init.intero_buttons["jointure"] = False, (False, None), (False, None)
                                        elif result[1] == 1:
                                            init.error = True, "error: to join 2 concept they need to have the same reference"
                                            error_time = time.time()
                                            init.intero_buttons["jointure"] = False, (False, None), (False, None)
                                    else:
                                        init.bfn_fun = result[1]
                                        init.intero_buttons["jointure"] = False, (False, None), (False, None)
                                        init.error = True, "the concepts have join successfully"
                                        error_time = time.time()

                        elif screen.get_width() * 0.8 + 10 + 70 <= init.mouse[0] <= screen.get_width() * 0.8 + 70 + 10 + 70 and screen.get_height() * 0.1 + 120 <= init.mouse[1] <= screen.get_height() * 0.1 + 30 + 120:
                            init.intero_buttons["Copy"] = True, (False, None), (False, None), None
                            init.intero_buttons["jointure"] = False, (False, None), (False, None)
                        elif init.intero_buttons["Copy"][0]:
                            if not init.intero_buttons["Copy"][1][0]:
                                if screen.get_width() * 0.05 <= init.mouse[0] <= screen.get_width() * 0.05 + screen.get_width() * 0.7 and screen.get_width() * 0.05 <= init.mouse[1] <= screen.get_width() * 0.05 + screen.get_height() * 0.8:
                                    init.intero_buttons["Copy"] = True, (True, init.mouse), (False, None), None
                                    break
                                else:
                                    init.error = True, "error 1: please click in the container"
                                    error_time = time.time()
                                    break
                            if init.intero_buttons["Copy"][1][0] and not init.intero_buttons["Copy"][2][0]:
                                if screen.get_width() * 0.05 <= init.mouse[0] <= screen.get_width() * 0.05 + screen.get_width() * 0.7 and screen.get_width() * 0.05 <= init.mouse[1] <= screen.get_width() * 0.05 + screen.get_height() * 0.8:
                                    init.intero_buttons["Copy"] = True, init.intero_buttons["Copy"][1], (True, init.mouse), None
                                    init.error = True, "please click in a empty space to paste it"
                                    error_time = time.time()
                                    break
                                else:
                                    init.error = True, "error 2: please click in the container"
                                    error_time = time.time()
                                    break
                            if init.intero_buttons["Copy"][2][0]:
                                if screen.get_width() * 0.05 <= init.mouse[0] <= screen.get_width() * 0.05 + screen.get_width() * 0.7 and screen.get_width() * 0.05 <= init.mouse[1] <= screen.get_width() * 0.05 + screen.get_height() * 0.8:
                                    first_point = init.intero_buttons["Copy"][1][1]
                                    second_point = init.intero_buttons["Copy"][2][1]
                                    rect = pygame.Rect(first_point[0], first_point[1], second_point[0] - first_point[0], second_point[1] - first_point[1])

                                    objs_rect = get_rects(init.bfn_fun, init, screen.get_width() * 0.05, screen.get_width() * 0.05)
                                    contains = []
                                    for i in range(len(objs_rect)):
                                        if not objs_rect[i] in contains:
                                            if rect.left <= objs_rect[i].left and rect.top <= objs_rect[i].top and rect.right >= objs_rect[i].right and rect.bottom >= objs_rect[i].bottom:
                                                contains.append(init.bfn_fun[i])

                                    if len(contains) == 0:
                                        init.error = True, "error : please select a graph to copy"
                                        error_time = time.time()
                                        init.intero_buttons["Copy"] = False, (False, None), (False, None), None
                                        break

                                    contains_fillterd = contains
                                    contains_fillterd_copy = Copy(contains_fillterd)


                                    if len(contains_fillterd) == 0:
                                        init.error = True, "error : you can't copy a relation"
                                        error_time = time.time()
                                        init.intero_buttons["Copy"] = False, (False, None), (False, None), None
                                        break

                                    offset_x = init.mouse[0] - (contains_fillterd[0].x + screen.get_width() * 0.05)
                                    offset_y = init.mouse[1] - (contains_fillterd[0].y + screen.get_width() * 0.05)

                                    if type(contains_fillterd_copy) == Concept: contains_fillterd_copy = [contains_fillterd_copy]
                                    contains_fillterd_copy = update_fait_coordinates_copy(contains_fillterd_copy, offset_x, offset_y - init.make_bfn_offset)
                                    # contains_fillterd_copy = get_objs(contains_fillterd_copy)
                                    init.bfn_fun += contains_fillterd_copy

                                    init.intero_buttons["Copy"] = False, (False, None), (False, None), None
                                    init.error = True, "copied successfully"
                                    error_time = time.time()
                                    break
                                else:
                                    init.error = True, "error 3: please click in the container"
                                    error_time = time.time()
                                    break
                        elif init.intero_buttons["Restriction"][0] and screen.get_width() * 0.05 <= init.mouse[0] <= screen.get_width() * 0.7 and screen.get_width() * 0.05 <= init.mouse[1] <= screen.get_height() * 0.8:
                            rect = Rect(init.mouse[0], init.mouse[1]  - init.make_bfn_offset, 1, 1)
                            objs_rect = get_rects(init.bfn_fun, init, screen.get_width() * 0.05, screen.get_width() * 0.05)

                            collide = pygame.Rect.collidelist(rect, objs_rect)
                            if collide == -1:
                                init.error = True, "error : please select a concept"
                                error_time = time.time()
                            elif type(init.bfn_fun[collide]) == Relation:
                                init.error = True, "error : you can't restric relations"
                                error_time = time.time()
                            elif type(init.bfn_fun[collide]) == Concept:
                                init.intero_buttons["Restriction"] = False, True, init.bfn_fun[collide], False
                                init.Restriction_saved_ref = init.bfn_fun[collide].ref
                        elif init.intero_buttons["Restriction"][2] and screen.get_width() / 2 - 400 / 2 + 70 + init.font2.size("ref : ")[0] <= init.mouse[0] <= screen.get_width() / 2 - 400 / 2 + 70 + init.font2.size("ref : ")[0] + init.font2.size(init.intero_buttons["Restriction"][2].ref)[
                            0] + 10 and screen.get_height() / 2 - 400 / 2 + 100 <= init.mouse[1] <= screen.get_height() / 2 - 400 / 2 + 100 + 10 + init.font2.size("A")[1]:
                            init.intero_buttons["Restriction"] = False, True, init.intero_buttons["Restriction"][2], not init.intero_buttons["Restriction"][3]
                        elif init.intero_buttons["Restriction"][1] and screen.get_width() / 2 - 400 / 2 + 100 <= init.mouse[0] <= screen.get_width() / 2 - 400 / 2 + 100 + 70 and screen.get_height() / 2 - 400 / 2 + 300 <= init.mouse[1] <= screen.get_height() / 2 - 400 / 2 + 300 + 40:
                            init.intero_buttons["Restriction"] = False, False, None, False
                        elif init.intero_buttons["Restriction"][1] and screen.get_width() / 2 - 400 / 2 + 200 <= init.mouse[0] <= screen.get_width() / 2 - 400 / 2 + 200 + 70 and screen.get_height() / 2 - 400 / 2 + 300 <= init.mouse[1] <= screen.get_height() / 2 - 400 / 2 + 300 + 40:
                            init.intero_buttons["Restriction"][2].ref = init.Restriction_saved_ref
                            init.intero_buttons["Restriction"] = False, False, None, False
                        elif screen.get_width() * 0.8 <= init.mouse[0] <= screen.get_width() * 0.8 + 70 and screen.get_height() * 0.1 + 80 <= init.mouse[1] <= screen.get_height() * 0.1 + 30 + 80:
                            init.intero_buttons["make BFN"] = False
                    elif screen.get_width() * 0.8 <= init.mouse[0] <= screen.get_width() * 0.8 + 70 and screen.get_height() * 0.1 + 40 <= init.mouse[1] <= screen.get_height() * 0.1 + 30 + 40:
                        init.intero_buttons["show BR"] = not init.intero_buttons["show BR"]
                        init.intero_buttons["show BF"] = False
                        init.intero_buttons["make BFN"] = False
                        init.intero_buttons["auto BFN"] = False
                    elif screen.get_width() * 0.8 <= init.mouse[0] <= screen.get_width() * 0.8 + 70 and screen.get_height() * 0.1 <= init.mouse[1] <= screen.get_height() * 0.1 + 30:
                        init.intero_buttons["show BF"] = not init.intero_buttons["show BF"]
                        init.intero_buttons["show BR"] = False
                        init.intero_buttons["make BFN"] = False
                        init.intero_buttons["auto BFN"] = False
                    elif screen.get_width() * 0.8 <= init.mouse[0] <= screen.get_width() * 0.8 + 70 and screen.get_height() * 0.1 + 80 <= init.mouse[1] <= screen.get_height() * 0.1 + 30 + 80:
                        init.intero_buttons["show BF"] = False
                        init.intero_buttons["show BR"] = False
                        init.intero_buttons["make BFN"] = True
                        init.intero_buttons["auto BFN"] = False
                    elif screen.get_width() * 0.8 <= init.mouse[0] <= screen.get_width() * 0.8 + 70 and screen.get_height() * 0.1 + 120 <= init.mouse[1] <= screen.get_height() * 0.1 + 30 + 120:
                        init.intero_buttons["show BF"] = False
                        init.intero_buttons["show BR"] = False
                        init.intero_buttons["make BFN"] = False
                        init.intero_buttons["auto BFN"] = not init.intero_buttons["auto BFN"]
                        init.BFN = Copy(init.bfn)
                        auto_BFN(screen, init)
                    elif init.intero_buttons["auto BFN"] and screen.get_width() * 0.8 + 80 <= init.mouse[0] <= screen.get_width() * 0.8 + 150 and screen.get_height() * 0.1 + 120 <= init.mouse[1] <= screen.get_height() * 0.1 + 30 + 120:
                        init.intero_buttons["chainage_avant"] = not init.intero_buttons["chainage_avant"]

                        chainge_avant(init)
                        auto_BFN(screen, init)








            elif event.type == pygame.MOUSEWHEEL:
                if init.bf_interface and 82 <= init.mouse[0] <= 82 + screen.get_width() * 0.6 and screen.get_height() * 0.05 <= init.mouse[1] <= screen.get_height() * 0.05 + screen.get_height() * 0.9:
                    init.bf_interface_offset += event.y * 10
                elif init.br_interface and 82 <= init.mouse[0] <= 82 + screen.get_width() * 0.6 and screen.get_height() * 0.05 <= init.mouse[1] <= screen.get_height() * 0.05 + screen.get_height() * 0.9:
                    init.br_interface_offset += event.y * 10
                elif init.edit_display and 50 + 25 <= init.mouse[0] <= 50 + 25 + (screen.get_width() - 200) / 3 - 50 and 80 + 50 <= init.mouse[1] <= 80 + 50 + screen.get_height() - 130 - 100:
                    init.offset_bf_list += event.y * 10
                elif init.edit_display and 50 * 2 + init.width + 25 <= init.mouse[0] <= 50 * 2 + init.width + 25 + (screen.get_width() - 200) / 3 - 50 and 80 + 50 <= init.mouse[1] <= 80 + 50 + screen.get_height() - 130 - 100:
                    init.offset_br_list += event.y * 10
                elif init.edit_display and 50 * 3 + init.width * 2 + 25 <= init.mouse[0] <= 50 * 3 + init.width * 2 + 25 + (screen.get_width() - 200) / 3 - 50 and 80 + 50 <= init.mouse[1] <= 80 + 50 + screen.get_height() - 130 - 100:
                    init.vo_offset += event.y * 10
                elif init.interro_display and init.intero_buttons["make BFN"]:
                    if screen.get_width() * 0.05 <= init.mouse[0] <= screen.get_width() * 0.05 + screen.get_width() * 0.7 and screen.get_width() * 0.05 <= init.mouse[1] <= screen.get_width() * 0.05 + screen.get_height() * 0.8:
                        init.make_bfn_offset += event.y * 10
                    if init.show_rq and screen.get_width() * 0.76 <= init.mouse[0] <= screen.get_width() and screen.get_height() * 0.7 <= init.mouse[1] <= screen.get_height() :
                        init.fun_rq_offset += event.y * 10
                    if init.show_answer and screen.get_width() * 0.76 <= init.mouse[0] <= screen.get_width() and screen.get_height() * 0.7 <= init.mouse[1] <= screen.get_height() :
                        init.fun_answer_offset += event.y * 10
                    if init.show_answer_filter and screen.get_width() * 0.76 <= init.mouse[0] <= screen.get_width() and screen.get_height() * 0.7 <= init.mouse[1] <= screen.get_height() :
                        init.fun_answer_filter_offset += event.y * 10
                elif init.interro_display and init.intero_buttons["auto BFN"]:
                    if screen.get_width() * 0.05 <= init.mouse[0] <= screen.get_width() * 0.05 + screen.get_width() * 0.7 and screen.get_width() * 0.05 <= init.mouse[1] <= screen.get_width() * 0.05 + screen.get_height() * 0.8:
                        init.auto_bfn_offset += event.y * 10

            elif event.type == pygame.KEYDOWN:
                if not init.intero_buttons["projection"] and event.key == pygame.K_ESCAPE and not init.br_interface and not init.bf_interface:
                    sys.exit()
                elif init.interro_display:
                    if init.intero_buttons["Restriction"][3]:
                        if event.key == pygame.K_BACKSPACE:
                            ref = init.intero_buttons["Restriction"][2].ref[:-1]
                            Restriction(init.intero_buttons["Restriction"][2], ref)
                            init.intero_buttons["Restriction"] = False, True, init.intero_buttons["Restriction"][2], True
                        elif event.key == pygame.K_RETURN:
                            init.intero_buttons["Restriction"] = False, True, init.intero_buttons["Restriction"][2], False
                        else:
                            ref = init.intero_buttons["Restriction"][2].ref + event.unicode
                            Restriction(init.intero_buttons["Restriction"][2], ref)
                            init.intero_buttons["Restriction"] = False, True, init.intero_buttons["Restriction"][2], True
                    elif init.intero_buttons["projection"]:
                        if init.new_concept and init.new_concept_in[0]:
                            if init.new_concept_name_typing:
                                if event.key == pygame.K_BACKSPACE:
                                    init.new_concept_name = init.new_concept_name[:-1]
                                elif event.key == pygame.K_RETURN:
                                    init.new_concept_name_typing = False
                                elif event.key == pygame.K_TAB:
                                    init.new_concept_name_typing = False
                                    init.new_concept_ref_typing = True
                                else:
                                    init.new_concept_name += event.unicode
                            elif init.new_concept_ref_typing:
                                if event.key == pygame.K_BACKSPACE:
                                    init.new_concept_ref = init.new_concept_ref[:-1]
                                elif event.key == pygame.K_RETURN:
                                    init.new_concept_ref_typing = False
                                elif event.key == pygame.K_TAB:
                                    init.new_concept_name_typing = True
                                    init.new_concept_ref_typing = False
                                else:
                                    init.new_concept_ref += event.unicode
                        elif init.new_relation and init.new_relation_in[0]:
                            if init.new_relation_name_typing:
                                if event.key == pygame.K_BACKSPACE:
                                    init.new_relation_name = init.new_relation_name[:-1]
                                elif event.key == pygame.K_RETURN:
                                    init.new_relation_name_typing = False
                                else:
                                    init.new_relation_name += event.unicode
                        else:
                            if event.key == pygame.K_ESCAPE:
                                init.new_concept = False
                                init.new_relation = False
                                init.new_fait = False, False, []
                                init.new_arc = False

                elif init.bf_interface :

                    if init.new_concept and init.new_concept_in[0] :
                        if init.new_concept_name_typing:
                            if event.key == pygame.K_BACKSPACE:
                                init.new_concept_name = init.new_concept_name[:-1]
                            elif event.key == pygame.K_RETURN:
                                init.new_concept_name_typing = False
                            elif event.key == pygame.K_TAB:
                                init.new_concept_name_typing = False
                                init.new_concept_ref_typing = True
                            else:
                                init.new_concept_name += event.unicode
                        elif init.new_concept_ref_typing:
                            if event.key == pygame.K_BACKSPACE:
                                init.new_concept_ref = init.new_concept_ref[:-1]
                            elif event.key == pygame.K_RETURN:
                                init.new_concept_ref_typing = False
                            elif event.key == pygame.K_TAB:
                                init.new_concept_name_typing = True
                                init.new_concept_ref_typing = False
                            else:
                                init.new_concept_ref += event.unicode
                    elif init.new_relation and init.new_relation_in[0]:
                        if init.new_relation_name_typing:
                            if event.key == pygame.K_BACKSPACE:
                                init.new_relation_name = init.new_relation_name[:-1]
                            elif event.key == pygame.K_RETURN:
                                init.new_relation_name_typing = False
                            else:
                                init.new_relation_name += event.unicode
                    else:
                        if event.key == pygame.K_ESCAPE:
                            init.new_concept = False
                            init.new_relation = False
                            init.new_fait =  False, False, []
                            init.new_arc = False
                elif init.br_interface:
                    if init.new_concept and init.new_concept_in[0]:
                        if init.new_concept_name_typing:
                            if event.key == pygame.K_BACKSPACE:
                                init.new_concept_name = init.new_concept_name[:-1]
                            elif event.key == pygame.K_RETURN:
                                init.new_concept_name_typing = False
                            elif event.key == pygame.K_TAB:
                                init.new_concept_name_typing = False
                                init.new_concept_ref_typing = True
                            else:
                                init.new_concept_name += event.unicode
                        elif init.new_concept_ref_typing:
                            if event.key == pygame.K_BACKSPACE:
                                init.new_concept_ref = init.new_concept_ref[:-1]
                            elif event.key == pygame.K_RETURN:
                                init.new_concept_ref_typing = False
                            elif event.key == pygame.K_TAB:
                                init.new_concept_name_typing = True
                                init.new_concept_ref_typing = False
                            else:
                                init.new_concept_ref += event.unicode
                    elif init.new_relation and init.new_relation_in[0]:
                        if init.new_relation_name_typing:
                            if event.key == pygame.K_BACKSPACE:
                                init.new_relation_name = init.new_relation_name[:-1]
                            elif event.key == pygame.K_RETURN:
                                init.new_relation_name_typing = False
                            else:
                                init.new_relation_name += event.unicode
                    else:
                        if event.key == pygame.K_ESCAPE:
                            init.new_concept = False
                            init.new_relation = False


                            if not init.new_arc_point1[0]:
                                init.new_arc = False
        keys = pygame.key.get_pressed()
        if init.br_interface:
            if init.new_concept and init.new_concept_in[0]:
                if init.new_concept_name_typing:
                    if keys[pygame.K_BACKSPACE]:
                        init.new_concept_name = init.new_concept_name[:-1]

                elif init.new_concept_ref_typing:
                    if keys[pygame.K_BACKSPACE]:
                        init.new_concept_ref = init.new_concept_ref[:-1]

            elif init.new_relation and init.new_relation_in[0]:
                if init.new_relation_name_typing:
                    if keys[pygame.K_BACKSPACE]:
                        init.new_relation_name = init.new_relation_name[:-1]
        elif init.bf_interface:
            if init.new_concept and init.new_concept_in[0]:
                if init.new_concept_name_typing:
                    if keys[pygame.K_BACKSPACE]:
                        init.new_concept_name = init.new_concept_name[:-1]

                elif init.new_concept_ref_typing:
                    if keys[pygame.K_BACKSPACE]:
                        init.new_concept_ref = init.new_concept_ref[:-1]

            elif init.new_relation and init.new_relation_in[0]:
                if init.new_relation_name_typing:
                    if keys[pygame.K_BACKSPACE]:
                        init.new_relation_name = init.new_relation_name[:-1]
        if init.edit_display:
            display_edit(screen, init)
        elif init.interro_display:
            display_interro(screen, init)

        draw(screen, init)
        if init.bf_interface:
            new_bf_intrface(screen, init)
        elif init.br_interface:
            new_br_intrface(screen, init)
        elif init.intero_buttons["projection"]:
            new_rq_intrface(screen, init)
        elif init.fun_projecting:
            if init.show_rq:
                show_fun_rq(screen, init)
            elif init.show_answer:
                show_fun_answer(screen, init)
            elif init.show_answer_filter:
                show_fun_answer_filter(screen, init)


        if init.error[0]:
            if time.time() - error_time > 2:
                init.error = False, None
            else:
                raise_(screen, init, init.error[1])
        pygame.display.update()


if __name__ == '__main__':
    main()
