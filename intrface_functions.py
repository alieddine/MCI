import copy
import sys
import time
from array import array
from shlex import shlex

import pygame
from pygame.locals import Rect

from classs import Concept, Relation


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

    if 150 + bf_surface.get_width() / 2 - init.font2.size("save BF")[0] / 2 - 8 <= init.mouse[0] <= 150 + bf_surface.get_width() / 2 - init.font2.size("save BF")[0] / 2 - 8 + init.font2.size("save BF")[0] + 16 and 80 + bf_surface.get_height() - 34 <= init.mouse[
        1] <= 80 + bf_surface.get_height() - 34 + 25:
        pygame.draw.rect(bf_surface, (50, 50, 50), (100 + bf_surface.get_width() / 2 - init.font2.size("save BF")[0] / 2 - 10, bf_surface.get_height() - 36, init.font2.size("save BF")[0] + 20, 29), border_radius=10)
        new_bf = init.font2.render("save BF", True, (255, 255, 255))
    else:
        pygame.draw.rect(bf_surface, (255, 255, 255), (100 + bf_surface.get_width() / 2 - init.font2.size("save BF")[0] / 2 - 10, bf_surface.get_height() - 36, init.font2.size("save BF")[0] + 20, 29), border_radius=10)
        new_bf = init.font2.render("save BF", True, (50, 50, 50))
    pygame.draw.rect(bf_surface, (255, 255, 255), (100 + bf_surface.get_width() / 2 - init.font2.size("save BF")[0] / 2 - 10, bf_surface.get_height() - 36, init.font2.size("save BF")[0] + 20, 29), 2, border_radius=10)
    bf_surface.blit(new_bf, (100 + bf_surface.get_width() / 2 - init.font2.size("save BF")[0] / 2, bf_surface.get_height() - 32))

    bf_list_surface = pygame.Surface((bf_surface.get_width() - 50, bf_surface.get_height() - 100))
    bf_list_surface.fill((70, 70, 70))

    if not len(init.bfn) == 0:
        render_multi_line(bf_list_surface, init.font2, init.bfn, 10, 10, init.font2.size("A")[1], init, init.offset_bf_list)
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

    if 50 * 2 + 100 + init.width + br_surface.get_width() / 2 - init.font2.size("save BR")[0] / 2 - 8 <= init.mouse[0] <= 50 * 2 + 100 + init.width + br_surface.get_width() / 2 - init.font2.size("save BR")[0] / 2 - 8 + init.font2.size("save BR")[0] + 16 and 80 + br_surface.get_height() - 34 <= init.mouse[1] <= 80 + br_surface.get_height() - 34 + 25:
        pygame.draw.rect(br_surface, (50, 50, 50), (100 + br_surface.get_width() / 2 - init.font2.size("save BR")[0] / 2 - 10, br_surface.get_height() - 36, init.font2.size("save BR")[0] + 20, 29), border_radius=10)
        new_bf = init.font2.render("save BR", True, (255, 255, 255))
    else:
        pygame.draw.rect(br_surface, (255, 255, 255), (100 + br_surface.get_width() / 2 - init.font2.size("save BR")[0] / 2 - 10, br_surface.get_height() - 36, init.font2.size("save BR")[0] + 20, 29), border_radius=10)
        new_bf = init.font2.render("save BR", True, (50, 50, 50))
    pygame.draw.rect(br_surface, (255, 255, 255), (100 + br_surface.get_width() / 2 - init.font2.size("save BR")[0] / 2 - 10, br_surface.get_height() - 36, init.font2.size("save BR")[0] + 20, 29), 2, border_radius=10)
    br_surface.blit(new_bf, (100 + br_surface.get_width() / 2 - init.font2.size("save BR")[0] / 2, br_surface.get_height() - 32))


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


def new_rq_intrface(screen, init):
    from classs import Concept
    black_fillter = pygame.Surface((screen.get_width(), screen.get_height()))
    black_fillter.fill((0, 0, 0))
    black_fillter.set_alpha(128)
    screen.blit(black_fillter, (0, 0))

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

    main_container = pygame.Surface((screen.get_width() * 0.6, screen.get_height() * 0.3))
    main_container.fill((50, 50, 50))
    pygame.draw.rect(main_container, (255, 255, 255), (0, 0, main_container.get_width(), main_container.get_height()), 2)

    if not len(init.fun_rq) == 0:
        for element in init.fun_rq:
            if type(element) == Concept:
                pygame.draw.rect(main_container, (255, 255, 255), (element.x - 80, element.y - screen.get_height() * 0.05 + 0, 20 + init.font2.size(element.name + " : " + element.ref)[0], 40), 2)
                main_container.blit(init.font2.render((element.name + " : " + element.ref), True, (255, 255, 255)), (element.x + (20 + init.font2.size(element.name + " : " + element.ref)[0]) / 2 - init.font2.size(element.name + " : " + element.ref)[0] / 2 - 80, element.y + 10 - screen.get_height() * 0.05 + 0))
            else:
                pygame.draw.rect(main_container, (255, 255, 255), (element.x - 80, element.y - screen.get_height() * 0.05 + 0, 20 + init.font2.size(element.name)[0], 40), 2, 20)
                main_container.blit(init.font2.render(element.name, True, (255, 255, 255)), (element.x + (20 + init.font2.size(element.name)[0]) / 2 - init.font2.size(element.name)[0] / 2 - 80, element.y + 10 - screen.get_height() * 0.05 + 0))
            draw_arc(element, init, screen, main_container, 0)

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
        if init.new_fait[0]:
            if len(init.new_fait[2]) == 1:
                draw_one_arc(init.new_fait[2][0], init.mouse, init, screen, main_container, 0)
            elif len(init.new_fait[2]) == 2:
                if not init.new_fait[1]:
                    draw_arrow(screen, pygame.Vector2(init.mouse[0] - 10, init.mouse[1]), pygame.Vector2(init.mouse[0] + 20, init.mouse[1]), (255, 255, 255), 2, 10, 5)
                    draw_one_arc(init.new_fait[2][0], init.new_fait[2][1], init, screen, main_container, 0)
                else:
                    draw_one_arc(init.new_fait[2][0], init.new_fait[2][1], init, screen, main_container, 0)
                    draw_one_arc(init.new_fait[2][1], init.mouse, init, screen, main_container, 0)
        else:
            draw_arrow(screen, pygame.Vector2(init.mouse[0] - 10, init.mouse[1]), pygame.Vector2(init.mouse[0] + 20, init.mouse[1]), (255, 255, 255), 2, 10, 5)

    if init.erase_button:
        rect = Rect(init.mouse[0], init.mouse[1] - 0, 1, 1)
        bfn_rec = get_rects(init.fun_rq, init)
        collide = pygame.Rect.collidelist(rect, bfn_rec)
        if collide == -1:
            screen.blit(pygame.image.load("images/erase_white.png"), (init.mouse[0] - 20, init.mouse[1] - 20))
        else:
            screen.blit(pygame.image.load("images/erase_red.png"), (init.mouse[0] - 20, init.mouse[1] - 20))


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

    if not len(init.bfn) == 0:
        for element in init.bfn:
            if type(element) == Concept:
                pygame.draw.rect(main_container, (255, 255, 255), (element.x - 80, element.y - screen.get_height() * 0.05 + init.bf_interface_offset, 20 + init.font2.size(element.name + " : " + element.ref)[0], 40), 2)
                main_container.blit(init.font2.render((element.name + " : " + element.ref), True, (255, 255, 255)), (element.x + (20 + init.font2.size(element.name + " : " + element.ref)[0]) / 2 - init.font2.size(element.name + " : " + element.ref)[0] / 2 - 80, element.y + 10 - screen.get_height() * 0.05 + init.bf_interface_offset))
            else:
                pygame.draw.rect(main_container, (255, 255, 255), (element.x - 80, element.y - screen.get_height() * 0.05 + init.bf_interface_offset, 20 + init.font2.size(element.name)[0], 40), 2, 20)
                main_container.blit(init.font2.render(element.name, True, (255, 255, 255)), (element.x + (20 + init.font2.size(element.name)[0]) / 2 - init.font2.size(element.name)[0] / 2 - 80, element.y + 10 - screen.get_height() * 0.05 + init.bf_interface_offset))
            draw_arc(element, init, screen, main_container, init.bf_interface_offset)

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
        if init.new_fait[0]:
            if len(init.new_fait[2]) == 1:
                draw_one_arc(init.new_fait[2][0], init.mouse, init, screen, main_container, init.bf_interface_offset)
            elif len(init.new_fait[2]) == 2:
                if not init.new_fait[1]:
                    draw_arrow(screen, pygame.Vector2(init.mouse[0] - 10, init.mouse[1]), pygame.Vector2(init.mouse[0] + 20, init.mouse[1]), (255, 255, 255), 2, 10, 5)
                    draw_one_arc(init.new_fait[2][0], init.new_fait[2][1], init, screen, main_container, init.bf_interface_offset)
                else:
                    draw_one_arc(init.new_fait[2][0], init.new_fait[2][1], init, screen, main_container, init.bf_interface_offset)
                    draw_one_arc(init.new_fait[2][1], init.mouse, init, screen, main_container, init.bf_interface_offset)
        else:
            draw_arrow(screen, pygame.Vector2(init.mouse[0] - 10, init.mouse[1]), pygame.Vector2(init.mouse[0] + 20, init.mouse[1]), (255, 255, 255), 2, 10, 5)

    if init.erase_button:
        rect = Rect(init.mouse[0], init.mouse[1] - init.bf_interface_offset, 1, 1)
        bfn_rec = get_rects(init.bfn, init)
        collide = pygame.Rect.collidelist(rect, bfn_rec)
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

def draw_one_arc(obj, element, init, screen, main_container, offset):
    from classs import Concept, Relation
    if type(obj) == Concept:
        first_point_rect = Rect(obj.x, obj.y, 20 + init.font2.size(obj.name + " : " + obj.ref)[0], 40)
    else:
        first_point_rect = Rect(obj.x, obj.y, 20 + init.font2.size(obj.name)[0], 40)

    if type(element) == Concept:
        second_point_rect = Rect(element.x, element.y, 20 + init.font2.size(element.name + " : " + element.ref)[0], 40)
    elif type(element) == Relation:
        second_point_rect = Rect(element.x, element.y, 20 + init.font2.size(element.name)[0], 40)
    else:
        second_point_rect = Rect(element[0], element[1], 1, 1)
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
    draw_arrow(screen, pygame.Vector2(x1, y1+ offset), pygame.Vector2(x2, y2 + offset), (255, 255, 255), 3, 20, 10)


def draw_arc_intero(obj, init, offsetx_y, main_container, offset):
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
        draw_arrow(main_container, pygame.Vector2(x1 + offsetx_y[0], y1 + offsetx_y[1]+ offset), pygame.Vector2(x2 + offsetx_y[0], y2 + offsetx_y[1] + offset), (255, 255, 255), 3, 20, 10)


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


def Restriction_intface(screen, init, obj):
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


def auto_BFN(screen, init):
    init.BFN = Simplification(init.BFN)
    clock = pygame.time.Clock()
    for concept_1 in init.BFN:
        clock.tick(60)
        if type(concept_1) == Concept:
            for concept_2 in init.BFN:
                clock.tick(60)

                if type(concept_2) == Concept and concept_1 != concept_2 and concept_1.name == concept_2.name and concept_1.ref == concept_2.ref:
                    draw_BFN(screen, init, concept_1, concept_2)
                    clock.tick(1)
                    init.BFN = Jointure(concept_1, concept_2, init.BFN)[1]
                    draw_BFN(screen, init, concept_1, concept_2)


def draw_BFN(screen, init, c1, c2):
    element_drwaned = []
    main_surface = pygame.Surface((screen.get_width() * 0.7, screen.get_height() * 0.8))
    main_surface.fill((70, 70, 70))
    main_surface.set_alpha(230)
    screen.blit(main_surface, (screen.get_width() * 0.05, screen.get_width() * 0.05))

    main_surface.set_alpha(230)
    for obj in init.BFN:
        if not obj in element_drwaned:
            if type(obj) == Concept:
                if obj == c1 or obj == c2:
                    pygame.draw.rect(screen, (255, 0, 0), (obj.x + screen.get_width() * 0.05, obj.y + screen.get_width() * 0.05 + init.auto_bfn_offset, 20 + init.font2.size(obj.name + " : " + obj.ref)[0], 40), 2)
                else:
                    pygame.draw.rect(screen, (255, 255, 255), (obj.x + screen.get_width() * 0.05, obj.y + screen.get_width() * 0.05 + init.auto_bfn_offset, 20 + init.font2.size(obj.name + " : " + obj.ref)[0], 40), 2)
                screen.blit(init.font2.render((obj.name + " : " + obj.ref), True, (255, 255, 255)),
                                  (obj.x + screen.get_width() * 0.05 + (20 + init.font2.size(obj.name + " : " + obj.ref)[0]) / 2 - init.font2.size(obj.name + " : " + obj.ref)[0] / 2, obj.y + 10 + screen.get_width() * 0.05 + init.auto_bfn_offset))
            else:
                pygame.draw.rect(screen, (255, 255, 255), (obj.x + screen.get_width() * 0.05, obj.y + screen.get_width() * 0.05 + init.auto_bfn_offset, 20 + init.font2.size(obj.name)[0], 40), 2, 20)
                screen.blit(init.font2.render(obj.name, True, (255, 255, 255)), (obj.x + screen.get_width() * 0.05 + (20 + init.font2.size(obj.name)[0]) / 2 - init.font2.size(obj.name)[0] / 2, obj.y + 10 + screen.get_width() * 0.05 + init.auto_bfn_offset))
            element_drwaned.append(obj)
            draw_arc_intero(obj, init, (screen.get_width() * 0.05, screen.get_width() * 0.05), screen, init.auto_bfn_offset)
    pygame.display.update()


def display_interro(screen, init):

    main_surface = pygame.Surface((screen.get_width() * 0.7, screen.get_height() * 0.8))
    main_surface.fill((70, 70, 70))
    main_surface.set_alpha(230)

    show_bf_button = pygame.Surface((70, 30))
    show_br_button = pygame.Surface((70, 30))
    make_bfn_button = pygame.Surface((70, 30))
    mauto_bfn_button = pygame.Surface((70, 30))
    if not init.intero_buttons["make BFN"] and not init.intero_buttons["auto BFN"] and not init.intero_buttons["show BR"] and not init.intero_buttons["show BF"]: main_surface.blit(init.font3.render("None", True, (255, 0, 0)), (main_surface.get_width() / 2 - init.font3.size("None")[0] / 2,  main_surface.get_height() / 2 - init.font3.size("None")[1] / 2))
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

    if init.intero_buttons["make BFN"] or screen.get_width() * 0.8 <= init.mouse[0] <= screen.get_width() * 0.8 + 70 and screen.get_height() * 0.1 + 80 <= init.mouse[1] <= screen.get_height() * 0.1 + 30 + 80:
        make_bfn_button.fill((230, 230, 230))
        make_bfn_button.blit(init.font.render("make BFN", True, (255, 0, 0)), (70 / 2 - init.font.size("make BFN")[0] / 2, 30 / 2 - init.font.size("make BFN")[1] / 2 ))

    else:
        make_bfn_button.fill((255, 255, 255))
        make_bfn_button.blit(init.font.render("make BFN", True, (0, 0, 0)), (70 / 2 - init.font.size("make BFN")[0] / 2, 30 / 2 - init.font.size("make BFN")[1] / 2))
    screen.blit(make_bfn_button, (screen.get_width() * 0.8, screen.get_height() * 0.1 + 80))

    if screen.get_width() * 0.8 <= init.mouse[0] <= screen.get_width() * 0.8 + 70 and screen.get_height() * 0.1 + 120 <= init.mouse[1] <= screen.get_height() * 0.1 + 30 + 120:
        mauto_bfn_button.fill((0, 0, 0))
        mauto_bfn_button.blit(init.font.render("auto BFN", True, (255, 0, 0)), (70 / 2 - init.font.size("auto BFN")[0] / 2, 30 / 2 - init.font.size("auto BFN")[1] / 2))

    else:
        mauto_bfn_button.fill((255, 255, 255))
        mauto_bfn_button.blit(init.font.render("auto BFN", True, (0, 0, 0)), (70 / 2 - init.font.size("auto BFN")[0] / 2, 30 / 2 - init.font.size("auto BFN")[1] / 2))
    screen.blit(mauto_bfn_button, (screen.get_width() * 0.8, screen.get_height() * 0.1 + 120))



    if init.intero_buttons["auto BFN"]:
        chainage_avant_button = pygame.Surface((70, 30))
        if screen.get_width() * 0.8 + 80 <= init.mouse[0] <= screen.get_width() * 0.8 + 150 and screen.get_height() * 0.1 + 120 <= init.mouse[1] <= screen.get_height() * 0.1 + 30 + 120:
            chainage_avant_button.fill((0, 0, 0))
            chainage_avant_button.blit(init.font.render("avant", True, (255, 0, 0)), (70 / 2 - init.font.size("avant")[0] / 2, 30 / 2 - init.font.size("avant")[1] / 2))

        else:
            chainage_avant_button.fill((255, 255, 255))
            chainage_avant_button.blit(init.font.render("avant", True, (0, 0, 0)), (70 / 2 - init.font.size("avant")[0] / 2, 30 / 2 - init.font.size("avant")[1] / 2))
        screen.blit(chainage_avant_button, (screen.get_width() * 0.8 + 80, screen.get_height() * 0.1 + 120))

        element_drwaned = []
        for obj in init.BFN:
            if not obj in element_drwaned:
                if type(obj) == Concept:
                    pygame.draw.rect(main_surface, (255, 255, 255), (obj.x, obj.y + init.auto_bfn_offset, 20 + init.font2.size(obj.name + " : " + obj.ref)[0], 40), 2)
                    main_surface.blit(init.font2.render((obj.name + " : " + obj.ref), True, (255, 255, 255)),
                                      (obj.x + (20 + init.font2.size(obj.name + " : " + obj.ref)[0]) / 2 - init.font2.size(obj.name + " : " + obj.ref)[0] / 2, obj.y + 10 + init.auto_bfn_offset))
                else:
                    pygame.draw.rect(main_surface, (255, 255, 255), (obj.x, obj.y + init.auto_bfn_offset, 20 + init.font2.size(obj.name)[0], 40), 2, 20)
                    main_surface.blit(init.font2.render(obj.name, True, (255, 255, 255)), (obj.x + (20 + init.font2.size(obj.name)[0]) / 2 - init.font2.size(obj.name)[0] / 2, obj.y + 10 + init.auto_bfn_offset))
                element_drwaned.append(obj)
                draw_arc_intero(obj, init, (0, 0), main_surface, init.auto_bfn_offset)

    if init.intero_buttons["make BFN"]:
        element_drwaned = []
        for element in init.bfn_fun:
            obj = element
            if not obj in element_drwaned:
                if type(obj) == Concept:
                    color = (255, 255, 255)
                    if obj == init.intero_buttons["fragmentation"][1][1] or obj == init.intero_buttons["Restriction_1"][1][1] or obj ==init.intero_buttons["Restriction_1"][2][1]:
                        color = (255, 0, 0)
                    pygame.draw.rect(main_surface, color, (obj.x, obj.y + init.make_bfn_offset, 20 + init.font2.size(obj.name + " : " + obj.ref)[0], 40), 2)
                    main_surface.blit(init.font2.render((obj.name + " : " + obj.ref), True, color),
                                      (obj.x + (20 + init.font2.size(obj.name + " : " + obj.ref)[0]) / 2 - init.font2.size(obj.name + " : " + obj.ref)[0] / 2, obj.y + 10 + init.make_bfn_offset))
                else:
                    pygame.draw.rect(main_surface, (255, 255, 255), (obj.x, obj.y + init.make_bfn_offset, 20 + init.font2.size(obj.name)[0], 40), 2, 20)
                    main_surface.blit(init.font2.render(obj.name, True, (255, 255, 255)), (obj.x + (20 + init.font2.size(obj.name)[0]) / 2 - init.font2.size(obj.name)[0] / 2, obj.y + 10 + init.make_bfn_offset))
                element_drwaned.append(obj)
                draw_arc_intero(obj, init, (0, 0), main_surface, init.make_bfn_offset)
        Restriction_button = pygame.Surface((70, 30))
        if init.intero_buttons["Restriction"][0] or screen.get_width() * 0.8 + 10 + 70 <= init.mouse[0] <= screen.get_width() * 0.8 + 70 + 10 + 70 and screen.get_height() * 0.1 + 80 <= init.mouse[1] <= screen.get_height() * 0.1 + 30 + 80:
            Restriction_button.fill((230, 230, 230))
            Restriction_button.blit(init.font.render("Restriction", True, (255, 0, 0)), (70 / 2 - init.font.size("Restriction")[0] / 2, 30 / 2 - init.font.size("Restriction")[1] / 2))

        else:
            Restriction_button.fill((255, 255, 255))
            Restriction_button.blit(init.font.render("Restriction", True, (0, 0, 0)), (70 / 2 - init.font.size("Restriction")[0] / 2, 30 / 2 - init.font.size("Restriction")[1] / 2))
        screen.blit(Restriction_button, (screen.get_width() * 0.8 + 10 + 70, screen.get_height() * 0.1 + 80))

        Restriction_button = pygame.Surface((70, 30))
        if init.intero_buttons["Restriction_1"][0] or screen.get_width() * 0.8 + 10 + 150 <= init.mouse[0] <= screen.get_width() * 0.8 + 150 + 10 + 70 and screen.get_height() * 0.1 + 80 <= init.mouse[1] <= screen.get_height() * 0.1 + 30 + 80:
            Restriction_button.fill((230, 230, 230))
            Restriction_button.blit(init.font.render("Restriction_1", True, (255, 0, 0)), (70 / 2 - init.font.size("Restriction_1")[0] / 2, 30 / 2 - init.font.size("Restriction_1")[1] / 2))

        else:
            Restriction_button.fill((255, 255, 255))
            Restriction_button.blit(init.font.render("Restriction_1", True, (0, 0, 0)), (70 / 2 - init.font.size("Restriction")[0] / 2, 30 / 2 - init.font.size("Restriction_1")[1] / 2))
        screen.blit(Restriction_button, (screen.get_width() * 0.8 + 10 + 150, screen.get_height() * 0.1 + 80))

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

        projection_button = pygame.Surface((70, 30))
        if init.intero_buttons["projection"] or screen.get_width() * 0.8 + 10 + 70 <= init.mouse[0] <= screen.get_width() * 0.8 + 70 + 10 + 70 and screen.get_height() * 0.1 + 240 <= init.mouse[1] <= screen.get_height() * 0.1 + 30 + 240:
            projection_button.fill((230, 230, 230))
            projection_button.blit(init.font.render("projection", True, (255, 0, 0)), (70 / 2 - init.font.size("projection")[0] / 2, 30 / 2 - init.font.size("projection")[1] / 2))

        else:
            projection_button.fill((255, 255, 255))
            projection_button.blit(init.font.render("projection", True, (0, 0, 0)), (70 / 2 - init.font.size("projection")[0] / 2, 30 / 2 - init.font.size("projection")[1] / 2))
        screen.blit(projection_button, (screen.get_width() * 0.8 + 10 + 70, screen.get_height() * 0.1 + 240))

        simplification_button = pygame.Surface((70, 30))
        if init.intero_buttons["Simplification"] or screen.get_width() * 0.8 + 10 + 70 <= init.mouse[0] <= screen.get_width() * 0.8 + 70 + 10 + 70 and screen.get_height() * 0.1 + 280 <= init.mouse[1] <= screen.get_height() * 0.1 + 30 + 280:
            simplification_button.fill((230, 230, 230))
            simplification_button.blit(init.font.render("Simplification", True, (255, 0, 0)), (70 / 2 - init.font.size("Simplification")[0] / 2, 30 / 2 - init.font.size("Simplification")[1] / 2))

        else:
            simplification_button.fill((255, 255, 255))
            simplification_button.blit(init.font.render("Simplification", True, (0, 0, 0)), (70 / 2 - init.font.size("Simplification")[0] / 2, 30 / 2 - init.font.size("Simplification")[1] / 2))
        screen.blit(simplification_button, (screen.get_width() * 0.8 + 10 + 70, screen.get_height() * 0.1 + 280))


    elif init.intero_buttons["show BF"]:
        element_drwaned = []
        for element in init.bfn:
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
            draw_arc_intero(obj, init, (0, 0), main_surface, 0)

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
                    draw_arc_intero(obj, init, (0, 0), main_surface, 0)
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
                    draw_arc_intero(obj, init, (0, 0), main_surface, 0)
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
        Restriction_intface(screen, init, init.intero_buttons["Restriction"][2])

    if init.intero_buttons["Copy"][0] and init.intero_buttons["make BFN"]:
        if init.intero_buttons["Copy"][1][0] and not init.intero_buttons["Copy"][2][0]:
            pygame.draw.rect(screen, (255, 255, 255), (init.intero_buttons["Copy"][1][1][0], init.intero_buttons["Copy"][1][1][1], init.mouse[0] - init.intero_buttons["Copy"][1][1][0], init.mouse[1] - init.intero_buttons["Copy"][1][1][1]), 2)
        if init.intero_buttons["Copy"][2][0]:
            pygame.draw.rect(screen, (255, 255, 255), (init.intero_buttons["Copy"][1][1][0], init.intero_buttons["Copy"][1][1][1], init.intero_buttons["Copy"][2][1][0] - init.intero_buttons["Copy"][1][1][0], init.intero_buttons["Copy"][2][1][1] - init.intero_buttons["Copy"][1][1][1]), 2)
    if init.intero_buttons["jointure"][2][0] and init.intero_buttons["jointure"][1][0]:
        window_widh_buttons(screen, init, "do you want to join them")

    if init.intero_buttons["Restriction_1"][2][0]:
        window_widh_buttons(screen, init, "do you want to restrict")


    if init.fun_projecting:
        show_rq_button = pygame.Surface((70, 30))
        if init.show_rq or 20 <= init.mouse[0] <= 20 + 70 and screen.get_height() * 0.8 <= init.mouse[1] <= screen.get_height() * 0.8 + 30:
            show_rq_button.fill((230, 230, 230))
            show_rq_button.blit(init.font.render("show rq", True, (255, 0, 0)), (70 / 2 - init.font.size("show rq")[0] / 2, 30 / 2 - init.font.size("show rq")[1] / 2))

        else:
            show_rq_button.fill((255, 255, 255))
            show_rq_button.blit(init.font.render("show rq", True, (0, 0, 0)), (70 / 2 - init.font.size("show rq")[0] / 2, 30 / 2 - init.font.size("show rq")[1] / 2))
        screen.blit(show_rq_button, (20, screen.get_height() * 0.8))

        show_answer_button = pygame.Surface((70, 30))
        if init.show_answer or 20 <= init.mouse[0] <= 20 + 70 and screen.get_height() * 0.8 + 40 <= init.mouse[1] <= screen.get_height() * 0.8 + 40 + 30:
            show_answer_button.fill((230, 230, 230))
            show_answer_button.blit(init.font.render("show answer", True, (255, 0, 0)), (70 / 2 - init.font.size("show answer")[0] / 2, 30 / 2 - init.font.size("show answer")[1] / 2))

        else:
            show_answer_button.fill((255, 255, 255))
            show_answer_button.blit(init.font.render("show answer", True, (0, 0, 0)), (70 / 2 - init.font.size("show answer")[0] / 2, 30 / 2 - init.font.size("show answer")[1] / 2))
        screen.blit(show_answer_button, (20, screen.get_height() * 0.8 + 40))

        filter_button = pygame.Surface((70, 30))
        if init.show_answer_filter or 100 <= init.mouse[0] <= 100 + 70 and screen.get_height() * 0.8 + 40 <= init.mouse[1] <= screen.get_height() * 0.8 + 40 + 30:
            filter_button.fill((230, 230, 230))
            filter_button.blit(init.font.render("filter", True, (255, 0, 0)), (70 / 2 - init.font.size("filter")[0] / 2, 30 / 2 - init.font.size("filter")[1] / 2))

        else:
            filter_button.fill((255, 255, 255))
            filter_button.blit(init.font.render("filter", True, (0, 0, 0)), (70 / 2 - init.font.size("filter")[0] / 2, 30 / 2 - init.font.size("filter")[1] / 2))
        screen.blit(filter_button, (100, screen.get_height() * 0.8 + 40))

        stop_projection_button = pygame.Surface((70, 30))
        if 20 <= init.mouse[0] <= 20 + 70 and screen.get_height() * 0.8 + 80 <= init.mouse[1] <= screen.get_height() * 0.8 + 80 + 30:
            stop_projection_button.fill((230, 230, 230))
            stop_projection_button.blit(init.font.render("stop", True, (255, 0, 0)), (70 / 2 - init.font.size("stop")[0] / 2, 30 / 2 - init.font.size("stop")[1] / 2))

        else:
            stop_projection_button.fill((255, 255, 255))
            stop_projection_button.blit(init.font.render("stop", True, (0, 0, 0)), (70 / 2 - init.font.size("stop")[0] / 2, 30 / 2 - init.font.size("stop")[1] / 2))
        screen.blit(stop_projection_button, (20, screen.get_height() * 0.8 + 80))


def show_fun_rq(screen, init):
    main_surface = pygame.Surface((screen.get_width() * 0.8, screen.get_height() * 0.3))
    main_surface.fill((50, 50, 50))
    first = init.fun_rq[0]
    for element in init.fun_rq:
        if first.x > element.x:
            first = element
    offset_x = (screen.get_width() * 0.2 + 20) - (first.x)
    offset_y = (screen.get_height() * 0.7 + 20) - (first.y)
    init.fun_rq = update_fait_coordinates_copy(init.fun_rq, offset_x, offset_y)
    element_drwaned = []
    for element in init.fun_rq:
        obj = element
        if not obj in element_drwaned:
            if type(obj) == Concept:
                color = (255, 255, 255)
                if obj.ref == "*":
                    color = (255, 0, 0)
                pygame.draw.rect(main_surface, color, (obj.x - screen.get_width() * 0.2, obj.y - screen.get_height() * 0.7 + init.fun_rq_offset, 20 + init.font2.size(obj.name + " : " + obj.ref)[0], 40), 2)
                main_surface.blit(init.font2.render((obj.name + " : " + obj.ref), True, color),
                                  (obj.x - screen.get_width() * 0.2 + (20 + init.font2.size(obj.name + " : " + obj.ref)[0]) / 2 - init.font2.size(obj.name + " : " + obj.ref)[0] / 2, obj.y - screen.get_height() * 0.7 + 10 + init.fun_rq_offset))
            else:
                pygame.draw.rect(main_surface, (255, 255, 255), (obj.x - screen.get_width() * 0.2, obj.y - screen.get_height() * 0.7 + init.fun_rq_offset, 20 + init.font2.size(obj.name)[0], 40), 2, 20)
                main_surface.blit(init.font2.render(obj.name, True, (255, 255, 255)), (obj.x - screen.get_width() * 0.2 + (20 + init.font2.size(obj.name)[0]) / 2 - init.font2.size(obj.name)[0] / 2, obj.y - screen.get_height() * 0.7 + 10 + init.fun_rq_offset))
            element_drwaned.append(obj)
            draw_arc_intero(obj, init, (- screen.get_width() * 0.2, - screen.get_height() * 0.7), main_surface, init.fun_rq_offset)

    screen.blit(main_surface, (screen.get_width() * 0.2, screen.get_height() * 0.7))
    pygame.draw.rect(screen, (255, 255, 255), (screen.get_width() * 0.2, screen.get_height() * 0.7, screen.get_width() * 0.8, screen.get_height() * 0.3), 2)


def show_fun_answer(screen, init):
    main_surface = pygame.Surface((screen.get_width() * 0.8, screen.get_height() * 0.3))
    main_surface.fill((50, 50, 50))
    rq_faits = objs_to_faits(init.fun_rq)
    s = ""
    space = 0
    if not init.fun_answer == False:
        for i, element in enumerate(init.fun_answer):
            if type(rq_faits[i]) == Concept:
                s += "concept "+ str(i)+" ::  "+ str(rq_faits[i].name)+ " : "+ str(rq_faits[i].ref)
                space = len("concept "+ str(i)+" ::  "+ str(rq_faits[i].name)+ " : "+ str(rq_faits[i].ref))
            else:
                s += "fait "+ str(i)+" ::  "+ str(rq_faits[i][0].name) + " : " + str(rq_faits[i][0].ref) + "=>"+ str(rq_faits[i][1].name) + "=>" + str(rq_faits[i][2].name) + " : " + str(rq_faits[i][2].ref)
                space = len("fait "+ str(i)+" ::  "+ str(rq_faits[i][0].name) + " : " + str(rq_faits[i][0].ref) + "=>"+ str(rq_faits[i][1].name) + "=>" + str(rq_faits[i][2].name) + " : " + str(rq_faits[i][2].ref))
            s += "\n"
            for j, r in enumerate(element):
                s += "_" * space

                if type(r) == Concept:
                    s += "answer "+ str(j) + " ::  "+ str(r.name)+ " : "+ str(r.ref)
                    s += "\n"

                else:
                    s += "answer "+ str(j) + " ::  "+ str(r[0].name)+ " : "+ str(r[0].ref)  + "=>"+ str(r[1].name) + "=>"+ str(r[2].name) + " : "+ str(r[2].ref)
                s += "\n"
        render_multi_line_string(main_surface, init.font2, s, 20, 20, init.font2.size("A")[1], init.fun_answer_offset)

    else:
        main_surface.blit(init.font3.render("Null :d ", True, (255, 255, 255)), (50, 50))

    screen.blit(main_surface, (screen.get_width() * 0.2, screen.get_height() * 0.7))
    pygame.draw.rect(screen, (255, 255, 255), (screen.get_width() * 0.2, screen.get_height() * 0.7, screen.get_width() * 0.8, screen.get_height() * 0.3), 2)


def show_fun_answer_filter(screen, init):
    main_surface = pygame.Surface((screen.get_width() * 0.8, screen.get_height() * 0.3))
    main_surface.fill((50, 50, 50))

    array, premis_Y = update_relge_coordinates(init, init.fun_answer_filter, 20, 20)

    element_drwaned = []
    for obj in array:
        if not obj in element_drwaned:
            if type(obj) == Concept:
                pygame.draw.rect(main_surface, (255, 255, 255), (obj.x, obj.y + init.fun_answer_filter_offset, 20 + init.font2.size(obj.name + " : " + obj.ref)[0], 40), 2)
                main_surface.blit(init.font2.render((obj.name + " : " + obj.ref), True, (255, 255, 255)),
                                  (obj.x + (20 + init.font2.size(obj.name + " : " + obj.ref)[0]) / 2 - init.font2.size(obj.name + " : " + obj.ref)[0] / 2, obj.y + 10  + init.fun_answer_filter_offset))
            else:
                pygame.draw.rect(main_surface, (255, 255, 255), (obj.x, obj.y  + init.fun_answer_filter_offset, 20 + init.font2.size(obj.name)[0], 40), 2, 20)
                main_surface.blit(init.font2.render(obj.name, True, (255, 255, 255)), (obj.x + (20 + init.font2.size(obj.name)[0]) / 2 - init.font2.size(obj.name)[0] / 2, obj.y + 10  + init.fun_answer_filter_offset))

            element_drwaned.append(obj)
        draw_arc_intero(obj, init, (0, 0), main_surface, init.fun_answer_filter_offset)

    screen.blit(main_surface, (screen.get_width() * 0.2, screen.get_height() * 0.7))
    pygame.draw.rect(screen, (255, 255, 255), (screen.get_width() * 0.2, screen.get_height() * 0.7, screen.get_width() * 0.8, screen.get_height() * 0.3), 2)



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


def get_rects(bfn, init, x=0, y=0):
    offset = 0
    rects = []
    for element in bfn:
        if type(element) == Concept:
            rects.append(pygame.Rect(element.x + x, element.y + y + offset, 20 + init.font2.size(element.name + " : " + element.ref)[0], 40))
        elif type(element) == Relation:
            rects.append(pygame.Rect(element.x + x, element.y + y + offset, 20 + init.font2.size(element.name)[0], 40))
    return rects


def get_objs(bfn):
    objs = []
    for element in bfn:
        if type(element) == Concept and element not in objs:
            objs.append(element)
            continue
        elif type(element) == Relation and element not in objs:
            objs.append(element)
            continue
        for e in element:
            if type(e) == Concept and e not in objs:
                objs.append(e)
            elif type(e) == Relation and e not in objs:
                objs.append(e)
    return objs

def get_objs_and_rects(screen, array, init):
    objs_rect = []
    objs = []
    for element in array:
        if type(element) == Concept:
            objs.append(element)
            objs_rect.append(pygame.Rect(element.x + screen.get_width() * 0.05, element.y + screen.get_width() * 0.05 + init.make_bfn_offset, 20 + init.font2.size(element.name + " : " + element.ref)[0], 40))
        else:
            objs_rect.append(pygame.Rect(element.x + screen.get_width() * 0.05, element.y + screen.get_width() * 0.05 + init.make_bfn_offset, 20 + init.font2.size(element.name)[0], 40))
            objs.append(element)
    return objs, objs_rect


def objs_to_faits(contains):


    # list of concept and relation ++++> fait, concept esole
    contains_fillterd = []
    for element in contains:
        if type(element) == Concept and len(element.arcs) == 0 and len(element.arcs_back) == 0:
            contains_fillterd.append(element)
            continue
        elif type(element) == Concept and len(element.arcs) != 0:
            alone = False
            for relation in element.arcs:
                if relation in contains:
                    if relation.arcs[0] in contains:
                        fait = [element, relation, relation.arcs[0]]
                        if not fait in contains_fillterd: contains_fillterd.append(fait)
                    alone = True
                elif not alone and not element in contains_fillterd:
                    contains_fillterd.append(element)
    for element in contains:
        if type(element) == Concept and len(element.arcs) == 0 and len(element.arcs_back) != 0:
            not_in = False
            for sous_element in contains_fillterd:
                if type(sous_element) != Concept and element == sous_element[2]:
                    not_in = True
                    break
            if not not_in and not element in contains_fillterd:
                contains_fillterd.append(element)
    return contains_fillterd


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
                element.x = regle_x + 40
                element.y = regle_y
                if len(element.arcs) == 1:
                    element.arcs[0].x = element.x + 20 + 20 + 20 + init.font2.size(element.name + " : " + element.ref)[0]
                    element.arcs[0].y = element.y
                elif len(element.arcs) > 1:

                    for i in range(len(element.arcs)):
                        if i == 0:
                            element.arcs[i].x = element.x + 20 + 20 + 20 + init.font2.size(element.name + " : " + element.ref)[0]
                            element.arcs[i].y = element.y

                        elif i == 1:
                            element.arcs[i].x = element.x + 20 + 20 + 20 + init.font2.size(element.name + " : " + element.ref)[0]
                            element.arcs[i].y = element.y + max_y
                            max_y += 60
                        elif i > 1:
                            element.arcs[i].x = element.x + 20 + 20 + 20 + init.font2.size(element.name + " : " + element.ref)[0]
                            element.arcs[i].y = element.arcs[1].y + (i - 1) * 60
                            max_y += 60
            elif len(element.arcs_back) != 0:
                element.x = element.arcs_back[0].x + 20 + 80 + 20 + init.font2.size(element.name)[0]
                element.y = element.arcs_back[0].y
                if len(element.arcs) == 1:
                    element.arcs[0].x = element.x + 20 + 20 + 20 + init.font2.size(element.name + " : " + element.ref)[0]
                    element.arcs[0].y = element.y
                elif len(element.arcs) > 1:

                    for i in range(len(element.arcs)):
                        if i == 0:
                            element.arcs[i].x = element.x + 20 + 20 + 20 + init.font2.size(element.name + " : " + element.ref)[0]
                            element.arcs[i].y = element.y

                        elif i == 1:
                            element.arcs[i].x = element.x + 20 + 20 + 20 + init.font2.size(element.name + " : " + element.ref)[0]
                            element.arcs[i].y = element.y + max_y
                            max_y += 60
                        elif i > 1:
                            element.arcs[i].x = element.x + 20 + 20 + 20 + init.font2.size(element.name + " : " + element.ref)[0]
                            element.arcs[i].y = element.arcs[1].y + (i - 1) * 60
                            max_y += 60
            elif len(element.arcs_back) == 0:
                element.x = regle_x + 40
                element.y = regle_y + max_y
                max_y += 50
                if len(element.arcs) == 1:
                    element.arcs[0].x = element.x + 20 + 20 + 20 + init.font2.size(element.name + " : " + element.ref)[0]
                    element.arcs[0].y = element.y
                elif len(element.arcs) > 1:

                    for i in range(len(element.arcs)):
                        if i == 0:
                            element.arcs[i].x = element.x + 20 + 20 + 20 + init.font2.size(element.name + " : " + element.ref)[0]
                            element.arcs[i].y = element.y

                        elif i == 1:
                            element.arcs[i].x = element.x + 20 + 20 + 20 + init.font2.size(element.name + " : " + element.ref)[0]
                            element.arcs[i].y = element.y + max_y
                            max_y += 60
                        elif i > 1:
                            element.arcs[i].x = element.x + 20 + 20 + 20 + init.font2.size(element.name + " : " + element.ref)[0]
                            element.arcs[i].y = element.arcs[1].y + (i - 1) * 60
                            max_y += 60

    return array, max_y


def update_fait_coordinates_copy(array, x, y):
    corrected = []

    for element in array:
        if not element in corrected:
            element.x += x
            element.y += y
            corrected.append(element)
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
    i = 0
    for element in array:
        if type(element) == Concept and len(element.arcs) == 0 and len(element.arcs_back) == 0:
            printing = element.name + " : " + element.ref
            screen.blit(font.render(printing, True, (255, 255, 255)), (x, offset + y + font_size * i))
            i += 1
        elif type(element) == Concept and not len(element.arcs) == 0:
            for relation in element.arcs:
                printing = element.name + " : " + element.ref + " ==> " + relation.name + " ==> " + relation.arcs[0].name + " : " + relation.arcs[0].ref
                screen.blit(font.render(printing, True, (255, 255, 255)), (x, offset + y + font_size * i))
                i += 1


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


def render_multi_line_string(screen, font, text, x, y, fsize, offset):
    lines = text.splitlines()
    for i, l in enumerate(lines):
        screen.blit(font.render(l, 0, (255, 255, 255)), (x, y + offset + fsize * i))


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
    for element in init.bfn:
        if type(element) == Concept:
            if not element.ref in I and not element.ref == "*":
                I.append(element.ref)
                marqueurs_list.append([element.ref, element.name])
            if not element.name in concept_list:
                concept_list.append(element.name)
            for relation in element.arcs:
                signature = [element.name, relation.name, relation.arcs[0].name]
                if not signature in signatures_list:
                    signatures_list.append(signature)
        elif type(element) == Relation:
            if not element.name in relation_list:
                relation_list.append(element.name)

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


def Copy(arr):
    obj_new_id_dics = {}
    for element in arr:
        if type(element) == Concept:
            if element not in obj_new_id_dics:
                obj_new_id_dics[element] = copy.deepcopy(element)
        elif type(element) == Relation:
            if element not in obj_new_id_dics:
                obj_new_id_dics[element] = copy.deepcopy(element)

    new_arr = arr.copy()

    delete_relations = []
    for element in arr:
        if type(element) == Relation:
            if element.arcs[0] not in obj_new_id_dics or len(element.arcs) == 0:
                delete_relations.append(element)
                continue
            if element.arcs_back[0] not in obj_new_id_dics or len(element.arcs_back) == 0:
                delete_relations.append(element)
                continue
    for element in delete_relations:
        new_arr.remove(element)
        arr.remove(element)
        obj_new_id_dics.pop(element)
    for i, element in enumerate(arr):
        new_arr[i] = obj_new_id_dics[element]

        delete_arc = []
        for j, arcs in enumerate(element.arcs):
            if arcs not in obj_new_id_dics:
                if j + 1 < len(new_arr[i].arcs):
                    delete_arc.append(new_arr[i].arcs[j])
                    continue
            if arcs in obj_new_id_dics:
                new_arr[i].arcs[j] = obj_new_id_dics[arcs]
        for e in delete_arc:
            if e not in obj_new_id_dics:
                new_arr[i].arcs.remove(e)
        delete_arc = []
        for j, arcs_back in enumerate(element.arcs_back):
            if arcs_back not in obj_new_id_dics:
                if j + 1 < len(new_arr[i].arcs_back):
                    delete_arc.append(new_arr[i].arcs_back[j])
                    continue
            if arcs_back in obj_new_id_dics:
                new_arr[i].arcs_back[j] = obj_new_id_dics[arcs_back]
        for e in delete_arc:
            if e not in obj_new_id_dics:
                new_arr[i].arcs_back.remove(e)

    return new_arr


def Jointure(concept_1, concept_2, array):
    if concept_1.name != concept_2.name:
        return False, 0
    elif concept_1.ref != concept_2.ref:
        return False, 1
    else:
        concept_1.arcs += concept_2.arcs
        concept_1.arcs_back += concept_2.arcs_back
        for refernce in concept_2.arcs_back:
            refernce.arcs.remove(concept_2)
            refernce.arcs.append(concept_1)
        for refernce in concept_2.arcs:
            refernce.arcs_back.remove(concept_2)
            refernce.arcs_back.append(concept_1)
        array.remove(concept_2)
        return True, array


def Fragmentation(concept, array, init, screen):
    new_concept = Copy([concept])[0]
    for relation in concept.arcs:
        relation.arcs_back = [new_concept]
    new_concept.arcs = concept.arcs.copy()
    new_concept.arcs_back = []
    concept.arcs = []
    new_concept.x = init.mouse[0] - screen.get_width() * 0.05
    if init.intero_buttons["fragmentation"][1][0]:
        new_concept.y = init.mouse[1] - screen.get_width() * 0.05 - init.make_bfn_offset
    else:
        new_concept.y = init.mouse[1] - screen.get_width() * 0.05

    array.append(new_concept)


def Restriction(concept, ref):
    concept.ref = ref


def Restriction_1(concept_1, concept_2):
    concept_1.ref = concept_2.ref


def Projection(rq, bfn):

    for element in rq:
        if len(element.arcs_back) == 0:
            firist_rq = element
            break

    rq_faits = objs_to_faits(rq)
    bfn_faits = objs_to_faits(bfn)
    answers = [] * len(rq_faits)
    stop = False
    found_fait = False
    for i, element in enumerate(rq_faits):
        stop = False
        answer = []
        if type(element) != Concept:
            c1 = element[0]
            r1 = element[1]
            c2 = element[2]
            if c1.ref != "*" and c2.ref != "*":
                for e in bfn_faits:
                    if type(e) != Concept:
                        c1_2 = e[0]
                        r1_2 = e[1]
                        c2_2 = e[2]
                        if c1.name == c1_2.name and c2.name == c2_2.name and r1.name == r1_2.name and c1.ref == c1_2.ref and c2.ref == c2_2.ref:
                            found_fait = True
                            answer.append(e)
                            break
                if not found_fait:
                    stop = True
            elif c1.ref == "*" and c2.ref != "*":
                for e in bfn_faits:
                    if type(e) != Concept:
                        c1_2 = e[0]
                        r1_2 = e[1]
                        c2_2 = e[2]
                        if c1.name == c1_2.name and c2.name == c2_2.name and r1.name == r1_2.name and c1_2.ref != "*" and c2.ref == c2_2.ref:
                            found_fait = True
                            answer.append(e)
                if not found_fait:
                    stop = True
            elif c2.ref == "*" and c1.ref != "*":
                for e in bfn_faits:
                    if type(e) != Concept:
                        c1_2 = e[0]
                        r1_2 = e[1]
                        c2_2 = e[2]
                        # if c1.name == c1_2.name and c2.name == c2_2.name and r1.name == r1_2.name and c1.ref == c1_2.ref and c2_2.ref != "*":
                        if c1.name == c1_2.name:
                            if c2.name == c2_2.name:
                                if r1.name == r1_2.name:
                                    if c1.ref == c1_2.ref:
                                        if c2_2.ref != "*":
                                            found_fait = True
                                            answer.append(e)
                if not found_fait:
                    stop = True
            elif c2.ref == "*" and c1.ref == "*":
                for e in bfn_faits:
                    if type(e) != Concept:
                        c1_2 = e[0]
                        r1_2 = e[1]
                        c2_2 = e[2]
                        if c1.name == c1_2.name and c2.name == c2_2.name and r1.name == r1_2.name and "*" != c1_2.ref and c2_2.ref != "*":
                            found_fait = True
                            answer.append(e)
                if not found_fait:
                    stop = True

        elif type(element) == Concept:
            if element.ref != "*":
                for e in bfn:
                    if type(e) == Concept:
                        if element.name == e.name and e.ref != "*":
                            found_fait = True
                            answer.append(e)
                            break
                if not found_fait:
                    stop = True
            else:
                for e in bfn:
                    if type(e) == Concept:
                        if element.name == e.name and e.ref != "*":
                            found_fait = True
                            answer.append(e)
                if not found_fait:
                    stop = True
        if stop or len(answer) == 0: return False
        answers.append(answer)


    return answers


def Simplification(arr):
    arr = objs_to_faits(arr)

    stop = False
    while not stop:
        for element in arr:
            delete_arr = []
            found = False
            for e in arr:
                if type(element) == type(e) == Concept:
                    if element.name == e.name and element != e:
                        delete_arr.append(e)
                        found = True
                elif type(element) != type(e) and type(e) == Concept and element != e:
                    if (element[0].name == e.name and element[0].ref == e.ref) or (element[2].name == e.name and element[2].ref == e.ref):
                        delete_arr.append(e)
                        found = True
                elif type(element) == type(e):
                    if element != e and element[0].name == e[0].name and element[0].ref == e[0].ref and element[1].name == e[1].name and element[2].name == e[2].name and element[2].ref == e[2].ref:
                        delete_arr.append(e)
                        found = True
            if found:
                break
        if found:
            for element in delete_arr:
                arr.remove(element)
        if not found:
            stop = True
    arr = get_objs(arr)
    return arr


def filter_answers(answers):
    for i, element in enumerate(answers):
        print(i)
        for j, e in enumerate(element):
            if type(e) == Concept:
                pass
            else:
                pass
            print(" " * 10, j)
            print(e)

    i = 0
    lines = []
    while i <= len(answers):
        delete_answer = []
        if len(answers) > 1:
            for element in answers[i]:
                found = False

                for next_element in answers[i + 1]:
                    if element[-1] == next_element[0]:
                        found = True

                if not found:
                    delete_answer.append(element)
            for r in delete_answer:
                answers[i].remove(r)
        i += 1
        if i+1 == len(answers): break

    l = []
    for i, element in enumerate(answers):
        print(i)
        for j, e in enumerate(element):
            l.append(e)
    join = False
    stop = False
    while not stop:
        join_element = []
        join = False
        for element in l:
            for e in l:
                if e != element and element[0] == e[-1]:
                    join = True
                    join_element = [l.index(e), l.index(element)]
                    break
            if join: break
        if join:
            dont_know = False
            for p, ja in enumerate(l):
                if l[join_element[0]][-1] == ja[0] and p != join_element[0]:
                    if not dont_know:
                        dont_know = True
                        continue
                    a = []
                    for k in l[join_element[0]]:
                        a.append(k)
                    l.append(a)
                    break
            for k in l[join_element[1]][1:]:
                l[join_element[0]].append(k)
            l.pop(join_element[1])
        if not join: stop = True
    print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
    k = []
    for i in l:
        print(i)
        k.append(Copy(i))

    answers_obj = get_objs(k)

    return answers_obj, l


def chainge_avant(init):
    print("chainage avant")
    stop = False
    add_conclusion_all = []
    while not stop:
        add_conclusion = []
        regle_applique = False
        for regle in init.br_main_list:

            result = Projection(regle["premise"], init.BFN)
            if result != False:
                result = filter_answers(result)[1]
                if len(result) != 0:
                    conclusion = regle["conclusion"]
                    if type(conclusion) != Concept:
                        for answer in result:
                            conclusion_copy = Copy(conclusion)
                            for element in conclusion_copy:
                                if type(element) == Concept and element.ref == "*":
                                    for ans in answer:
                                        if ans.name == element.name:
                                            Restriction_1(element, ans)
                                            break
                            in_this_same = False
                            for same in add_conclusion_all:
                                if len(same) == len(conclusion_copy):
                                    added = True
                                    for index, s in enumerate(same):
                                        if type(s) == Concept:
                                            if not (same[index].name == conclusion_copy[index].name and same[index].ref == conclusion_copy[index].ref):
                                                added = False
                                                break
                                        else:
                                            if not (same[index].name == conclusion_copy[index].name):
                                                added = False
                                                break
                                    if added:
                                        in_this_same = True
                                if in_this_same:
                                    break
                            if not in_this_same:
                                add_conclusion_all.append(conclusion_copy)
                                add_conclusion.append(conclusion_copy)
                                regle_applique = True


        if regle_applique:
            for add in add_conclusion:
                if type(add) != Concept:
                    for a in add:
                        init.BFN.append(a)
            init.BFN = Simplification(init.BFN)
            for concept_1 in init.BFN:
                if type(concept_1) == Concept:
                    for concept_2 in init.BFN:
                        if type(concept_2) == Concept and concept_1 != concept_2 and concept_1.name == concept_2.name and concept_1.ref == concept_2.ref:
                            init.BFN = Jointure(concept_1, concept_2, init.BFN)[1]
        else:
            stop = True



