import constantes
from item import Item
from personaje import Personaje
obstaculos = [0,2,3,4,5,6,7]
class Mundo():
    def __init__(self):
        self.map_tiles = []
        self.obstaculos_tiles = []

    def process_data(self, data, tile_list):
        self.level_length = len(data)
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                image = tile_list[tile]
                image_rect = image.get_rect()
                image_x = x * constantes.TILE_SIZE
                image_y = y * constantes.TILE_SIZE
                image_rect.center = (image_x, image_y)
                tile_data = [image, image_rect, image_x, image_y]
                self.map_tiles.append(tile_data)
                if tile in obstaculos:
                    self.obstaculos_tiles.append(tile_data)

    def draw(self, surface):
        for tile in self.map_tiles:
            surface.blit(tile[0], tile[1])