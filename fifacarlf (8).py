"""
Sandbox Open World Game
-----------------------
ตัวละครและไอเทมจากภาพวาด:
- โกเลม (สีชมพู/บานเย็น) = ตัวละครผู้เล่น
- มุทแมน (ครีปเปอร์ตัวใหญ่ สีเขียว) และ แทก (ครีปเปอร์ตัวเล็ก สีเขียว) = มอนสเตอร์ที่เดินไปมาและระเบิดเมื่อเข้าใกล้
- ต้นไม้ปากฉลาม (สีเขียว) = มอนสเตอร์ต้นไม้ที่กัดผู้เล่นเมื่ออยู่ใกล้
- ลูกดอกดำ และ นกหลากสี = ไอเทมที่ตกลงมาจากฟ้า เก็บแล้วได้บัฟ (ความเร็ว / กระโดดสูง)
- ลูกบอล (สีส้ม) = ไอเทมที่ตกลงมาจากฟ้า เก็บ 1 ลูกแล้วปลดล็อกยิงเลเซอร์ได้แบบไม่จำกัดตลอดไป
- เห็ด (สีแดงจุดขาว) = วางอยู่บนพื้น เดินไปแตะแล้วจะกระโดดสูงทันที (เหมือนแทรมโพลีน)
- หมูสีชมพู และ หมูตาสีแดง = เดินเล่นอยู่บนพื้น ยิงเลเซอร์ใส่แล้วจะแปลงร่างเป็นพันธมิตรหน้าตาเหมือนโกเลม
  คอยช่วยยิงเลเซอร์ใส่แพทแมนให้เรา
- แพทแมน (ตัวสีดำ มีแขนขา) = มอนสเตอร์ใต้ดิน มีอยู่ 1 ตัวในโลก เดินลาดตระเวนอยู่ใต้พื้นดิน
  ยิงเลเซอร์ใส่ผู้เล่นเมื่อเข้าใกล้ ทำลายมันได้ด้วยเลเซอร์ของโกเลม เมื่อตายจะดรอปดาบให้เก็บ
- แร่ใต้ดิน (ถ่านหิน / เหล็ก / ทอง / เพชร) = ฝังอยู่ในชั้นหิน ยิ่งลึกยิ่งหายาก ขุดแล้วเก็บเข้ากระเป๋า
- หมู่บ้าน = มี 2 แห่งในโลก มีบ้านให้เห็น และมนุษย์เหล็กเฝ้าอยู่ คอยทุบครีปเปอร์ที่เดินเข้ามาใกล้
- ไก่ วัว หนอน (สีชมพู พวกเดียวกับหมู) = เดินเล่นอยู่บนพื้นเหมือนหมู ยิงเลเซอร์ใส่แล้วแปลงร่างเป็นพันธมิตรได้เช่นกัน
- ทะเล = อยู่สุดขอบด้านหนึ่งของแผนที่ ว่ายน้ำ/เดินลุยได้ ไม่ใช่ของแข็ง
- ต้นไม้ = ขึ้นอยู่ทั่วพื้นดินเป็นฉากตกแต่ง ไม่เป็นของแข็งกีดขวางทาง
- กิ้งก่า = เดินไปมาบนพื้นเร็วๆ เปลี่ยนทิศบ่อย เป็นสัตว์ป่าเฉยๆ ไม่โจมตีและไม่แปลงร่าง
- ในทะเล: ปลา (ว่ายไปมา) แมงกะพุน (ลอยขึ้นลงแบบโปร่งแสง) และสาหร่าย (โยกไหวอยู่กับพื้นทะเล) ล้วนเป็นสิ่งมีชีวิต/ตกแต่งเฉยๆ
- ชาวบ้าน = เดินไปมาอยู่แถวหมู่บ้าน เป็นมิตร ไม่โจมตีใคร
- เห็ดเดินได้ = เห็ดที่เดินไปมาได้เองเหมือนสัตว์ป่าตัวหนึ่ง (คนละแบบกับเห็ดกระโดดที่วางอยู่กับที่)

วิธีเล่น:
  A / Left  = เดินซ้าย
  D / Right = เดินขวา
  W / Space = กระโดด
  คลิกซ้าย  = ขุด/ทำลายบล็อก
  คลิกขวา   = วางบล็อกที่เลือกไว้
  1 / 2 / 3 = เลือกบล็อก (หญ้า / ดิน / หิน)
  F         = ยิงเลเซอร์ (ต้องมีพลังเลเซอร์)
  R         = เริ่มเกมใหม่ (หลังจากตาย)
"""

import tkinter as tk
import random
import math

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
TILE = 32
WORLD_W = 120          # tiles
WORLD_H = 40           # tiles
VIEW_W = 960
VIEW_H = 640
GRAVITY = 0.55
MAX_FALL = 14
MOVE_SPEED = 4.2
JUMP_SPEED = -11.5
REACH = TILE * 4.5     # how far the player can break/place blocks

LASER_SPEED = 16
LASER_LIFETIME = 35           # frames a laser bolt survives
PLAYER_LASER_DAMAGE = 45
PATMAN_HP = 120
PATMAN_LASER_DAMAGE = 12
PATMAN_LASER_COOLDOWN = 100
PATMAN_DETECT_RADIUS = TILE * 9
MUSHROOM_BOUNCE_SPEED = -18.0    # velocity applied when touching a mushroom
MUSHROOM_COOLDOWN = 18           # frames before a mushroom can bounce again
IRON_GOLEM_PUNCH_RADIUS = TILE * 3
IRON_GOLEM_PUNCH_COOLDOWN = 40
SEA_WIDTH = 14                    # tiles of ocean at the right edge of the map
SEA_LEVEL_TILE = WORLD_H // 2
SEA_FLOOR_TILE = WORLD_H - 3

AIR, GRASS, DIRT, STONE, COAL, IRON, GOLD, DIAMOND, WOOD, WATER = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
TILE_COLORS = {
    GRASS: "#4caf50", DIRT: "#8b5a2b", STONE: "#8a8a8a",
    COAL: "#3b3b3b", IRON: "#c9a27a", GOLD: "#ffd54f", DIAMOND: "#4dd0e1",
    WOOD: "#a1662f", WATER: "#2196f3",
}
TILE_NAMES = {
    GRASS: "หญ้า", DIRT: "ดิน", STONE: "หิน",
    COAL: "ถ่านหิน", IRON: "เหล็ก", GOLD: "ทอง", DIAMOND: "เพชร",
    WOOD: "ไม้", WATER: "น้ำ",
}
ORE_TILES = (COAL, IRON, GOLD, DIAMOND)
SOLID_TILES = (GRASS, DIRT, STONE, COAL, IRON, GOLD, DIAMOND, WOOD)

FPS_MS = 33  # ~30 fps


# ---------------------------------------------------------------------------
# World generation
# ---------------------------------------------------------------------------
def generate_world():
    world = [[AIR] * WORLD_W for _ in range(WORLD_H)]
    land_w = WORLD_W - SEA_WIDTH
    height = WORLD_H // 2
    heights = []
    for _ in range(WORLD_W):
        height += random.choice([-1, 0, 0, 0, 1])
        height = max(8, min(WORLD_H - 6, height))
        heights.append(height)

    for x in range(WORLD_W):
        h = heights[x]
        world[h][x] = GRASS
        for y in range(h + 1, min(h + 4, WORLD_H)):
            world[y][x] = DIRT
        for y in range(h + 4, WORLD_H):
            world[y][x] = STONE

    # embed ore veins in the stone layer; deeper = rarer
    for x in range(WORLD_W):
        h = heights[x]
        for y in range(h + 4, WORLD_H):
            depth = y - (h + 4)
            r = random.random()
            if depth >= 16 and r < 0.02:
                world[y][x] = DIAMOND
            elif depth >= 10 and r < 0.035:
                world[y][x] = GOLD
            elif depth >= 4 and r < 0.06:
                world[y][x] = IRON
            elif depth >= 0 and r < 0.09:
                world[y][x] = COAL

    # carve a sea along the right edge of the map
    sea_level = SEA_LEVEL_TILE
    for x in range(land_w, WORLD_W):
        heights[x] = sea_level
        for y in range(0, sea_level):
            world[y][x] = AIR
        for y in range(sea_level, SEA_FLOOR_TILE):
            world[y][x] = WATER
        for y in range(SEA_FLOOR_TILE, WORLD_H):
            world[y][x] = STONE

    # build two villages on land, each guarded by an iron golem
    villages = []
    for center_tx in (land_w // 4, (land_w * 3) // 4):
        base_h = build_village(world, heights, center_tx)
        villages.append((center_tx, base_h))

    return world, heights, villages


def build_village(world, heights, center_tx):
    """Flattens the ground under a village footprint and builds a simple house."""
    footprint = 7
    half = footprint // 2
    base_h = heights[center_tx]
    for x in range(center_tx - half, center_tx + half + 1):
        if 0 <= x < WORLD_W:
            heights[x] = base_h
            for y in range(0, base_h):
                world[y][x] = AIR
            world[base_h][x] = GRASS
            for y in range(base_h + 1, min(base_h + 4, WORLD_H)):
                world[y][x] = DIRT
            for y in range(base_h + 4, WORLD_H):
                world[y][x] = STONE

    house_w, house_h = 5, 4
    hx0 = center_tx - house_w // 2
    for yy in range(base_h - house_h, base_h):
        for xx in range(hx0, hx0 + house_w):
            if yy == base_h - house_h or yy == base_h - 1 or xx == hx0 or xx == hx0 + house_w - 1:
                world[yy][xx] = WOOD
            else:
                world[yy][xx] = AIR
    world[base_h - 1][center_tx] = AIR  # door
    return base_h


def tile_at(world, tx, ty):
    if 0 <= tx < WORLD_W and 0 <= ty < WORLD_H:
        return world[ty][tx]
    if ty >= WORLD_H:
        return STONE
    return AIR


def box_collides(world, x, y, w, h):
    """AABB collision check against solid tiles using the box corners/edges."""
    if x < 0 or x + w > WORLD_W * TILE or y + h > WORLD_H * TILE:
        return True
    left = int(x // TILE)
    right = int((x + w - 1) // TILE)
    top = int(y // TILE)
    bottom = int((y + h - 1) // TILE)
    for ty in range(top, bottom + 1):
        for tx in range(left, right + 1):
            if tile_at(world, tx, ty) in SOLID_TILES:
                return True
    return False


LAND_W = WORLD_W - SEA_WIDTH  # x-range (in tiles) that is dry land, not ocean


# ---------------------------------------------------------------------------
# Entities
# ---------------------------------------------------------------------------
class Entity:
    def __init__(self, x, y, w, h):
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.vx, self.vy = 0.0, 0.0
        self.on_ground = False
        self.alive = True

    def move(self, world, dx, dy):
        # horizontal
        new_x = self.x + dx
        if not box_collides(world, new_x, self.y, self.w, self.h):
            self.x = new_x
        else:
            self.vx = 0
        # vertical
        new_y = self.y + dy
        if not box_collides(world, self.x, new_y, self.w, self.h):
            self.y = new_y
            self.on_ground = False
        else:
            if dy > 0:
                self.on_ground = True
            self.vy = 0

    def center(self):
        return self.x + self.w / 2, self.y + self.h / 2


class Golem(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, TILE - 6, int(TILE * 1.6))
        self.hp = 100
        self.max_hp = 100
        self.speed_timer = 0
        self.jump_timer = 0
        self.facing = 1
        self.score = 0
        self.invuln = 0
        self.laser_unlocked = False  # unlocked permanently after collecting 1 ball
        self.laser_cd = 0            # cooldown between player laser shots
        self.has_sword = False
        self.ores = {COAL: 0, IRON: 0, GOLD: 0, DIAMOND: 0}


class Creeper(Entity):
    def __init__(self, x, y, big=True):
        size = int(TILE * 1.5) if big else int(TILE * 1.05)
        super().__init__(x, y, size - 4, size)
        self.big = big
        self.dir = random.choice([-1, 1])
        self.change_timer = random.randint(30, 90)
        self.fuse = None  # countdown to explosion
        self.respawn_timer = 0


class PlantMonster(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, TILE - 8, int(TILE * 1.3))
        self.bite_cd = 0
        self.chomp = 0  # animation timer


class FallingItem(Entity):
    def __init__(self, x, y, kind):
        super().__init__(x, y, TILE - 10, TILE - 10)
        self.kind = kind  # 'dart', 'bird', 'ball', or 'sword'
        self.ground_timer = 0


class Patman(Entity):
    """Underground monster with arms/legs that fires lasers at the player."""

    def __init__(self, x, y):
        super().__init__(x, y, TILE - 6, int(TILE * 1.5))
        self.hp = PATMAN_HP
        self.max_hp = PATMAN_HP
        self.dir = random.choice([-1, 1])
        self.facing = self.dir
        self.change_timer = random.randint(40, 100)
        self.laser_cd = random.randint(30, PATMAN_LASER_COOLDOWN)
        self.flash = 0


class Laser:
    """A laser bolt fired by either the player or a Patman."""

    def __init__(self, x, y, vx, vy, owner, color):
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy
        self.owner = owner  # 'player' or 'patman'
        self.color = color
        self.life = LASER_LIFETIME


class Mushroom(Entity):
    """Sits on the ground; touching it launches the player into a high jump."""

    def __init__(self, x, y):
        super().__init__(x, y, TILE - 4, int(TILE * 0.9))
        self.bounce_cd = 0
        self.squish = 0


class Pig(Entity):
    """Wanders on the surface. Shooting it with the player's laser turns it into an Ally.
    kind is one of 'pig', 'chicken', 'cow', 'worm' - all are pink and all convert."""

    SIZES = {
        "pig": (TILE - 8, int(TILE * 0.9)),
        "chicken": (TILE - 14, int(TILE * 0.8)),
        "cow": (int(TILE * 1.3), int(TILE * 1.1)),
        "worm": (int(TILE * 1.4), TILE - 14),
    }

    def __init__(self, x, y, kind="pig", red_eyes=False):
        w, h = self.SIZES.get(kind, self.SIZES["pig"])
        super().__init__(x, y, w, h)
        self.kind = kind
        self.dir = random.choice([-1, 1])
        self.change_timer = random.randint(40, 100)
        self.red_eyes = red_eyes


class Ally(Entity):
    """A former pig, now golem-shaped, that helps shoot lasers at Patman."""

    def __init__(self, x, y, red_eyes=False):
        super().__init__(x, y, TILE - 6, int(TILE * 1.6))
        self.facing = 1
        self.red_eyes = red_eyes
        self.laser_cd = random.randint(10, 30)


class IronGolem(Entity):
    """Guards a village: patrols nearby and punches any creeper that wanders close."""

    def __init__(self, x, y, patrol_min_x, patrol_max_x):
        super().__init__(x, y, int(TILE * 1.3), int(TILE * 2.0))
        self.patrol_min_x = patrol_min_x
        self.patrol_max_x = patrol_max_x
        self.dir = 1
        self.facing = 1
        self.punch_cd = 0
        self.punch_flash = 0


class Tree(Entity):
    """Purely decorative - does not block movement."""

    def __init__(self, x, y, scale=1.0):
        w = int(TILE * 1.6 * scale)
        h = int(TILE * 3.2 * scale)
        super().__init__(x - w / 2, y - h, w, h)


class Lizard(Entity):
    """Neutral wildlife: darts along the ground, doesn't attack or transform."""

    def __init__(self, x, y):
        super().__init__(x, y, int(TILE * 0.75), int(TILE * 0.35))
        self.dir = random.choice([-1, 1])
        self.change_timer = random.randint(20, 60)
        self.pause_timer = 0


class Fish(Entity):
    """Swims freely within the sea's bounding box."""

    def __init__(self, x, y):
        super().__init__(x, y, int(TILE * 0.6), int(TILE * 0.32))
        self.dir = random.choice([-1, 1])
        self.vdir = random.choice([-1, 1])
        self.change_timer = random.randint(40, 100)


class Jellyfish(Entity):
    """Drifts slowly up and down in the sea, pulsing gently."""

    def __init__(self, x, y):
        super().__init__(x, y, int(TILE * 0.55), int(TILE * 0.7))
        self.vdir = random.choice([-1, 1])
        self.change_timer = random.randint(60, 140)
        self.phase = random.uniform(0, 6.28)


class Seaweed(Entity):
    """Anchored to the sea floor; sways in place, purely decorative."""

    def __init__(self, x, y, height):
        w = TILE * 0.3
        super().__init__(x - w / 2, y - height, w, height)
        self.phase = random.uniform(0, 6.28)


class Villager(Entity):
    """Friendly NPC that wanders around a village. Never attacks or is attacked."""

    def __init__(self, x, y, patrol_min_x, patrol_max_x):
        super().__init__(x, y, int(TILE * 0.6), int(TILE * 1.4))
        self.patrol_min_x = patrol_min_x
        self.patrol_max_x = patrol_max_x
        self.dir = random.choice([-1, 1])
        self.facing = self.dir
        self.change_timer = random.randint(60, 150)


class MushroomWalker(Entity):
    """A mushroom that walks around like a small animal (distinct from the bounce-pad Mushroom)."""

    def __init__(self, x, y):
        super().__init__(x, y, int(TILE * 0.8), int(TILE * 0.75))
        self.dir = random.choice([-1, 1])
        self.change_timer = random.randint(50, 120)


# ---------------------------------------------------------------------------
# Game
# ---------------------------------------------------------------------------
class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Sandbox Open World")
        self.canvas = tk.Canvas(root, width=VIEW_W, height=VIEW_H, bg="#87CEEB",
                                 highlightthickness=0)
        self.canvas.pack()

        self.keys = set()
        self.selected_block = GRASS
        self.game_over = False

        self.canvas.bind_all("<KeyPress>", self.on_key_down)
        self.canvas.bind_all("<KeyRelease>", self.on_key_up)
        self.canvas.bind("<Button-1>", self.on_break_block)
        self.canvas.bind("<Button-3>", self.on_place_block)

        self.new_game()
        self.loop()

    # -------------------------------------------------------------- setup
    def new_game(self):
        self.world, heights, villages = generate_world()
        self.heights = heights
        self.villages = villages
        self.game_over = False

        spawn_tx = WORLD_W // 2
        spawn_y = (heights[spawn_tx] - 3) * TILE
        self.player = Golem(spawn_tx * TILE, spawn_y)

        self.creepers = []
        for _ in range(7):
            tx = random.randint(5, LAND_W - 5)
            ty = heights[tx] - 2
            big = random.random() < 0.5
            self.creepers.append(Creeper(tx * TILE, ty * TILE, big))

        self.plants = []
        for _ in range(5):
            tx = random.randint(5, LAND_W - 5)
            ty = heights[tx] - 1
            self.plants.append(PlantMonster(tx * TILE, ty * TILE))

        self.mushrooms = []
        for _ in range(6):
            tx = random.randint(5, LAND_W - 5)
            ty = heights[tx] - 1
            self.mushrooms.append(Mushroom(tx * TILE + 2, ty * TILE + (TILE - int(TILE * 0.9))))

        self.patmen = []
        for _ in range(1):
            tx = random.randint(5, LAND_W - 5)
            ty = min(WORLD_H - 3, heights[tx] + random.randint(4, 8))
            self.patmen.append(Patman(tx * TILE, ty * TILE))

        self.pigs = []
        for kind, count in (("pig", 5), ("chicken", 4), ("cow", 3), ("worm", 3)):
            for _ in range(count):
                tx = random.randint(5, LAND_W - 5)
                ty = heights[tx] - 1
                red_eyes = random.random() < 0.35 if kind == "pig" else False
                self.pigs.append(Pig(tx * TILE, ty * TILE, kind, red_eyes))
        self.allies = []

        self.trees = []
        for _ in range(12):
            tx = random.randint(3, LAND_W - 3)
            ty = heights[tx]
            scale = random.uniform(0.8, 1.3)
            self.trees.append(Tree(tx * TILE + TILE / 2, ty * TILE, scale))

        self.lizards = []
        for _ in range(6):
            tx = random.randint(5, LAND_W - 5)
            ty = heights[tx] - 1
            self.lizards.append(Lizard(tx * TILE, ty * TILE))

        sea_x0 = LAND_W * TILE
        sea_x1 = WORLD_W * TILE
        sea_y0 = SEA_LEVEL_TILE * TILE
        sea_y1 = SEA_FLOOR_TILE * TILE
        self.sea_bounds = (sea_x0, sea_x1, sea_y0, sea_y1)
        self.anim_timer = 0

        self.fish = []
        for _ in range(8):
            x = random.uniform(sea_x0 + 20, sea_x1 - 40)
            y = random.uniform(sea_y0 + 10, sea_y1 - 20)
            self.fish.append(Fish(x, y))

        self.jellyfish = []
        for _ in range(4):
            x = random.uniform(sea_x0 + 20, sea_x1 - 40)
            y = random.uniform(sea_y0 + 10, sea_y1 - 20)
            self.jellyfish.append(Jellyfish(x, y))

        self.seaweeds = []
        for _ in range(10):
            x = random.uniform(sea_x0 + 10, sea_x1 - 10)
            height = random.uniform(TILE * 0.8, TILE * 1.8)
            self.seaweeds.append(Seaweed(x, sea_y1, height))

        self.iron_golems = []
        self.villagers = []
        for center_tx, base_h in villages:
            gx = (center_tx - 4) * TILE
            gy = (base_h - 2) * TILE
            patrol_min = (center_tx - 6) * TILE
            patrol_max = (center_tx + 6) * TILE
            self.iron_golems.append(IronGolem(gx, gy, patrol_min, patrol_max))

            vpatrol_min = (center_tx - 4) * TILE
            vpatrol_max = (center_tx + 4) * TILE
            for _ in range(2):
                vx = random.uniform(vpatrol_min, vpatrol_max)
                self.villagers.append(Villager(vx, (base_h - 2) * TILE, vpatrol_min, vpatrol_max))

        self.walking_mushrooms = []
        for _ in range(5):
            tx = random.randint(5, LAND_W - 5)
            ty = heights[tx] - 1
            self.walking_mushrooms.append(MushroomWalker(tx * TILE, ty * TILE))

        self.player_lasers = []
        self.patman_lasers = []

        self.items = []
        self.item_spawn_timer = 60

        self.camera_x = self.player.x - VIEW_W / 2
        self.camera_y = self.player.y - VIEW_H / 2

    # -------------------------------------------------------------- input
    def on_key_down(self, event):
        k = event.keysym.lower()
        self.keys.add(k)
        if k in ("1", "2", "3"):
            self.selected_block = {"1": GRASS, "2": DIRT, "3": STONE}[k]
        if k == "r" and self.game_over:
            self.new_game()
        if k == "f" and not self.game_over:
            self.fire_player_laser()

    def on_key_up(self, event):
        self.keys.discard(event.keysym.lower())

    def screen_to_tile(self, sx, sy):
        wx = sx + self.camera_x
        wy = sy + self.camera_y
        return int(wx // TILE), int(wy // TILE)

    def on_break_block(self, event):
        if self.game_over:
            return
        tx, ty = self.screen_to_tile(event.x, event.y)
        px, py = self.player.center()
        wx, wy = tx * TILE + TILE / 2, ty * TILE + TILE / 2
        if math.hypot(px - wx, py - wy) <= REACH:
            if 0 <= tx < WORLD_W and 0 <= ty < WORLD_H:
                t = self.world[ty][tx]
                if t == AIR or t == WATER:
                    return
                if t in ORE_TILES:
                    self.player.ores[t] += 1
                self.world[ty][tx] = AIR

    def on_place_block(self, event):
        if self.game_over:
            return
        tx, ty = self.screen_to_tile(event.x, event.y)
        px, py = self.player.center()
        wx, wy = tx * TILE + TILE / 2, ty * TILE + TILE / 2
        if math.hypot(px - wx, py - wy) <= REACH:
            if 0 <= tx < WORLD_W and 0 <= ty < WORLD_H:
                if self.world[ty][tx] == AIR:
                    block_rect = (tx * TILE, ty * TILE, TILE, TILE)
                    if not rects_overlap(block_rect, (self.player.x, self.player.y,
                                                        self.player.w, self.player.h)):
                        self.world[ty][tx] = self.selected_block

    # -------------------------------------------------------------- update
    def loop(self):
        if not self.game_over:
            self.update()
        self.render()
        self.root.after(FPS_MS, self.loop)

    def fire_player_laser(self):
        p = self.player
        if not p.laser_unlocked or p.laser_cd > 0:
            return
        p.laser_cd = 12
        cx, cy = p.center()
        self.player_lasers.append(Laser(cx, cy, LASER_SPEED * p.facing, 0, "player", "#ff2fd6"))

    def update(self):
        self.anim_timer += 1
        self.update_player()
        self.update_creepers()
        self.update_plants()
        self.update_mushrooms()
        self.update_pigs()
        self.update_lizards()
        self.update_fish()
        self.update_jellyfish()
        self.update_villagers()
        self.update_walking_mushrooms()
        self.update_patmen()
        self.update_allies()
        self.update_iron_golems()
        self.update_lasers()
        self.update_items()

        # camera follows player, clamped to world bounds
        self.camera_x = clamp(self.player.center()[0] - VIEW_W / 2,
                               0, WORLD_W * TILE - VIEW_W)
        self.camera_y = clamp(self.player.center()[1] - VIEW_H / 2,
                               0, WORLD_H * TILE - VIEW_H)

        if self.player.hp <= 0:
            self.game_over = True

    def update_player(self):
        p = self.player
        speed = MOVE_SPEED * (1.7 if p.speed_timer > 0 else 1.0)
        dx = 0
        if "a" in self.keys or "left" in self.keys:
            dx -= speed
            p.facing = -1
        if "d" in self.keys or "right" in self.keys:
            dx += speed
            p.facing = 1
        if ("w" in self.keys or "space" in self.keys) and p.on_ground:
            p.vy = JUMP_SPEED * (1.3 if p.jump_timer > 0 else 1.0)

        pcx, pcy = p.center()
        in_water = tile_at(self.world, int(pcx // TILE), int(pcy // TILE)) == WATER
        if in_water:
            p.vy = min(p.vy + GRAVITY * 0.25, 3.0)
            if "w" in self.keys or "space" in self.keys:
                p.vy = -3.2  # swim upward
        else:
            p.vy = min(p.vy + GRAVITY, MAX_FALL)
        p.move(self.world, dx, p.vy)

        if p.speed_timer > 0:
            p.speed_timer -= 1
        if p.jump_timer > 0:
            p.jump_timer -= 1
        if p.invuln > 0:
            p.invuln -= 1
        if p.laser_cd > 0:
            p.laser_cd -= 1

    def update_creepers(self):
        px, py = self.player.center()
        for c in self.creepers:
            if not c.alive:
                c.respawn_timer -= 1
                if c.respawn_timer <= 0:
                    tx = random.randint(5, WORLD_W - 5)
                    ty = self.heights[tx] - 2
                    c.x, c.y = tx * TILE, ty * TILE
                    c.alive = True
                    c.fuse = None
                    c.vx = c.vy = 0
                continue

            cx, cy = c.center()
            dist = math.hypot(px - cx, py - cy)

            if dist < TILE * 3.5:
                # chase / prime fuse
                c.dir = 1 if px > cx else -1
                if c.fuse is None:
                    c.fuse = 45
                else:
                    c.fuse -= 1
            else:
                c.fuse = None
                c.change_timer -= 1
                if c.change_timer <= 0:
                    c.dir = random.choice([-1, 1])
                    c.change_timer = random.randint(40, 100)

            speed = 2.4 if c.fuse is not None else 1.4
            c.vy = min(c.vy + GRAVITY, MAX_FALL)
            c.move(self.world, c.dir * speed, c.vy)

            if c.fuse is not None and c.fuse <= 0:
                self.explode_creeper(c)

    def explode_creeper(self, c):
        cx, cy = c.center()
        radius_tiles = 3 if c.big else 2
        ctx, cty = int(cx // TILE), int(cy // TILE)
        for ty in range(cty - radius_tiles, cty + radius_tiles + 1):
            for tx in range(ctx - radius_tiles, ctx + radius_tiles + 1):
                if math.hypot(tx - ctx, ty - cty) <= radius_tiles:
                    if 0 <= tx < WORLD_W and 0 <= ty < WORLD_H:
                        self.world[ty][tx] = AIR

        px, py = self.player.center()
        dist = math.hypot(px - cx, py - cy)
        if dist <= radius_tiles * TILE and self.player.invuln <= 0:
            dmg = 35 if c.big else 20
            self.player.hp = max(0, self.player.hp - dmg)
            self.player.invuln = 40

        c.alive = False
        c.respawn_timer = 150

    def update_plants(self):
        px, py = self.player.center()
        for plant in self.plants:
            plant.vy = min(plant.vy + GRAVITY, MAX_FALL)
            plant.move(self.world, 0, plant.vy)

            plx, ply = plant.center()
            dist = math.hypot(px - plx, py - ply)
            if plant.bite_cd > 0:
                plant.bite_cd -= 1
            if plant.chomp > 0:
                plant.chomp -= 1

            if dist < TILE * 1.2:
                plant.chomp = 10
                if plant.bite_cd <= 0 and self.player.invuln <= 0:
                    self.player.hp = max(0, self.player.hp - 8)
                    self.player.invuln = 30
                    plant.bite_cd = 45

    def update_pigs(self):
        for pig in self.pigs:
            pig.change_timer -= 1
            if pig.change_timer <= 0:
                pig.dir = random.choice([-1, 1])
                pig.change_timer = random.randint(60, 140)
            pig.vy = min(pig.vy + GRAVITY, MAX_FALL)
            pig.move(self.world, pig.dir * 1.2, pig.vy)

    def update_lizards(self):
        for lz in self.lizards:
            if lz.pause_timer > 0:
                lz.pause_timer -= 1
                move_dx = 0
            else:
                lz.change_timer -= 1
                if lz.change_timer <= 0:
                    if random.random() < 0.3:
                        lz.pause_timer = random.randint(20, 50)
                    else:
                        lz.dir = random.choice([-1, 1])
                    lz.change_timer = random.randint(20, 60)
                move_dx = lz.dir * 2.0
            lz.vy = min(lz.vy + GRAVITY, MAX_FALL)
            lz.move(self.world, move_dx, lz.vy)

    def update_fish(self):
        x0, x1, y0, y1 = self.sea_bounds
        for f in self.fish:
            f.change_timer -= 1
            if f.change_timer <= 0:
                f.dir = random.choice([-1, 1])
                f.vdir = random.choice([-1, 1])
                f.change_timer = random.randint(40, 100)
            f.x = clamp(f.x + f.dir * 1.6, x0, x1 - f.w)
            f.y = clamp(f.y + f.vdir * 0.4, y0, y1 - f.h)

    def update_jellyfish(self):
        x0, x1, y0, y1 = self.sea_bounds
        for j in self.jellyfish:
            j.change_timer -= 1
            if j.change_timer <= 0:
                j.vdir = random.choice([-1, 1])
                j.change_timer = random.randint(60, 140)
            j.y = clamp(j.y + j.vdir * 0.25, y0, y1 - j.h)
            j.x = clamp(j.x + math.sin(self.anim_timer * 0.02 + j.phase) * 0.3, x0, x1 - j.w)

    def update_villagers(self):
        for v in self.villagers:
            v.change_timer -= 1
            if v.change_timer <= 0:
                v.dir = random.choice([-1, 1])
                v.change_timer = random.randint(60, 150)
            new_x = v.x + v.dir * 0.9
            if new_x < v.patrol_min_x or new_x > v.patrol_max_x:
                v.dir *= -1
            v.facing = v.dir
            v.vy = min(v.vy + GRAVITY, MAX_FALL)
            v.move(self.world, v.dir * 0.9, v.vy)

    def update_walking_mushrooms(self):
        for wm in self.walking_mushrooms:
            wm.change_timer -= 1
            if wm.change_timer <= 0:
                wm.dir = random.choice([-1, 1])
                wm.change_timer = random.randint(50, 120)
            wm.vy = min(wm.vy + GRAVITY, MAX_FALL)
            wm.move(self.world, wm.dir * 1.0, wm.vy)

    def transform_pig(self, pig):
        self.pigs.remove(pig)
        ally = Ally(pig.x, pig.y, red_eyes=pig.red_eyes)
        self.allies.append(ally)

    def update_allies(self):
        alive_patmen = [pm for pm in self.patmen if pm.hp > 0]
        for ally in self.allies:
            ally.vy = min(ally.vy + GRAVITY, MAX_FALL)
            if ally.laser_cd > 0:
                ally.laser_cd -= 1

            if not alive_patmen:
                ally.move(self.world, 0, ally.vy)
                continue

            target = min(alive_patmen, key=lambda pm: math.hypot(
                pm.center()[0] - ally.center()[0], pm.center()[1] - ally.center()[1]))
            tx_, ty_ = target.center()
            ax, ay = ally.center()
            dx, dy = tx_ - ax, ty_ - ay
            ally.facing = 1 if dx > 0 else -1
            ally.move(self.world, clamp(dx, -2.4, 2.4), ally.vy)

            dist = math.hypot(dx, dy) or 1
            if dist < PATMAN_DETECT_RADIUS and ally.laser_cd <= 0:
                ally.laser_cd = 40 if ally.red_eyes else 60
                vx, vy = dx / dist * LASER_SPEED, dy / dist * LASER_SPEED
                self.player_lasers.append(Laser(ax, ay, vx, vy, "ally", "#00e5ff"))

    def update_iron_golems(self):
        for ig in self.iron_golems:
            ig.vy = min(ig.vy + GRAVITY, MAX_FALL)
            new_x = ig.x + ig.dir * 1.0
            if new_x < ig.patrol_min_x or new_x > ig.patrol_max_x:
                ig.dir *= -1
            ig.facing = ig.dir
            ig.move(self.world, ig.dir * 1.0, ig.vy)

            if ig.punch_cd > 0:
                ig.punch_cd -= 1
            if ig.punch_flash > 0:
                ig.punch_flash -= 1

            igx, igy = ig.center()
            if ig.punch_cd <= 0:
                for cr in self.creepers:
                    if not cr.alive:
                        continue
                    crx, cry = cr.center()
                    if math.hypot(igx - crx, igy - cry) < IRON_GOLEM_PUNCH_RADIUS:
                        cr.alive = False
                        cr.respawn_timer = 150
                        ig.punch_cd = IRON_GOLEM_PUNCH_COOLDOWN
                        ig.punch_flash = 10
                        break

    def update_mushrooms(self):
        p = self.player
        for m in self.mushrooms:
            if m.bounce_cd > 0:
                m.bounce_cd -= 1
            if m.squish > 0:
                m.squish -= 1
            player_rect = (p.x, p.y, p.w, p.h)
            mushroom_rect = (m.x, m.y, m.w, m.h)
            if m.bounce_cd <= 0 and rects_overlap(player_rect, mushroom_rect):
                p.vy = MUSHROOM_BOUNCE_SPEED
                p.on_ground = False
                m.bounce_cd = MUSHROOM_COOLDOWN
                m.squish = 10

    def update_patmen(self):
        px, py = self.player.center()
        for pm in self.patmen:
            if pm.hp <= 0:
                continue
            pmx, pmy = pm.center()
            dist = math.hypot(px - pmx, py - pmy)

            pm.change_timer -= 1
            if pm.change_timer <= 0 or dist < PATMAN_DETECT_RADIUS:
                pm.dir = 1 if px > pmx else -1
                pm.change_timer = random.randint(50, 110)
            pm.facing = pm.dir

            # Patman burrows through solid ground, so it ignores block collision
            # but stays confined to the underground layer.
            tx = max(0, min(WORLD_W - 1, int(pm.x // TILE)))
            min_y = (self.heights[tx] + 2) * TILE
            max_y = (WORLD_H - 2) * TILE
            pm.x = clamp(pm.x + pm.dir * 1.1, TILE, WORLD_W * TILE - TILE - pm.w)
            if dist < PATMAN_DETECT_RADIUS:
                pm.y += clamp(py - pmy, -1.0, 1.0) * 0.6
            pm.y = clamp(pm.y, min_y, max_y)

            if pm.laser_cd > 0:
                pm.laser_cd -= 1
            if pm.flash > 0:
                pm.flash -= 1

            if dist < PATMAN_DETECT_RADIUS and pm.laser_cd <= 0:
                pm.laser_cd = PATMAN_LASER_COOLDOWN
                dx, dy = px - pmx, py - pmy
                dlen = math.hypot(dx, dy) or 1
                vx = dx / dlen * LASER_SPEED
                vy = dy / dlen * LASER_SPEED
                self.patman_lasers.append(Laser(pmx, pmy, vx, vy, "patman", "#39ff14"))

    def on_patman_killed(self, pm):
        x, y = pm.center()
        sword = FallingItem(x - (TILE - 10) / 2, y - (TILE - 10) / 2, "sword")
        sword.vy = -3  # small pop before it settles
        self.items.append(sword)

    def update_lasers(self):
        # Player lasers drill through blocks and damage Patmen.
        still = []
        for laser in self.player_lasers:
            laser.x += laser.vx
            laser.y += laser.vy
            laser.life -= 1
            tx, ty = int(laser.x // TILE), int(laser.y // TILE)
            if 0 <= tx < WORLD_W and 0 <= ty < WORLD_H and self.world[ty][tx] != AIR:
                self.world[ty][tx] = AIR

            hit = False
            for pm in self.patmen:
                if pm.hp <= 0:
                    continue
                pmx, pmy = pm.center()
                if math.hypot(laser.x - pmx, laser.y - pmy) < TILE * 0.8:
                    pm.hp -= PLAYER_LASER_DAMAGE
                    pm.flash = 8
                    hit = True
                    if pm.hp <= 0:
                        self.on_patman_killed(pm)
                    break

            if not hit and laser.owner == "player":
                for pig in list(self.pigs):
                    pgx, pgy = pig.center()
                    if math.hypot(laser.x - pgx, laser.y - pgy) < TILE * 0.8:
                        self.transform_pig(pig)
                        hit = True
                        break

            in_bounds = 0 <= laser.x <= WORLD_W * TILE and 0 <= laser.y <= WORLD_H * TILE
            if laser.life > 0 and not hit and in_bounds:
                still.append(laser)
        self.player_lasers = still

        # Patman lasers hit the player.
        still = []
        px, py = self.player.center()
        for laser in self.patman_lasers:
            laser.x += laser.vx
            laser.y += laser.vy
            laser.life -= 1
            if math.hypot(laser.x - px, laser.y - py) < TILE * 0.7:
                if self.player.invuln <= 0:
                    self.player.hp = max(0, self.player.hp - PATMAN_LASER_DAMAGE)
                    self.player.invuln = 25
                continue
            if laser.life > 0:
                still.append(laser)
        self.patman_lasers = still

    def update_items(self):
        self.item_spawn_timer -= 1
        if self.item_spawn_timer <= 0:
            self.item_spawn_timer = random.randint(90, 180)
            tx = random.randint(2, WORLD_W - 2)
            kind = random.choice(["dart", "bird", "ball"])
            self.items.append(FallingItem(tx * TILE, 0, kind))

        px, py = self.player.center()
        still_alive = []
        for it in self.items:
            it.vy = min(it.vy + GRAVITY * 0.6, MAX_FALL)
            it.move(self.world, 0, it.vy)
            if it.on_ground:
                it.ground_timer += 1

            ix, iy = it.center()
            if math.hypot(px - ix, py - iy) < TILE:
                if it.kind == "dart":
                    self.player.speed_timer = 300
                elif it.kind == "bird":
                    self.player.jump_timer = 300
                elif it.kind == "ball":
                    self.player.laser_unlocked = True
                elif it.kind == "sword":
                    self.player.has_sword = True
                self.player.score += 1
                continue  # collected, drop it

            if it.ground_timer > 240:
                continue  # despawn after sitting too long

            still_alive.append(it)
        self.items = still_alive

    # -------------------------------------------------------------- render
    def render(self):
        c = self.canvas
        c.delete("all")

        tx0 = max(0, int(self.camera_x // TILE) - 1)
        tx1 = min(WORLD_W, int((self.camera_x + VIEW_W) // TILE) + 2)
        ty0 = max(0, int(self.camera_y // TILE) - 1)
        ty1 = min(WORLD_H, int((self.camera_y + VIEW_H) // TILE) + 2)

        for ty in range(ty0, ty1):
            for tx in range(tx0, tx1):
                t = self.world[ty][tx]
                if t == AIR:
                    continue
                x0 = tx * TILE - self.camera_x
                y0 = ty * TILE - self.camera_y
                c.create_rectangle(x0, y0, x0 + TILE, y0 + TILE,
                                    fill=TILE_COLORS[t], outline="#2b2b2b")

        for tree in self.trees:
            self.draw_tree(tree)
        for sw in self.seaweeds:
            self.draw_seaweed(sw)
        for f in self.fish:
            self.draw_fish(f)
        for j in self.jellyfish:
            self.draw_jellyfish(j)
        for plant in self.plants:
            self.draw_plant(plant)
        for m in self.mushrooms:
            self.draw_mushroom(m)
        for pig in self.pigs:
            self.draw_pig(pig)
        for wm in self.walking_mushrooms:
            self.draw_walking_mushroom(wm)
        for lz in self.lizards:
            self.draw_lizard(lz)
        for v in self.villagers:
            self.draw_villager(v)
        for ally in self.allies:
            self.draw_ally(ally)
        for ig in self.iron_golems:
            self.draw_iron_golem(ig)
        for cr in self.creepers:
            if cr.alive:
                self.draw_creeper(cr)
        for pm in self.patmen:
            if pm.hp > 0:
                self.draw_patman(pm)
        for it in self.items:
            self.draw_item(it)
        for laser in self.player_lasers:
            self.draw_laser(laser)
        for laser in self.patman_lasers:
            self.draw_laser(laser)
        self.draw_golem(self.player)

        self.draw_hud()

        if self.game_over:
            c.create_rectangle(0, 0, VIEW_W, VIEW_H, fill="black", stipple="gray50")
            c.create_text(VIEW_W / 2, VIEW_H / 2 - 20, text="เกมโอเวอร์",
                          fill="white", font=("TH Sarabun New", 36, "bold"))
            c.create_text(VIEW_W / 2, VIEW_H / 2 + 30,
                          text=f"เก็บไอเทมได้ {self.player.score} ชิ้น  |  กด R เพื่อเริ่มใหม่",
                          fill="white", font=("TH Sarabun New", 18))

    def w2s(self, wx, wy):
        return wx - self.camera_x, wy - self.camera_y

    def draw_golem(self, p):
        x0, y0 = self.w2s(p.x, p.y)
        x1, y1 = x0 + p.w, y0 + p.h
        body_color = "#e91e63" if p.invuln % 10 < 5 or p.invuln == 0 else "#ffffff"
        # head
        head_h = p.h * 0.3
        self.canvas.create_rectangle(x0, y0, x1, y0 + head_h, fill=body_color, outline="black")
        eye_y = y0 + head_h * 0.4
        self.canvas.create_rectangle(x0 + p.w * 0.25, eye_y, x0 + p.w * 0.4, eye_y + 4, fill="black")
        self.canvas.create_rectangle(x0 + p.w * 0.6, eye_y, x0 + p.w * 0.75, eye_y + 4, fill="black")
        # body
        self.canvas.create_rectangle(x0, y0 + head_h, x1, y1, fill=body_color, outline="black")
        # arms
        arm_y = y0 + head_h + 5
        self.canvas.create_line(x0, arm_y, x0 - 12 * p.facing, arm_y + 15, fill=body_color, width=6)
        self.canvas.create_line(x1, arm_y, x1 + 12 * p.facing, arm_y + 15, fill=body_color, width=6)

    def draw_creeper(self, cr):
        x0, y0 = self.w2s(cr.x, cr.y)
        x1, y1 = x0 + cr.w, y0 + cr.h
        color = "#3fa34d" if cr.fuse is None else ("#ffffff" if cr.fuse % 6 < 3 else "#3fa34d")
        self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="#1b4d24")
        # creeper face
        fw = cr.w * 0.2
        fh = cr.h * 0.15
        fx = x0 + cr.w * 0.2
        fy = y0 + cr.h * 0.2
        self.canvas.create_rectangle(fx, fy, fx + fw, fy + fh, fill="black")
        self.canvas.create_rectangle(fx + cr.w * 0.4, fy, fx + cr.w * 0.4 + fw, fy + fh, fill="black")
        mouth_y = y0 + cr.h * 0.45
        self.canvas.create_rectangle(x0 + cr.w * 0.3, mouth_y, x0 + cr.w * 0.7, mouth_y + cr.h * 0.3,
                                      fill="black")

    def draw_patman(self, pm):
        x0, y0 = self.w2s(pm.x, pm.y)
        x1, y1 = x0 + pm.w, y0 + pm.h
        color = "#ffffff" if pm.flash > 0 else "#1a1a1a"

        body_top = y0 + pm.h * 0.28
        legs_top = y1 - pm.h * 0.3
        leg_w = pm.w * 0.18

        # legs
        self.canvas.create_rectangle(x0 + pm.w * 0.15, legs_top,
                                      x0 + pm.w * 0.15 + leg_w, y1, fill=color, outline="black")
        self.canvas.create_rectangle(x1 - pm.w * 0.15 - leg_w, legs_top,
                                      x1 - pm.w * 0.15, y1, fill=color, outline="black")
        # body
        self.canvas.create_rectangle(x0 + pm.w * 0.12, body_top,
                                      x1 - pm.w * 0.12, legs_top, fill=color, outline="black")
        # arms
        arm_y = body_top + 6
        self.canvas.create_line(x0 + pm.w * 0.12, arm_y, x0 - 10 * pm.facing, arm_y + 14,
                                 fill=color, width=6)
        self.canvas.create_line(x1 - pm.w * 0.12, arm_y, x1 + 10 * pm.facing, arm_y + 14,
                                 fill=color, width=6)
        # head + bat-like ears
        self.canvas.create_oval(x0 + pm.w * 0.2, y0, x1 - pm.w * 0.2, body_top + 4,
                                 fill=color, outline="black")
        ear_h = pm.h * 0.18
        self.canvas.create_polygon(x0 + pm.w * 0.25, y0 + 4, x0 + pm.w * 0.32, y0 - ear_h,
                                    x0 + pm.w * 0.42, y0 + 4, fill=color, outline="black")
        self.canvas.create_polygon(x1 - pm.w * 0.25, y0 + 4, x1 - pm.w * 0.32, y0 - ear_h,
                                    x1 - pm.w * 0.42, y0 + 4, fill=color, outline="black")
        # glowing laser eyes
        eye_y = y0 + pm.h * 0.12
        self.canvas.create_oval(x0 + pm.w * 0.3, eye_y, x0 + pm.w * 0.3 + 5, eye_y + 5, fill="#39ff14")
        self.canvas.create_oval(x1 - pm.w * 0.3 - 5, eye_y, x1 - pm.w * 0.3, eye_y + 5, fill="#39ff14")
        # hp bar
        hp_w = pm.w * (pm.hp / pm.max_hp)
        self.canvas.create_rectangle(x0, y0 - 10, x1, y0 - 5, fill="#333333", outline="")
        self.canvas.create_rectangle(x0, y0 - 10, x0 + hp_w, y0 - 5, fill="#39ff14", outline="")

    def draw_laser(self, laser):
        x0, y0 = self.w2s(laser.x, laser.y)
        length = 14
        ang = math.atan2(laser.vy, laser.vx) if (laser.vx or laser.vy) else 0
        x1 = x0 - math.cos(ang) * length
        y1 = y0 - math.sin(ang) * length
        self.canvas.create_line(x1, y1, x0, y0, fill=laser.color, width=4)

    def draw_villager(self, v):
        x0, y0 = self.w2s(v.x, v.y)
        x1, y1 = x0 + v.w, y0 + v.h
        robe_color = "#8d6e4a"
        head_h = v.h * 0.32
        # robe/body (trapezoid-ish via rectangle for simplicity)
        self.canvas.create_rectangle(x0, y0 + head_h, x1, y1, fill=robe_color, outline="#5c452c")
        # head
        self.canvas.create_oval(x0, y0, x1, y0 + head_h, fill="#e0b088", outline="#5c452c")
        # simple face nose (villager-style)
        nose_cx = (x0 + x1) / 2 + v.facing * (v.w * 0.15)
        nose_cy = y0 + head_h * 0.55
        self.canvas.create_oval(nose_cx - 2, nose_cy - 3, nose_cx + 2, nose_cy + 5,
                                 fill="#c98f5e", outline="")
        # hat/band
        self.canvas.create_rectangle(x0, y0 + head_h * 0.7, x1, y0 + head_h * 0.85,
                                      fill="#5c452c", outline="")

    def draw_walking_mushroom(self, wm):
        x0, y0 = self.w2s(wm.x, wm.y)
        x1, y1 = x0 + wm.w, y0 + wm.h
        cap_bottom = y0 + wm.h * 0.55
        stem_w = wm.w * 0.5
        stem_x0 = x0 + (wm.w - stem_w) / 2
        # little legs
        leg_w = wm.w * 0.15
        self.canvas.create_rectangle(stem_x0 + 2, y1 - 5, stem_x0 + 2 + leg_w, y1 + 4,
                                      fill="#fff3d6", outline="#c9a86a")
        self.canvas.create_rectangle(x1 - stem_x0 - leg_w - 2, y1 - 5, x1 - stem_x0 - 2, y1 + 4,
                                      fill="#fff3d6", outline="#c9a86a")
        # stem
        self.canvas.create_rectangle(stem_x0, cap_bottom, stem_x0 + stem_w, y1,
                                      fill="#fff3d6", outline="#c9a86a")
        # cap
        self.canvas.create_arc(x0, y0, x1, cap_bottom + (cap_bottom - y0),
                                start=0, extent=180, fill="#e53935", outline="#7a1f1a", width=2)
        # spots
        cap_h = cap_bottom - y0
        for sx, sy, r in ((0.3, 0.4, 2.5), (0.6, 0.25, 2), (0.75, 0.5, 2.5)):
            spx = x0 + wm.w * sx
            spy = y0 + cap_h * sy
            self.canvas.create_oval(spx - r, spy - r, spx + r, spy + r, fill="white", outline="")

    def draw_mushroom(self, m):
        x0, y0 = self.w2s(m.x, m.y)
        x1, y1 = x0 + m.w, y0 + m.h
        squash = min(m.squish, 8)
        y0 += squash  # cap squishes down briefly after a bounce
        cap_bottom = y0 + (y1 - y0) * 0.45
        stem_w = m.w * 0.4
        stem_x0 = x0 + (m.w - stem_w) / 2
        # stem
        self.canvas.create_rectangle(stem_x0, cap_bottom, stem_x0 + stem_w, y1,
                                      fill="#fff3d6", outline="#c9a86a")
        # cap
        self.canvas.create_arc(x0, y0, x1, cap_bottom + (cap_bottom - y0),
                                start=0, extent=180, fill="#e53935", outline="#7a1f1a", width=2)
        # spots
        cap_h = cap_bottom - y0
        for sx, sy, r in ((0.28, 0.35, 3), (0.55, 0.2, 2.5), (0.72, 0.45, 3)):
            spx = x0 + m.w * sx
            spy = y0 + cap_h * sy
            self.canvas.create_oval(spx - r, spy - r, spx + r, spy + r, fill="white", outline="")

    def draw_pig(self, pig):
        if pig.kind == "chicken":
            self.draw_chicken(pig)
        elif pig.kind == "cow":
            self.draw_cow(pig)
        elif pig.kind == "worm":
            self.draw_worm(pig)
        else:
            self.draw_pig_body(pig)

    def draw_pig_body(self, pig):
        x0, y0 = self.w2s(pig.x, pig.y)
        x1, y1 = x0 + pig.w, y0 + pig.h
        body_color = "#ffb3c6" if not pig.red_eyes else "#ff8fa8"
        self.canvas.create_oval(x0, y0 + pig.h * 0.15, x1, y1, fill=body_color, outline="#c2607e")
        # ears
        self.canvas.create_polygon(x0 + pig.w * 0.1, y0 + pig.h * 0.2, x0 + pig.w * 0.25, y0,
                                    x0 + pig.w * 0.4, y0 + pig.h * 0.2, fill=body_color, outline="#c2607e")
        self.canvas.create_polygon(x1 - pig.w * 0.1, y0 + pig.h * 0.2, x1 - pig.w * 0.25, y0,
                                    x1 - pig.w * 0.4, y0 + pig.h * 0.2, fill=body_color, outline="#c2607e")
        # snout
        snout_cx = (x0 + x1) / 2
        snout_y = y0 + pig.h * 0.55
        self.canvas.create_oval(snout_cx - 8, snout_y - 5, snout_cx + 8, snout_y + 5,
                                 fill="#ff7f9e", outline="#c2607e")
        self.canvas.create_oval(snout_cx - 4, snout_y - 2, snout_cx - 1, snout_y + 1, fill="#8a3b4f")
        self.canvas.create_oval(snout_cx + 1, snout_y - 2, snout_cx + 4, snout_y + 1, fill="#8a3b4f")
        # eyes
        eye_color = "#e53935" if pig.red_eyes else "#3e2723"
        eye_y = y0 + pig.h * 0.3
        self.canvas.create_oval(x0 + pig.w * 0.25, eye_y, x0 + pig.w * 0.25 + 5, eye_y + 5, fill=eye_color)
        self.canvas.create_oval(x1 - pig.w * 0.25 - 5, eye_y, x1 - pig.w * 0.25, eye_y + 5, fill=eye_color)

    def draw_chicken(self, ch):
        x0, y0 = self.w2s(ch.x, ch.y)
        x1, y1 = x0 + ch.w, y0 + ch.h
        body_color = "#ffc1d9"
        self.canvas.create_oval(x0, y0 + ch.h * 0.2, x1, y1, fill=body_color, outline="#d9789e")
        # head
        head_r = ch.w * 0.28
        hx, hy = x1 - head_r * 0.6, y0 + ch.h * 0.3
        self.canvas.create_oval(hx - head_r, hy - head_r, hx + head_r, hy + head_r,
                                 fill=body_color, outline="#d9789e")
        # comb
        self.canvas.create_polygon(hx - 3, hy - head_r, hx, hy - head_r - 6, hx + 3, hy - head_r,
                                    fill="#e53935")
        # beak
        self.canvas.create_polygon(hx + head_r, hy, hx + head_r + 7, hy + 2, hx + head_r, hy + 4,
                                    fill="#ffb300")
        # eye
        self.canvas.create_oval(hx + 2, hy - 3, hx + 5, hy, fill="#3e2723")
        # wing
        self.canvas.create_oval(x0 + ch.w * 0.15, y0 + ch.h * 0.45, x0 + ch.w * 0.55, y1 - 2,
                                 fill="#ff8fb3", outline="")

    def draw_cow(self, cow):
        x0, y0 = self.w2s(cow.x, cow.y)
        x1, y1 = x0 + cow.w, y0 + cow.h
        body_color = "#ffb3c6"
        self.canvas.create_oval(x0, y0 + cow.h * 0.15, x1, y1, fill=body_color, outline="#c2607e", width=2)
        # pink/white spots
        for sx, sy, r in ((0.25, 0.4, 8), (0.6, 0.6, 7), (0.75, 0.3, 6)):
            spx = x0 + cow.w * sx
            spy = y0 + cow.h * sy
            self.canvas.create_oval(spx - r, spy - r, spx + r, spy + r, fill="#ffe6ee", outline="")
        # ears/horns
        self.canvas.create_line(x0 + cow.w * 0.15, y0 + cow.h * 0.2, x0 + cow.w * 0.05, y0,
                                 fill="#e8b4bf", width=4)
        self.canvas.create_line(x1 - cow.w * 0.15, y0 + cow.h * 0.2, x1 - cow.w * 0.05, y0,
                                 fill="#e8b4bf", width=4)
        # snout
        snout_cx = (x0 + x1) / 2
        snout_y = y0 + cow.h * 0.6
        self.canvas.create_oval(snout_cx - 10, snout_y - 6, snout_cx + 10, snout_y + 6,
                                 fill="#ff7f9e", outline="#c2607e")
        self.canvas.create_oval(snout_cx - 5, snout_y - 2, snout_cx - 2, snout_y + 1, fill="#8a3b4f")
        self.canvas.create_oval(snout_cx + 2, snout_y - 2, snout_cx + 5, snout_y + 1, fill="#8a3b4f")
        # eyes
        eye_y = y0 + cow.h * 0.3
        self.canvas.create_oval(x0 + cow.w * 0.28, eye_y, x0 + cow.w * 0.28 + 5, eye_y + 5, fill="#3e2723")
        self.canvas.create_oval(x1 - cow.w * 0.28 - 5, eye_y, x1 - cow.w * 0.28, eye_y + 5, fill="#3e2723")

    def draw_worm(self, worm):
        x0, y0 = self.w2s(worm.x, worm.y)
        x1, y1 = x0 + worm.w, y0 + worm.h
        cy = (y0 + y1) / 2
        segs = 4
        seg_w = worm.w / segs
        for i in range(segs):
            sx0 = x0 + i * seg_w
            color = "#ff9ebd" if i % 2 == 0 else "#ff7fa8"
            self.canvas.create_oval(sx0, y0, sx0 + seg_w + 2, y1, fill=color, outline="#d9789e")
        # eyes at the front segment
        eye_x = x1 - seg_w * 0.4
        self.canvas.create_oval(eye_x - 2, cy - 5, eye_x + 2, cy - 1, fill="#3e2723")
        self.canvas.create_oval(eye_x - 2, cy + 1, eye_x + 2, cy + 5, fill="#3e2723")

    def draw_ally(self, ally):
        x0, y0 = self.w2s(ally.x, ally.y)
        x1, y1 = x0 + ally.w, y0 + ally.h
        body_color = "#ff6fae" if not ally.red_eyes else "#ff3d7f"
        head_h = ally.h * 0.3
        self.canvas.create_rectangle(x0, y0, x1, y0 + head_h, fill=body_color, outline="#00e5ff")
        eye_y = y0 + head_h * 0.4
        self.canvas.create_rectangle(x0 + ally.w * 0.25, eye_y, x0 + ally.w * 0.4, eye_y + 4, fill="black")
        self.canvas.create_rectangle(x0 + ally.w * 0.6, eye_y, x0 + ally.w * 0.75, eye_y + 4, fill="black")
        self.canvas.create_rectangle(x0, y0 + head_h, x1, y1, fill=body_color, outline="#00e5ff")
        arm_y = y0 + head_h + 5
        self.canvas.create_line(x0, arm_y, x0 - 12 * ally.facing, arm_y + 15, fill=body_color, width=6)
        self.canvas.create_line(x1, arm_y, x1 + 12 * ally.facing, arm_y + 15, fill=body_color, width=6)

    def draw_iron_golem(self, ig):
        x0, y0 = self.w2s(ig.x, ig.y)
        x1, y1 = x0 + ig.w, y0 + ig.h
        color = "#eeeeee" if ig.punch_flash > 0 else "#9e9e9e"
        legs_top = y1 - ig.h * 0.28
        leg_w = ig.w * 0.22
        # legs
        self.canvas.create_rectangle(x0 + ig.w * 0.12, legs_top, x0 + ig.w * 0.12 + leg_w, y1,
                                      fill=color, outline="#4a4a4a", width=2)
        self.canvas.create_rectangle(x1 - ig.w * 0.12 - leg_w, legs_top, x1 - ig.w * 0.12, y1,
                                      fill=color, outline="#4a4a4a", width=2)
        # body
        body_top = y0 + ig.h * 0.28
        self.canvas.create_rectangle(x0 + ig.w * 0.05, body_top, x1 - ig.w * 0.05, legs_top,
                                      fill=color, outline="#4a4a4a", width=2)
        # arms (thick, iron-golem style)
        arm_y = body_top + 4
        self.canvas.create_rectangle(x0 - ig.w * 0.18, arm_y, x0 + ig.w * 0.05, arm_y + ig.h * 0.4,
                                      fill=color, outline="#4a4a4a", width=2)
        self.canvas.create_rectangle(x1 - ig.w * 0.05, arm_y, x1 + ig.w * 0.18, arm_y + ig.h * 0.4,
                                      fill=color, outline="#4a4a4a", width=2)
        # head
        self.canvas.create_rectangle(x0 + ig.w * 0.2, y0, x1 - ig.w * 0.2, body_top + 2,
                                      fill=color, outline="#4a4a4a", width=2)
        eye_y = y0 + ig.h * 0.1
        self.canvas.create_rectangle(x0 + ig.w * 0.3, eye_y, x0 + ig.w * 0.3 + 5, eye_y + 5, fill="#e53935")
        self.canvas.create_rectangle(x1 - ig.w * 0.3 - 5, eye_y, x1 - ig.w * 0.3, eye_y + 5, fill="#e53935")
        # rust/plate details
        self.canvas.create_line(x0 + ig.w * 0.05, body_top + ig.h * 0.15, x1 - ig.w * 0.05,
                                 body_top + ig.h * 0.15, fill="#6b6b6b")

    def draw_seaweed(self, sw):
        x0, y0 = self.w2s(sw.x, sw.y)
        x1, y1 = x0 + sw.w, y0 + sw.h
        cx = (x0 + x1) / 2
        base_y = y1
        sway = math.sin(self.anim_timer * 0.04 + sw.phase) * (sw.w * 1.5)
        segs = 4
        points = []
        for i in range(segs + 1):
            frac = i / segs
            py = base_y - (base_y - y0) * frac
            px = cx + sway * (frac * frac)
            points.extend([px, py])
        self.canvas.create_line(*points, fill="#2e7d4f", width=max(3, int(sw.w * 0.4)),
                                 smooth=True, capstyle="round")

    def draw_fish(self, f):
        x0, y0 = self.w2s(f.x, f.y)
        x1, y1 = x0 + f.w, y0 + f.h
        cy = (y0 + y1) / 2
        body_color = "#ff8a3d" if f.dir > 0 else "#ffb74d"
        head_x = x1 if f.dir > 0 else x0
        tail_x = x0 if f.dir > 0 else x1
        self.canvas.create_oval(x0 + f.w * 0.15, y0, x1 - f.w * 0.15, y1, fill=body_color, outline="#c9660a")
        tail_mid = tail_x + (f.w * 0.2 if f.dir > 0 else -f.w * 0.2)
        self.canvas.create_polygon(tail_x, cy, tail_mid, y0, tail_mid, y1, fill=body_color, outline="#c9660a")
        eye_x = head_x - (f.w * 0.22 if f.dir > 0 else -f.w * 0.22)
        self.canvas.create_oval(eye_x - 2, cy - 3, eye_x + 2, cy + 1, fill="#212121")

    def draw_jellyfish(self, j):
        x0, y0 = self.w2s(j.x, j.y)
        x1, y1 = x0 + j.w, y0 + j.h
        pulse = math.sin(self.anim_timer * 0.05 + j.phase) * (j.h * 0.08)
        bell_bottom = y0 + j.h * 0.55 + pulse
        self.canvas.create_arc(x0, y0, x1, bell_bottom + (bell_bottom - y0),
                                start=0, extent=180, fill="#ce93d8", outline="#8e24aa",
                                stipple="gray50", width=1)
        tentacle_count = 4
        for i in range(tentacle_count):
            tx = x0 + (i + 0.5) * (j.w / tentacle_count)
            wobble = math.sin(self.anim_timer * 0.08 + j.phase + i) * 4
            self.canvas.create_line(tx, bell_bottom, tx + wobble, y1, fill="#ba68c8", width=2)

    def draw_tree(self, tree):
        x0, y0 = self.w2s(tree.x, tree.y)
        x1, y1 = x0 + tree.w, y0 + tree.h
        trunk_w = tree.w * 0.22
        trunk_x0 = (x0 + x1) / 2 - trunk_w / 2
        trunk_top = y0 + tree.h * 0.4
        self.canvas.create_rectangle(trunk_x0, trunk_top, trunk_x0 + trunk_w, y1,
                                      fill="#6d4c28", outline="#4a3218")
        # layered canopy (three overlapping blobs for a fuller look)
        cx = (x0 + x1) / 2
        canopy_r = tree.w * 0.55
        self.canvas.create_oval(cx - canopy_r, y0, cx + canopy_r, y0 + tree.h * 0.55,
                                 fill="#2e7d32", outline="#1b5e20")
        self.canvas.create_oval(cx - canopy_r * 0.75, y0 - tree.h * 0.1,
                                 cx + canopy_r * 0.4, y0 + tree.h * 0.32,
                                 fill="#388e3c", outline="")
        self.canvas.create_oval(cx - canopy_r * 0.3, y0 - tree.h * 0.15,
                                 cx + canopy_r * 0.85, y0 + tree.h * 0.28,
                                 fill="#43a047", outline="")

    def draw_lizard(self, lz):
        x0, y0 = self.w2s(lz.x, lz.y)
        x1, y1 = x0 + lz.w, y0 + lz.h
        body_color = "#7cb342"
        # tail
        self.canvas.create_line(x0, (y0 + y1) / 2, x0 - lz.w * 0.35, y1, fill=body_color, width=4)
        # body
        self.canvas.create_oval(x0, y0, x1 - lz.w * 0.15, y1, fill=body_color, outline="#4a7c1f")
        # spots
        for sx, sy in ((0.3, 0.3), (0.55, 0.6)):
            spx = x0 + lz.w * sx
            spy = y0 + lz.h * sy
            self.canvas.create_oval(spx - 2, spy - 2, spx + 2, spy + 2, fill="#33691e")
        # head + eye
        head_cx = x1 - lz.w * 0.2
        head_cy = (y0 + y1) / 2
        self.canvas.create_oval(head_cx - lz.w * 0.18, y0, x1, y1, fill=body_color, outline="#4a7c1f")
        self.canvas.create_oval(x1 - 5, head_cy - 3, x1 - 1, head_cy + 1, fill="#212121")

    def draw_plant(self, plant):
        x0, y0 = self.w2s(plant.x, plant.y)
        x1, y1 = x0 + plant.w, y0 + plant.h
        stem_x = (x0 + x1) / 2
        self.canvas.create_line(stem_x, y1, stem_x, y0 + plant.h * 0.4, fill="#2e7d32", width=5)
        mouth_open = 6 + plant.chomp
        self.canvas.create_polygon(
            x0, y0 + plant.h * 0.4,
            x1, y0 + plant.h * 0.4,
            stem_x, y0 - mouth_open,
            fill="#43a047", outline="#1b5e20")
        # teeth
        for i in range(4):
            tx = x0 + (x1 - x0) * (i / 3)
            self.canvas.create_line(tx, y0 + plant.h * 0.4, tx, y0 + plant.h * 0.4 - 6, fill="white")
        # roots
        for dx in (-8, 0, 8):
            self.canvas.create_line(stem_x, y1, stem_x + dx, y1 + 10, fill="#2e7d32", width=3)

    def draw_item(self, it):
        x0, y0 = self.w2s(it.x, it.y)
        x1, y1 = x0 + it.w, y0 + it.h
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        if it.kind == "dart":
            self.canvas.create_polygon(cx, y0, x1, cy, cx, y1, x0, cy,
                                        fill="#2b2b2b", outline="#3fa34d", width=2)
        elif it.kind == "bird":
            self.canvas.create_oval(x0, y0, x1, y1, fill="#e91e63", outline="#1976d2", width=2)
            self.canvas.create_polygon(cx, y0, x1, cy, cx, cy, fill="#cddc39")
        elif it.kind == "ball":
            self.canvas.create_oval(x0, y0, x1, y1, fill="#ff9800", outline="#5d4037", width=2)
            self.canvas.create_line(x0, cy, x1, cy, fill="#5d4037")
            self.canvas.create_line(cx, y0, cx, y1, fill="#5d4037")
        elif it.kind == "sword":
            self.canvas.create_line(cx, y0, cx, y1 - 4, fill="#cfd8dc", width=4)
            self.canvas.create_line(x0 + 3, y1 - 8, x1 - 3, y1 - 8, fill="#8d6e63", width=4)
            self.canvas.create_rectangle(cx - 3, y1 - 6, cx + 3, y1, fill="#4e342e")

    def draw_hud(self):
        c = self.canvas
        p = self.player
        # health bar
        c.create_rectangle(10, 10, 210, 30, fill="#333333", outline="white")
        hp_w = 200 * (p.hp / p.max_hp)
        c.create_rectangle(10, 10, 10 + hp_w, 30, fill="#e53935", outline="")
        c.create_text(110, 20, text=f"HP {p.hp}/{p.max_hp}", fill="white")

        # laser status
        c.create_rectangle(10, 34, 210, 52, fill="#333333", outline="white")
        if p.laser_unlocked:
            c.create_rectangle(10, 34, 210, 52, fill="#ff2fd6", outline="")
            laser_text = "เลเซอร์: ไม่จำกัด (กด F ยิง)"
        else:
            laser_text = "เก็บลูกบอลเพื่อปลดล็อกเลเซอร์"
        c.create_text(110, 43, text=laser_text, fill="white", font=("TH Sarabun New", 9))

        c.create_text(10, 70, anchor="w", text=f"ไอเทมที่เก็บได้: {p.score}", fill="black",
                      font=("TH Sarabun New", 12, "bold"))

        buffs = []
        if p.speed_timer > 0:
            buffs.append(f"ความเร็ว +70% ({p.speed_timer // 30 + 1}s)")
        if p.jump_timer > 0:
            buffs.append(f"กระโดดสูง ({p.jump_timer // 30 + 1}s)")
        if buffs:
            c.create_text(10, 90, anchor="w", text=" | ".join(buffs), fill="#1565c0",
                          font=("TH Sarabun New", 11))

        if p.has_sword:
            c.create_text(10, 110, anchor="w", text="ได้ดาบจากแพทแมนแล้ว!", fill="#6a1b9a",
                          font=("TH Sarabun New", 11, "bold"))

        ore_text = (f"ถ่านหิน {p.ores[COAL]}  เหล็ก {p.ores[IRON]}  "
                    f"ทอง {p.ores[GOLD]}  เพชร {p.ores[DIAMOND]}")
        c.create_text(10, 130, anchor="w", text=ore_text, fill="#37474f",
                      font=("TH Sarabun New", 11, "bold"))

        c.create_text(VIEW_W - 10, 20, anchor="e",
                      text=f"บล็อกที่เลือก: {TILE_NAMES[self.selected_block]} (กด 1/2/3)",
                      fill="black", font=("TH Sarabun New", 12, "bold"))
        c.create_text(VIEW_W - 10, 45, anchor="e",
                      text="A/D เดิน | W/Space กระโดด | คลิกซ้ายขุด | คลิกขวาวาง | F ยิงเลเซอร์",
                      fill="black", font=("TH Sarabun New", 10))


def rects_overlap(a, b):
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    return ax < bx + bw and ax + aw > bx and ay < by + bh and ay + ah > by


def clamp(v, lo, hi):
    if hi < lo:
        return lo
    return max(lo, min(hi, v))


if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()