import re
from numpy import number
import pygame
import os
import file_parsing

#SOLUTION VISUALIZATION
WIDTH, HEIGHT = 1100 , 750
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Solution Visualization - Traffic Signaling")
back_ground = pygame.image.load(os.path.join('images', '0.png'))
FPS = 60

# cars
CAR_WIDTH = 70
CAR_HEIGHT = 70
CAR_IMAGE = pygame.image.load(os.path.join('images', 'car.png'))
CAR_IMAGE = pygame.transform.scale(CAR_IMAGE, (CAR_WIDTH,CAR_HEIGHT))

CAR_AMESTERDAM =  pygame.transform.flip(pygame.transform.scale(CAR_IMAGE, (CAR_WIDTH,CAR_HEIGHT)), True, False)
CAR_ROMA = pygame.transform.flip(pygame.transform.scale(CAR_IMAGE, (CAR_WIDTH,CAR_HEIGHT)), True, False)
CAR_ATHENES = pygame.transform.rotate(pygame.transform.scale(CAR_IMAGE, (CAR_WIDTH,CAR_HEIGHT)),90)
CAR_LONDON = pygame.transform.rotate(pygame.transform.scale(CAR_IMAGE, (CAR_WIDTH,CAR_HEIGHT)),90)
CAR_MOSCOW = pygame.transform.rotate(pygame.transform.scale(CAR_IMAGE, (CAR_WIDTH,CAR_HEIGHT)),-45)

# streets
STREET_WIDTH = 60
STREET_HEIGHT = 450
STREET_HEIGHT_OBLIQUE = 700
STREET_IMAGE = pygame.image.load(os.path.join('images', 'street_2.webp'))

STREET_AMESTERDAM_IMAGE = pygame.transform.rotate(pygame.transform.scale(STREET_IMAGE, (STREET_WIDTH,STREET_HEIGHT)),90)
STREET_ROMA_IMAGE = pygame.transform.rotate(pygame.transform.scale(STREET_IMAGE, (STREET_WIDTH,STREET_HEIGHT)),90)
STREET_ATHENAS_IMAGE = pygame.transform.scale(STREET_IMAGE, (STREET_WIDTH,STREET_HEIGHT))
STREET_LONDON_IMAGE = pygame.transform.scale(STREET_IMAGE, (STREET_WIDTH,STREET_HEIGHT))
STREET_MOSCOW_IMAGE = pygame.transform.rotate(pygame.transform.scale(STREET_IMAGE, (STREET_WIDTH,STREET_HEIGHT_OBLIQUE)),45)

# intersections
INTERSECTION_WIDTH = 100
INTERSECTION_HEIGHT = 100

INTERSECTION_IMAGE_0 = pygame.image.load(os.path.join('images', 'intersection_0.png'))
INTERSECTION_IMAGE_0 = pygame.transform.scale(INTERSECTION_IMAGE_0, (INTERSECTION_WIDTH,INTERSECTION_HEIGHT))

INTERSECTION_IMAGE_1 = pygame.image.load(os.path.join('images', 'intersection_1.png'))
INTERSECTION_IMAGE_1 = pygame.transform.scale(INTERSECTION_IMAGE_1, (INTERSECTION_WIDTH,INTERSECTION_HEIGHT))

INTERSECTION_IMAGE_2 = pygame.image.load(os.path.join('images', 'intersection_2.png'))
INTERSECTION_IMAGE_2 = pygame.transform.scale(INTERSECTION_IMAGE_2, (INTERSECTION_WIDTH,INTERSECTION_HEIGHT))

INTERSECTION_IMAGE_3 = pygame.image.load(os.path.join('images', 'intersection_3.png'))
INTERSECTION_IMAGE_3 = pygame.transform.scale(INTERSECTION_IMAGE_3, (INTERSECTION_WIDTH,INTERSECTION_HEIGHT))

# intersection's position
INTERSECTION_COORDINATES_0 = (650,150)
INTERSECTION_COORDINATES_1 = (200,150)
INTERSECTION_COORDINATES_2 = (650,600)
INTERSECTION_COORDINATES_3 = (200,600)


# street's position : final_initial
STREET_AMESTERDAM_POSITION = [(INTERSECTION_COORDINATES_1[0] + 50, INTERSECTION_COORDINATES_1[1]), INTERSECTION_COORDINATES_0]
STREET_ROMA_POSITION = [(INTERSECTION_COORDINATES_3[0]+50, INTERSECTION_COORDINATES_3[1]+40), INTERSECTION_COORDINATES_2]
STREET_ATHENAS_POSITION = [(INTERSECTION_COORDINATES_1[0], INTERSECTION_COORDINATES_1[1]+50), INTERSECTION_COORDINATES_3]
STREET_LONDON_POSITION = [(INTERSECTION_COORDINATES_0[0] +40, INTERSECTION_COORDINATES_0[1]+50), INTERSECTION_COORDINATES_2]
STREET_MOSCOW_POSITION = [INTERSECTION_COORDINATES_1,INTERSECTION_COORDINATES_2] #só moscovo está invertida

#define car's initial position
CAR_AMESTERDAM_POSITION_END = [STREET_AMESTERDAM_POSITION[0][0], STREET_AMESTERDAM_POSITION[0][1]]
CAR_ROMA_POSITION_END = [STREET_ROMA_POSITION[0][0], STREET_ROMA_POSITION[0][1]+25]
CAR_ATHENES_POSITION_END = [STREET_ATHENAS_POSITION[0][0], STREET_ATHENAS_POSITION[0][1]]
CAR_LONDON_POSITION_END = [STREET_LONDON_POSITION[0][0],STREET_ATHENAS_POSITION[0][1]]
CAR_MOSCOW_POSITION_END = [STREET_MOSCOW_POSITION[1][0], STREET_MOSCOW_POSITION[1][1]]

CAR_AMESTERDAM_POSITION_BEGINING = [STREET_AMESTERDAM_POSITION[1][0], STREET_AMESTERDAM_POSITION[1][1]]
CAR_ROMA_POSITION_BEGINING = [STREET_ROMA_POSITION[1][0], STREET_ROMA_POSITION[1][1]+25]
CAR_ATHENES_POSITION_BEGINING = [STREET_ATHENAS_POSITION[1][0], STREET_ATHENAS_POSITION[1][1]]
CAR_LONDON_POSITION_BEGINING = [STREET_LONDON_POSITION[1][0],STREET_ATHENAS_POSITION[1][1]]
CAR_MOSCOW_POSITION_BEGINING = [STREET_MOSCOW_POSITION[0][0], STREET_MOSCOW_POSITION[0][1]]

#traffic ligths
TRAFFIC_LIGHT_WIDTH = 35
TRAFFIC_LIGHT_HEIGHT = 35
RED_LIGHT = pygame.image.load(os.path.join('images', 'red_ligth.png'))
RED_LIGHT = pygame.transform.scale(RED_LIGHT, (TRAFFIC_LIGHT_WIDTH,TRAFFIC_LIGHT_HEIGHT))
GREEN_LIGHT = pygame.image.load(os.path.join('images', 'green_ligth.png'))
GREEN_LIGHT = pygame.transform.scale(GREEN_LIGHT, (TRAFFIC_LIGHT_WIDTH,TRAFFIC_LIGHT_HEIGHT))

#time's font color20
CLOCK_WIDTH = 50
CLOCK_HEIGHT = 50
CLOCK = pygame.image.load(os.path.join('images', 'clock.png'))
CLOCK = pygame.transform.scale(CLOCK, (CLOCK_WIDTH,CLOCK_HEIGHT))
GREY = (105, 105, 105)

# points
POINTS = pygame.image.load(os.path.join('images', 'points.png'))
POINTS = pygame.transform.scale(POINTS, (CLOCK_WIDTH,CLOCK_HEIGHT))

class Visualization:
    def __init__(self, intersections, streets, cars):
        self.intersections = intersections
        self.streets = streets
        self.cars = cars
        self.points = 0

        self.intersections_rect = self.define_intersections()
        self.streets_rect = self.define_streets()
        self.cars_positions = self.define_cars()
        self.traffic_lights = self.define_traffic_lights()

    def define_intersections(self):
        intersection_list_rect = {}

        intersection_0 = pygame.Rect(INTERSECTION_COORDINATES_0[0], INTERSECTION_COORDINATES_1[1],INTERSECTION_WIDTH, INTERSECTION_HEIGHT)
        intersection_list_rect[0] = (intersection_0, INTERSECTION_IMAGE_0)
        
        intersection_1 = pygame.Rect(INTERSECTION_COORDINATES_1[0], INTERSECTION_COORDINATES_1[1],INTERSECTION_WIDTH, INTERSECTION_HEIGHT)
        intersection_list_rect[1] = (intersection_1, INTERSECTION_IMAGE_1)
        
        intersection_2 = pygame.Rect(INTERSECTION_COORDINATES_2[0], INTERSECTION_COORDINATES_2[1],INTERSECTION_WIDTH, INTERSECTION_HEIGHT)
        intersection_list_rect[2] = (intersection_2, INTERSECTION_IMAGE_2)

        intersection_3 = pygame.Rect(INTERSECTION_COORDINATES_3[0], INTERSECTION_COORDINATES_3[1],INTERSECTION_WIDTH, INTERSECTION_HEIGHT)
        intersection_list_rect[3] = (intersection_3, INTERSECTION_IMAGE_3)

        return intersection_list_rect


    def define_streets(self) :
        streets_list_rect = {}

        moscow_street = pygame.Rect(STREET_MOSCOW_POSITION[0][0], STREET_MOSCOW_POSITION[0][1],STREET_WIDTH, STREET_HEIGHT_OBLIQUE)
        streets_list_rect["rue-de-moscou"] = (moscow_street, STREET_MOSCOW_IMAGE, self.streets["rue-de-moscou"].length)

        athenas_street = pygame.Rect(STREET_ATHENAS_POSITION[0][0], STREET_ATHENAS_POSITION[0][1],STREET_WIDTH, STREET_HEIGHT)
        streets_list_rect["rue-d-athenes"] = (athenas_street, STREET_ATHENAS_IMAGE, self.streets["rue-d-athenes"].length)

        roma_street = pygame.Rect(STREET_ROMA_POSITION[0][0], STREET_ROMA_POSITION[0][1],STREET_WIDTH, STREET_HEIGHT)
        streets_list_rect["rue-de-rome"] = (roma_street, STREET_ROMA_IMAGE, self.streets["rue-de-rome"].length)

        amsterdam_street = pygame.Rect(STREET_AMESTERDAM_POSITION[0][0], STREET_AMESTERDAM_POSITION[0][1],STREET_WIDTH, STREET_HEIGHT)
        streets_list_rect["rue-d-amsterdam"] = (amsterdam_street , STREET_AMESTERDAM_IMAGE, self.streets["rue-d-amsterdam"].length)
        
        london_street = pygame.Rect(STREET_LONDON_POSITION[0][0], STREET_LONDON_POSITION[0][1],STREET_WIDTH, STREET_HEIGHT)
        streets_list_rect["rue-de-londres"] = (london_street , STREET_LONDON_IMAGE, self.streets["rue-de-londres"].length)

        return streets_list_rect


    def define_cars(self):
        # define initial car's position
        cars_positions = {}
        for car in self.cars:
            current_street = car.streets[car.current_street_index]
            if current_street.name == "rue-d-amsterdam":
                cars_positions[car] = [CAR_AMESTERDAM, CAR_AMESTERDAM_POSITION_END]
            elif current_street.name == "rue-de-rome":
                cars_positions[car] = [CAR_ROMA,CAR_ROMA_POSITION_END]
            elif current_street.name == "rue-d-athenes":
                cars_positions[car] = [CAR_ATHENES,CAR_ATHENES_POSITION_END]
            elif current_street.name == "rue-de-londres":
                cars_positions[car] = [CAR_LONDON,CAR_LONDON_POSITION_END]
            elif current_street.name == "rue-de-moscou":
                cars_positions[car] = [CAR_MOSCOW,CAR_MOSCOW_POSITION_END]
            
        return cars_positions
    
    def define_traffic_lights(self):
        traffic_ligths = {}

        moscow = pygame.Rect(STREET_MOSCOW_POSITION[0][0]+60, STREET_MOSCOW_POSITION[0][1]+60,TRAFFIC_LIGHT_WIDTH, TRAFFIC_LIGHT_HEIGHT)
        traffic_ligths["rue-de-moscou"] = [moscow, GREEN_LIGHT, RED_LIGHT]

        athenas = pygame.Rect(STREET_ATHENAS_POSITION[0][0]+10, STREET_ATHENAS_POSITION[0][1]+20,TRAFFIC_LIGHT_WIDTH, TRAFFIC_LIGHT_HEIGHT)
        traffic_ligths["rue-d-athenes"] =  [athenas, GREEN_LIGHT, RED_LIGHT]

        london = pygame.Rect(STREET_LONDON_POSITION[0][0]+10, STREET_LONDON_POSITION[0][1]+20,TRAFFIC_LIGHT_WIDTH, TRAFFIC_LIGHT_HEIGHT)
        traffic_ligths["rue-de-londres"] =  [london, GREEN_LIGHT, RED_LIGHT]

        amsterdam = pygame.Rect(STREET_AMESTERDAM_POSITION[0][0]+20, STREET_AMESTERDAM_POSITION[0][1]+10,TRAFFIC_LIGHT_WIDTH, TRAFFIC_LIGHT_HEIGHT)
        traffic_ligths["rue-d-amsterdam"] = [amsterdam, GREEN_LIGHT, RED_LIGHT]

        roma = pygame.Rect(STREET_ROMA_POSITION[0][0]+20, STREET_ROMA_POSITION[0][1],TRAFFIC_LIGHT_WIDTH, TRAFFIC_LIGHT_HEIGHT)
        traffic_ligths["rue-de-rome"] =  [roma, GREEN_LIGHT, RED_LIGHT]

        return traffic_ligths

    def draw_time(self,time_elapsed):
        WIN.blit(CLOCK,(20,20))

        font1 = pygame.font.SysFont('chalkduster.ttf', 30)
        img = font1.render(str(time_elapsed), True, GREY)
        WIN.blit(img, (80, 35))

    def draw_cars_arrived(self, number_cars_arrived):
        WIN.blit(CAR_AMESTERDAM,(150,15))
        font1 = pygame.font.SysFont('chalkduster.ttf', 30)
        img = font1.render(str(number_cars_arrived), True, GREY)
        WIN.blit(img, (230, 35))
    
    def draw_points(self,total_points):
        WIN.blit(POINTS,(300,20))
        font1 = pygame.font.SysFont('chalkduster.ttf', 30)
        img = font1.render(str(total_points), True, GREY)
        WIN.blit(img, (360, 35))

    def draw_window(self, streets, time_elapsed, number_cars_arrived, total_points):
        WIN.blit(back_ground, (0, 0))
        
        #top bar indormation
        self.draw_time(time_elapsed)
        self.draw_cars_arrived(number_cars_arrived)
        self.draw_points(total_points)


        for street in streets:
            WIN.blit(self.streets_rect[street][1],(self.streets_rect[street][0].x,self.streets_rect[street][0].y))
   
        for intersection in self.intersections:
            WIN.blit(self.intersections_rect[intersection.id][1], (self.intersections_rect[intersection.id][0].x, self.intersections_rect[intersection.id][0].y))

        for street in streets:
            if streets[street].green_light:
                WIN.blit(self.traffic_lights[street][1],(self.traffic_lights[street][0].x,self.traffic_lights[street][0].y))
            else:
                WIN.blit(self.traffic_lights[street][2],(self.traffic_lights[street][0].x,self.traffic_lights[street][0].y))
        
        for car in self.cars_positions:
            WIN.blit(self.cars_positions[car][0], (self.cars_positions[car][1][0], self.cars_positions[car][1][1]))

        pygame.display.update()

    def update_car_position(self, car, current_street):
        # andar uma unidade para a frente na mesma estrada

        step_normal = (STREET_HEIGHT/current_street.length)/100

        if current_street.name == "rue-d-amsterdam": # esquerda -> direita
            print("estou a mover o carro na rua de amesterdão")
            self.cars_positions[car][1][0] -= step_normal
            
        elif current_street.name == "rue-de-rome": # esquerda -> direita
            self.cars_positions[car][1][0] -= step_normal

        elif current_street.name == "rue-d-athenes": # baixo -> cima
            self.cars_positions[car][1][1] -= step_normal

        elif current_street.name == "rue-de-londres": # baixo -> cima
            self.cars_positions[car][1][1] -= step_normal

        elif current_street.name == "rue-de-moscou": #canto superior esqueda -> canto inferior direita
            self.cars_positions[car][1][0] += step_normal
            self.cars_positions[car][1][1] += step_normal
    
    def change_car_street(self,car):
        current_street = car.streets[car.current_street_index]

        if current_street.name == "rue-d-amsterdam": # esquerda -> direita
            self.cars_positions[car] = [CAR_AMESTERDAM, CAR_AMESTERDAM_POSITION_BEGINING]
        elif current_street.name == "rue-de-rome": # esquerda -> direita
            self.cars_positions[car] = [CAR_ROMA, CAR_ROMA_POSITION_BEGINING]
        elif current_street.name == "rue-d-athenes": # baixo -> cima(
            self.cars_positions[car] = [CAR_ATHENES,CAR_ATHENES_POSITION_BEGINING]
        elif current_street.name == "rue-de-londres": # baixo -> cima
            self.cars_positions[car] = [CAR_LONDON,CAR_LONDON_POSITION_BEGINING]
        elif current_street.name == "rue-de-moscou": #canto superior esqueda -> canto inferior direita
            self.cars_positions[car] = [CAR_MOSCOW,CAR_MOSCOW_POSITION_BEGINING]
