# Minecraft Overviewer Docker Image

## Running Minecraft Overviewer

```
docker pull mide/minecraft-overviewer:latest
docker run \
  --rm \
  -e MINECRAFT_VERSION="1.14" \
  -v /home/user/minecraft/:/home/minecraft/server/:ro \
  -v /srv/http/minecraft/:/home/minecraft/render/:rw \
  mide/minecraft-overviewer:latest
```

## Environment Variables

### Required

- `MINECRAFT_VERSION`
  Set to the version of Minecraft the world is based from (Like `1.14`). Used for textures.

### Optional
- `ADDITIONAL_ARGS`
  Default Value: _null_. Set to contain any additional arguments you'd like to pass into `overviewer.py`.

- `RENDER_MAP`
  Default Value: `true`. Set to `false` if you do not want to render the map. This is useful for POI only-updates.

- `RENDER_POI`
  Default Value: `true`. Set to `false` to disable rendering of POI (points of interest).
