import pygame
import pymunk

class Mouse():
    def __init__(self, state, ball_radius, cube_size):
        self.state = state
        self.ball_radius = ball_radius
        self.cube_size = cube_size

    def Add_Ball(self, space, pos, radius, mass, elasticity, friction, color):
        moment = pymunk.moment_for_circle(mass, 0, radius)
        body = pymunk.Body(mass, moment, body_type=pymunk.Body.DYNAMIC)
        body.position = pos
        shape = pymunk.Circle(body, radius)
        shape.color = color
        space.add(body, shape)
        shape.elasticity = elasticity
        shape.friction = friction
        return shape

    def Add_Cube(self, space, pos, size, color, elasticity, friction):
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body, size)
        shape.elasticity = elasticity
        shape.friction = friction
        shape.color = color
        space.add(body, shape)
        return shape

    def getstate(self, event, screen):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

        if self.state == 'ReadyToAddBall':
            circle_radius = self.ball_radius
            circle_color = (255, 255, 255)
            outline_thickness = 3
            pygame.draw.circle(screen, circle_color, (self.mouse_x, self.mouse_y), circle_radius, outline_thickness)
            if self.mouse_x > 300 and event.type == pygame.MOUSEBUTTONDOWN:
                return 'DrawBall'

        if self.state == 'ReadyToAddCube':
            square_size = self.cube_size
            square_color = (255, 255, 255)
            outline_thickness = 3
            pygame.draw.rect(screen, square_color, (
            self.mouse_x - square_size // 2, self.mouse_y - square_size // 2, square_size, square_size),outline_thickness)
            if self.mouse_x > 300 and event.type == pygame.MOUSEBUTTONDOWN:
                 return 'DrawCube'

        if self.state == 'ReadyToAddDraw':
            square_size = 20
            square_color = (255, 255, 0)
            outline_thickness = 3
            pygame.draw.rect(screen, square_color, (
                self.mouse_x - square_size // 2, self.mouse_y - square_size // 2, square_size, square_size),
                             outline_thickness)
            if self.mouse_x > 300 and event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'DrawModeCube'
                return 'DrawModeCube'

        if self.state == 'DrawModeCube':
            if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
                return 'DrawModeCube'
            if event.type == pygame.MOUSEBUTTONUP:
                self.state = 'ReadyToAddDraw'
                return None

        return None