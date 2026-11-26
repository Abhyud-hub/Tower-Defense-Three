import pygame


pygame.init()
WHITE = (255, 255, 255)


def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)

def blit_text_center(win, text, font, color):
    render = font.render(text, 1, color)
    win.blit(render, (win.get_width() / 2 - render.get_width() / 2, win.get_height() / 2 - render.get_height() / 2))

def pixel_collision(a, b):
    # Match the rotation and centered positioning used by blit_rotate_center
    image_a = pygame.transform.rotate(a.image, a.heading)
    image_b = pygame.transform.rotate(b.image, b.heading)

    original_rect_a = a.image.get_rect(topleft=(a.x, a.y))
    original_rect_b = b.image.get_rect(topleft=(b.x, b.y))

    rect_a = image_a.get_rect(center=original_rect_a.center)
    rect_b = image_b.get_rect(center=original_rect_b.center)

    mask_a = pygame.mask.from_surface(image_a)
    mask_b = pygame.mask.from_surface(image_b)

    offset = (rect_b.left - rect_a.left, rect_b.top - rect_a.top)
    return mask_a.overlap(mask_b, offset) is not None