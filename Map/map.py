class ZoomIn:
    def __init__(self):
        self.zoom = 0

    def zoom_update(self):
        self.zoom += 1


level_1 = [
           '  XXXXXXXXXXXX           XXXXXXX',
           ' XXXXXXXXXXXXXX         XXXXXXXXX',
           'XXXXXXXXXXXXXXXX       XXXXXXXXXXX',
           'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
           'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
           ' XXXXXXXXXXXXXX        XXXXXXXXXXX',
           '  XXXXXXXXXXXX          XXXXXXXXX',
           '      XXXX               XXXXXXX',
           '      XXXX                 XXX',
           '      XXXX                 XXX',
           '      XXXX                 XXX',
           '  XXXXXXXXXXXX             XXX',
           ' XXXXXXXXXXXXXX          XXXXX',
           'XXXXXXXXXXXXXXXX        XXXXXX',
           'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX ',
           'XXXXXXXXXXXXXXXXXXXXXXXXXXX   ',
           ' XXXXXXXXXXXXXX ',
           '  XXXXXXXXXXXX  ']


zoom = ZoomIn()

tile_size = 32 + 16 + zoom.zoom


WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500

