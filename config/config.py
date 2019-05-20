import os


def playerIcons(poi):
    if poi['id'] == 'Player':
        poi['icon'] = "https://overviewer.org/avatar/{}".format(poi['EntityId'])
        return "Last known location for {}".format(poi['EntityId'])


# Only signs with "-- RENDER --" in them, and no others. Otherwise, people
# can't have secret bases and the render is too busy anyways.
def signFilter(poi):
    if poi['id'] in ['Sign', 'minecraft:sign']:
        if '-- RENDER --' in poi.values():
            return "\n".join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']])


worlds['minecraft'] = "/home/minecraft/server/world"
outputdir = "/home/minecraft/render/"
texturepath = "/home/minecraft/{}.jar".format(os.environ['MINECRAFT_VERSION'])

markers = [
    dict(name="Players", filterFunction=playerIcons),
    dict(name="Signs", filterFunction=signFilter)
]

renders["day"] = {
    'world': 'minecraft',
    'title': 'Day',
    'crop': (-1500, -1500, 1500, 1500),
    'rendermode': 'smooth_lighting',
    "dimension": "overworld",
    'markers': markers
}

renders["night"] = {
    'world': 'minecraft',
    'title': 'Night',
    'crop': (-1500, -1500, 1500, 1500),
    'rendermode': 'smooth_night',
    "dimension": "overworld",
    'markers': markers
}

renders["nether"] = {
    "world": "minecraft",
    "title": "Nether",
    'crop': (-1500, -1500, 1500, 1500),
    "rendermode": 'nether_smooth_lighting',
    "dimension": "nether",
    'markers': markers
}

renders["end"] = {
    "world": "minecraft",
    "title": "End",
    'crop': (-1500, -1500, 1500, 1500),
    "rendermode": [Base(), EdgeLines(), SmoothLighting(strength=0.5)],
    "dimension": "end",
    'markers': markers
}

renders["overlay_biome"] = {
    'world': 'minecraft',
    'rendermode': [ClearBase(), BiomeOverlay()],
    'title': "Biome Coloring Overlay",
    'crop': (-1500, -1500, 1500, 1500),
    "dimension": "overworld",
    'overlay': ["day"]
}

renders["overlay_mobs"] = {
    'world': 'minecraft',
    'rendermode': [ClearBase(), SpawnOverlay()],
    'title': "Mob Spawnable Areas Overlay",
    'crop': (-1500, -1500, 1500, 1500),
    "dimension": "overworld",
    'overlay': ["day"]
}

renders["overlay_slime"] = {
    'world': 'minecraft',
    'rendermode': [ClearBase(), SlimeOverlay()],
    'title': "Slime Chunk Overlay",
    'crop': (-1500, -1500, 1500, 1500),
    "dimension": "overworld",
    'overlay': ["day"]
}
