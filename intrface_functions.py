import copy
import time
from array import array
from shlex import shlex

import pygame
from pygame.locals import Rect

from classs import Concept


def draw(screen, init):
    top_bar = pygame.Surface((screen.get_width(), 30))
    top_bar.fill((80, 80, 80))
    top_bar_title = init.font2.render("MCI TP", True, (255, 255, 255))
    top_bar.blit(top_bar_title, (screen.get_width() / 2 - init.font2.size("MCI TP")[0] / 2, 5))
    if init.edit_display or not init.bf_interface and 55 <= init.mouse[0] <= 55 + 30 + init.font2.size("edit")[0] and 0 <= init.mouse[1] <= 30:
        top_bar_edit = init.font2.render("edit", True, (255, 0, 0))
    else:
        top_bar_edit = init.font2.render("edit", True, (255, 255, 255))

    if init.interro_display or not init.bf_interface and 80 + 10 + init.font2.size("edit")[0] <= init.mouse[0] <= 80 + 10 + init.font2.size("edit")[0] + 30 + init.font2.size("interro")[0] and 0 <= init.mouse[1] <= 30:
        top_bar_interro = init.font2.render("interro", True, (255, 0, 0))
    else:
        top_bar_interro = init.font2.render("interro", True, (255, 255, 255))

    top_bar_edit_background = pygame.Surface((30 + init.font2.size("edit")[0], 30))
    if init.edit_display:
        top_bar_edit_background.fill((35, 35, 35))
    else:
        top_bar_edit_background.fill((60, 60, 60))
    top_bar.blit(top_bar_edit_background, (55, 0))
    top_bar_interro_background = pygame.Surface((30 + init.font2.size("interro")[0], 30))
    if init.interro_display:
        top_bar_interro_background.fill((35, 35, 35))
    else:
        top_bar_interro_background.fill((60, 60, 60))
    top_bar.blit(top_bar_interro_background, (80 + 10 + init.font2.size("edit")[0], 0))
    top_bar.blit(top_bar_edit_background, (55, 0))
    top_bar.blit(top_bar_edit, (55 + (30 + init.font2.size("edit")[0]) / 2 - init.font2.size("edit")[0] / 2, 5))
    top_bar.blit(top_bar_interro, (80 + 10 + init.font2.size("edit")[0] + (30 + init.font2.size("interro")[0]) / 2 - init.font2.size("interro")[0] / 2, 5))
    screen.blit(top_bar, (0, 0))

    if not init.bf_interface and screen.get_width() - 25 <= init.mouse[0] <= screen.get_width() - 5 and 5 <= init.mouse[1] <= 25:
        exit_btn = pygame.image.load("images/exit_red.png")
    else:
        exit_btn = pygame.image.load("images/exit_white.png")
    screen.blit(exit_btn, (screen.get_width() - 25, 5))


def display_edit(screen, init):

    width = (screen.get_width() - 200) / 3
    height = screen.get_height() - 130

    bf_surface = pygame.Surface((width, height))
    bf_surface.fill((50, 50, 50))
    bf_title = init.font3.render("Base de Fait", True, (255, 255, 255))
    bf_surface.blit(bf_title, (bf_surface.get_width() / 2 - init.font3.size("Base de Fait")[0] / 2, 7))
    if 50 + bf_surface.get_width() / 2 - init.font2.size("new BF")[0] / 2 - 8 <= init.mouse[0] <= 50 + bf_surface.get_width() / 2 - init.font2.size("new BF")[0] / 2 - 8 + init.font2.size("new BF")[0] + 16 and 80 + bf_surface.get_height() - 34 <= init.mouse[1] <= 80 + bf_surface.get_height() - 34 + 25:
        pygame.draw.rect(bf_surface, (50, 50, 50), (bf_surface.get_width() / 2 - init.font2.size("new BF")[0] / 2 - 10, bf_surface.get_height() - 36, init.font2.size("new BF")[0] + 20, 29), border_radius=10)
        new_bf = init.font2.render("edit BF", True, (255, 255, 255))
    else:
        pygame.draw.rect(bf_surface, (255, 255, 255), (bf_surface.get_width() / 2 - init.font2.size("new BF")[0] / 2 - 10, bf_surface.get_height() - 36, init.font2.size("new BF")[0] + 20, 29), border_radius=10)
        new_bf = init.font2.render("edit BF", True, (50, 50, 50))
    pygame.draw.rect(bf_surface, (255, 255, 255), (bf_surface.get_width() / 2 - init.font2.size("new BF")[0] / 2 - 10, bf_surface.get_height() - 36, init.font2.size("new BF")[0] + 20, 29), 2, border_radius=10)
    bf_surface.blit(new_bf, (bf_surface.get_width() / 2 - init.font2.size("new BF")[0] / 2, bf_surface.get_height() - 32))
    bf_list_surface = pygame.Surface((bf_surface.get_width() - 50, bf_surface.get_height() - 100))
    bf_list_surface.fill((70, 70, 70))

    if not len(init.bf_main_list) == 0:
        render_multi_line(bf_list_surface, init.font2, init.bf_main_list, 10, 10, init.font2.size("A")[1], init, init.offset_bf_list)
    pygame.draw.rect(bf_list_surface, (35, 35, 35), (0, 0, bf_list_surface.get_width(), bf_list_surface.get_height()), 4)

    bf_surface.blit(bf_list_surface, (25, 50))
    bf_surface.set_alpha(230)
    screen.blit(bf_surface, (50, 80))

    br_surface = pygame.Surface((width, height))
    br_surface.fill((50, 50, 50))
    br_title = init.font3.render("Base de Regle", True, (255, 255, 255))
    br_surface.blit(br_title, (br_surface.get_width() / 2 - init.font3.size("Base de Regle")[0] / 2, 7))
    if 50 * 2 + width + br_surface.get_width() / 2 - init.font2.size("new BR")[0] / 2 - 8 <= init.mouse[0] <= 50 * 2 + width + br_surface.get_width() / 2 - init.font2.size("new BR")[0] / 2 - 8 + init.font2.size("new BR")[0] + 16 and 80 + br_surface.get_height() - 34 <= init.mouse[1] <= 80 + br_surface.get_height() - 34 + 25:
        pygame.draw.rect(br_surface, (50, 50, 50), (br_surface.get_width() / 2 - init.font2.size("new BR")[0] / 2 - 10, br_surface.get_height() - 36, init.font2.size("new BR")[0] + 20, 29), border_radius=10)
        new_br = init.font2.render("new BR", True, (255, 255, 255))
    else:
        pygame.draw.rect(br_surface, (255, 255, 255), (br_surface.get_width() / 2 - init.font2.size("new BR")[0] / 2 - 10, br_surface.get_height() - 36, init.font2.size("new BR")[0] + 20, 29), border_radius=10)
        new_br = init.font2.render("new BR", True, (50, 50, 50))
    pygame.draw.rect(br_surface, (255, 255, 255), (br_surface.get_width() / 2 - init.font2.size("new BR")[0] / 2 - 10, br_surface.get_height() - 36, init.font2.size("new BR")[0] + 20, 29), 2, border_radius=10)
    br_surface.blit(new_br, (br_surface.get_width() / 2 - init.font2.size("new BR")[0] / 2, br_surface.get_height() - 32))
    br_list_surface = pygame.Surface((br_surface.get_width() - 50, br_surface.get_height() - 100))
    br_list_surface.fill((70, 70, 70))
    if not len(init.br_main_list) == 0:
        render_multi_line_br(br_list_surface, init.font2, init.br_main_list, 10, 10, init.font2.size("A")[1], init, init.offset_br_list)
    pygame.draw.rect(br_list_surface, (35, 35, 35), (0, 0, br_list_surface.get_width(), br_list_surface.get_height()), 4)

    br_surface.blit(br_list_surface, (25, 50))
    br_surface.set_alpha(230)
    screen.blit(br_surface, (50 * 2 + width, 80))

    vo_surface = pygame.Surface((width, height))
    vo_surface.fill((50, 50, 50))
    vo_title = init.font3.render("vocabulaire", True, (255, 255, 255))
    vo_surface.blit(vo_title, (vo_surface.get_width() / 2 - init.font3.size("vocabulaire")[0] / 2, 7))

    vo_list_surface = pygame.Surface((vo_surface.get_width() - 50, vo_surface.get_height() - 100))
    vo_list_surface.fill((70, 70, 70))
    l = get_vocabulaire(init)
    display_vo_list(vo_list_surface, init, init.vo_offset, l[0], l[1], l[2], l[3], l[4])
    pygame.draw.rect(vo_list_surface, (35, 35, 35), (0, 0, vo_list_surface.get_width(), vo_list_surface.get_height()), 4)
    vo_surface.blit(vo_list_surface, (25, 50))
    vo_surface.set_alpha(230)
    screen.blit(vo_surface, (50 * 3 + width * 2, 80))


def new_bf_intrface(screen, init):
    from classs import Concept
    black_fillter = pygame.Surface((screen.get_width(), screen.get_height()))
    black_fillter.fill((0, 0, 0))
    black_fillter.set_alpha(128)
    screen.blit(black_fillter, (0, 0))


    pygame.draw.rect(screen, (255, 255, 255), (80, screen.get_height() * 0.05, screen.get_width() * 0.6, screen.get_height() * 0.9), 2)

    side_container = pygame.Surface((screen.get_width() * 0.2, screen.get_height() * 0.6))
    side_container.fill((50, 50, 50))
    side_container.blit(init.font2.render("Concept", True, (255, 255, 255)), (side_container.get_width() / 2 - init.font2.size("Concept")[0] / 2, 20))
    if 80 + screen.get_width() * 0.6 + 80 + side_container.get_width() / 2 - 70 <= init.mouse[0] <= 80 + screen.get_width() * 0.6 + 80 + side_container.get_width() / 2 - 70 + 140 and screen.get_height() * 0.2 + 10 + init.font2.size("Concept")[1] * 2 <= init.mouse[1] <= screen.get_height() * 0.2 + 10 + init.font2.size("Concept")[1] * 2  + 40:
        pygame.draw.rect(side_container, (255, 0, 0), (side_container.get_width() / 2 - 70, 10 + init.font2.size("Concept")[1] * 2, 140, 40), 2)
        side_container.blit(init.font2.render("Name : Ref", True, (255, 0, 0)), (side_container.get_width() / 2 - 70 + 140 / 2 - init.font2.size("Name : Ref")[0] / 2, 10 + init.font2.size("Concept")[1] * 2 + 10))
    else:
        pygame.draw.rect(side_container, (255, 255, 255), (side_container.get_width() / 2 - 70, 10 + init.font2.size("Concept")[1] * 2, 140, 40), 2)
        side_container.blit(init.font2.render("Name : Ref", True, (255, 255, 255)), (side_container.get_width() / 2 - 70 + 140 / 2 - init.font2.size("Name : Ref")[0] / 2, 10 + init.font2.size("Concept")[1] * 2 + 10))

    side_container.blit(init.font2.render("Relation", True, (255, 255, 255)), (side_container.get_width() / 2 - init.font2.size("Relation")[0] / 2, 120))
    if 80 + screen.get_width() * 0.6 + 80 + side_container.get_width() / 2 - 70 <= init.mouse[0] <= 80 + screen.get_width() * 0.6 + 80 + side_container.get_width() / 2 - 70 + 140 and screen.get_height() * 0.2 + 110 + init.font2.size("Relation")[1] * 2 <= init.mouse[1] <= screen.get_height() * 0.2 + 110 + init.font2.size("Relation")[1] * 2 + 40:
        pygame.draw.rect(side_container, (255, 0, 0), (side_container.get_width() / 2 - 70, 110 + init.font2.size("Relation")[1] * 2, 140, 40), 2, 20)
        side_container.blit(init.font2.render("Name", True, (255, 0, 0)), (side_container.get_width() / 2 - 70 + 140 / 2 - init.font2.size("Name")[0] / 2, 110 + init.font2.size("Relation")[1] * 2 + 10))
    else:
        pygame.draw.rect(side_container, (255, 255, 255), (side_container.get_width() / 2 - 70, 110 + init.font2.size("Relation")[1] * 2, 140, 40), 2, 20)
        side_container.blit(init.font2.render("Name", True, (255, 255, 255)), (side_container.get_width() / 2 - 70 + 140 / 2 - init.font2.size("Name")[0] / 2, 110 + init.font2.size("Relation")[1] * 2 + 10))


    if 80 + screen.get_width() * 0.6 + 80 + 80 - 40 <= init.mouse[0] <= 80 + screen.get_width() * 0.6 + 80 + 80 - 40  + 80 and screen.get_height() * 0.2 + side_container.get_height() - 70 <= init.mouse[1] <= screen.get_height() * 0.2 + side_container.get_height() - 70 + 30:
        pygame.draw.rect(side_container, (50, 50, 50), (80, side_container.get_height() - 70, 80, 30), border_radius=4)
        side_container.blit(init.font2.render("Save", True, (255, 0, 0)), (80 - init.font2.size("Save")[0] / 2, side_container.get_height() - 66))
    else:
        pygame.draw.rect(side_container, (255, 255, 255), (80 - 40, side_container.get_height() - 70, 80, 30), border_radius=4)
        side_container.blit(init.font2.render("Save", True, (50, 50, 50)), (80 - init.font2.size("Save")[0] / 2, side_container.get_height() - 66))

    if 80 + screen.get_width() * 0.6 + side_container.get_width() - 80 + 80 - 40 <= init.mouse[0] <= 80 + screen.get_width() * 0.6 + side_container.get_width() - 80 + 80 - 40  + 80 and screen.get_height() * 0.2 + side_container.get_height() - 70 <= init.mouse[1] <= screen.get_height() * 0.2 + side_container.get_height() - 70 + 30:
        pygame.draw.rect(side_container, (50, 50, 50), (side_container.get_width() - 80, side_container.get_height() - 70, 80, 30), border_radius=4)
        side_container.blit(init.font2.render("Cancel", True, (255, 0, 0)), (side_container.get_width() - 80 - init.font2.size("Cancel")[0] / 2, side_container.get_height() - 66))
    else:
        pygame.draw.rect(side_container, (255, 255, 255), (side_container.get_width() - 80 - 40, side_container.get_height() - 70, 80, 30), border_radius=4)
        side_container.blit(init.font2.render("Cancel", True, (50, 50, 50)), (side_container.get_width() - 80 - init.font2.size("Cancel")[0] / 2, side_container.get_height() - 66))

    side_container.blit(init.font2.render("Arc", True, (255, 255, 255)), (side_container.get_width() / 2 - init.font2.size("Arc")[0] / 2, 220))
    screen.blit(side_container, (80 + screen.get_width() * 0.6 + 80, screen.get_height() * 0.2))

    if 80 + screen.get_width() * 0.6 + 80 + side_container.get_width() / 2 - 70 <= init.mouse[0] <= 80 + screen.get_width() * 0.6 + 80 + side_container.get_width() / 2 - 70 + 140 and screen.get_height() * 0.2 + 210 + init.font2.size("Arc")[1] * 2 <= init.mouse[1] <= screen.get_height() * 0.2 + 210 + init.font2.size("Arc")[1] * 2 + 40:
        pygame.draw.line(screen, (255, 0, 0), (80 + screen.get_width() * 0.6 + 80 + side_container.get_width() / 2 - 70, screen.get_height() * 0.2 + 210 + init.font2.size("Arc")[1] * 2 + 20), (80 + screen.get_width() * 0.6 + 80 + side_container.get_width() / 2 - 70 + 140, screen.get_height() * 0.2 + 210 + init.font2.size("Arc")[1] * 2 + 20), 2)
    else:
        pygame.draw.line(screen, (255, 255, 255), (80 + screen.get_width() * 0.6 + 80 + side_container.get_width() / 2 - 70, screen.get_height() * 0.2 + 210 + init.font2.size("Arc")[1] * 2 + 20), (80 + screen.get_width() * 0.6 + 80 + side_container.get_width() / 2 - 70 + 140, screen.get_height() * 0.2 + 210 + init.font2.size("Arc")[1] * 2 + 20), 2)

    main_container = pygame.Surface((screen.get_width() * 0.6, screen.get_height() * 0.9))
    main_container.fill((50, 50, 50))
    pygame.draw.rect(main_container, (255, 255, 255), (0, 0, main_container.get_width(), main_container.get_height()), 2)

    if not len(init.bf_array) == 0:
        for element in init.bf_array:
            if type(element) == Concept:
                pygame.draw.rect(main_container, (255, 255, 255), (element.x - 80, element.y - screen.get_height() * 0.05 + init.bf_interface_offset, 20 + init.font2.size(element.name + " : " + element.ref)[0], 40), 2)
                main_container.blit(init.font2.render((element.name + " : " + element.ref), True, (255, 255, 255)), (element.x + (20 + init.font2.size(element.name + " : " + element.ref)[0]) / 2 - init.font2.size(element.name + " : " + element.ref)[0] / 2 - 80, element.y + 10 - screen.get_height() * 0.05 + init.bf_interface_offset))
            else:
                pygame.draw.rect(main_container, (255, 255, 255), (element.x - 80, element.y - screen.get_height() * 0.05 + init.bf_interface_offset, 20 + init.font2.size(element.name)[0], 40), 2, 20)
                main_container.blit(init.font2.render(element.name, True, (255, 255, 255)), (element.x + (20 + init.font2.size(element.name)[0]) / 2 - init.font2.size(element.name)[0] / 2 - 80, element.y + 10 - screen.get_height() * 0.05 + init.bf_interface_offset))
            draw_arc(element, init, screen, main_container, init.bf_interface_offset)


    # if not len(init.bf_arc_array) == 0:
    #     for element in init.bf_arc_array:
    #         if element[0].right < element[1].left:
    #             x1 = element[0].right
    #             y1 = element[0].top + 20
    #             x2 = element[1].left
    #             y2 = element[1].top + 20
    #         elif element[0].left > element[1].right:
    #             x1 = element[0].left
    #             y1 = element[0].top + 20
    #             x2 = element[1].right
    #             y2 = element[1].top + 20
    #         elif element[0].top > element[1].top:
    #             x1 = element[0].left + (element[0].right - element[0].left) / 2
    #             y1 = element[0].top
    #             x2 = element[1].left + (element[1].right - element[1].left) / 2
    #             y2 = element[1].bottom
    #         else:
    #             x1 = element[0].left + (element[0].right - element[0].left) / 2
    #             y1 = element[0].bottom
    #             x2 = element[1].left + (element[1].right - element[1].left) / 2
    #             y2 = element[1].top
    #         draw_arrow(main_container, pygame.Vector2(x1 - 80, y1 - screen.get_height() * 0.05), pygame.Vector2(x2 - 80, y2 - screen.get_height() * 0.05), (255, 255, 255), 3, 20, 10)
    element_drwaned = []
    for element in init.bf_main_list:
        if type(element) == Concept:
            obj = element
            if not obj in element_drwaned:
                if type(obj) == Concept:
                    pygame.draw.rect(main_container, (255, 255, 255), (obj.x - 80, obj.y - screen.get_height() * 0.05 + init.bf_interface_offset, 20 + init.font2.size(obj.name + " : " + obj.ref)[0], 40), 2)
                    main_container.blit(init.font2.render((obj.name + " : " + obj.ref), True, (255, 255, 255)),
                                      (obj.x + (20 + init.font2.size(obj.name + " : " + obj.ref)[0]) / 2 - init.font2.size(obj.name + " : " + obj.ref)[0] / 2 - 80, obj.y + 10 - screen.get_height() * 0.05 + init.bf_interface_offset))
                else:
                    pygame.draw.rect(main_container, (255, 255, 255), (obj.x - 80, obj.y - screen.get_height() * 0.05 + init.bf_interface_offset, 20 + init.font2.size(obj.name)[0], 40), 2, 20)
                    main_container.blit(init.font2.render(obj.name, True, (255, 255, 255)), (obj.x + (20 + init.font2.size(obj.name)[0]) / 2 - init.font2.size(obj.name)[0] / 2 - 80, obj.y + 10 - screen.get_height() * 0.05 + init.bf_interface_offset))

                element_drwaned.append(obj)
                continue
        for obj in element:
            if not obj in element_drwaned:
                if type(obj) == Concept:
                    pygame.draw.rect(main_container, (255, 255, 255), (obj.x - 80, obj.y - screen.get_height() * 0.05 + init.bf_interface_offset, 20 + init.font2.size(obj.name + " : " + obj.ref)[0], 40), 2)
                    main_container.blit(init.font2.render((obj.name + " : " + obj.ref), True, (255, 255, 255)),
                                        (obj.x + (20 + init.font2.size(obj.name + " : " + obj.ref)[0]) / 2 - init.font2.size(obj.name + " : " + obj.ref)[0] / 2 - 80, obj.y + 10 - screen.get_height() * 0.05 + init.bf_interface_offset))
                else:
                    pygame.draw.rect(main_container, (255, 255, 255), (obj.x - 80, obj.y - screen.get_height() * 0.05 + init.bf_interface_offset, 20 + init.font2.size(obj.name)[0], 40), 2, 20)
                    main_container.blit(init.font2.render(obj.name, True, (255, 255, 255)), (obj.x + (20 + init.font2.size(obj.name)[0]) / 2 - init.font2.size(obj.name)[0] / 2 - 80, obj.y + 10 - screen.get_height() * 0.05 + init.bf_interface_offset))

                element_drwaned.append(obj)
            draw_arc(obj, init, screen, main_container, init.bf_interface_offset)
    screen.blit(main_container, (80, screen.get_height() * 0.05))

    if init.erase_button or 40 + screen.get_width() * 0.6 <= init.mouse[0] <= 40 + screen.get_width() * 0.6 + 20 and 10 + screen.get_height() * 0.05 <= init.mouse[1] <= 10 + screen.get_height() * 0.05 + 20 :
        erase_button = pygame.image.load("images/erase_red.png")
    else:
        erase_button = pygame.image.load("images/erase_white.png")
    screen.blit(erase_button, (40 + screen.get_width() * 0.6, 10 + screen.get_height() * 0.05))

    pygame.draw.rect(screen, (255, 255, 255), (80 + screen.get_width() * 0.6 + 80, screen.get_height() * 0.2, screen.get_width() * 0.2, screen.get_height() * 0.6), 2)


    if init.new_concept:
        if init.new_concept_in[0]:
            screen.blit(black_fillter, (0, 0))
            name_ref = pygame.Surface((screen.get_width() * 0.2, screen.get_height() * 0.3))
            name_ref.fill((50, 50, 50))
            name_ref.blit(init.font2.render("Name : ", True, (255, 255, 255)), (50, 50))
            name_ref.blit(init.font2.render(init.new_concept_name, True, (255, 255, 255)), (150, 50))
            if init.new_concept_name_typing or screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + 140 <= init.mouse[0] <= screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + 140 +  init.font2.size(init.new_concept_name)[0] + 20 and screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + 45 <= init.mouse[1] <= screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + 45 +  init.font2.size("A")[1] + 10:
                name_ref.blit(init.font2.render(init.new_concept_name, True, (255, 0, 0)), (150, 50))
                pygame.draw.rect(name_ref, (255, 0, 0), (140, 45, init.font2.size(init.new_concept_name)[0] + 20, init.font2.size("A")[1] + 10), 2)
            else:
                name_ref.blit(init.font2.render(init.new_concept_name, True, (255, 255, 255)), (150, 50))
                pygame.draw.rect(name_ref, (255, 255, 255), (140, 45, init.font2.size(init.new_concept_name)[0] + 20, init.font2.size("A")[1] + 10), 2)

            name_ref.blit(init.font2.render("Ref : ", True, (255, 255, 255)), (50, 100))
            if init.new_concept_ref_typing or screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + 140 <= init.mouse[0] <= screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + 140 + init.font2.size(init.new_concept_ref)[0] + 20 and screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + 95 <= init.mouse[1] <= screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + 95 + init.font2.size("A")[1] + 10:
                name_ref.blit(init.font2.render(init.new_concept_ref, True, (255, 0, 0)), (150, 100))
                pygame.draw.rect(name_ref, (255, 0, 0), (140, 95, init.font2.size(init.new_concept_ref)[0] + 20, init.font2.size("A")[1] + 10), 2)
            else:
                name_ref.blit(init.font2.render(init.new_concept_ref, True, (255, 255, 255)), (150, 100))
                pygame.draw.rect(name_ref, (255, 255, 255), (140, 95, init.font2.size(init.new_concept_ref)[0] + 20, init.font2.size("A")[1] + 10), 2)
            if screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + name_ref.get_width() / 2 - 25 <= init.mouse[0] <= screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + name_ref.get_width() / 2 - 25 + 50 and screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + name_ref.get_height() - 70 <= init.mouse[1] <= screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + name_ref.get_height() - 70 + 30:
                pygame.draw.rect(name_ref, (180, 180, 180), (name_ref.get_width() / 2 - 25, name_ref.get_height() - 70, 50, 30), border_radius=4)
                name_ref.blit(init.font2.render("ADD", True, (255, 0, 0)), (name_ref.get_width() / 2 - init.font2.size("ADD")[0] / 2, name_ref.get_height() - 66))
            else:
                pygame.draw.rect(name_ref, (255, 255, 255), (name_ref.get_width() / 2 - 25, name_ref.get_height() - 70, 50, 30), border_radius=4)
                name_ref.blit(init.font2.render("ADD", True, (50, 50, 50)), (name_ref.get_width() / 2 - init.font2.size("ADD")[0] / 2, name_ref.get_height() - 66))

            screen.blit(name_ref, (screen.get_width() / 2 - screen.get_width() * 0.2 / 2, screen.get_height() / 2 - screen.get_height() * 0.3 / 2))
        else:
            pygame.draw.rect(screen, (255, 255, 255), (init.mouse[0], init.mouse[1], 140, 40), 2)
            screen.blit(init.font2.render("Name : Ref", True, (255, 255, 255)), (init.mouse[0] + (20 + init.font2.size("Name")[0]) / 2 - init.font2.size("Name")[0] / 2, init.mouse[1] + 10))

    elif init.new_relation:
        if init.new_relation_in[0]:
            screen.blit(black_fillter, (0, 0))
            name_ref = pygame.Surface((screen.get_width() * 0.2, screen.get_height() * 0.3))
            name_ref.fill((50, 50, 50))
            name_ref.blit(init.font2.render("Name : ", True, (255, 255, 255)), (50, 50))
            name_ref.blit(init.font2.render(init.new_relation_name, True, (255, 255, 255)), (150, 50))
            if init.new_relation_name_typing or screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + 140 <= init.mouse[0] <= screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + 140 +  init.font2.size(init.new_relation_name)[0] + 20 and screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + 45 <= init.mouse[1] <= screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + 45 +  init.font2.size("A")[1] + 10:
                name_ref.blit(init.font2.render(init.new_relation_name, True, (255, 0, 0)), (150, 50))
                pygame.draw.rect(name_ref, (255, 0, 0), (140, 45, init.font2.size(init.new_relation_name)[0] + 20, init.font2.size("A")[1] + 10), 2)
            else:
                name_ref.blit(init.font2.render(init.new_relation_name, True, (255, 255, 255)), (150, 50))
                pygame.draw.rect(name_ref, (255, 255, 255), (140, 45, init.font2.size(init.new_relation_name)[0] + 20, init.font2.size("A")[1] + 10), 2)

            if screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + name_ref.get_width() / 2 - 25 <= init.mouse[0] <= screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + name_ref.get_width() / 2 - 25 + 50 and screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + name_ref.get_height() - 70 <= init.mouse[1] <= screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + name_ref.get_height() - 70 + 30:
                pygame.draw.rect(name_ref, (180, 180, 180), (name_ref.get_width() / 2 - 25, name_ref.get_height() - 70, 50, 30), border_radius=4)
                name_ref.blit(init.font2.render("ADD", True, (255, 0, 0)), (name_ref.get_width() / 2 - init.font2.size("ADD")[0] / 2, name_ref.get_height() - 66))
            else:
                pygame.draw.rect(name_ref, (255, 255, 255), (name_ref.get_width() / 2 - 25, name_ref.get_height() - 70, 50, 30), border_radius=4)
                name_ref.blit(init.font2.render("ADD", True, (50, 50, 50)), (name_ref.get_width() / 2 - init.font2.size("ADD")[0] / 2, name_ref.get_height() - 66))

            screen.blit(name_ref, (screen.get_width() / 2 - screen.get_width() * 0.2 / 2, screen.get_height() / 2 - screen.get_height() * 0.3 / 2))
        else:
            pygame.draw.rect(screen, (255, 255, 255), (init.mouse[0], init.mouse[1], 140, 40), 2, 20)
            screen.blit(init.font2.render("Name", True, (255, 255, 255)), (init.mouse[0] + (20 + init.font2.size("Name")[0]) / 2 - init.font2.size("Name")[0] / 2, init.mouse[1] + 10))

    elif init.new_arc:
        if init.new_arc_point1[0]:
            if init.mouse[1] <= init.new_arc_point1[1].top + 40 + init.bf_interface_offset:
                if init.new_arc_point1[1].left < init.mouse[0] < init.new_arc_point1[1].right:
                    draw_arrow(screen, pygame.Vector2(init.mouse[0], init.new_arc_point1[1].top + init.bf_interface_offset), pygame.Vector2(init.mouse[0], init.mouse[1]), (255, 255, 255), 2, 20, 10)
                elif init.new_arc_point1[1].left >= init.mouse[0]:
                    draw_arrow(screen, pygame.Vector2(init.new_arc_point1[1].left, init.new_arc_point1[1].top + 20 + init.bf_interface_offset), pygame.Vector2(init.mouse[0], init.mouse[1]), (255, 255, 255), 2, 20, 10)
                elif init.mouse[0] >= init.new_arc_point1[1].right:
                    draw_arrow(screen, pygame.Vector2(init.new_arc_point1[1].right, init.new_arc_point1[1].top + 20 + init.bf_interface_offset), pygame.Vector2(init.mouse[0], init.mouse[1]), (255, 255, 255), 2, 20, 10)
            elif init.mouse[1] > init.new_arc_point1[1].bottom + init.bf_interface_offset:
                if init.new_arc_point1[1].left <= init.mouse[0] <= init.new_arc_point1[1].right:
                    draw_arrow(screen, pygame.Vector2(init.mouse[0], init.new_arc_point1[1].bottom + init.bf_interface_offset), pygame.Vector2(init.mouse[0], init.mouse[1]), (255, 255, 255), 2, 20, 10)
                elif init.new_arc_point1[1].left > init.mouse[0]:
                    draw_arrow(screen, pygame.Vector2(init.new_arc_point1[1].left, init.new_arc_point1[1].bottom + init.bf_interface_offset), pygame.Vector2(init.mouse[0], init.mouse[1]), (255, 255, 255), 2, 20, 10)
                elif init.mouse[0] > init.new_arc_point1[1].right:
                    draw_arrow(screen, pygame.Vector2(init.new_arc_point1[1].right, init.new_arc_point1[1].bottom + init.bf_interface_offset), pygame.Vector2(init.mouse[0], init.mouse[1]), (255, 255, 255), 2, 20, 10)

        else:
            draw_arrow(screen, pygame.Vector2(init.mouse[0] - 10, init.mouse[1]), pygame.Vector2(init.mouse[0] + 20, init.mouse[1]), (255, 255, 255), 2, 10, 5)

    if init.erase_button:
        rect = Rect(init.mouse[0], init.mouse[1] - init.bf_interface_offset, 1, 1)
        collide = pygame.Rect.collidelist(rect, init.bf_list_rect)
        if collide == -1:
            screen.blit(pygame.image.load("images/erase_white.png"), (init.mouse[0] - 20, init.mouse[1] - 20))
        else:
            screen.blit(pygame.image.load("images/erase_red.png"), (init.mouse[0] - 20, init.mouse[1] - 20))


def draw_arc(obj, init, screen, main_container, offset):
    from classs import Concept
    if type(obj) == Concept:
        first_point_rect = Rect(obj.x, obj.y, 20 + init.font2.size(obj.name + " : " + obj.ref)[0], 40)
    else:
        first_point_rect = Rect(obj.x, obj.y, 20 + init.font2.size(obj.name)[0], 40)

    for element in obj.arcs:
        if type(element) == Concept:
            second_point_rect = Rect(element.x, element.y, 20 + init.font2.size(element.name + " : " + element.ref)[0], 40)
        else:
            second_point_rect = Rect(element.x, element.y, 20 + init.font2.size(element.name)[0], 40)
        if first_point_rect.right < second_point_rect.left:
            x1 = first_point_rect.right
            y1 = first_point_rect.top + 20
            x2 = second_point_rect.left
            y2 = second_point_rect.top + 20
        elif first_point_rect.left > second_point_rect.right:
            x1 = first_point_rect.left
            y1 = first_point_rect.top + 20
            x2 = second_point_rect.right
            y2 = second_point_rect.top + 20
        elif first_point_rect.top > second_point_rect.top:
            x1 = first_point_rect.left + (first_point_rect.right - first_point_rect.left) / 2
            y1 = first_point_rect.top
            x2 = second_point_rect.left + (second_point_rect.right - second_point_rect.left) / 2
            y2 = second_point_rect.bottom
        else:
            x1 = first_point_rect.left + (first_point_rect.right - first_point_rect.left) / 2
            y1 = first_point_rect.bottom
            x2 = second_point_rect.left + (second_point_rect.right - second_point_rect.left) / 2
            y2 = second_point_rect.top
        draw_arrow(main_container, pygame.Vector2(x1 - 80, y1 - screen.get_height() * 0.05 + offset), pygame.Vector2(x2 - 80, y2 - screen.get_height() * 0.05 + offset), (255, 255, 255), 3, 20, 10)


def draw_arc_intero(obj, init, screen, main_container, offset):
    from classs import Concept
    if type(obj) == Concept:
        first_point_rect = Rect(obj.x, obj.y, 20 + init.font2.size(obj.name + " : " + obj.ref)[0], 40)
    else:
        first_point_rect = Rect(obj.x, obj.y, 20 + init.font2.size(obj.name)[0], 40)

    for element in obj.arcs:
        if type(element) == Concept:
            second_point_rect = Rect(element.x, element.y, 20 + init.font2.size(element.name + " : " + element.ref)[0], 40)
        else:
            second_point_rect = Rect(element.x, element.y, 20 + init.font2.size(element.name)[0], 40)
        if first_point_rect.right < second_point_rect.left:
            x1 = first_point_rect.right
            y1 = first_point_rect.top + 20
            x2 = second_point_rect.left
            y2 = second_point_rect.top + 20
        elif first_point_rect.left > second_point_rect.right:
            x1 = first_point_rect.left
            y1 = first_point_rect.top + 20
            x2 = second_point_rect.right
            y2 = second_point_rect.top + 20
        elif first_point_rect.top > second_point_rect.top:
            x1 = first_point_rect.left + (first_point_rect.right - first_point_rect.left) / 2
            y1 = first_point_rect.top
            x2 = second_point_rect.left + (second_point_rect.right - second_point_rect.left) / 2
            y2 = second_point_rect.bottom
        else:
            x1 = first_point_rect.left + (first_point_rect.right - first_point_rect.left) / 2
            y1 = first_point_rect.bottom
            x2 = second_point_rect.left + (second_point_rect.right - second_point_rect.left) / 2
            y2 = second_point_rect.top
        draw_arrow(main_container, pygame.Vector2(x1, y1 + offset), pygame.Vector2(x2 , y2 + offset), (255, 255, 255), 3, 20, 10)


def new_br_intrface(screen, init):
    from classs import Concept
    black_fillter = pygame.Surface((screen.get_width(), screen.get_height()))
    black_fillter.fill((0, 0, 0))
    black_fillter.set_alpha(128)
    screen.blit(black_fillter, (0, 0))

    pygame.draw.rect(screen, (255, 255, 255), (80, screen.get_height() * 0.05, screen.get_width() * 0.6, screen.get_height() * 0.9), 2)

    side_container = pygame.Surface((screen.get_width() * 0.2, screen.get_height() * 0.6))
    side_container.fill((50, 50, 50))
    side_container.blit(init.font2.render("Concept", True, (255, 255, 255)), (side_container.get_width() / 2 - init.font2.size("Concept")[0] / 2, 20))
    if 80 + screen.get_width() * 0.6 + 80 + side_container.get_width() / 2 - 70 <= init.mouse[0] <= 80 + screen.get_width() * 0.6 + 80 + side_container.get_width() / 2 - 70 + 140 and screen.get_height() * 0.2 + 10 + init.font2.size("Concept")[1] * 2 <= init.mouse[1] <= screen.get_height() * 0.2 + 10 + init.font2.size("Concept")[1] * 2 + 40:
        pygame.draw.rect(side_container, (255, 0, 0), (side_container.get_width() / 2 - 70, 10 + init.font2.size("Concept")[1] * 2, 140, 40), 2)
        side_container.blit(init.font2.render("Name : Ref", True, (255, 0, 0)), (side_container.get_width() / 2 - 70 + 140 / 2 - init.font2.size("Name : Ref")[0] / 2, 10 + init.font2.size("Concept")[1] * 2 + 10))
    else:
        pygame.draw.rect(side_container, (255, 255, 255), (side_container.get_width() / 2 - 70, 10 + init.font2.size("Concept")[1] * 2, 140, 40), 2)
        side_container.blit(init.font2.render("Name : Ref", True, (255, 255, 255)), (side_container.get_width() / 2 - 70 + 140 / 2 - init.font2.size("Name : Ref")[0] / 2, 10 + init.font2.size("Concept")[1] * 2 + 10))

    side_container.blit(init.font2.render("Relation", True, (255, 255, 255)), (side_container.get_width() / 2 - init.font2.size("Relation")[0] / 2, 120))
    if 80 + screen.get_width() * 0.6 + 80 + side_container.get_width() / 2 - 70 <= init.mouse[0] <= 80 + screen.get_width() * 0.6 + 80 + side_container.get_width() / 2 - 70 + 140 and screen.get_height() * 0.2 + 110 + init.font2.size("Relation")[1] * 2 <= init.mouse[1] <= screen.get_height() * 0.2 + 110 + init.font2.size("Relation")[1] * 2 + 40:
        pygame.draw.rect(side_container, (255, 0, 0), (side_container.get_width() / 2 - 70, 110 + init.font2.size("Relation")[1] * 2, 140, 40), 2, 20)
        side_container.blit(init.font2.render("Name", True, (255, 0, 0)), (side_container.get_width() / 2 - 70 + 140 / 2 - init.font2.size("Name")[0] / 2, 110 + init.font2.size("Relation")[1] * 2 + 10))
    else:
        pygame.draw.rect(side_container, (255, 255, 255), (side_container.get_width() / 2 - 70, 110 + init.font2.size("Relation")[1] * 2, 140, 40), 2, 20)
        side_container.blit(init.font2.render("Name", True, (255, 255, 255)), (side_container.get_width() / 2 - 70 + 140 / 2 - init.font2.size("Name")[0] / 2, 110 + init.font2.size("Relation")[1] * 2 + 10))

    if 80 + screen.get_width() * 0.6 + 80 + 80 - 40 <= init.mouse[0] <= 80 + screen.get_width() * 0.6 + 80 + 80 - 40 + 80 and screen.get_height() * 0.2 + side_container.get_height() - 70 <= init.mouse[1] <= screen.get_height() * 0.2 + side_container.get_height() - 70 + 30:
        pygame.draw.rect(side_container, (50, 50, 50), (80, side_container.get_height() - 70, 80, 30), border_radius=4)
        side_container.blit(init.font2.render("Save", True, (255, 0, 0)), (80 - init.font2.size("Save")[0] / 2, side_container.get_height() - 66))
    else:
        pygame.draw.rect(side_container, (255, 255, 255), (80 - 40, side_container.get_height() - 70, 80, 30), border_radius=4)
        side_container.blit(init.font2.render("Save", True, (50, 50, 50)), (80 - init.font2.size("Save")[0] / 2, side_container.get_height() - 66))

    if 80 + screen.get_width() * 0.6 + side_container.get_width() - 80 + 80 - 40 <= init.mouse[0] <= 80 + screen.get_width() * 0.6 + side_container.get_width() - 80 + 80 - 40 + 80 and screen.get_height() * 0.2 + side_container.get_height() - 70 <= init.mouse[1] <= screen.get_height() * 0.2 + side_container.get_height() - 70 + 30:
        pygame.draw.rect(side_container, (50, 50, 50), (side_container.get_width() - 80, side_container.get_height() - 70, 80, 30), border_radius=4)
        side_container.blit(init.font2.render("Cancel", True, (255, 0, 0)), (side_container.get_width() - 80 - init.font2.size("Cancel")[0] / 2, side_container.get_height() - 66))
    else:
        pygame.draw.rect(side_container, (255, 255, 255), (side_container.get_width() - 80 - 40, side_container.get_height() - 70, 80, 30), border_radius=4)
        side_container.blit(init.font2.render("Cancel", True, (50, 50, 50)), (side_container.get_width() - 80 - init.font2.size("Cancel")[0] / 2, side_container.get_height() - 66))

    side_container.blit(init.font2.render("Arc", True, (255, 255, 255)), (side_container.get_width() / 2 - init.font2.size("Arc")[0] / 2, 220))
    screen.blit(side_container, (80 + screen.get_width() * 0.6 + 80, screen.get_height() * 0.2))

    if 80 + screen.get_width() * 0.6 + 80 + side_container.get_width() / 2 - 70 <= init.mouse[0] <= 80 + screen.get_width() * 0.6 + 80 + side_container.get_width() / 2 - 70 + 140 and screen.get_height() * 0.2 + 210 + init.font2.size("Arc")[1] * 2 <= init.mouse[1] <= screen.get_height() * 0.2 + 210 + \
            init.font2.size("Arc")[1] * 2 + 40:
        pygame.draw.line(screen, (255, 0, 0), (80 + screen.get_width() * 0.6 + 80 + side_container.get_width() / 2 - 70, screen.get_height() * 0.2 + 210 + init.font2.size("Arc")[1] * 2 + 20),(80 + screen.get_width() * 0.6 + 80 + side_container.get_width() / 2 - 70 + 140, screen.get_height() * 0.2 + 210 + init.font2.size("Arc")[1] * 2 + 20), 2)
    else:
        pygame.draw.line(screen, (255, 255, 255), (80 + screen.get_width() * 0.6 + 80 + side_container.get_width() / 2 - 70, screen.get_height() * 0.2 + 210 + init.font2.size("Arc")[1] * 2 + 20),(80 + screen.get_width() * 0.6 + 80 + side_container.get_width() / 2 - 70 + 140, screen.get_height() * 0.2 + 210 + init.font2.size("Arc")[1] * 2 + 20), 2)

    main_container = pygame.Surface((screen.get_width() * 0.6, screen.get_height() * 0.9))
    main_container.fill((50, 50, 50))
    pygame.draw.rect(main_container, (255, 255, 255), (0, 0, main_container.get_width(), main_container.get_height()), 2)

    if not len(init.br_array) == 0:
        for element in init.br_array:
            if type(element) == Concept:
                pygame.draw.rect(main_container, (255, 255, 255), (element.x - 80, element.y - screen.get_height() * 0.05 + init.br_interface_offset, 20 + init.font2.size(element.name + " : " + element.ref)[0], 40), 2)
                main_container.blit(init.font2.render((element.name + " : " + element.ref), True, (255, 255, 255)), (element.x + (20 + init.font2.size(element.name + " : " + element.ref)[0]) / 2 - init.font2.size(element.name + " : " + element.ref)[0] / 2 - 80, element.y + 10 - screen.get_height() * 0.05 + init.br_interface_offset))
            else:
                pygame.draw.rect(main_container, (255, 255, 255), (element.x - 80, element.y - screen.get_height() * 0.05 + init.br_interface_offset, 20 + init.font2.size(element.name)[0], 40), 2, 20)
                main_container.blit(init.font2.render(element.name, True, (255, 255, 255)), (element.x + (20 + init.font2.size(element.name)[0]) / 2 - init.font2.size(element.name)[0] / 2 - 80, element.y + 10 - screen.get_height() * 0.05 + init.br_interface_offset))
            draw_arc(element, init, screen, main_container, init.br_interface_offset)

    # if not len(init.br_arc_array) == 0:
    #     for element in init.br_arc_array:
    #         if element[0].right < element[1].left:
    #             x1 = element[0].right
    #             y1 = element[0].top + 20
    #             x2 = element[1].left
    #             y2 = element[1].top + 20
    #         elif element[0].left > element[1].right:
    #             x1 = element[0].left
    #             y1 = element[0].top + 20
    #             x2 = element[1].right
    #             y2 = element[1].top + 20
    #         elif element[0].top > element[1].top:
    #             x1 = element[0].left + (element[0].right - element[0].left) / 2
    #             y1 = element[0].top
    #             x2 = element[1].left + (element[1].right - element[1].left) / 2
    #             y2 = element[1].bottom
    #         else:
    #             x1 = element[0].left + (element[0].right - element[0].left) / 2
    #             y1 = element[0].bottom
    #             x2 = element[1].left + (element[1].right - element[1].left) / 2
    #             y2 = element[1].top
    #         draw_arrow(main_container, pygame.Vector2(x1 - 80, y1 - screen.get_height() * 0.05 + init.br_interface_offset), pygame.Vector2(x2 - 80, y2 - screen.get_height() * 0.05 + init.br_interface_offset), (255, 255, 255), 3, 20, 10)

    if init.x:
        element_drwaned = []
        for element in init.br_main_list:
            for obj in element:
                if not obj in element_drwaned:
                    if type(obj) == Concept:
                        pygame.draw.rect(main_container, (255, 255, 255), (obj.x - 80, obj.y - screen.get_height() * 0.05 + init.br_interface_offset, 20 + init.font2.size(obj.name + " : " + obj.ref)[0], 40), 2)
                        main_container.blit(init.font2.render((obj.name + " : " + obj.ref), True, (255, 255, 255)), (obj.x + (20 + init.font2.size(obj.name + " : " + obj.ref)[0]) / 2 - init.font2.size(obj.name + " : " + obj.ref)[0] / 2 - 80, obj.y + 10 - screen.get_height() * 0.05 + init.br_interface_offset))
                    else:
                        pygame.draw.rect(main_container, (255, 255, 255), (obj.x - 80, obj.y - screen.get_height() * 0.05 + init.br_interface_offset, 20 + init.font2.size(obj.name)[0], 40), 2, 20)
                        main_container.blit(init.font2.render(obj.name, True, (255, 255, 255)), (obj.x + (20 + init.font2.size(obj.name)[0]) / 2 - init.font2.size(obj.name)[0] / 2 - 80, obj.y + 10 - screen.get_height() * 0.05 + init.br_interface_offset))

                    element_drwaned.append(obj)
                draw_arc(obj, init, screen, main_container, init.br_interface_offset)
    pygame.draw.line(main_container, (255, 255, 255), (init.regle_separator[0][0] - 80, init.regle_separator[0][1] - screen.get_height() * 0.05 + init.br_interface_offset), (init.regle_separator[1][0] - 80, init.regle_separator[1][1] - screen.get_height() * 0.05 + init.br_interface_offset), 2)
    screen.blit(main_container, (80, screen.get_height() * 0.05))

    if init.erase_button or 40 + screen.get_width() * 0.6 <= init.mouse[0] <= 40 + screen.get_width() * 0.6 + 20 and 10 + screen.get_height() * 0.05 <= init.mouse[1] <= 10 + screen.get_height() * 0.05 + 20:
        erase_button = pygame.image.load("images/erase_red.png")
    else:
        erase_button = pygame.image.load("images/erase_white.png")
    screen.blit(erase_button, (40 + screen.get_width() * 0.6, 10 + screen.get_height() * 0.05))

    pygame.draw.rect(screen, (255, 255, 255), (80 + screen.get_width() * 0.6 + 80, screen.get_height() * 0.2, screen.get_width() * 0.2, screen.get_height() * 0.6), 2)
    is_time_passed = False
    if time.time() - init.time > 0.5:
        init.time = time.time()
        is_time_passed = True
    if init.new_concept:
        if init.new_concept_in[0]:
            screen.blit(black_fillter, (0, 0))
            name_ref = pygame.Surface((screen.get_width() * 0.2, screen.get_height() * 0.3))
            name_ref.fill((50, 50, 50))
            name_ref.blit(init.font2.render("Name : ", True, (255, 255, 255)), (50, 50))
            name_ref.blit(init.font2.render(init.new_concept_name, True, (255, 255, 255)), (150, 50))
            if init.new_concept_name_typing or screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + 140 <= init.mouse[0] <= screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + 140 + init.font2.size(init.new_concept_name)[0] + 20 and screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + 45 <= init.mouse[1] <= screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + 45 + init.font2.size("A")[1] + 10:
                if is_time_passed: pygame.draw.line(name_ref, (255, 0, 0), (150 + init.font2.size(init.new_concept_name)[0] + 2, 50), (150 + init.font2.size(init.new_concept_name)[0] + 2, init.font2.size("A")[1] + 50), 2)
                name_ref.blit(init.font2.render(init.new_concept_name, True, (255, 0, 0)), (150, 50))
                pygame.draw.rect(name_ref, (255, 0, 0), (140, 45, init.font2.size(init.new_concept_name)[0] + 20, init.font2.size("A")[1] + 10), 2)
            else:
                name_ref.blit(init.font2.render(init.new_concept_name, True, (255, 255, 255)), (150, 50))
                pygame.draw.rect(name_ref, (255, 255, 255), (140, 45, init.font2.size(init.new_concept_name)[0] + 20, init.font2.size("A")[1] + 10), 2)

            name_ref.blit(init.font2.render("Ref : ", True, (255, 255, 255)), (50, 100))
            if init.new_concept_ref_typing or screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + 140 <= init.mouse[0] <= screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + 140 + init.font2.size(init.new_concept_ref)[0] + 20 and screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + 95 <= init.mouse[1] <= screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + 95 + init.font2.size("A")[1] + 10:
                if is_time_passed: pygame.draw.line(name_ref, (255, 0, 0), (150 + init.font2.size(init.new_concept_ref)[0] + 2, 50), (150 + init.font2.size(init.new_concept_ref)[0] + 2, init.font2.size("A")[1] + 50), 2)
                name_ref.blit(init.font2.render(init.new_concept_ref, True, (255, 0, 0)), (150, 100))
                pygame.draw.rect(name_ref, (255, 0, 0), (140, 95, init.font2.size(init.new_concept_ref)[0] + 20, init.font2.size("A")[1] + 10), 2)
            else:
                name_ref.blit(init.font2.render(init.new_concept_ref, True, (255, 255, 255)), (150, 100))
                pygame.draw.rect(name_ref, (255, 255, 255), (140, 95, init.font2.size(init.new_concept_ref)[0] + 20, init.font2.size("A")[1] + 10), 2)
            if screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + name_ref.get_width() / 2 - 25 <= init.mouse[0] <= screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + name_ref.get_width() / 2 - 25 + 50 and screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + name_ref.get_height() - 70 <= init.mouse[1] <= screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + name_ref.get_height() - 70 + 30:
                pygame.draw.rect(name_ref, (180, 180, 180), (name_ref.get_width() / 2 - 25, name_ref.get_height() - 70, 50, 30), border_radius=4)
                name_ref.blit(init.font2.render("ADD", True, (255, 0, 0)), (name_ref.get_width() / 2 - init.font2.size("ADD")[0] / 2, name_ref.get_height() - 66))
            else:
                pygame.draw.rect(name_ref, (255, 255, 255), (name_ref.get_width() / 2 - 25, name_ref.get_height() - 70, 50, 30), border_radius=4)
                name_ref.blit(init.font2.render("ADD", True, (50, 50, 50)), (name_ref.get_width() / 2 - init.font2.size("ADD")[0] / 2, name_ref.get_height() - 66))

            screen.blit(name_ref, (screen.get_width() / 2 - screen.get_width() * 0.2 / 2, screen.get_height() / 2 - screen.get_height() * 0.3 / 2))
        else:
            pygame.draw.rect(screen, (255, 255, 255), (init.mouse[0], init.mouse[1], 140, 40), 2)
            screen.blit(init.font2.render("Name : Ref", True, (255, 255, 255)), (init.mouse[0] + (20 + init.font2.size("Name")[0]) / 2 - init.font2.size("Name")[0] / 2, init.mouse[1] + 10))

    elif init.new_relation:
        if init.new_relation_in[0]:
            screen.blit(black_fillter, (0, 0))
            name_ref = pygame.Surface((screen.get_width() * 0.2, screen.get_height() * 0.3))
            name_ref.fill((50, 50, 50))
            name_ref.blit(init.font2.render("Name : ", True, (255, 255, 255)), (50, 50))
            name_ref.blit(init.font2.render(init.new_relation_name, True, (255, 255, 255)), (150, 50))
            if init.new_relation_name_typing or screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + 140 <= init.mouse[0] <= screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + 140 + init.font2.size(init.new_relation_name)[0] + 20 and screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + 45 <= init.mouse[1] <= screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + 45 + init.font2.size("A")[1] + 10:
                if is_time_passed: pygame.draw.line(name_ref, (255, 0, 0), (150 + init.font2.size(init.new_relation_name)[0] + 2, 50), (150 + init.font2.size(init.new_relation_name)[0] + 2, init.font2.size("A")[1] + 50), 2)
                name_ref.blit(init.font2.render(init.new_relation_name, True, (255, 0, 0)), (150, 50))
                pygame.draw.rect(name_ref, (255, 0, 0), (140, 45, init.font2.size(init.new_relation_name)[0] + 20, init.font2.size("A")[1] + 10), 2)
            else:
                name_ref.blit(init.font2.render(init.new_relation_name, True, (255, 255, 255)), (150, 50))
                pygame.draw.rect(name_ref, (255, 255, 255), (140, 45, init.font2.size(init.new_relation_name)[0] + 20, init.font2.size("A")[1] + 10), 2)

            if screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + name_ref.get_width() / 2 - 25 <= init.mouse[0] <= screen.get_width() / 2 - screen.get_width() * 0.2 / 2 + name_ref.get_width() / 2 - 25 + 50 and screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + name_ref.get_height() - 70 <= init.mouse[1] <= screen.get_height() / 2 - screen.get_height() * 0.3 / 2 + name_ref.get_height() - 70 + 30:
                pygame.draw.rect(name_ref, (180, 180, 180), (name_ref.get_width() / 2 - 25, name_ref.get_height() - 70, 50, 30), border_radius=4)
                name_ref.blit(init.font2.render("ADD", True, (255, 0, 0)), (name_ref.get_width() / 2 - init.font2.size("ADD")[0] / 2, name_ref.get_height() - 66))
            else:
                pygame.draw.rect(name_ref, (255, 255, 255), (name_ref.get_width() / 2 - 25, name_ref.get_height() - 70, 50, 30), border_radius=4)
                name_ref.blit(init.font2.render("ADD", True, (50, 50, 50)), (name_ref.get_width() / 2 - init.font2.size("ADD")[0] / 2, name_ref.get_height() - 66))

            screen.blit(name_ref, (screen.get_width() / 2 - screen.get_width() * 0.2 / 2, screen.get_height() / 2 - screen.get_height() * 0.3 / 2))
        else:
            pygame.draw.rect(screen, (255, 255, 255), (init.mouse[0], init.mouse[1], 140, 40), 2, 20)
            screen.blit(init.font2.render("Name", True, (255, 255, 255)), (init.mouse[0] + (20 + init.font2.size("Name")[0]) / 2 - init.font2.size("Name")[0] / 2, init.mouse[1] + 10))

    elif init.new_arc:
        if init.new_arc_point1[0]:
            if init.mouse[1] <= init.new_arc_point1[1].top + 40 + init.br_interface_offset:
                if init.new_arc_point1[1].left < init.mouse[0] < init.new_arc_point1[1].right:
                    draw_arrow(screen, pygame.Vector2(init.mouse[0], init.new_arc_point1[1].top + init.br_interface_offset), pygame.Vector2(init.mouse[0], init.mouse[1]), (255, 255, 255), 2, 20, 10)
                elif init.new_arc_point1[1].left >= init.mouse[0]:
                    draw_arrow(screen, pygame.Vector2(init.new_arc_point1[1].left, init.new_arc_point1[1].top + 20 + init.br_interface_offset), pygame.Vector2(init.mouse[0], init.mouse[1]), (255, 255, 255), 2, 20, 10)
                elif init.mouse[0] >= init.new_arc_point1[1].right:
                    draw_arrow(screen, pygame.Vector2(init.new_arc_point1[1].right, init.new_arc_point1[1].top + 20 + init.br_interface_offset), pygame.Vector2(init.mouse[0], init.mouse[1]), (255, 255, 255), 2, 20, 10)
            elif init.mouse[1] > init.new_arc_point1[1].bottom + init.br_interface_offset:
                if init.new_arc_point1[1].left <= init.mouse[0] <= init.new_arc_point1[1].right:
                    draw_arrow(screen, pygame.Vector2(init.mouse[0], init.new_arc_point1[1].bottom + init.br_interface_offset), pygame.Vector2(init.mouse[0], init.mouse[1]), (255, 255, 255), 2, 20, 10)
                elif init.new_arc_point1[1].left > init.mouse[0]:
                    draw_arrow(screen, pygame.Vector2(init.new_arc_point1[1].left, init.new_arc_point1[1].bottom + init.br_interface_offset), pygame.Vector2(init.mouse[0], init.mouse[1]), (255, 255, 255), 2, 20, 10)
                elif init.mouse[0] > init.new_arc_point1[1].right:
                    draw_arrow(screen, pygame.Vector2(init.new_arc_point1[1].right, init.new_arc_point1[1].bottom + init.br_interface_offset), pygame.Vector2(init.mouse[0], init.mouse[1]), (255, 255, 255), 2, 20, 10)

        else:
            draw_arrow(screen, pygame.Vector2(init.mouse[0] - 10, init.mouse[1]), pygame.Vector2(init.mouse[0] + 20, init.mouse[1]), (255, 255, 255), 2, 10, 5)

    if init.erase_button:
        rect = Rect(init.mouse[0], init.mouse[1] - init.br_interface_offset, 1, 1)
        collide = pygame.Rect.collidelist(rect, init.br_list_rect)
        if collide == -1:
            screen.blit(pygame.image.load("images/erase_white.png"), (init.mouse[0] - 20, init.mouse[1] - 20))
        else:
            screen.blit(pygame.image.load("images/erase_red.png"), (init.mouse[0] - 20, init.mouse[1] - 20))


def change_ref(screen, init, obj):
    dark_filter = pygame.Surface((screen.get_width(), screen.get_height()))
    dark_filter.fill((0, 0, 0))
    dark_filter.set_alpha(128)
    screen.blit(dark_filter, (0, 0))

    main_surface = pygame.Surface((400, 400))
    main_surface.fill((50, 50, 50))
    main_surface.blit(init.font2.render("ref : ", True, (255, 255, 255)), (50, 100))
    main_surface.blit(init.font2.render(obj.ref, True, (255, 255, 255)), (80 + init.font2.size("ref : ")[0], 100))
    if init.intero_buttons["Restriction"][3] or init.intero_buttons["Restriction"][2] and screen.get_width() / 2 - 400 / 2 + 70 + init.font2.size("ref : ")[0] <= init.mouse[0] <= screen.get_width() / 2 - 400 / 2 + 70 + init.font2.size("ref : ")[0] + init.font2.size(init.intero_buttons["Restriction"][2].ref)[0] + 10 and screen.get_height() / 2 - 400 / 2 + 100 <= init.mouse[1] <= screen.get_height() / 2 - 400 / 2 + 100 + 10 + init.font2.size("A")[1]:
        pygame.draw.rect(main_surface, (255, 0, 0), (70 + init.font2.size("ref : ")[0], 95, init.font2.size(obj.ref)[0] + 20, 10 + init.font2.size("A")[1]), 2)
    else:
        pygame.draw.rect(main_surface, (255, 255, 255), (70 + init.font2.size("ref : ")[0], 95, init.font2.size(obj.ref)[0] + 20, 10 + init.font2.size("A")[1]), 2)

    ok_button = pygame.Surface((70, 40))

    if screen.get_width() / 2 - 400 / 2 + 100 <= init.mouse[0] <= screen.get_width() / 2 - 400 / 2 + 100 + 70 and screen.get_height() / 2 - 400 / 2 + 300 <= init.mouse[1] <= screen.get_height() / 2 - 400 / 2 + 300 + 40:
        ok_button.fill((200, 200, 200))
        main_surface.blit(ok_button, (100, 300))
        main_surface.blit(init.font2.render("ok", True, (255, 0, 0)), (100 + 70 / 2 - init.font2.size("ok")[0] / 2, 300 + 40 / 2 - init.font2.size("A")[1] / 2))

    else:
        ok_button.fill((255, 255, 255))
        main_surface.blit(ok_button, (100, 300))
        main_surface.blit(init.font2.render("ok", True, (0, 0, 0)), (100 + 70 / 2 - init.font2.size("ok")[0] / 2, 300 + 40 / 2 - init.font2.size("A")[1] / 2))

    cancel_button = pygame.Surface((70, 40))
    if screen.get_width() / 2 - 400 / 2 + 200 <= init.mouse[0] <= screen.get_width() / 2 - 400 / 2 + 200 + 70 and screen.get_height() / 2 - 400 / 2 + 300 <= init.mouse[1] <= screen.get_height() / 2 - 400 / 2 + 300 + 40:
        cancel_button.fill((200, 200, 200))
        main_surface.blit(cancel_button, (200, 300))
        main_surface.blit(init.font2.render("cancel", True, (255, 0, 0)), (200 + 70 / 2 - init.font2.size("cancel")[0] / 2, 300 + 40 / 2 - init.font2.size("A")[1] / 2))
    else:
        cancel_button.fill((255, 255, 255))
        main_surface.blit(cancel_button, (200, 300))
        main_surface.blit(init.font2.render("cancel", True, (0, 0, 0)), (200 + 70 / 2 - init.font2.size("cancel")[0] / 2, 300 + 40 / 2 - init.font2.size("A")[1] / 2))

    screen.blit(main_surface, (screen.get_width() / 2 - 400 / 2, screen.get_height() / 2 - 400 / 2))


def display_interro(screen, init):

    main_surface = pygame.Surface((screen.get_width() * 0.7, screen.get_height() * 0.8))
    main_surface.fill((70, 70, 70))
    main_surface.set_alpha(230)

    show_bf_button = pygame.Surface((70, 30))
    show_br_button = pygame.Surface((70, 30))
    make_bfn_button = pygame.Surface((70, 30))

    if screen.get_width() * 0.8 <= init.mouse[0] <= screen.get_width() * 0.8 + 70 and screen.get_height() * 0.1 <= init.mouse[1] <= screen.get_height() * 0.1 + 30:
        show_bf_button.fill((230, 230, 230))
        show_bf_button.blit(init.font.render("show BF", True, (255, 0, 0)), (70 / 2 - init.font.size("show BF")[0] / 2, 30 / 2 - init.font.size("show BF")[1] / 2 ))

    else:
        show_bf_button.fill((255, 255, 255))
        show_bf_button.blit(init.font.render("show BF", True, (0, 0, 0)), (70 / 2 - init.font.size("show BF")[0] / 2, 30 / 2 - init.font.size("show BF")[1] / 2))
    screen.blit(show_bf_button, (screen.get_width() * 0.8, screen.get_height() * 0.1))

    if screen.get_width() * 0.8 <= init.mouse[0] <= screen.get_width() * 0.8 + 70 and screen.get_height() * 0.1 + 40 <= init.mouse[1] <= screen.get_height() * 0.1 + 30 + 40:
        show_br_button.fill((230, 230, 230))
        show_br_button.blit(init.font.render("show BR", True, (255, 0, 0)), (70 / 2 - init.font.size("show BR")[0] / 2, 30 / 2 - init.font.size("show BR")[1] / 2 ))

    else:
        show_br_button.fill((255, 255, 255))
        show_br_button.blit(init.font.render("show BR", True, (0, 0, 0)), (70 / 2 - init.font.size("show BR")[0] / 2, 30 / 2 - init.font.size("show BR")[1] / 2))
    screen.blit(show_br_button, (screen.get_width() * 0.8, screen.get_height() * 0.1 + 40))

    if screen.get_width() * 0.8 <= init.mouse[0] <= screen.get_width() * 0.8 + 70 and screen.get_height() * 0.1 + 80 <= init.mouse[1] <= screen.get_height() * 0.1 + 30 + 80:
        make_bfn_button.fill((230, 230, 230))
        make_bfn_button.blit(init.font.render("make BFN", True, (255, 0, 0)), (70 / 2 - init.font.size("make BFN")[0] / 2, 30 / 2 - init.font.size("make BFN")[1] / 2 ))

    else:
        make_bfn_button.fill((255, 255, 255))
        make_bfn_button.blit(init.font.render("make BFN", True, (0, 0, 0)), (70 / 2 - init.font.size("make BFN")[0] / 2, 30 / 2 - init.font.size("make BFN")[1] / 2))
    screen.blit(make_bfn_button, (screen.get_width() * 0.8, screen.get_height() * 0.1 + 80))

    if init.intero_buttons["make BFN"]:
        element_drwaned = []
        for element in init.bfn_fun:
            if type(element) == Concept:
                obj = element
                if not obj in element_drwaned:
                    if type(obj) == Concept:
                        pygame.draw.rect(main_surface, (255, 255, 255), (obj.x, obj.y + init.make_bfn_offset, 20 + init.font2.size(obj.name + " : " + obj.ref)[0], 40), 2)
                        main_surface.blit(init.font2.render((obj.name + " : " + obj.ref), True, (255, 255, 255)),
                                          (obj.x + (20 + init.font2.size(obj.name + " : " + obj.ref)[0]) / 2 - init.font2.size(obj.name + " : " + obj.ref)[0] / 2, obj.y + 10 + init.make_bfn_offset))
                    else:
                        pygame.draw.rect(main_surface, (255, 255, 255), (obj.x, obj.y + init.make_bfn_offset, 20 + init.font2.size(obj.name)[0], 40), 2, 20)
                        main_surface.blit(init.font2.render(obj.name, True, (255, 255, 255)), (obj.x + (20 + init.font2.size(obj.name)[0]) / 2 - init.font2.size(obj.name)[0] / 2, obj.y + 10 + init.make_bfn_offset))
                    element_drwaned.append(obj)
                continue
            for obj in element:
                if not obj in element_drwaned:
                    if type(obj) == Concept:
                        pygame.draw.rect(main_surface, (255, 255, 255), (obj.x, obj.y + init.make_bfn_offset, 20 + init.font2.size(obj.name + " : " + obj.ref)[0], 40), 2)
                        main_surface.blit(init.font2.render((obj.name + " : " + obj.ref), True, (255, 255, 255)),
                                          (obj.x + (20 + init.font2.size(obj.name + " : " + obj.ref)[0]) / 2 - init.font2.size(obj.name + " : " + obj.ref)[0] / 2, obj.y + 10 + init.make_bfn_offset))
                    else:
                        pygame.draw.rect(main_surface, (255, 255, 255), (obj.x, obj.y + init.make_bfn_offset, 20 + init.font2.size(obj.name)[0], 40), 2, 20)
                        main_surface.blit(init.font2.render(obj.name, True, (255, 255, 255)), (obj.x + (20 + init.font2.size(obj.name)[0]) / 2 - init.font2.size(obj.name)[0] / 2, obj.y + 10 + init.make_bfn_offset))
                    element_drwaned.append(obj)
                draw_arc_intero(obj, init, screen, main_surface, init.make_bfn_offset)
        Restriction_button = pygame.Surface((70, 30))
        if init.intero_buttons["Restriction"][0] or screen.get_width() * 0.8 + 10 + 70 <= init.mouse[0] <= screen.get_width() * 0.8 + 70 + 10 + 70 and screen.get_height() * 0.1 + 80 <= init.mouse[1] <= screen.get_height() * 0.1 + 30 + 80:
            Restriction_button.fill((230, 230, 230))
            Restriction_button.blit(init.font.render("Restriction", True, (255, 0, 0)), (70 / 2 - init.font.size("Restriction")[0] / 2, 30 / 2 - init.font.size("Restriction")[1] / 2))

        else:
            Restriction_button.fill((255, 255, 255))
            Restriction_button.blit(init.font.render("Restriction", True, (0, 0, 0)), (70 / 2 - init.font.size("Restriction")[0] / 2, 30 / 2 - init.font.size("Restriction")[1] / 2))
        screen.blit(Restriction_button, (screen.get_width() * 0.8 + 10 + 70, screen.get_height() * 0.1 + 80))

        copy_button = pygame.Surface((70, 30))
        if init.intero_buttons["Copy"][0] or screen.get_width() * 0.8 + 10 + 70 <= init.mouse[0] <= screen.get_width() * 0.8 + 70 + 10 + 70 and screen.get_height() * 0.1 + 120 <= init.mouse[1] <= screen.get_height() * 0.1 + 30 + 120:
            copy_button.fill((230, 230, 230))
            copy_button.blit(init.font.render("Copy", True, (255, 0, 0)), (70 / 2 - init.font.size("Copy")[0] / 2, 30 / 2 - init.font.size("Copy")[1] / 2))

        else:
            copy_button.fill((255, 255, 255))
            copy_button.blit(init.font.render("Copy", True, (0, 0, 0)), (70 / 2 - init.font.size("Copy")[0] / 2, 30 / 2 - init.font.size("Copy")[1] / 2))
        screen.blit(copy_button, (screen.get_width() * 0.8 + 10 + 70, screen.get_height() * 0.1 + 120))

        jointure_button = pygame.Surface((70, 30))
        if init.intero_buttons["jointure"][0] or screen.get_width() * 0.8 + 10 + 70 <= init.mouse[0] <= screen.get_width() * 0.8 + 70 + 10 + 70 and screen.get_height() * 0.1 + 160 <= init.mouse[1] <= screen.get_height() * 0.1 + 30 + 160:
            jointure_button.fill((230, 230, 230))
            jointure_button.blit(init.font.render("jointure", True, (255, 0, 0)), (70 / 2 - init.font.size("jointure")[0] / 2, 30 / 2 - init.font.size("jointure")[1] / 2))

        else:
            jointure_button.fill((255, 255, 255))
            jointure_button.blit(init.font.render("jointure", True, (0, 0, 0)), (70 / 2 - init.font.size("jointure")[0] / 2, 30 / 2 - init.font.size("jointure")[1] / 2))
        screen.blit(jointure_button, (screen.get_width() * 0.8 + 10 + 70, screen.get_height() * 0.1 + 160))

        fragmentation_button = pygame.Surface((70, 30))
        if init.intero_buttons["fragmentation"][0] or screen.get_width() * 0.8 + 10 + 70 <= init.mouse[0] <= screen.get_width() * 0.8 + 70 + 10 + 70 and screen.get_height() * 0.1 + 200 <= init.mouse[1] <= screen.get_height() * 0.1 + 30 + 200:
            fragmentation_button.fill((230, 230, 230))
            fragmentation_button.blit(init.font.render("fragme...", True, (255, 0, 0)), (70 / 2 - init.font.size("fragme...")[0] / 2, 30 / 2 - init.font.size("fragme...")[1] / 2))

        else:
            fragmentation_button.fill((255, 255, 255))
            fragmentation_button.blit(init.font.render("fragme...", True, (0, 0, 0)), (70 / 2 - init.font.size("fragme...")[0] / 2, 30 / 2 - init.font.size("fragme...")[1] / 2))
        screen.blit(fragmentation_button, (screen.get_width() * 0.8 + 10 + 70, screen.get_height() * 0.1 + 200))

    elif init.intero_buttons["show BF"]:
        element_drwaned = []
        for element in init.bf_main_list:
            if type(element) == Concept:
                obj = element
                if not obj in element_drwaned:
                    if type(obj) == Concept:
                        pygame.draw.rect(main_surface, (255, 255, 255), (obj.x, obj.y, 20 + init.font2.size(obj.name + " : " + obj.ref)[0], 40), 2)
                        main_surface.blit(init.font2.render((obj.name + " : " + obj.ref), True, (255, 255, 255)),
                                            (obj.x + (20 + init.font2.size(obj.name + " : " + obj.ref)[0]) / 2 - init.font2.size(obj.name + " : " + obj.ref)[0] / 2, obj.y + 10))
                    else:
                        pygame.draw.rect(main_surface, (255, 255, 255), (obj.x, obj.y, 20 + init.font2.size(obj.name)[0], 40), 2, 20)
                        main_surface.blit(init.font2.render(obj.name, True, (255, 255, 255)), (obj.x + (20 + init.font2.size(obj.name)[0]) / 2 - init.font2.size(obj.name)[0] / 2, obj.y + 10))

                    element_drwaned.append(obj)
                    continue
            for obj in element:
                if not obj in element_drwaned:
                    if type(obj) == Concept:
                        pygame.draw.rect(main_surface, (255, 255, 255), (obj.x, obj.y, 20 + init.font2.size(obj.name + " : " + obj.ref)[0], 40), 2)
                        main_surface.blit(init.font2.render((obj.name + " : " + obj.ref), True, (255, 255, 255)),
                                            (obj.x + (20 + init.font2.size(obj.name + " : " + obj.ref)[0]) / 2 - init.font2.size(obj.name + " : " + obj.ref)[0] / 2, obj.y + 10))
                    else:
                        pygame.draw.rect(main_surface, (255, 255, 255), (obj.x, obj.y, 20 + init.font2.size(obj.name)[0], 40), 2, 20)
                        main_surface.blit(init.font2.render(obj.name, True, (255, 255, 255)), (obj.x + (20 + init.font2.size(obj.name)[0]) / 2 - init.font2.size(obj.name)[0] / 2, obj.y + 10))

                    element_drwaned.append(obj)
                draw_arc_intero(obj, init, screen, main_surface, 0)
    elif init.intero_buttons["show BR"]:
        element_drwaned = []

        regle_y = 10
        j = -1
        for element in init.br_main_list:
            # regle 1
            j += 1
            premis_Y = 10
            main_surface.blit(init.font2.render(f"Regel : {j}", True, (255, 0, 0)), (20, regle_y))
            main_surface.blit(init.font.render(f"premise", True, (255, 0, 0)), (30, regle_y + 30))

            if len(element["premise"]) != 0:
                array, premis_Y = update_relge_coordinates(init, element["premise"], regle_y + 50)
                for obj in array:
                    if not obj in element_drwaned:
                        if type(obj) == Concept:
                            pygame.draw.rect(main_surface, (255, 255, 255), (obj.x , obj.y , 20 + init.font2.size(obj.name + " : " + obj.ref)[0], 40), 2)
                            main_surface.blit(init.font2.render((obj.name + " : " + obj.ref), True, (255, 255, 255)),
                                              (obj.x + (20 + init.font2.size(obj.name + " : " + obj.ref)[0]) / 2 - init.font2.size(obj.name + " : " + obj.ref)[0] / 2, obj.y + 10))
                        else:
                            pygame.draw.rect(main_surface, (255, 255, 255), (obj.x , obj.y, 20 + init.font2.size(obj.name)[0], 40), 2, 20)
                            main_surface.blit(init.font2.render(obj.name, True, (255, 255, 255)), (obj.x + (20 + init.font2.size(obj.name)[0]) / 2 - init.font2.size(obj.name)[0] / 2, obj.y + 10))

                        element_drwaned.append(obj)
                    draw_arc_intero(obj, init, screen, main_surface, 0)
            regle_y += premis_Y + 50
            pygame.draw.line(main_surface, (255, 255, 255), (0, regle_y + 25), (main_surface.get_width(), regle_y + 25), 2)
            main_surface.blit(init.font.render(f"conclusion, {regle_y}", True, (255, 0, 0)), (30, regle_y + 50))
            regle_y += 50
            if len(element["conclusion"]) != 0:
                array, premis_Y = update_relge_coordinates(init, element["conclusion"], regle_y + 20)
                regle_y += 20
                for obj in array:
                    if not obj in element_drwaned:
                        if type(obj) == Concept:
                            pygame.draw.rect(main_surface, (255, 255, 255), (obj.x , obj.y , 20 + init.font2.size(obj.name + " : " + obj.ref)[0], 40), 2)
                            main_surface.blit(init.font2.render((obj.name + " : " + obj.ref), True, (255, 255, 255)),
                                              (obj.x + (20 + init.font2.size(obj.name + " : " + obj.ref)[0]) / 2 - init.font2.size(obj.name + " : " + obj.ref)[0] / 2, obj.y + 10))
                        else:
                            pygame.draw.rect(main_surface, (255, 255, 255), (obj.x , obj.y, 20 + init.font2.size(obj.name)[0], 40), 2, 20)
                            main_surface.blit(init.font2.render(obj.name, True, (255, 255, 255)), (obj.x + (20 + init.font2.size(obj.name)[0]) / 2 - init.font2.size(obj.name)[0] / 2, obj.y + 10))

                        element_drwaned.append(obj)
                    draw_arc_intero(obj, init, screen, main_surface, 0)
            regle_y += premis_Y


    pygame.draw.rect(screen, (255, 255, 255), (screen.get_width() * 0.05, screen.get_width() * 0.05, screen.get_width() * 0.7, screen.get_height() * 0.8), 2)
    if init.intero_buttons["jointure"][0] and init.intero_buttons["jointure"][1][0]:
        obj = init.intero_buttons["jointure"][1][1]
        pygame.draw.rect(main_surface, (255, 0, 0), (obj.x, obj.y + init.make_bfn_offset, 20 + init.font2.size(obj.name + " : " + obj.ref)[0], 40), 2)
        main_surface.blit(init.font2.render((obj.name + " : " + obj.ref), True, (255, 0, 0)),
                          (obj.x + (20 + init.font2.size(obj.name + " : " + obj.ref)[0]) / 2 - init.font2.size(obj.name + " : " + obj.ref)[0] / 2, obj.y + 10 + init.make_bfn_offset))
        if init.intero_buttons["jointure"][2][0]:
            obj = init.intero_buttons["jointure"][2][1]
            pygame.draw.rect(main_surface, (255, 0, 0), (obj.x, obj.y + init.make_bfn_offset, 20 + init.font2.size(obj.name + " : " + obj.ref)[0], 40), 2)
            main_surface.blit(init.font2.render((obj.name + " : " + obj.ref), True, (255, 0, 0)),
                              (obj.x + (20 + init.font2.size(obj.name + " : " + obj.ref)[0]) / 2 - init.font2.size(obj.name + " : " + obj.ref)[0] / 2, obj.y + 10 + init.make_bfn_offset))

    screen.blit(main_surface, (screen.get_width() * 0.05, screen.get_width() * 0.05))
    if init.intero_buttons["fragmentation"][1] and init.intero_buttons["make BFN"]:
        pass
    if init.intero_buttons["Restriction"][1] and init.intero_buttons["make BFN"]:
        change_ref(screen, init, init.intero_buttons["Restriction"][2])

    if init.intero_buttons["Copy"][0] and init.intero_buttons["make BFN"]:
        if init.intero_buttons["Copy"][1][0] and not init.intero_buttons["Copy"][2][0]:
            pygame.draw.rect(screen, (255, 255, 255), (init.intero_buttons["Copy"][1][1][0], init.intero_buttons["Copy"][1][1][1], init.mouse[0] - init.intero_buttons["Copy"][1][1][0], init.mouse[1] - init.intero_buttons["Copy"][1][1][1]), 2)
        if init.intero_buttons["Copy"][2][0]:
            pygame.draw.rect(screen, (255, 255, 255), (init.intero_buttons["Copy"][1][1][0], init.intero_buttons["Copy"][1][1][1], init.intero_buttons["Copy"][2][1][0] - init.intero_buttons["Copy"][1][1][0], init.intero_buttons["Copy"][2][1][1] - init.intero_buttons["Copy"][1][1][1]), 2)
    if init.intero_buttons["jointure"][2][0] and init.intero_buttons["jointure"][1][0]:
        window_widh_buttons(screen, init, "do you want to join them")


def window_widh_buttons(screen, init, message):
    surface = pygame.Surface((init.font2.size(message)[0] + 100, 130))
    surface.fill((0, 0, 0))
    surface.set_alpha(180)
    surface.blit(init.font2.render(message, True, (255, 255, 255)), ((init.font2.size(message)[0] + 100) / 2 - init.font2.size(message)[0] / 2, 20))
    confirm_button = pygame.Surface((50, 30))
    if (init.font2.size(message)[0] + 100) / 2 - 110 / 2 + screen.get_width() / 2 - (init.font2.size(message)[0] + 50) / 2 <= init.mouse[0] <= 50 + screen.get_width() / 2 - (init.font2.size(message)[0] + 50) / 2 + (init.font2.size(message)[0] + 100) / 2 - 110 / 2 and 80 + screen.get_height() * 0.7 <= init.mouse[1] <= 110 + screen.get_height() * 0.7:
        confirm_button.fill((0, 255, 0))
        confirm_button.blit(init.font.render("confirm", True, (255, 255, 255)), (50 / 2 - init.font.size("confirm")[0] / 2, 30 / 2 - init.font.size("confirm")[1] / 2))

    else:
        confirm_button.fill((255, 255, 255))
        confirm_button.blit(init.font.render("confirm", True, (0, 0, 0)), (50 / 2 - init.font.size("confirm")[0] / 2, 30 / 2 - init.font.size("confirm")[1] / 2))
    surface.blit(confirm_button, ((init.font2.size(message)[0] + 100) / 2 - 110 / 2, 80))

    cancel_button = pygame.Surface((50, 30))
    if (init.font2.size(message)[0] + 100) / 2 - 110 / 2 + 60 + screen.get_width() / 2 - (init.font2.size(message)[0] + 50) / 2 <= init.mouse[0] <= (init.font2.size(message)[0] + 100) / 2 - 110 / 2 + 60 + 50 + screen.get_width() / 2 - (init.font2.size(message)[0] + 50) / 2 and 80 + screen.get_height() * 0.7 <= init.mouse[1] <= 110 + screen.get_height() * 0.7:
        cancel_button.fill((255, 0, 0))
        cancel_button.blit(init.font.render("cancel", True, (255, 255, 255)), (50 / 2 - init.font.size("cancel")[0] / 2, 30 / 2 - init.font.size("cancel")[1] / 2))

    else:
        cancel_button.fill((255, 255, 255))
        cancel_button.blit(init.font.render("cancel", True, (0, 0, 0)), (50 / 2 - init.font.size("cancel")[0] / 2, 30 / 2 - init.font.size("cancel")[1] / 2))
    surface.blit(cancel_button, ((init.font2.size(message)[0] + 100) / 2 - 110 / 2 + 60, 80))

    screen.blit(surface, (screen.get_width() / 2 - (init.font2.size(message)[0] + 50) / 2, screen.get_height() * 0.7))


def deep_cpopy(contains_fillterd):
    # list of concept and relation ++++> fait, concept esole
    # contains_fillterd = []
    # for element in contains:
    #     if type(element) == Concept and len(element.arcs) == 0 and len(element.arcs_back) == 0:
    #         contains_fillterd.append(element)
    #         continue
    #     elif type(element) == Concept and len(element.arcs) != 0:
    #         alone = False
    #         for relation in element.arcs:
    #             if relation in contains:
    #                 if relation.arcs[0] in contains:
    #                     fait = [element, relation, relation.arcs[0]]
    #                     if not fait in contains_fillterd: contains_fillterd.append(fait)
    #                 alone = True
    #             elif not alone and not element in contains_fillterd:
    #                 contains_fillterd.append(element)
    # for element in contains:
    #     if type(element) == Concept and len(element.arcs) == 0 and len(element.arcs_back) != 0:
    #         not_in = False
    #         for sous_element in contains_fillterd:
    #             if type(sous_element) != Concept and element == sous_element[2]:
    #                 not_in = True
    #                 break
    #         if not not_in and not element in contains_fillterd:
    #             contains_fillterd.append(element)

    obj_new_id_dics = {}
    for element in contains_fillterd:
        if type(element) == Concept:
            if element not in obj_new_id_dics:
                obj_new_id_dics[element] = copy.deepcopy(element)
        else:
            if element[0] not in obj_new_id_dics:
                obj_new_id_dics[element[0]] = copy.deepcopy(element[0])
            if element[1] not in obj_new_id_dics:
                obj_new_id_dics[element[1]] = copy.deepcopy(element[1])
            if element[2] not in obj_new_id_dics:
                obj_new_id_dics[element[2]] = copy.deepcopy(element[2])

    contains_fillterd_copy = copy.deepcopy(contains_fillterd)

    for i, element in enumerate(contains_fillterd):
        if type(element) == Concept:
            contains_fillterd_copy[i] = obj_new_id_dics[element]
            for j, arc in enumerate(element.arcs):
                if not arc in obj_new_id_dics:
                    if j < len(contains_fillterd_copy[i].arcs):
                        contains_fillterd_copy[i].arcs.pop(j)
                else:
                    contains_fillterd_copy[i].arcs[j] = obj_new_id_dics[arc]
            for j, arc_back in enumerate(element.arcs_back):
                if not arc_back in obj_new_id_dics:
                    contains_fillterd_copy[i].arcs_back.pop(j)
                else:
                    contains_fillterd_copy[i].arcs_back[j] = obj_new_id_dics[arc_back]
        else:
            for k, e in enumerate(element):
                if type(e) == Concept:
                    contains_fillterd_copy[i][k] = obj_new_id_dics[e]
                    # print(element[0].arcs)
                    for j, arc in enumerate(e.arcs):
                        if not arc in obj_new_id_dics:
                            if j < len(contains_fillterd_copy[i][k].arcs): contains_fillterd_copy[i][k].arcs.pop(j)
                        else:
                            contains_fillterd_copy[i][k].arcs[j] = obj_new_id_dics[arc]
                    for j, arc_back in enumerate(e.arcs_back):
                        if not arc_back in obj_new_id_dics:
                            if j < len(contains_fillterd_copy[i][k].arcs_back): contains_fillterd_copy[i][k].arcs_back.pop(j)
                        else:
                            contains_fillterd_copy[i][k].arcs_back[j] = obj_new_id_dics[arc_back]
                else:

                    contains_fillterd_copy[i][k] = obj_new_id_dics[e]
                    for j, arc in enumerate(e.arcs):
                        if not arc in obj_new_id_dics:
                            if j < len(contains_fillterd_copy[i][k].arcs): contains_fillterd_copy[i][k].arcs.pop(j)
                        else:
                            contains_fillterd_copy[i][k].arcs[j] = obj_new_id_dics[arc]
    return contains_fillterd_copy



def raise_(screen, init, error):
    error_surface = pygame.Surface((init.font2.size(error)[0] + 50, 60))
    error_surface.fill((0, 0, 0))
    error_surface.set_alpha(180)
    error_surface.blit(init.font2.render(error, True, (255, 0, 0)), ((init.font2.size(error)[0] + 50) / 2 - init.font2.size(error)[0] / 2 , 20))
    screen.blit(error_surface, (screen.get_width() / 2 - (init.font2.size(error)[0] + 50) / 2, screen.get_height() * 0.8))


def update_relge_coordinates(init, array, regle_y, regle_x=20):
    max_y = 60
    for element in array:
        if type(element) == Concept:
            if element == array[0]:
                element.x = regle_x
                element.y = regle_y
                if len(element.arcs) == 1:
                    element.arcs[0].x = element.x + 20 + 20 + init.font2.size(element.name + " : " + element.ref)[0]
                    element.arcs[0].y = element.y
                elif len(element.arcs) > 1:

                    for i in range(len(element.arcs)):
                        if i == 0:
                            element.arcs[i].x = element.x + 20 + 20 + init.font2.size(element.name + " : " + element.ref)[0]
                            element.arcs[i].y = element.y

                        elif i == 1:
                            element.arcs[i].x = element.x + 20 + 20 + init.font2.size(element.name + " : " + element.ref)[0]
                            element.arcs[i].y = element.y + max_y
                            max_y += 60
                        elif i > 1:
                            element.arcs[i].x = element.x + 20 + 20 + init.font2.size(element.name + " : " + element.ref)[0]
                            element.arcs[i].y = element.arcs[1].y + (i - 1) * 60
                            max_y += 60
            elif len(element.arcs_back) != 0:
                element.x = element.arcs_back[0].x + 20 + 20 + init.font2.size(element.name)[0]
                element.y = element.arcs_back[0].y
                if len(element.arcs) == 1:
                    element.arcs[0].x = element.x + 20 + 20 + init.font2.size(element.name + " : " + element.ref)[0]
                    element.arcs[0].y = element.y
                elif len(element.arcs) > 1:

                    for i in range(len(element.arcs)):
                        if i == 0:
                            element.arcs[i].x = element.x + 20 + 20 + init.font2.size(element.name + " : " + element.ref)[0]
                            element.arcs[i].y = element.y

                        elif i == 1:
                            element.arcs[i].x = element.x + 20 + 20 + init.font2.size(element.name + " : " + element.ref)[0]
                            element.arcs[i].y = element.y + max_y
                            max_y += 60
                        elif i > 1:
                            element.arcs[i].x = element.x + 20 + 20 + init.font2.size(element.name + " : " + element.ref)[0]
                            element.arcs[i].y = element.arcs[1].y + (i - 1) * 60
                            max_y += 60
            elif len(element.arcs_back) == 0:
                element.x = regle_x
                element.y = max_y + 60
                max_y += 50
                if len(element.arcs) == 1:
                    element.arcs[0].x = element.x + 20 + 20 + init.font2.size(element.name + " : " + element.ref)[0]
                    element.arcs[0].y = element.y
                elif len(element.arcs) > 1:

                    for i in range(len(element.arcs)):
                        if i == 0:
                            element.arcs[i].x = element.x + 20 + 20 + init.font2.size(element.name + " : " + element.ref)[0]
                            element.arcs[i].y = element.y

                        elif i == 1:
                            element.arcs[i].x = element.x + 20 + 20 + init.font2.size(element.name + " : " + element.ref)[0]
                            element.arcs[i].y = element.y + max_y
                            max_y += 60
                        elif i > 1:
                            element.arcs[i].x = element.x + 20 + 20 + init.font2.size(element.name + " : " + element.ref)[0]
                            element.arcs[i].y = element.arcs[1].y + (i - 1) * 60
                            max_y += 60

    return array, max_y


def update_fait_coordinates_copy(array, x, y):
    corrected = []
    for element in array:
        if type(element) == Concept:
            if not element in corrected:
                element.x += x
                element.y += y
                corrected.append(element)
        else:
            if not element[0] in corrected:
                element[0].x += x
                element[0].y += y
                corrected.append(element[0])
            if not element[1] in corrected:
                element[1].x += x
                element[1].y += y
                corrected.append(element[1])
            if not element[2] in corrected:
                element[2].x += x
                element[2].y += y
                corrected.append(element[2])
    return array


def draw_arrow(surface: pygame.Surface,start: pygame.Vector2,end: pygame.Vector2,color: tuple,body_width: int = 2,head_width: int = 4,head_height: int = 2):

    arrow = start - end
    angle = arrow.angle_to(pygame.Vector2(0, -1))
    body_length = arrow.length() - head_height

    # Create the triangle head around the origin
    head_verts = [
        pygame.Vector2(0, head_height / 2),  # Center
        pygame.Vector2(head_width / 2, -head_height / 2),  # Bottomright
        pygame.Vector2(-head_width / 2, -head_height / 2),  # Bottomleft
    ]
    # Rotate and translate the head into place
    translation = pygame.Vector2(0, arrow.length() - (head_height / 2)).rotate(-angle)
    for i in range(len(head_verts)):
        head_verts[i].rotate_ip(-angle)
        head_verts[i] += translation
        head_verts[i] += start

    pygame.draw.polygon(surface, color, head_verts)

    # Stop weird shapes when the arrow is shorter than arrow head
    if arrow.length() >= head_height:
        # Calculate the body rect, rotate and translate into place
        body_verts = [
            pygame.Vector2(-body_width / 2, body_length / 2),  # Topleft
            pygame.Vector2(body_width / 2, body_length / 2),  # Topright
            pygame.Vector2(body_width / 2, -body_length / 2),  # Bottomright
            pygame.Vector2(-body_width / 2, -body_length / 2),  # Bottomleft
        ]
        translation = pygame.Vector2(0, body_length / 2).rotate(-angle)
        for i in range(len(body_verts)):
            body_verts[i].rotate_ip(-angle)
            body_verts[i] += translation
            body_verts[i] += start

        pygame.draw.polygon(surface, color, body_verts)


def render_multi_line(screen, font, array, x, y, font_size, init, offset):
    for i in range(len(array)):
        if type(array[i]) == Concept:
            printing = array[i].name + " : " + array[i].ref
            screen.blit(font.render(printing, True, (255, 255, 255)), (x, offset + y + font_size * i))
        else:
            printing = array[i][0].name + " : " + array[i][0].ref + " ==> " + array[i][1].name  + " ==> " + array[i][2].name + " : " + array[i][2].ref
            screen.blit(font.render(printing, True, (255, 255, 255)), (x, offset + y + font_size * i))


def render_multi_line_br(screen, font, array, x, y, font_size, init, offset):
    i = 0
    j = 0
    for element in array:
        if element["premise"] == [] and element["conclusion"] == []:
            continue
        screen.blit(font.render(f"Regle {j} : ---------------------------------------------", True, (255, 255, 255)), (x, offset + y + font_size * i))
        i += 1
        screen.blit(init.font.render(f"premise", True, (255, 255, 255)), (x, 2 + offset + y + font_size * i))
        i += 1
        list = array_premise_conclusion(element["premise"])
        for premise in list:
            screen.blit(font.render(premise, True, (255, 255, 255)), (x, offset + y + font_size * i))
            i += 1
        screen.blit(init.font.render(f"conclusion", True, (255, 255, 255)), (x,  2 + offset + y + font_size * i))
        i += 1
        list = array_premise_conclusion(element["conclusion"])
        for premise in list:
            screen.blit(font.render(premise, True, (255, 255, 255)), (x, offset + y + font_size * i))
            i += 1
        i += 1
        j += 1


def array_premise_conclusion(list):
    from classs import Concept
    list_to_retuer = []
    for element in list:
        if type(element) == Concept:
            for link in element.arcs:
                list_to_retuer.append(element.name + ":" + element.ref + "==>" + link.name + "==>" + link.arcs[0].name + ":" + link.arcs[0].ref)
    return list_to_retuer


def get_vocabulaire(init):
    from classs import Concept, Relation

    concept_list = []
    relation_list = []
    signatures_list = []
    I = []
    marqueurs_list = []
    for element in init.bf_main_list:
        signature = []
        if type(element) == Concept:
            signature.append(element.name)
            if not element.ref in I and not element.ref == "*":
                I.append(element.ref)
                marqueurs_list.append([element.ref, element.name])
            if not element.name in concept_list:
                concept_list.append(element.name)
            continue
        elif type(element[0]) == Concept:
            signature.append(element[0].name)
            if not element[0].ref in I and not element[0].ref == "*":
                I.append(element[0].ref)
                marqueurs_list.append([element[0].ref, element[0].name])
            if not element[0].name in concept_list:
                concept_list.append(element[0].name)

        if type(element[1]) == Relation:
            signature.append(element[1].name)
            if not element[1].name in relation_list:
                relation_list.append(element[1].name)
        if type(element[2]) == Concept:
            signature.append(element[2].name)
            if not element[2].ref in I and not element[2].ref == "*":
                I.append(element[2].ref)
                marqueurs_list.append([element[2].ref, element[2].name])
            if not element[2].name in concept_list:
                concept_list.append(element[2].name)
        if not signature in signatures_list and len(signature) == 3:
            signatures_list.append(signature)
    return concept_list, relation_list, signatures_list, I, marqueurs_list


def display_vo_list(screen, init, offset, concept_list, relation_list, signatures_list, I, marqueurs_list):
    screen.blit(init.font2.render("Concept : --------------------------------------------------------------", True, (255, 255, 255)), (10, offset + 10 + init.font2.size("A")[1] * 0))
    i = 1
    for element in concept_list:
        screen.blit(init.font2.render(element, True, (255, 255, 255)), (30, offset + 10 + init.font2.size("A")[1] * i))
        i += 1

    screen.blit(init.font2.render("Relation : -------------------------------------------------------------------------", True, (255, 255, 255)), (10, offset + 10 + init.font2.size("A")[1] * i))
    i += 1
    for element in relation_list:
        screen.blit(init.font2.render(element, True, (255, 255, 255)), (30, offset + 10 + init.font2.size("A")[1] * i))
        i += 1

    screen.blit(init.font2.render("Les signatures : --------------------------------------------------------------", True, (255, 255, 255)), (10, offset + 10 + init.font2.size("A")[1] * i))
    i += 1
    for element in signatures_list:
        screen.blit(init.font2.render(element[1] + " (" + element[0] + " , " + element[2] + ")", True, (255, 255, 255)), (30, offset + 10 + init.font2.size("A")[1] * i))
        i += 1

    screen.blit(init.font2.render("Les marqueurs : --------------------------------------------------------------", True, (255, 255, 255)), (10, offset + 10 + init.font2.size("A")[1] * i))
    i += 1
    instance = "I = {"
    for element in I:
        instance += element + "; "
    instance = instance[:-2]
    instance += "}"
    screen.blit(init.font2.render(instance , True, (255, 255, 255)), (30, offset + 10 + init.font2.size("A")[1] * i))
    i += 1
    for element in marqueurs_list:
        screen.blit(init.font2.render("t(" + element[0] + ")" + " = " + element[1], True, (255, 255, 255)), (30, offset + 10 + init.font2.size("A")[1] * i))
        i += 1


