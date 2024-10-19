import pygame
from math import *
import random
import time
from pygame.locals import *

pygame.init()

# 全局变量:

FPS = 60
# 由于假设只在Windows系统上运行该游戏，直接使用了Windows文件路径格式
# operator_image = pygame.image.load(r"C:\Users\86182\Desktop\weapon_gun_image.png")

# operator_left_image = pygame.image.load(r"C:\Users\10131\Desktop\operator_left_image.png")
# operator_right_image = pygame.image.load(r"C:\Users\10131\Desktop\operator_right_image.png")
# enemy_test_image = pygame.image.load(r"C:\Users\10131\Desktop\enemy_test_image.png")
# weapon_gun_image_right = pygame.image.load(r"C:\Users\10131\Desktop\weapon_gun_image_right.png")
# weapon_gun_image_left = pygame.image.load(r"C:\Users\10131\Desktop\weapon_gun_image_left.png")
# enemy_test_body_image = pygame.image.load(r"C:\Users\10131\Desktop\enemy_test_body_image.png")
# attacking_mod_switch_image = pygame.image.load(r"C:\Users\10131\Desktop\attacking_mod_switch_image.png")
# weapon_sword_image_right = pygame.image.load(r"C:\Users\10131\Desktop\weapon_sword_image_right.png")
# weapon_sword_image_left = pygame.image.load(r"C:\Users\10131\Desktop\weapon_sword_image_left.png")
# prop_explosive_image = pygame.image.load(r"C:\Users\10131\Desktop\prop_explosive.png")
# prop_explosive_effect_image = pygame.image.load(r"C:\Users\10131\Desktop\prop_explosive_effect.png")

# operator_left_image = pygame.transform.scale(pygame.image.load(r"C:\Users\86182\Desktop\operator_left_image.png"), (100, 100))
# enemy_test_image = pygame.transform.scale(pygame.image.load(r"C:\Users\86182\Desktop\enemy_test_image.png"), (100, 100))
# enemy_test_body_image = pygame.transform.scale(pygame.image.load(r"C:\Users\86182\Desktop\enemy_test_body_image.png"), (75, 75))
# enemy_test_body_image_rotated = []
# for temp_degree in range(10):
# enemy_test_body_image_rotated.append(pygame.transform.rotate(enemy_test_body_image, random.randrange(0, 360)))
# attacking_mod_switch_image = pygame.transform.scale(pygame.image.load(r"C:\Users\86182\Desktop\attacking_mod_switch_image.png"), (75, 50))
# prop_explosive_image = pygame.transform.scale(pygame.image.load(r"C:\Users\86182\Desktop\prop_explosive.png"), (100, 125))
# prop_explosive_effect_image = pygame.image.load(r"C:\Users\86182\Desktop\prop_explosive_effect.png")
# prop_explosive_effect_image = []
# for temp_i in range(8):
# prop_explosive_effect_image.append(pygame.transform.scale(pygame.image.load(r"C:\Users\86182\Desktop\IMG0000" + str(temp_i) + ".bmp"), (100, 100)))
# tomb_image = pygame.transform.scale(pygame.image.load(r"C:\Users\86182\Desktop\tomb.png"), (100, 100))

# pygame.mouse.set_visible(False)
# root_loc_for_images = r"C:\Users\10131\Desktop\photos_for_game"
root_loc_for_images = r"photos_for_game"
str_operator_left_image = root_loc_for_images + r"\operator_left_image.png"
str_enemy_test_image = root_loc_for_images + r"\enemy_test_image.png"
str_test_body_image = root_loc_for_images + r"\enemy_test_body_image.png"
str_attacking_mod_switch = root_loc_for_images + r"\attacking_mod_switch_image.png"
str_prop_explosive_effect_image = root_loc_for_images + r"\prop_explosive.png"
operator_left_image = pygame.transform.scale(pygame.image.load(str_operator_left_image), (100, 75))
enemy_test_image = pygame.transform.scale(pygame.image.load(str_enemy_test_image), (100, 75))
enemy_test_body_image = pygame.transform.scale(pygame.image.load(str_test_body_image), (75, 75))
enemy_test_body_image_rotated = []
for temp_degree in range(10):
    enemy_test_body_image_rotated.append(pygame.transform.rotate(enemy_test_body_image, random.randrange(0, 360)))
attacking_mod_switch_image = pygame.transform.scale(pygame.image.load(str_attacking_mod_switch), (75, 50))
prop_explosive_image = pygame.transform.scale(pygame.image.load(str_prop_explosive_effect_image), (100, 125))
# prop_explosive_effect_image = pygame.image.load(r"C:\Users\86182\Desktop\prop_explosive_effect.png")
prop_explosive_effect_image = []
for temp_i in range(8):
    prop_explosive_effect_image.append(
        pygame.transform.scale(pygame.image.load(root_loc_for_images + r"\IMG0000" + str(temp_i) + ".bmp"), (100, 100)))
tomb_image = pygame.transform.scale(pygame.image.load(root_loc_for_images + r"\tomb.png"), (100, 100))
tree_image = pygame.transform.scale(pygame.image.load(root_loc_for_images + r"\prop_tree.png"), (100, 100))
stone_image = pygame.transform.scale(pygame.image.load(root_loc_for_images + r"\prop_stone.png"), (100, 100))

window_width = 1200
window_height = 800
window = pygame.display.set_mode((window_width, window_height))  # 设置display窗口对象的基本属性，如size(width, height)
operator_width = 100
operator_height = 100
enemy_test_width = 100
enemy_test_height = 100
moving_speed = 3
# ground_location = 350
max_bullets = 10
velocity = 20
# odd_num_list = []
falling_speed = 0.1
jumping_height = 10
hit_back = 10
hit_range = 100
explosive_num = 2
velocity_ = 1.2
'''ground_start = [100, 200, 300]
ground_end = [200, 300, 400]
ground_loc = [ground_location - 50, ground_location - 100, ground_location - 50]'''

enemy_test_hit = pygame.USEREVENT + 1
blocked = pygame.USEREVENT + 900

createVar = locals()
myVarList = []
for i in range(explosive_num):
    createVar['prop_hit_' + str(i)] = i
    myVarList.append(createVar['prop_hit_' + str(i)])
    myVarList[i] = pygame.USEREVENT + (i + 2)
createVar_1 = locals()
myVarList_1 = []
for i in range(10):
    createVar_1['any' + str(i)] = i
    myVarList_1.append(createVar_1['any' + str(i)])
    myVarList_1[i] = pygame.USEREVENT + (i + 100)

timer_explosive = []


class Character(object):

    def __init__(self, health, status, starting_x, starting_y, width, height, attacking_mod):
        self.health = health
        self.status = status
        self.x = starting_x
        self.y = starting_y
        self.width = width
        self.height = height
        self.attacking_mod = attacking_mod

    def attacking_mod_switch(self, temp):
        self.attacking_mod = temp


class Bonus(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


class SceneProp(object):

    def __init__(self, x, y, width, height, death_effect):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.death_effect = death_effect
        self.health = 5

    def hit_handle(self):
        self.health -= 1


class Enemy(object):

    def __init__(self, x, y, width, height, death_effect):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.death_effect = death_effect
        self.health = 10

    def hit_handle(self):
        self.health -= 1


def explosion_handle(explosive, timer_1):
    if timer_1 in range(10):
        temp_1 = 0
        window.blit(prop_explosive_effect_image[temp_1], (explosive.x, explosive.y))
    elif timer_1 in range(10, 20):
        temp_1 = 1
        window.blit(prop_explosive_effect_image[temp_1], (explosive.x, explosive.y))
    elif timer_1 in range(20, 30):
        temp_1 = 2
        window.blit(prop_explosive_effect_image[temp_1], (explosive.x, explosive.y))
    elif timer_1 in range(30, 40):
        temp_1 = 3
        window.blit(prop_explosive_effect_image[temp_1], (explosive.x, explosive.y))
    elif timer_1 in range(40, 50):
        temp_1 = 4
        window.blit(prop_explosive_effect_image[temp_1], (explosive.x, explosive.y))
    elif timer_1 in range(50, 60):
        temp_1 = 5
        window.blit(prop_explosive_effect_image[temp_1], (explosive.x, explosive.y))
    elif timer_1 in range(60, 70):
        temp_1 = 6
        window.blit(prop_explosive_effect_image[temp_1], (explosive.x, explosive.y))
    elif timer_1 in range(70, 80):
        temp_1 = 7
        window.blit(prop_explosive_effect_image[temp_1], (explosive.x, explosive.y))
    else:
        window.blit(enemy_test_body_image_rotated[explosive.death_effect], (explosive.x, explosive.y))


def operator_direction(enemy_num, bullets_type_a, operator_x, operator_y, current_image, enemy_list, enemy_class_list,
                       operator, attacking_mod_switch, explosive_list):
    global timer_explosive
    window.fill((254, 250, 238))
    x, y = pygame.mouse.get_pos()
    angle = atan2(y - operator_y, x - operator_x)  # 两点间线段的弧度值
    angle_degree = degrees(angle)  # 弧度转角度
    '''operator = pygame.transform.rotate(operator_image, -angle_degree)'''

    # for each in range(6):
    # window.blit(tree_image, (100 + 100 * each, 100))
    window.blit(stone_image, (400, 400))

    for bullet in bullets_type_a:
        pygame.draw.rect(window, (255, 255, 0), bullet[0])

    if operator.attacking_mod == 0:
        weapon_gun = pygame.transform.rotate(operator_left_image, - angle_degree)
        window.blit(weapon_gun, (operator_x, operator_y))
    elif operator.attacking_mod == 1:
        weapon_gun = pygame.transform.rotate(operator_left_image, - angle_degree)
        window.blit(weapon_gun, (operator_x, operator_y))

    for each_explosive in range(explosive_num):
        if explosive_list[each_explosive].health > 0:
            window.blit(prop_explosive_image, (explosive_list[each_explosive].x, explosive_list[each_explosive].y))
        else:
            timer_explosive[each_explosive] += 1
            explosion_handle(explosive_list[each_explosive], timer_explosive[each_explosive])

    if operator.attacking_mod == 1:
        window.blit(attacking_mod_switch_image, (attacking_mod_switch.x, attacking_mod_switch.y))

    for each in range(enemy_num):
        angle_ = atan2(operator.y - enemy_list[each].y, operator.x - enemy_list[each].x)  # 两点间线段的弧度值
        angle_degree_ = degrees(angle_)  # 弧度转角度

        if enemy_class_list[each].health:
            enemy_test_image_ = pygame.transform.rotate(enemy_test_image, - angle_degree_)
            window.blit(enemy_test_image_, (enemy_list[each].x, enemy_list[each].y))
            pygame.draw.rect(window, (0, 255, 0), (enemy_list[each].x, enemy_list[each].y - 5, 40, 8))  # 失去的生命值
            pygame.draw.rect(window, (255, 0, 0),
                             (enemy_list[each].x + enemy_class_list[each].health * 4, enemy_list[each].y - 10,
                              40 - enemy_class_list[each].health * 4, 8))
        else:
            window.blit(tomb_image, (enemy_list[each].x, enemy_list[each].y))

    '''pygame.draw.line(window, (255, 0, 0,), (0, ground_location + operator_height),
                     (window_width, ground_location + operator_height))'''

    pygame.display.update()


def get_explosive_random_loc():
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    return x, y


def bullet_operation(bullets_type_a, operator_x, operator_y, enemy_list, explosive_rect, stone, stone_rect):
    for bullet_item in bullets_type_a:
        x = bullet_item[1]
        y = bullet_item[2]
        angle = atan2(y - operator_y, x - operator_x)  # 两点间线段的弧度值
        angle_degree = degrees(angle)  # 弧度转角度

        if 0 <= - angle_degree <= 90:
            arc = atan2(operator_y - y, x - operator_x)
            bullet_item[0].x += velocity * cos(arc)
            bullet_item[0].y -= velocity * sin(arc)
            each = 0
            for enemy_test in enemy_list:
                if enemy_test.colliderect(bullet_item[0]):
                    try:
                        pygame.event.post(pygame.event.Event(myVarList_1[each]))
                        bullets_type_a.remove(bullet_item)
                    except ValueError:
                        pass
                each += 1
            for temp_j in range(explosive_num):
                if explosive_rect[temp_j].colliderect(bullet_item[0]):
                    pygame.event.post(pygame.event.Event(myVarList[temp_j]))
                    bullets_type_a.remove(bullet_item)
            if stone_rect.colliderect(bullet_item[0]):
                try:
                    bullets_type_a.remove(bullet_item)
                except ValueError:
                    pass

        if 90 < - angle_degree <= 180:
            arc = atan2(operator_y - y, operator_x - x)
            bullet_item[0].x -= velocity * cos(arc)
            bullet_item[0].y -= velocity * sin(arc)
            each = 0
            for enemy_test in enemy_list:
                if enemy_test.colliderect(bullet_item[0]):
                    pygame.event.post(pygame.event.Event(myVarList_1[each]))
                    try:
                        bullets_type_a.remove(bullet_item)
                    except ValueError:
                        pass
                each += 1
            for temp_j in range(explosive_num):
                if explosive_rect[temp_j].colliderect(bullet_item[0]):
                    pygame.event.post(pygame.event.Event(myVarList[temp_j]))
                    try:
                        bullets_type_a.remove(bullet_item)
                    except ValueError:
                        pass
            if stone_rect.colliderect(bullet_item[0]):
                try:
                    bullets_type_a.remove(bullet_item)
                except ValueError:
                    pass

        if - 90 <= - angle_degree < 0:
            arc = atan2(y - operator_y, x - operator_x)
            bullet_item[0].x += velocity * cos(arc)
            bullet_item[0].y += velocity * sin(arc)
            each = 0
            for enemy_test in enemy_list:
                if enemy_test.colliderect(bullet_item[0]):
                    pygame.event.post(pygame.event.Event(myVarList_1[each]))
                    try:
                        bullets_type_a.remove(bullet_item)
                    except ValueError:
                        pass
                each += 1
            for temp_j in range(explosive_num):
                if explosive_rect[temp_j].colliderect(bullet_item[0]):
                    pygame.event.post(pygame.event.Event(myVarList[temp_j]))
                    try:
                        bullets_type_a.remove(bullet_item)
                    except ValueError:
                        pass
            if stone_rect.colliderect(bullet_item[0]):
                bullets_type_a.remove(bullet_item)

        if - 180 < - angle_degree < - 90:
            arc = atan2(y - operator_y, operator_x - x)
            bullet_item[0].x -= velocity * cos(arc)
            bullet_item[0].y += velocity * sin(arc)
            each = 0
            for enemy_test in enemy_list:
                if enemy_test.colliderect(bullet_item[0]):
                    pygame.event.post(pygame.event.Event(myVarList_1[each]))
                    try:
                        bullets_type_a.remove(bullet_item)
                    except ValueError:
                        pass
                each += 1
            for temp_j in range(explosive_num):
                if explosive_rect[temp_j].colliderect(bullet_item[0]):
                    pygame.event.post(pygame.event.Event(myVarList[temp_j]))
                    try:
                        bullets_type_a.remove(bullet_item)
                    except ValueError:
                        pass
            if stone_rect.colliderect(bullet_item[0]):
                bullets_type_a.remove(bullet_item)


def death_handle(enemy_test_health):
    if enemy_test_health <= 0:
        return False
    return True


'''def ground_loc_variable(operator):
    if ground_start[0] <= operator.x <= ground_end[0]:
        return ground_loc[0]
    if ground_start[1] <= operator.x <= ground_end[1]:
        return ground_loc[1]
    if ground_start[2] <= operator.x <= ground_end[2]:
        return ground_loc[2]'''

'''def gravity_and_jump_handle(keys, key_type, is_jumping, time_interval, operator):
    if key_type:
        is_jumping = True
    if is_jumping:
        if time_interval >= - jumping_height:
            gravity = 0.5
            if time_interval < 0:
                gravity = - 0.5
            operator.y -= 0.5 * gravity * (time_interval ** 2)
            time_interval -= 0.5
        else:
            operator.y = ground_location
            is_jumping = False
            time_interval = jumping_height
    return keys, is_jumping, time_interval, operator'''


def get_start_point():
    temp_rand = random.randrange(0, 4)
    if temp_rand == 0:
        start_x = random.randrange(-100, window_width + 100)
        start_y = random.randrange(-100, 0)
    if temp_rand == 1:
        start_x = random.randrange(-100, window_width + 100)
        start_y = random.randrange(window_height, window_height + 100)
    if temp_rand == 2:
        start_x = random.randrange(-100, 0)
        start_y = random.randrange(-100, window_height + 100)
    if temp_rand == 3:
        start_x = random.randrange(window_width, window_width + 100)
        start_y = random.randrange(-100, window_height + 100)
    return start_x, start_y


def collider_check(operator, blit_loc):
    for each in blit_loc:
        if each[0] - 125 < operator.x < each[0] + 125 and each[1] - 125 < operator.y < each[1] + 125:
            return False
    return True


def enemy_movement_handle(enemy_list, operator, enemy_class_list):
    each = 0
    for enemy in enemy_list:
        if enemy_class_list[each].health > 0:
            angle = atan2(operator.y - enemy.y, operator.x - enemy.x)  # 两点间线段的弧度值
            angle_degree = degrees(angle)  # 弧度转角度

            if 0 <= - angle_degree <= 90:
                arc = atan2(enemy.y - operator.y, operator.x - enemy.x)
                enemy.x += velocity_ * cos(arc)
                enemy.y -= velocity_ * sin(arc)
                '''for prop in explosive_rect_list:
                    if enemy.colliderect(prop):
                        enemy_list.remove(enemy)'''

            if 90 < - angle_degree <= 180:
                arc = atan2(enemy.y - operator.y, enemy.x - operator.x)
                enemy.x -= velocity_ * cos(arc)
                enemy.y -= velocity_ * sin(arc)

            if - 90 <= - angle_degree < 0:
                arc = atan2(operator.y - enemy.y, operator.x - enemy.x)
                enemy.x += velocity_ * cos(arc)
                enemy.y += velocity_ * sin(arc)

            if - 180 < - angle_degree < - 90:
                arc = atan2(operator.y - enemy.y, enemy.x - operator.x)
                enemy.x -= velocity_ * cos(arc)
                enemy.y += velocity_ * sin(arc)

        each += 1


def round_test(enemy_class_list, enemy_num):
    count = 0
    for each in enemy_class_list:
        if each.health <= 0:
            count += 1
    if count == enemy_num:
        return True
    else:
        return False


def main():
    enemy_num = 0
    global_count = 0
    operator = Character(10, True, 200, 350, operator_width, operator_height, 1)  # attacking_mod == 0 为远程
    while True:
        enemy_num = global_count
        global global_timer
        global_timer = 0
        global timer_explosive

        createVar_1 = locals()
        for temp_name in range(explosive_num):
            createVar_1['timer_' + str(temp_name + 1)] = temp_name
            timer_explosive.append(createVar_1['timer_' + str(temp_name + 1)])
            timer_explosive[temp_name] = 0

        attacking_mod_switch = Bonus(200, 0, 50, 0)

        createVar_2 = locals()
        explosive_list = []
        blit_loc = []
        for temp_name in range(explosive_num):
            createVar_2['explosive_' + str(temp_name + 1)] = temp_name
            explosive_list.append(createVar_2['timer_' + str(temp_name + 1)])
            while True:
                start_x, start_y = get_explosive_random_loc()
                k = 0
                for each in blit_loc:
                    k += 1
                    if each[0] - 125 < start_x < each[0] + 125 and each[1] - 125 < start_y < each[1] + 125:
                        break
                if k == len(blit_loc):
                    break
            blit_loc.append((start_x, start_y))
            explosive_list[temp_name] = SceneProp(start_x, start_y, 100, 125, random.randrange(0, 9))

        '''explosive = SceneProp(100, 100, 50, 50, 0)
        explosive_1 = SceneProp(200, 100, 50, 50, 0)'''

        '''time_interval_operator = jumping_height
        is_jumping_operator = False

        time_interval_enemy_test = jumping_height
        is_jumping_enemy_test = False'''

        current_image = operator_left_image
        bullets_type_a = []

        # 创建敌人的实体类：
        enemy_class_list = []
        createVar_5 = locals()
        for each in range(enemy_num):
            createVar_5['enemy_class' + str(each + 1)] = each
            enemy_class_list.append(createVar_5['enemy_class' + str(each + 1)])
        for each in range(enemy_num):
            x, y = get_start_point()
            enemy_class_list[each] = Enemy(x, y, enemy_test_width, enemy_test_height, 1)

        # 创建敌人的精灵类：
        enemy_list = []
        createVar_4 = locals()
        for each in range(enemy_num):
            createVar_4['enemy_' + str(each + 1)] = each
            enemy_list.append(createVar_4['enemy_' + str(each + 1)])
        for each in range(enemy_num):
            enemy_list[each] = pygame.Rect(enemy_class_list[each].x, enemy_class_list[each].y, enemy_test_width,
                                           enemy_test_height)

        operator_rect = pygame.Rect(100, 350, operator_width, operator_height)

        createVar_3 = locals()
        explosive_rect_list = []
        for temp_name in range(explosive_num):
            createVar_3['explosive_rect_' + str(temp_name + 1)] = temp_name
            explosive_rect_list.append(createVar_3['explosive_rect_' + str(temp_name + 1)])
        for temp_name_1 in range(explosive_num):
            explosive_rect_list[temp_name_1] = pygame.Rect(explosive_list[temp_name_1].x, explosive_list[temp_name_1].y,
                                                           explosive_list[temp_name_1].width,
                                                           explosive_list[temp_name_1].height)

        stone = SceneProp(400, 400, stone_image.get_width(), stone_image.get_height(), 1)
        stone_rect = pygame.Rect(400, 400, stone_image.get_width(), stone_image.get_height())

        clock = pygame.time.Clock()  # pygame的时钟函数，用来确保在任何设备上循环运行频率均是FPShz（FPS = 60）
        run = True
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():  # 收集所有的事件
                if event.type == pygame.QUIT:  # 关闭窗口
                    run = False
                    pygame.quit()

                if event.type == blocked:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN and operator.attacking_mod == 0:
                    if pygame.mouse.get_pressed(3):
                        bullet = pygame.Rect(operator.x + current_image.get_width() // 2,
                                             operator.y + current_image.get_height() // 2, 15, 15)
                        x, y = pygame.mouse.get_pos()
                        bullets_type_a.append([bullet, x, y])

                for each in range(enemy_num):
                    try:
                        if event.type == myVarList_1[each] and enemy_class_list[each].health > 0:
                            enemy_class_list[each].health -= 1

                            angle = atan2(operator.y - enemy_list[each].y, operator.x - enemy_list[each].x)  # 两点间线段的弧度值
                            angle_degree = degrees(angle)  # 弧度转角度
                            velocity_1 = 10

                            if 0 <= - angle_degree <= 90:
                                arc = atan2(enemy_list[each].y - operator.y, operator.x - enemy_list[each].x)
                                enemy_list[each].x -= velocity_1 * cos(arc)
                                enemy_list[each].y += velocity_1 * sin(arc)

                            if 90 < - angle_degree <= 180:
                                arc = atan2(enemy_list[each].y - operator.y, enemy_list[each].x - operator.x)
                                enemy_list[each].x += velocity_1 * cos(arc)
                                enemy_list[each].y += velocity_1 * sin(arc)

                            if - 90 <= - angle_degree < 0:
                                arc = atan2(operator.y - enemy_list[each].y, operator.x - enemy_list[each].x)
                                enemy_list[each].x -= velocity_1 * cos(arc)
                                enemy_list[each].y -= velocity_1 * sin(arc)

                            if - 180 < - angle_degree < - 90:
                                arc = atan2(operator.y - enemy_list[each].y, enemy_list[each].x - operator.x)
                                enemy_list[each].x += velocity_1 * cos(arc)
                                enemy_list[each].y -= velocity_1 * sin(arc)
                            # enemy_list[each].x -= hit_back
                    except IndexError:
                        pass

                for each_event in range(explosive_num):
                    if event.type == myVarList[each_event] and explosive_list[each_event].health > 0:
                        explosive_list[each_event].hit_handle()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e and attacking_mod_switch.x < operator.x < attacking_mod_switch.x + \
                            attacking_mod_switch.width:
                        operator.attacking_mod_switch(0)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        pygame.event.post(pygame.event.Event(blocked))
                        global_count += 1

            if attacking_mod_switch.y <= 350:
                attacking_mod_switch.y += 1

            enemy_movement_handle(enemy_list, operator, enemy_class_list)

            try:
                keys_get_pressed = pygame.key.get_pressed()  # 收集键盘给出的“长按”操作
                if keys_get_pressed[pygame.K_d]:
                    operator.x += moving_speed
                if keys_get_pressed[pygame.K_a]:
                    operator.x -= moving_speed
                if keys_get_pressed[pygame.K_w]:
                    operator.y -= moving_speed
                if keys_get_pressed[pygame.K_s]:
                    operator.y += moving_speed
            except pygame.error:
                pass

            '''if keys_get_pressed[pygame.K_RIGHT]:
                enemy_test.x += moving_speed
            if keys_get_pressed[pygame.K_LEFT]:
                enemy_test.x -= moving_speed
            if keys_get_pressed[pygame.K_UP]:
                enemy_test.y -= moving_speed
            if keys_get_pressed[pygame.K_DOWN]:
                enemy_test.y += moving_speed'''

            '''keys, is_jumping_operator, time_interval_operator, operator = \
                gravity_and_jump_handle(keys, keys[pygame.K_SPACE], is_jumping_operator, time_interval_operator, operator)
            keys, is_jumping_enemy_test, time_interval_enemy_test, enemy_test = \
                gravity_and_jump_handle(keys, keys[pygame.K_j], is_jumping_enemy_test, time_interval_enemy_test, enemy_test)'''

            '''for temp in odd_num_list:
                operator.y += odd_num_list[temp] * falling_speed
                if operator.y >= 100:
                    break'''

            operator_direction(enemy_num, bullets_type_a, operator.x, operator.y, current_image, enemy_list,
                               enemy_class_list, operator, attacking_mod_switch, explosive_list)  # 带入相应函数执行

            if operator.attacking_mod == 0:
                bullet_operation(bullets_type_a, operator.x, operator.y, enemy_list, explosive_rect_list, stone,
                                 stone_rect)

            global_timer += 1
            print(global_timer // 60)

            '''if round_test(enemy_class_list, enemy_num):
                pygame.event.post(pygame.event.Event(blocked))
                global_count += 1'''


main()

if __name__ == "__main__":
    main()
