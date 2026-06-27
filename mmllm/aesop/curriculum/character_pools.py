"""Character name pools for the K-12 Clojure curriculum.

Per the user's variation-pool directive, each pool is sized at ~200
entries (universal human and primary animal pools) or ~60 (specialty
roles) so the model generalizes name -> subject/object relationship
rather than memorizing specific names.

Pools used at draw time: see _pick_<fable>_chars in
mmllm/aesop/curriculum/generator.py and the per-fable Character
construction sites for which pool maps to which role.
"""

from __future__ import annotations


HUMAN_F = (
    "Mira", "Anika", "Fionnuala", "Thora", "Beatriz", "Tatiana", "Saskia",
    "Genevieve", "Klara", "Yara", "Eveline", "Aislinn", "Bridget", "Cora",
    "Dagmar", "Elsa", "Freya", "Greta", "Helga", "Ingrid", "Jutta", "Karin",
    "Lena", "Maja", "Nora", "Olga", "Petra", "Rosa", "Sigrid", "Tilda",
    "Ula", "Vera", "Wilma", "Xenia", "Yelena", "Zara", "Adela", "Bianca",
    "Carlotta", "Donata", "Elena", "Fabia", "Giulia", "Helena", "Isabella",
    "Lucia", "Marta", "Nadia", "Ottilia", "Paola", "Renata", "Serafina",
    "Teodora", "Valeria", "Amalia", "Brigida", "Cecilia", "Dorotea",
    "Emilia", "Florencia", "Gemma", "Honora", "Iris", "Juliana", "Lavinia",
    "Mathilde", "Noemi", "Octavia", "Philippa", "Rosalia", "Sabina",
    "Theodora", "Ursula", "Vivien", "Winifred", "Yseult", "Zelda", "Anouk",
    "Brigitte", "Celestine", "Delphine", "Eloise", "Fleur", "Gisele",
    "Helene", "Inez", "Jeanne", "Lisette", "Mireille", "Ninon", "Odile",
    "Pernille", "Rosalind", "Solange", "Therese", "Veronique", "Yvette",
    "Birgit", "Cosima", "Dorothea", "Erika", "Friederike", "Gretchen",
    "Hannelore", "Irmgard", "Johanna", "Liesel", "Margarethe", "Nikola",
    "Roswitha", "Sieglinde", "Trudi", "Ulrike", "Walburga", "Wiebke",
    "Zenta", "Alenka", "Bronislava", "Dragana", "Evgenia", "Galina",
    "Halina", "Ivana", "Jelena", "Katarzyna", "Ludmila", "Marina", "Natalya",
    "Oksana", "Polina", "Radmila", "Slavena", "Tamara", "Veronika", "Zofia",
    "Aoife", "Caitlin", "Deirdre", "Eithne", "Grainne", "Maeve", "Niamh",
    "Orla", "Roisin", "Sinead", "Una", "Sorcha", "Branwen", "Carys",
    "Eira", "Gwyneth", "Mair", "Rhian", "Seren", "Tegan", "Bronwen",
    "Estrid", "Gudrun", "Halla", "Idun", "Liv", "Runa", "Signe", "Solveig",
    "Tove", "Vigdis", "Astrid", "Hilde", "Kari", "Solvi", "Agata",
    "Beata", "Czeslawa", "Danuta", "Edyta", "Hanna", "Iwona", "Jadwiga",
    "Krystyna", "Marzena", "Wanda", "Aniko", "Boglarka", "Csilla", "Eniko",
    "Hajna", "Ilona", "Reka", "Tunde", "Zsofia", "Adriana", "Dorina",
    "Floarea", "Lacramioara", "Mihaela", "Sanda", "Tudora", "Voica", "Calista",
    "Despina", "Eudora", "Galini", "Iola", "Kalliope", "Lydia", "Melina",
    "Phaedra", "Thalia", "Xanthe", "Zoe",
)


HUMAN_M = (
    "Aldric", "Luka", "Tomas", "Mateo", "Otto", "Henrik", "Soren", "Marcus",
    "Cyril", "Owain", "Dmitri", "Anselm", "Hugo", "Lior", "Bram", "Caspar",
    "Diederik", "Emiel", "Floris", "Gijs", "Hendrik", "Joost", "Kasper",
    "Lambert", "Maarten", "Niels", "Pieter", "Rutger", "Sander", "Thijs",
    "Willem", "Bastian", "Conrad", "Dieter", "Erich", "Friedrich", "Gunther",
    "Helmut", "Ivo", "Jorg", "Klaus", "Ludwig", "Manfred", "Norbert", "Oskar",
    "Reiner", "Stefan", "Theobald", "Ulrich", "Volker", "Wendel", "Aurelio",
    "Benedetto", "Cesare", "Domenico", "Emilio", "Fabrizio", "Giancarlo",
    "Lorenzo", "Maurizio", "Niccolo", "Orlando", "Paolo", "Renzo", "Salvatore",
    "Tiziano", "Umberto", "Valentino", "Andres", "Cristobal", "Diego",
    "Eduardo", "Federico", "Gabriel", "Hernan", "Ignacio", "Joaquin",
    "Leonardo", "Miguel", "Nicolas", "Pablo", "Rafael", "Santiago", "Mauricio",
    "Vicente", "Adrien", "Bertrand", "Cedric", "Damien", "Etienne", "Florent",
    "Gaspard", "Hippolyte", "Jerome", "Lucien", "Mathieu", "Olivier",
    "Quentin", "Romain", "Sebastien", "Thierry", "Vincent", "Xavier",
    "Bohumil", "Drazen", "Filip", "Goran", "Ivan", "Jaroslav", "Kazimir",
    "Lubomir", "Milos", "Nikolai", "Ondrej", "Petar", "Radek", "Stanislav",
    "Tadeusz", "Vaclav", "Yuri", "Zdenek", "Andrej", "Bogdan", "Casimir",
    "Damir", "Erazm", "Feliks", "Grzegorz", "Jaromir", "Konrad", "Lech",
    "Mieczyslaw", "Marek", "Pawel", "Rafal", "Slawomir", "Tomasz", "Wojciech",
    "Aindreas", "Brendan", "Cathal", "Declan", "Eamon", "Fionn", "Gareth",
    "Iarlaith", "Kevan", "Lorcan", "Niall", "Oscar", "Padraic", "Ronan",
    "Seamus", "Tadhg", "Aneirin", "Bedwyr", "Cadell", "Dylan", "Emrys",
    "Gawain", "Huw", "Idris", "Llew", "Madoc", "Rhys", "Tegwyn", "Aksel",
    "Birger", "Egil", "Fredrik", "Gustav", "Halvar", "Ivar", "Jens", "Knut",
    "Leif", "Magnus", "Olav", "Ragnar", "Stig", "Torbjorn", "Ulf", "Viggo",
    "Aristos", "Costas", "Demetrios", "Evangelos", "Galen", "Iason",
    "Kostis", "Lysander", "Nikos", "Orestes", "Petros", "Stavros", "Thanos",
    "Vasilis", "Xenon", "Yannis", "Aharon", "Barak", "Doron", "Eitan",
    "Gilad", "Hadar", "Itai", "Levi", "Naftali", "Reuven", "Shimon", "Yaron",
    "Zev", "Alaric", "Baldwin",
)


HUMAN_ELDER_F = (
    "Hilda", "Adelaide", "Cordelia", "Petra", "Constance", "Ingrid", "Augusta",
    "Beatrice", "Clementine", "Domitilla", "Eulalia", "Frederica", "Gertrude",
    "Henriette", "Imelda", "Jacquelyn", "Katharina", "Leonora", "Mathilda",
    "Nicoletta", "Octavia", "Philomena", "Quintina", "Rosamund", "Severina",
    "Theodelinda", "Ursulina", "Valentina", "Wilhelmina", "Xaveria", "Yolanda",
    "Zenobia", "Albertina", "Bertilda", "Cassandra", "Domenica", "Engelberta",
    "Fernanda", "Gunhilda", "Hortensia", "Isidora", "Josephina", "Kunigunde",
    "Liutgard", "Margarethe", "Nicephora", "Onorata", "Perpetua", "Romualda",
    "Salomea", "Tertia", "Ulvilda", "Vespasia", "Walpurga", "Yvonette",
    "Zerlina", "Apollonia", "Brunhilda", "Cunegonda", "Drusilla",
)


HUMAN_ELDER_M = (
    "Bartholomew", "Cassius", "Theodoric", "Magnus", "Septimus", "Alaric",
    "Ambrose", "Benedict", "Cornelius", "Demetrius", "Edmund", "Ferdinand",
    "Gerhardt", "Horatio", "Ignatius", "Jeremias", "Kasimir", "Leopold",
    "Mortimer", "Nathaniel", "Oswald", "Percival", "Quintus", "Reginald",
    "Sigismund", "Tobias", "Ulysses", "Valerian", "Walther", "Xaverius",
    "Zacharias", "Anselmo", "Baltasar", "Crispin", "Diogenes", "Ezekiel",
    "Florentin", "Gildas", "Hieronymus", "Iustinian", "Joachim", "Konstantin",
    "Lucretius", "Maximilian", "Nikodemus", "Obadiah", "Polycarp", "Remigius",
    "Salvius", "Theophilus", "Urbanus", "Venantius", "Wenceslas", "Yves",
    "Zephaniah", "Anastasius", "Bonifacius", "Casimir", "Dorotheus", "Euclid",
)


HARE_NAMES = (
    "Whisker", "Dart", "Fleet", "Bolt", "Bound", "Swift", "Dash", "Zip",
    "Flick", "Skim", "Skip", "Sprint", "Streak", "Whisk", "Flit", "Bounce",
    "Quick", "Rush", "Spry", "Hasty", "Brisk", "Nimble", "Lithe", "Agile",
    "Fleeting", "Vault", "Leap", "Hop", "Jolt", "Snap", "Flash", "Whirr",
    "Whish", "Zoom", "Lively", "Skitter", "Skedaddle", "Hurry", "Scurry",
    "Speedy", "Pacer", "Racer", "Galop", "Sprightly", "Quickfoot", "Lightfoot",
    "Swiftpaw", "Fleetpaw", "Bouncer", "Springer",
    "Clover", "Heather", "Briar", "Sorrel", "Thistle", "Fern", "Bracken",
    "Willow", "Birch", "Hazel", "Rowan", "Aspen", "Ivy", "Holly", "Hawthorn",
    "Dandelion", "Buttercup", "Daisy", "Foxglove", "Bluebell", "Primrose",
    "Cowslip", "Yarrow", "Mallow", "Lupine", "Vetch", "Sage", "Mint",
    "Thyme", "Rosemary", "Lavender", "Marigold", "Saffron", "Honeysuckle",
    "Speedwell", "Cornflower", "Poppy", "Ragwort", "Bramble", "Furze",
    "Gorse", "Whin", "Heath", "Moor", "Glen", "Dell", "Mead", "Glade",
    "Brook", "Thistledown",
    "Pip", "Filbert", "Skitterling", "Mouse", "Vole", "Shrew", "Wren", "Robin",
    "Sparrow", "Finch", "Lark", "Linnet", "Pipit", "Tit", "Stoat", "Weasel",
    "Marten", "Ferret", "Polecat", "Hamster", "Gerbil", "Dormouse", "Mole",
    "Hedgepig", "Hedgehog", "Squirrel", "Chipmunk", "Bunny", "Kit", "Doe",
    "Buck", "Leveret", "Coney", "Lapin", "Jackrabbit", "Cottontail",
    "Pika", "Marmot", "Lemming", "Capybara", "Beaver", "Otter", "Stoatling",
    "Whiskling", "Bunneh", "Pipsqueak", "Furrling", "Tufty", "Snoutkin",
    "Burrkin",
    "Whiskerton", "Twitcher", "Bouncekin", "Snickerton", "Pouncer", "Tumbler",
    "Flopsy", "Mopsy", "Jumper", "Wriggle", "Wiggle", "Giggle", "Pickle",
    "Tickle", "Nibble", "Snuffle", "Snickerkin", "Chitter", "Chatter", "Patter",
    "Scamper", "Caper", "Frolic", "Gambol", "Romp", "Prance", "Bounder",
    "Bopper", "Bouncebob", "Skipperton", "Hopkin", "Tippet", "Twinkle",
    "Pebble", "Flutter", "Twirl", "Pirouette", "Whirlikin", "Snippet",
    "Tassle", "Bramblefoot", "Cloverpaw", "Skimble", "Flickerton",
    "Blossom", "Petalfoot", "Mossy", "Tuftkin", "Scampkin", "Dappling",
    "Springle",
)


TORTOISE_NAMES = (
    "Mossback", "Cobble", "Stoneheart", "Slate", "Granite", "Boulder",
    "Pebble", "Flint", "Chert", "Quartz", "Basalt", "Schist", "Marble",
    "Limestone", "Sandstone", "Shale", "Gneiss", "Obsidian", "Pumice",
    "Mudstone", "Cobblestone", "Gravel", "Bedrock", "Crag", "Tor", "Bluff",
    "Mound", "Cairn", "Boulderkin", "Stonefoot", "Pebblepaw", "Heavyback",
    "Slowstep", "Plodder", "Trundler", "Lumber", "Heave", "Hulk", "Bulk",
    "Solid", "Steady", "Stout", "Sturdy", "Firm", "Anchor", "Ballast",
    "Heft", "Mass", "Weight", "Burden", "Stoneback",
    "Sage", "Elder", "Wisp", "Patient", "Stoic", "Solemn", "Grave", "Ponder",
    "Muse", "Mull", "Dwell", "Deepen", "Linger", "Tarry", "Bide", "Dawdle",
    "Loiter", "Saunter", "Amble", "Mosey", "Stroll", "Meander", "Wander",
    "Roam", "Drift", "Ramble", "Trudge", "Trek", "Tramp", "Slog", "Crawl",
    "Creep", "Inch", "Ooze", "Plod", "Toddle", "Hobble", "Shuffle", "Lumberkin",
    "Drone", "Drowse", "Doze", "Yawn", "Slumber", "Snooze", "Repose",
    "Calmway", "Hushwise", "Quietkin", "Stillpaw", "Sloward",
    "Loam", "Shalekin", "Burrow", "Mire", "Bog", "Fen", "Marsh", "Mead",
    "Heath", "Moor", "Wold", "Glade", "Dell", "Hollow", "Trench", "Furrow",
    "Trough", "Gully", "Ravine", "Glen", "Dene", "Holt", "Copse", "Thicket",
    "Brake", "Brackenback", "Mossfoot", "Lichen", "Fungus", "Toadstool",
    "Mushroom", "Truffle", "Tuber", "Root", "Rhizome", "Stem", "Stalk",
    "Vine", "Tendril", "Creeper", "Climber", "Sprawl", "Spread", "Carpet",
    "Cushion", "Pillow", "Moundkin", "Knoll", "Hummock", "Hillock", "Tussock",
    "Umber", "Sienna", "Taupe", "Ochre", "Sepia", "Sable", "Russet",
    "Bistre", "Hazel", "Walnut", "Chestnut", "Mahogany", "Ebony", "Sorrel",
    "Roan", "Dun", "Bay", "Bistro", "Drab", "Khaki", "Olive", "Sageback",
    "Moss", "Fern", "Forest", "Pine", "Cedar", "Oakheart", "Bark", "Bough",
    "Twig", "Branch", "Knot", "Burl", "Knurl", "Gnarl", "Grain", "Whorl",
    "Ring", "Cambium", "Heartwood", "Sapwood", "Pith", "Marrow", "Tarbark",
    "Rootkin", "Ironback", "Steadypaw", "Slatekin", "Cragwise", "Gravelfoot",
)


CROW_NAMES = (
    "Raven", "Onyx", "Inkwing", "Jet", "Nightshade", "Pitch", "Soot", "Coal",
    "Ebon", "Sable", "Obsidian", "Carbon", "Tarwing", "Inkfeather", "Dusk",
    "Twilight", "Gloam", "Eclipse", "Shadow", "Umbra", "Penumbra", "Murk",
    "Mirk", "Cinder", "Char", "Smoulder", "Smoke", "Ash", "Soothe",
    "Nightfall", "Dimsky", "Veil", "Cloak", "Shroud", "Mantle", "Cowl",
    "Hood", "Hush", "Quill", "Quiver", "Plume", "Pinion", "Vane",
    "Featherdark", "Wingnight", "Skyshade", "Cloudshroud", "Stormcloak",
    "Tempest", "Squall", "Gale",
    "Cipher", "Riddle", "Glint", "Cunning", "Sly", "Wily", "Crafty", "Foxy",
    "Shrewd", "Astute", "Clever", "Witty", "Sharp", "Keen", "Bright",
    "Quickwit", "Wisecaw", "Sage", "Pundit", "Scholar", "Scribe", "Inkwell",
    "Parchment", "Vellum", "Folio", "Codex", "Tome", "Glyph", "Rune",
    "Sigil", "Mark", "Token", "Symbol", "Emblem", "Seal", "Crest", "Brand",
    "Insignia", "Hieroglyph", "Cipherwing", "Riddlecaw", "Puzzle", "Conundrum",
    "Enigma", "Mystery", "Secret", "Whisperer", "Trickster", "Beguiler",
    "Schemer", "Plotter",
    "Drift", "Spire", "Tower", "Vanekin", "Soar", "Glide", "Wheel", "Circle",
    "Loop", "Arc", "Sweep", "Swoop", "Plunge", "Dive", "Stoop", "Climb",
    "Rise", "Ascend", "Mount", "Loft", "Aloft", "Highwing", "Skybound",
    "Cloudlark", "Windrider", "Thermal", "Updraft", "Zephyr", "Squallwing",
    "Stormcaw", "Galewing", "Tempestcaw", "Whirlwind", "Eddy", "Currents",
    "Crosswind", "Sidewind", "Headwind", "Tailwind", "Lift", "Hover",
    "Float", "Coast", "Breeze", "Gust", "Bluster", "Buffet", "Whisk",
    "Veer", "Banking", "Pirouette",
    "Caw", "Pyrite", "Cobalt", "Slate", "Indigo", "Azurite", "Lapis",
    "Sapphire", "Onyxwing", "Hematite", "Galena", "Magnetite", "Bismuth",
    "Antimony", "Cinnabar", "Realgar", "Orpiment", "Chrysocolla", "Malachite",
    "Azure", "Cawlick", "Cackle", "Clatter", "Chatter", "Squawk", "Skreigh",
    "Croak", "Cluck", "Whoop", "Holler", "Shout", "Yowl", "Yawp", "Shriek",
    "Trill", "Warble", "Pipe", "Whistle", "Hum", "Buzz", "Drone", "Murmur",
    "Mutter", "Mumble", "Burble", "Babble", "Bicker", "Quibble", "Quirk",
    "Caper",
)


WOLF_NAMES = (
    "Fang", "Howl", "Shadow", "Pelt", "Snarl", "Lupin", "Vargr", "Wolfkin",
    "Hunter", "Stalker", "Prowler", "Lurker", "Pouncer", "Slayer", "Reaver",
    "Render", "Ripper", "Tearclaw", "Bloodfang", "Bonecrack", "Marrowbone",
    "Sinew", "Maw", "Jaws", "Tooth", "Tusk", "Talon", "Claw", "Gnasher",
    "Gnaw", "Bite", "Rend", "Shred", "Thresh", "Thrash", "Lash", "Whip",
    "Strike", "Smite", "Smitewolf", "Bound", "Sprint", "Rush", "Charge",
    "Stampede", "Trample", "Rampage", "Rage", "Fury", "Wrath", "Ire",
    "Greyback", "Smoke", "Ash", "Cinder", "Dusk", "Twilight", "Mist",
    "Fog", "Haze", "Murk", "Gloam", "Pewter", "Steel", "Iron", "Silver",
    "Argent", "Pewterfang", "Slatepaw", "Granite", "Stone", "Charcoal", "Soot",
    "Cobble", "Cobweb", "Wraith", "Spectre", "Shade", "Shadekin", "Phantom",
    "Wisp", "Vapor", "Cloud", "Drizzle", "Rime", "Frostkin", "Hoarfrost",
    "Snowfall", "Glacier", "Tundra", "Sleet", "Hail", "Storm", "Thunder",
    "Lightning", "Tempest", "Blizzard", "Squall", "Gale", "Whirlwind",
    "Cyclone", "Hurricane", "Typhoon", "Maelstrom",
    "Fenrir", "Skoll", "Lobo", "Garm", "Garmr", "Amarok", "Hati", "Geri",
    "Freki", "Vargar", "Lycaon", "Lycos", "Lykos", "Wulfric", "Ulfgar",
    "Beowulf", "Wolfram", "Wolfhart", "Wolfdietrich", "Adolph", "Rudolf",
    "Randolf", "Arnulf", "Wulf", "Ulv", "Ulvar", "Vargas", "Vlk", "Vukos",
    "Volkov", "Lupo", "Loup", "Loboso", "Madadh", "Brock", "Brackenfang", "Rhonwen",
    "Conan", "Conri", "Faolan", "Lowri", "Bleidd", "Faol", "Mac-tire",
    "Konungr", "Jarl", "Thane", "Earl", "Lord", "Sire", "Master", "Chief",
    "Alpha", "Pack",
    "Bramble", "Bracken", "Frost", "Stormtail", "Slate", "Ironclaw",
    "Steelfang", "Ironback", "Stoneheart", "Granitemaw", "Boulderpaw",
    "Cragclaw", "Tortail", "Fellpaw", "Wildfoot", "Roughpelt", "Burrcoat",
    "Briarback", "Thornfang", "Spinefang", "Razorback", "Bristleback",
    "Shaggymane", "Roughmane", "Tousled", "Tangled", "Mangy", "Scruffy",
    "Rangy", "Rugged", "Wildfang", "Wildmaw", "Wildwood", "Wildkin",
    "Forestpaw", "Nightwood", "Thornclaw", "Mossfang", "Ferncoat", "Hollowfang",
    "Hollowmaw", "Cavernkin", "Densworn", "Lairlord", "Denwarder", "Denkin",
    "Hollowback", "Wolfshade", "Shadepaw", "Duskpaw", "Nightclaw", "Moonkin",
    "Wanderfang", "Roamer",
)


DOG_NAMES = (
    "Rex", "Duke", "Buster", "Scout", "Patch", "Spot", "Buddy", "Max",
    "Charlie", "Cooper", "Toby", "Jack", "Bailey", "Murphy", "Riley",
    "Bruno", "Bear", "Tucker", "Beau", "Finn", "Gus", "Hank", "Otis",
    "Ozzie", "Rocco", "Rocky", "Sam", "Teddy", "Winston", "Wally", "Walter",
    "Henry", "Oliver", "Oscar", "Louie", "Leo", "Zeke", "Ace", "Bingo",
    "Boomer", "Champ", "Chester", "Diesel", "Frankie", "Hugo", "Jasper",
    "Kobe", "Loki", "Marley", "Milo",
    "Rover", "Tracker", "Hunter", "Ranger", "Sentry", "Watchdog", "Guardian",
    "Watcher", "Warden", "Keeper", "Herder", "Drover", "Shepherd", "Collie",
    "Setter", "Pointer", "Retriever", "Spaniel", "Terrier", "Hound",
    "Houndsman", "Tracksman", "Trailblazer", "Pathfinder", "Scoutmaster",
    "Sniffer", "Snoutling", "Nosey", "Whiff", "Sniff", "Snort", "Snuffler",
    "Bayer", "Howler", "Yipper", "Yelper", "Barker", "Woofer", "Growler",
    "Snarler", "Pacer", "Trotter", "Runner", "Galloper", "Bounder", "Leaper",
    "Springer", "Lunger", "Pouncer", "Stalker",
    "Rusty", "Tawny", "Sandy", "Shadow", "Inky", "Smokey", "Ashy", "Sooty",
    "Coal", "Ebony", "Cocoa", "Toffee", "Caramel", "Fudge", "Hazel", "Honey",
    "Mocha", "Latte", "Cinnamon", "Ginger", "Saffron", "Marigold", "Marmalade",
    "Pumpkin", "Squash", "Apricot", "Peach", "Cream", "Vanilla", "Buttermilk",
    "Snowy", "Snowball", "Cotton", "Cloud", "Pearl", "Ivory", "Alabaster",
    "Marble", "Granite", "Pewter", "Silver", "Sterling", "Steel", "Slate",
    "Charcoal", "Onyx", "Jet", "Raven", "Russet", "Auburn", "Chestnut",
    "Pip", "Mochi", "Ziggy", "Biscuit", "Pebble", "Pepper", "Salty",
    "Pickle", "Peanut", "Cashew", "Almond", "Walnut", "Acorn", "Berry",
    "Cherry", "Plum", "Olive", "Pippin", "Pumpernickel", "Pickles", "Noodle",
    "Bagel", "Muffin", "Crumpet", "Cookie", "Scoutie", "Sprocket", "Gizmo",
    "Widget", "Whatsit", "Whimsy", "Ditto", "Doodle", "Skipper", "Skippy",
    "Tippy", "Topsy", "Dottie", "Tiggs", "Banjo", "Boppy", "Roly", "Polly",
    "Wallace", "Yappy", "Zippy", "Zoomer", "Friski", "Tippet", "Snoopy",
)


SHEEP_NAMES = (
    "Wooly", "Fleecy", "Cottonkin", "Cloudwool", "Snowfleece", "Lambkin",
    "Frostwool", "Driftwool", "Flakewool", "Powdertuft", "Snowywool",
    "Snowball", "Mistlewool", "Hoarwool", "Rimewool", "Flurrywool",
    "Blizwool", "Whisptuft", "Cottonball", "Tuftwool", "Downy",
    "Fluffwool", "Plushy", "Poofwool", "Pompomtuft", "Puffwool",
    "Rufflewool", "Fuzzwool", "Nimbuswool", "Vaporwool",
    "Bleatling", "Baalamb", "Yeanlamb", "Ewekin", "Ramble", "Hornlet",
    "Mutton", "Nibblewool", "Grazer", "Munchwool", "Gambolwool",
    "Tinklebell", "Bellsy", "Jingle", "Trotwool", "Plodwool",
    "Eweling", "Lambling", "Babewool", "Wooliam", "Bobwool", "Tagwool",
    "Tagskin", "Curlywool", "Curlcoat", "Crimpcoat", "Crimplet",
    "Tuftling", "Bobtail", "Bobbinwool", "Roveswool", "Tagalong",
    "Strayling", "Strayswool", "Bleaty", "Yeantuft", "Sniffwool",
    "Snortwool", "Patwool", "Tiptoewool", "Tilkin", "Mim", "Bo", "Bea",
    "Bib", "Bop", "Pim", "Pum", "Pix", "Tup", "Lulu", "Mimi", "Bibi",
    "Coco", "Lala", "Mama", "Nana", "Sissy", "Missy", "Tessy", "Bess",
    "Tess", "Nell", "Ella", "Ettie", "Nettie", "Wooligan", "Mistypelt",
    "Foggypelt", "Snufflekin", "Tufty", "Tufter", "Lambchop",
    "Gentlewool", "Pebblewool", "Pasturekin", "Folder", "Pennedone",
    "Cornerwool", "Mossfleece", "Twigwool",
)


GOAT_NAMES = (
    "Billy", "Nanny", "Kidkin", "Buckhorn", "Capra", "Caprice",
    "Hircus", "Yeanling", "Pan", "Faun", "Satyr", "Cabri", "Chevre",
    "Bock", "Geiss", "Capricorn", "Tragos", "Tagus", "Jocko", "Gambol",
    "Ramble", "Tussle", "Headbutt", "Hornbeam", "Hornet", "Twohorn",
    "Hardhoof", "Cleftfoot", "Splithoof", "Bleat", "Bleater",
    "Wether", "Chevon", "Caprino", "Yael", "Lechero", "Caprigol",
    "Trotsky", "Prancer", "Vaulter", "Bounder", "Skipthorn",
    "Crackshell", "Brierhoof", "Burrgoat", "Whiskergoat",
    "Goatling", "Tippytoe", "Wibble", "Jiggle",
    "Thrymir", "Heidrun", "Tanngrisnir", "Tanngnost", "Amalthea",
    "Rufous", "Khaki", "Gimbal", "Capralino", "Yeanvale", "Hornkin",
    "Cliffwalker",
)


HEN_NAMES = (
    "Cluck", "Henrietta", "Pecky", "Featherly", "Plumea", "Goldhen",
    "Nuggethen", "Sunny", "Yolk", "Yolkie", "Sunnyside", "Eggie",
    "Speckle", "Henny", "Penny", "Penelope", "Prudence", "Patience",
    "Pearlhen", "Bessie", "Betty", "Belle", "Birdie", "Roosti",
    "Roostie", "Featherbell", "Coop", "Coopie", "Tweetkin", "Chickle",
    "Cackle", "Cluckling", "Plumelet", "Fluffyhen", "Puffhen",
    "Pluckwattle", "Wattle", "Wattles", "Beak", "Beaky", "Henkin",
    "Hatchling", "Brooder", "Sitter", "Layer", "Pecker", "Scratcher",
    "Strutter", "Bantam", "Banty", "Pullet", "Brownhen", "Russethen",
    "Roostling", "Flapper", "Featherton", "Spotty", "Speckly",
    "Dottyhen", "Bawk", "Bawker",
)


ROOSTER_NAMES = (
    "Chanticleer", "Crimson", "Caesar", "Ruff", "Crest", "Comb", "Spurs",
    "Dawncrow", "Sunrise", "Cocklebur", "Cockerel", "Brassneck", "Goldwing",
    "Bronzewing", "Copperback", "Rusticus", "Reginald", "Roderick", "Roland",
    "Rufus", "Maximus", "Imperator", "Senator", "Tribune", "Consul",
    "Sentinel", "Herald", "Crier", "Bugler", "Trumpeter", "Hornblow",
)


__all__ = (
    "HUMAN_F",
    "HUMAN_M",
    "HUMAN_ELDER_F",
    "HUMAN_ELDER_M",
    "HARE_NAMES",
    "TORTOISE_NAMES",
    "CROW_NAMES",
    "WOLF_NAMES",
    "DOG_NAMES",
    "SHEEP_NAMES",
    "GOAT_NAMES",
    "HEN_NAMES",
    "ROOSTER_NAMES",
)


def _smoke_test() -> None:
    pools = {
        "HUMAN_F": HUMAN_F, "HUMAN_M": HUMAN_M,
        "HUMAN_ELDER_F": HUMAN_ELDER_F, "HUMAN_ELDER_M": HUMAN_ELDER_M,
        "HARE_NAMES": HARE_NAMES, "TORTOISE_NAMES": TORTOISE_NAMES,
        "CROW_NAMES": CROW_NAMES, "WOLF_NAMES": WOLF_NAMES,
        "DOG_NAMES": DOG_NAMES, "SHEEP_NAMES": SHEEP_NAMES,
        "GOAT_NAMES": GOAT_NAMES, "HEN_NAMES": HEN_NAMES,
        "ROOSTER_NAMES": ROOSTER_NAMES,
    }
    for name, pool in pools.items():
        assert len(pool) == len(set(pool)), f"{name}: duplicates"
        assert all(2 <= len(x) <= 14 for x in pool), f"{name}: length out of range"
        assert all(isinstance(x, str) for x in pool), f"{name}: non-str"
        # Spot-check size targets
        if name in ("HUMAN_F", "HUMAN_M"):                 assert len(pool) >= 200, name
        elif name in ("HUMAN_ELDER_F", "HUMAN_ELDER_M"):    assert len(pool) >= 60,  name
        elif name in ("HARE_NAMES", "TORTOISE_NAMES",
                      "CROW_NAMES", "WOLF_NAMES",
                      "DOG_NAMES"):                          assert len(pool) >= 200, name
        elif name == "SHEEP_NAMES":                          assert len(pool) >= 100, name
    print(f"character_pools.py smoke_test: ok ({sum(len(p) for p in pools.values())} names across {len(pools)} pools)")


if __name__ == "__main__":
    _smoke_test()
