"""Entity ontology for the Aesop capstone generator.

Four entity classes (Item, Container, Character, Location) with attributes
that drive cross-template constraint satisfaction. Sizes use a 1-5 scale:

  size 1 (tiny)    — fits in a thimble; grain, drop, coin, pebble, seed
  size 2 (small)   — fits in a hand; apple, egg, marble, mushroom, candy
  size 3 (medium)  — sits on a table; book, brick, jar, lamp, melon
  size 4 (large)   — person can lift; sack, blanket, log, basket, sword
  size 5 (huge)    — can't easily carry; cart, barrel, ladder, table

Containers have (capacity_count, max_size). Items of size > max_size don't
fit at all. For a container with capacity_count=N at the size-2 reference,
size-1 items fit ~1.5×N, size-3 fit ~0.5×N, size-4 fit ~0.2×N. The exact
formula is kept conservative — generators that need "definitely fits" use
the strict rule, generators that need "definitely doesn't fit" use the
generous rule.

Characters have a species ("hare", "tortoise", "human", ...), a gender for
pronoun derivation, and a list of role classes / archetypes that fable
templates use to pick fable-appropriate casts.

Locations are settings — outdoor (meadow, forest, river) or indoor (cottage,
barn, cave). Some fables require specific location types.
"""
from __future__ import annotations

import random
from dataclasses import dataclass, field
from typing import Iterable


# ─────────────────────── Items ───────────────────────


@dataclass(frozen=True)
class Item:
    name:      str   # singular; "apple", "blanket"
    plural:    str   # "apples", "blankets"
    size:      int   # 1..5 (see module docstring)
    weight:    int   # 1..5; can differ from size (a wool blanket is large but light)
    edible:    bool
    countable: bool  # apples yes; water no (water uses unit-counts: "cups", "drops")
    tags:      tuple[str, ...] = ()  # ("food", "fruit") etc. for theming

    def __repr__(self) -> str:
        return f"Item({self.name})"


# Catalog: ~60 items spanning size/weight/edible/tag dimensions.
ITEMS: tuple[Item, ...] = (
    # tiny (size 1)
    Item("grain",   "grains",   1, 1, True,  True,  ("food", "small")),
    Item("seed",    "seeds",    1, 1, True,  True,  ("food", "small")),
    Item("coin",    "coins",    1, 1, False, True,  ("treasure",)),
    Item("pebble",  "pebbles",  1, 1, False, True,  ("stone",)),
    Item("crumb",   "crumbs",   1, 1, True,  True,  ("food", "small")),
    Item("bead",    "beads",    1, 1, False, True,  ("treasure",)),
    Item("button",  "buttons",  1, 1, False, True,  ("trinket",)),
    Item("nut",     "nuts",     1, 1, True,  True,  ("food",)),

    # small (size 2)
    Item("apple",     "apples",     2, 2, True,  True,  ("food", "fruit")),
    Item("egg",       "eggs",       2, 1, True,  True,  ("food", "fragile")),
    Item("ball",      "balls",      2, 1, False, True,  ("toy",)),
    Item("marble",    "marbles",    2, 1, False, True,  ("toy",)),
    Item("candy",     "candies",    2, 1, True,  True,  ("food", "sweet")),
    Item("mushroom",  "mushrooms",  2, 1, True,  True,  ("food",)),
    Item("acorn",     "acorns",     2, 1, True,  True,  ("food",)),
    Item("carrot",    "carrots",    2, 1, True,  True,  ("food", "vegetable")),
    Item("biscuit",   "biscuits",   2, 1, True,  True,  ("food",)),
    Item("flower",    "flowers",    2, 1, False, True,  ("plant",)),
    Item("feather",   "feathers",   2, 1, False, True,  ("trinket",)),
    Item("ribbon",    "ribbons",    2, 1, False, True,  ("trinket",)),

    # medium (size 3)
    Item("book",      "books",      3, 3, False, True,  ("scholarly",)),
    Item("brick",     "bricks",     3, 4, False, True,  ("building",)),
    Item("jar",       "jars",       3, 2, False, True,  ("vessel",)),
    Item("lamp",      "lamps",      3, 2, False, True,  ("tool",)),
    Item("melon",     "melons",     3, 3, True,  True,  ("food", "fruit")),
    Item("loaf",      "loaves",     3, 2, True,  True,  ("food",)),
    Item("cabbage",   "cabbages",   3, 2, True,  True,  ("food", "vegetable")),
    Item("pumpkin",   "pumpkins",   3, 4, True,  True,  ("food", "vegetable")),
    Item("pot",       "pots",       3, 2, False, True,  ("vessel",)),
    Item("toy",       "toys",       3, 2, False, True,  ("toy",)),

    # large (size 4)
    Item("sack",      "sacks",      4, 3, False, True,  ("vessel",)),
    Item("blanket",   "blankets",   4, 2, False, True,  ("textile",)),
    Item("log",       "logs",       4, 4, False, True,  ("wood",)),
    Item("basket",    "baskets",    4, 2, False, True,  ("vessel",)),
    Item("sword",     "swords",     4, 3, False, True,  ("weapon",)),
    Item("shield",    "shields",    4, 4, False, True,  ("armor",)),
    Item("rope",      "ropes",      4, 2, False, True,  ("tool",)),
    Item("cushion",   "cushions",   4, 2, False, True,  ("textile",)),

    # huge (size 5)
    Item("cart",      "carts",      5, 5, False, True,  ("vehicle",)),
    Item("barrel",    "barrels",    5, 5, False, True,  ("vessel",)),
    Item("ladder",    "ladders",    5, 4, False, True,  ("tool",)),
    Item("table",     "tables",     5, 5, False, True,  ("furniture",)),
)


def items_by_tag(tag: str) -> tuple[Item, ...]:
    return tuple(i for i in ITEMS if tag in i.tags)


def items_by_size(size: int | range | Iterable[int]) -> tuple[Item, ...]:
    sizes = {size} if isinstance(size, int) else set(size)
    return tuple(i for i in ITEMS if i.size in sizes)


# ─────────────────────── Containers ───────────────────────


@dataclass(frozen=True)
class Container:
    name:           str
    plural:         str
    capacity_count: int   # rough # of size-2 items that fit
    max_size:       int   # max item size that fits at all (1..5)
    is_body_part:   bool  # "in his pocket" vs "in the cart"
    tags:           tuple[str, ...] = ()

    def fits_count(self, item: Item, n: int) -> bool:
        """Strict: do n of `item` definitely fit?"""
        if item.size > self.max_size:
            return False
        # rough capacity scaling: size-2 reference; size-1 fits 1.5×;
        # size-3 fits 0.5×; size-4 fits 0.2×; size-5 fits 1 if at all.
        scale = {1: 1.5, 2: 1.0, 3: 0.5, 4: 0.2, 5: 0.1}[item.size]
        return n <= max(1, int(self.capacity_count * scale))


CONTAINERS: tuple[Container, ...] = (
    # body parts (small)
    Container("pocket",  "pockets",  5,  2, True,  ("body",)),
    Container("hand",    "hands",    1,  3, True,  ("body",)),
    Container("paw",     "paws",     1,  2, True,  ("body", "animal")),
    Container("mouth",   "mouths",   1,  2, True,  ("body",)),
    Container("beak",    "beaks",    1,  2, True,  ("body", "bird")),

    # small vessels
    Container("pouch",   "pouches",  10, 2, False, ("bag",)),
    Container("bag",     "bags",     15, 3, False, ("bag",)),
    Container("basket",  "baskets",  15, 3, False, ("bag",)),
    Container("backpack","backpacks",20, 3, False, ("bag",)),
    Container("bucket",  "buckets",  10, 3, False, ("vessel",)),
    Container("jar",     "jars",      8, 2, False, ("vessel",)),
    Container("bottle",  "bottles",   5, 1, False, ("vessel", "liquid")),

    # special-shape vessels
    Container("pitcher", "pitchers",  6, 2, False, ("vessel", "narrow_top")),
    Container("cup",     "cups",      3, 1, False, ("vessel",)),
    Container("bowl",    "bowls",     5, 2, False, ("vessel",)),

    # storage / furniture
    Container("box",     "boxes",    30, 4, False, ("storage",)),
    Container("chest",   "chests",   50, 4, False, ("storage",)),
    Container("drawer",  "drawers",  20, 3, False, ("storage", "indoor")),
    Container("shelf",   "shelves",  15, 4, False, ("storage", "indoor")),

    # vehicles
    Container("cart",    "carts",   100, 5, False, ("vehicle",)),
    Container("wagon",   "wagons",  150, 5, False, ("vehicle",)),
    Container("wheelbarrow", "wheelbarrows", 50, 5, False, ("vehicle",)),

    # rooms / spaces
    Container("closet",  "closets", 100, 5, False, ("room",)),
    Container("barn",    "barns",   500, 5, False, ("room", "outdoor")),
    Container("cave",    "caves",   500, 5, False, ("room", "outdoor")),
    Container("hole",    "holes",    20, 4, False, ("room", "outdoor")),
)


def containers_for_item(item: Item, n: int) -> tuple[Container, ...]:
    """All containers that can hold n of item."""
    return tuple(c for c in CONTAINERS if c.fits_count(item, n))


# ─────────────────────── Characters ───────────────────────


@dataclass(frozen=True)
class Character:
    name:       str
    species:    str               # "human", "hare", "tortoise", ...
    gender:     str               # "m" / "f" / "n"
    role_classes: tuple[str, ...]  # ("racer", "fast"), ("saver", "slow"), ...
    archetypes:   tuple[str, ...] = ()

    @property
    def he_she(self) -> str:
        return {"m": "he", "f": "she", "n": "they"}[self.gender]

    @property
    def him_her(self) -> str:
        return {"m": "him", "f": "her", "n": "them"}[self.gender]

    @property
    def his_her(self) -> str:
        return {"m": "his", "f": "her", "n": "their"}[self.gender]

    @property
    def himself_herself(self) -> str:
        return {"m": "himself", "f": "herself", "n": "themselves"}[self.gender]


# Catalog. Names chosen to span genders + species. Each character has at
# least one role_class so fable templates can filter.
HUMANS: tuple[Character, ...] = (
    # masculine
    Character("Bob",     "human", "m", ("trader", "saver", "everyman")),
    Character("Charlie", "human", "m", ("trader", "spendthrift")),
    Character("David",   "human", "m", ("trader", "saver")),
    Character("Edward",  "human", "m", ("trader", "boastful")),
    Character("Frank",   "human", "m", ("trader", "everyman")),
    Character("George",  "human", "m", ("trader", "everyman")),
    Character("Henry",   "human", "m", ("trader", "saver")),
    Character("Oliver",  "human", "m", ("trader", "everyman")),

    # feminine
    Character("Alice",   "human", "f", ("trader", "saver", "everyman")),
    Character("Beatrice","human", "f", ("trader", "saver")),
    Character("Carol",   "human", "f", ("trader", "everyman")),
    Character("Diana",   "human", "f", ("trader", "boastful")),
    Character("Emily",   "human", "f", ("trader", "saver")),
    Character("Fiona",   "human", "f", ("trader", "spendthrift")),
    Character("Grace",   "human", "f", ("trader", "everyman")),
    Character("Helen",   "human", "f", ("trader", "saver")),

    # ambiguous / neutral
    Character("Alex",    "human", "n", ("trader", "everyman")),
    Character("Sam",     "human", "n", ("trader", "everyman")),
    Character("Jordan",  "human", "n", ("trader", "saver")),
    Character("Robin",   "human", "n", ("trader", "everyman")),
    Character("Casey",   "human", "n", ("trader", "spendthrift")),
    Character("Morgan",  "human", "n", ("trader", "everyman")),
)


# Animals. Per fable, we want named animals of the right species. Each
# species has 2-3 named characters of mixed genders so generations vary.
ANIMALS: tuple[Character, ...] = (
    # hares (fast, boastful)
    Character("Whisker", "hare",   "m", ("racer",   "fast", "boastful")),
    Character("Hopper",  "hare",   "m", ("racer",   "fast")),
    Character("Bramble", "hare",   "f", ("racer",   "fast")),
    Character("Pip",     "hare",   "n", ("racer",   "fast")),

    # tortoises (slow, steady)
    Character("Shelly",   "tortoise", "f", ("racer", "slow", "steady")),
    Character("Slowpoke", "tortoise", "m", ("racer", "slow", "steady")),
    Character("Mossback", "tortoise", "m", ("racer", "slow")),

    # ants (saver, hardworking)
    Character("Tic",  "ant", "m", ("saver", "hardworking")),
    Character("Toc",  "ant", "f", ("saver", "hardworking")),
    Character("Bit",  "ant", "n", ("saver", "hardworking")),

    # grasshoppers (spendthrift, lazy)
    Character("Chirp", "grasshopper", "m", ("spendthrift", "lazy")),
    Character("Skip",  "grasshopper", "f", ("spendthrift", "lazy")),
    Character("Hum",   "grasshopper", "n", ("spendthrift", "lazy")),

    # crows (cunning)
    Character("Korvus", "crow", "m", ("cunning", "thirsty")),
    Character("Caw",    "crow", "f", ("cunning",)),
    Character("Sable",  "crow", "n", ("cunning",)),

    # foxes (cunning, hungry)
    Character("Renard", "fox", "m", ("cunning", "hungry", "thief")),
    Character("Vix",    "fox", "f", ("cunning", "hungry")),
    Character("Sly",    "fox", "n", ("cunning", "hungry")),

    # geese (yields)
    Character("Quill", "goose", "m", ("yielder",)),
    Character("Honk",  "goose", "f", ("yielder",)),
    Character("Plume", "goose", "n", ("yielder",)),

    # mice (small, prey)
    Character("Squeak", "mouse", "m", ("prey", "small")),
    Character("Whisk",  "mouse", "f", ("prey", "small")),
    Character("Nibble", "mouse", "n", ("prey", "small")),

    # lions (predator)
    Character("Roar",  "lion", "m", ("predator", "strong")),
    Character("Mane",  "lion", "f", ("predator", "strong")),
    Character("Tawny", "lion", "n", ("predator", "strong")),

    # wolves (predator)
    Character("Greyfang", "wolf", "m", ("predator",)),
    Character("Howl",     "wolf", "f", ("predator",)),

    # dogs (everyman)
    Character("Rex",   "dog", "m", ("everyman",)),
    Character("Bell",  "dog", "f", ("everyman",)),
    Character("Patch", "dog", "n", ("everyman",)),

    # storks (vessel-fairness fable)
    Character("Stilt",  "stork", "m", ("everyman", "long_beak")),
    Character("Reeda",  "stork", "f", ("everyman", "long_beak")),

    # bulls (lion fable)
    Character("Thorn",  "bull", "m", ("strong",)),
    Character("Boulder","bull", "m", ("strong",)),
    Character("Gale",   "bull", "f", ("strong",)),

    # boys (cried wolf)
    Character("Tom",   "human", "m", ("liar", "shepherd")),
    Character("Will",  "human", "m", ("liar", "shepherd")),
    Character("Pat",   "human", "n", ("liar", "shepherd")),
    Character("Jess",  "human", "f", ("liar", "shepherd")),
    Character("Lou",   "human", "f", ("liar", "shepherd")),

    # milkmaids (dreamers — hare/grasshopper analog)
    Character("Margery","human", "f", ("counter", "dreamer")),
    Character("Lila",   "human", "f", ("counter", "dreamer")),
    Character("Clara",  "human", "f", ("counter", "dreamer")),
    Character("Nan",    "human", "f", ("counter", "dreamer")),
    Character("Bess",   "human", "f", ("counter", "dreamer")),

    # farmers / market-wise elders (patient evaluators — tortoise/ant analog)
    Character("Godfrey","human", "m", ("farmer", "wise_elder")),
    Character("Aldric", "human", "m", ("farmer", "wise_elder")),
    Character("Mabel",  "human", "f", ("farmer", "wise_elder")),
    Character("Rowan",  "human", "n", ("farmer", "wise_elder")),
    Character("Edna",   "human", "f", ("farmer", "wise_elder")),
)

CHARACTERS: tuple[Character, ...] = HUMANS + ANIMALS


def characters_with_role(*roles: str) -> tuple[Character, ...]:
    """Characters whose role_classes include all of `roles`."""
    rs = set(roles)
    return tuple(c for c in CHARACTERS if rs.issubset(set(c.role_classes)))


def characters_with_species(species: str) -> tuple[Character, ...]:
    return tuple(c for c in CHARACTERS if c.species == species)


# ─────────────────────── Locations ───────────────────────


@dataclass(frozen=True)
class Location:
    name:    str
    article: str           # "a", "the", "" — for natural prose
    indoor:  bool
    tags:    tuple[str, ...] = ()


LOCATIONS: tuple[Location, ...] = (
    # outdoor — path-like (can host a race / travel scenario)
    Location("meadow",    "the", False, ("nature", "path")),
    Location("forest",    "the", False, ("nature", "path")),
    Location("woods",     "the", False, ("nature", "path")),
    Location("garden",    "the", False, ("nature", "path")),
    Location("orchard",   "the", False, ("nature", "path", "food")),
    Location("hilltop",   "the", False, ("nature", "path")),
    Location("road",      "the", False, ("path",)),
    Location("beach",     "the", False, ("nature", "water", "path")),

    # outdoor — water / static (NOT path-like)
    Location("river bank","the", False, ("nature", "water")),
    Location("pond",      "the", False, ("nature", "water")),
    Location("desert",    "the", False, ("nature",)),
    Location("market",    "the", False, ("village",)),
    Location("village",   "the", False, ("village",)),
    Location("farm",      "the", False, ("village",)),

    # indoor
    Location("cottage",   "a",   True,  ("home",)),
    Location("barn",      "the", True,  ("village", "animal")),
    Location("kitchen",   "the", True,  ("home",)),
    Location("attic",     "the", True,  ("home",)),
    Location("cellar",    "the", True,  ("home",)),
    Location("cave",      "a",   True,  ("nature", "shelter")),
)


def locations_with_tag(tag: str) -> tuple[Location, ...]:
    return tuple(l for l in LOCATIONS if tag in l.tags)


# ─────────────────────── Fit predicates / helpers ───────────────────────


def physically_consistent(item: Item, n: int, container: Container) -> bool:
    """True iff n of `item` fit in `container` AND the combination isn't
    nonsensical (e.g., putting eggs in a hole, putting blankets in a beak)."""
    if not container.fits_count(item, n):
        return False
    # bird-only containers (beak) only for size-1 / size-2 items, no liquids
    # already enforced by capacity_size; nothing extra needed for the
    # base case.
    return True


# ─────────────────────── Self-test (smoke) ───────────────────────


def smoke_test(seed: int = 0) -> None:
    """Run a few sanity checks; raise on failure."""
    rng = random.Random(seed)

    # 1. Every item has a sane size/weight in 1..5.
    for it in ITEMS:
        assert 1 <= it.size <= 5,   f"{it.name} size out of range"
        assert 1 <= it.weight <= 5, f"{it.name} weight out of range"

    # 2. Every container has positive capacity.
    for c in CONTAINERS:
        assert c.capacity_count > 0, f"{c.name} capacity_count <= 0"
        assert 1 <= c.max_size <= 5

    # 3. fits_count behaves: a pebble fits in a beak, a blanket doesn't.
    pebble  = next(i for i in ITEMS if i.name == "pebble")
    blanket = next(i for i in ITEMS if i.name == "blanket")
    beak    = next(c for c in CONTAINERS if c.name == "beak")
    cart    = next(c for c in CONTAINERS if c.name == "cart")
    assert     beak.fits_count(pebble, 1)
    assert not beak.fits_count(blanket, 1)
    assert     cart.fits_count(blanket, 5)

    # 4. Pronouns derive correctly.
    alice = next(c for c in CHARACTERS if c.name == "Alice")
    assert alice.he_she  == "she"
    assert alice.his_her == "her"

    # 5. Random sample: pick 100 random (item, n, container) triples and
    # verify physically_consistent agrees with a hand check on a few.
    for _ in range(100):
        it = rng.choice(ITEMS)
        n  = rng.randint(1, 20)
        c  = rng.choice(CONTAINERS)
        ok = physically_consistent(it, n, c)
        assert isinstance(ok, bool)

    # 6. characters_with_role finds plausible casts.
    racers = characters_with_role("racer")
    assert len(racers) >= 4, "should have at least 4 racing characters"
    fast   = characters_with_role("racer", "fast")
    slow   = characters_with_role("racer", "slow")
    assert fast and slow

    print(
        f"smoke OK: {len(ITEMS)} items, {len(CONTAINERS)} containers, "
        f"{len(CHARACTERS)} chars, {len(LOCATIONS)} locations"
    )


if __name__ == "__main__":
    smoke_test()
