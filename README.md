# VF-BlenderDriverFunctions
Functions for use in Blender channel drivers.

Installation and usage:
- Download the .py file
- Open up Blender preferences
- Install the add-on
- Enable
- Add a driver to any channel via keyboard shortcut (usually "D"), context menu (right-click), or directly (typing "#" and then the function)


## curveAtFrame
This driver function is intended to mimic Adobe After Effect's "valueAtTime" expression, returning the value of an animated channel from the specified point in time.

After Effects expression reference:
```javascript
thisComp.layer("Cube").transform.position.valueAtTime(time-0.167)[0]
```
This returns the value of the "Cube" layer's X position from 0.167 seconds in the past, relative to the current time.

Blender driver equivalent:
```javascript
curveAtFrame("Cube", 0, frame-5)
```
This returns the value of the "Cube" object's first animation curve from 5 frames in the past, relative to the current frame.

Note that Blender's time sampling doesn't allow references to an object's transform property; it has to be an animation curve, and it can only be referenced by index. The first channel that is keyframed will be assigned index 0, the second channel to be animated will be index 1, and so on.


## wiggle
Designed to mimic Adobe After Effect's "wiggle" expression with similar frequency (colloquially known as wiggles per second) and octave settings.

After Effects expression reference:
```javascript
seedRandom(4, true);
wiggle(3, 200, 1)
```
This automatically animates a channel using a static seed of 4 with about 3 "wiggles" per second, a potential distance range of -200 to 200 pixels, and 1 octave of noise.

Blender driver equivalent:
```javascript
wiggle(3, 0.2, 1, 4)
```
This automatically animates a channel and vaguely matches AE's 3 "wiggles" per second, a potential distance range of -200mm to 200mm (if used in a transform channel), with 1 octave of noise, and a random seed of 4 (seeds can be any floating point number, including negative numbers).

Note that unlike After Effects, driver functions in Blender don't automatically receive unique identifiers for each channel they are applied to, so a unique seed value must be provided by the user.
