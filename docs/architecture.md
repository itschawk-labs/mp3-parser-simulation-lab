# Architecture

## Logical Flow

### Clean Path

```text
practice_audio.mp3
        |
        v
ID3 parser
        |
        v
LAB_PARSER_TEST absent
        |
        v
Received = 0 bytes
        |
        v
Normal playback
        |
        v
No trigger action
```

### Crafted Path

```text
crafted_audio.mp3
        |
        v
ID3 parser
        |
        v
LAB_PARSER_TEST present
        |
        v
Received = 2048 bytes
        |
        v
Compare against simulated 256-byte limit
        |
        v
Boundary condition met
        |
        v
Controlled application branch
        |
        v
calc.exe launched
```

---

## Components

### MP3 Samples

The two MP3s provide controlled input variation.

### Mutagen

Used to read ID3 metadata.

### Pygame

Used for MP3 playback.

### Toy Player

Implements the intentionally defined parser-boundary logic.

### Windows Calculator

Used only as a visible, benign demonstration target.

### Process Monitor

Used to validate process creation.

---

## Trust Boundary

The core educational concept is the transition from:

```text
untrusted file data
```

to:

```text
parsed application state
```

to:

```text
application behavior
```

The security lesson is not that MP3 files are executable. The lesson is that software behavior depends on how untrusted input is interpreted.
