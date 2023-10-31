# Colorfusion
<p>
  <img src="https://img.shields.io/github/repo-size/memb3r/colorfusion"> <img src="https://img.shields.io/github/languages/top/memb3r/colorfusion?color=green"> <img src="https://img.shields.io/github/last-commit/memb3r/colorfusion">
</p>
My first library for import colors. Idk how to publish libraries into pip, but anyway, you can use it.

It's simple, because it's using ANSI Escape Codes and this codes are don't require any other libraries.

# How to use?
First, clone repo:

```bash
$ git clone https://github.com/memb3r/colorfusion
```

Now, you need to make a .py file in <code>colorfusion</code> folder.

Example code:

```python
from colorfusion import fuse

print(fuse.colorize("Red text", fuse.RED))
```

Also, you can use other colors:

```python
RED = fuse.colorize("Red text", fuse.RED)
GREEN = fuse.colorize("Green text", fuse.GREEN)
YELLOW = fuse.colorize("Yellow text", fuse.YELLOW)
BLUE = fuse.colorize("Blue text", fuse.BLUE)
MAGENTA = fuse.colorize("Magenta text", fuse.MAGENTA)
CYAN = fuse.colorize("Cyan text", fuse.CYAN)
WHITE = fuse.colorize("White text", fuse.WHITE)
RESET = fuse.colorize("Reset styles", fuse.RESET)
```

# License

idk
