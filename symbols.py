def right_arrow(color):
    c = color
    o = (0, 0, 0)
    return [
            o, o, o, o, o, o, o, o,
            o, o, o, o, c, o, o, o,
            o, o, o, o, c, c, o, o,
            o, o, o, o, c, c, c, o,
            c, c, c, c, c, c, c, c,
            o, o, o, o, c, c, c, o,
            o, o, o, o, c, c, o, o,
            o, o, o, o, c, o, o, o,
        ]

def left_arrow(color):
    c = color
    o = (0, 0, 0)
    return [
            o, o, o, o, o, o, o, o,
            o, o, o, c, o, o, o, o,
            o, o, c, c, o, o, o, o,
            o, c, c, c, o, o, o, o,
            c, c, c, c, c, c, c, c,
            o, c, c, c, o, o, o, o,
            o, o, c, c, o, o, o, o,
            o, o, o, c, o, o, o, o,
        ]

def up_arrow(color):
    c = color
    o = (0, 0, 0)
    return [
            o, o, o, c, o, o, o, o,
            o, o, c, c, c, o, o, o,
            o, c, c, c, c, c, o, o,
            c, c, c, c, c, c, c, o,
            o, o, o, c, o, o, o, o,
            o, o, o, c, o, o, o, o,
            o, o, o, c, o, o, o, o,
            o, o, o, c, o, o, o, o,
        ]

def down_arrow(color):
    c = color
    o = (0, 0, 0)
    return [
            o, o, o, c, o, o, o, o,
            o, o, o, c, o, o, o, o,
            o, o, o, c, o, o, o, o,
            o, o, o, c, o, o, o, o,
            c, c, c, c, c, c, c, o,
            o, c, c, c, c, c, o, o,
            o, o, c, c, c, o, o, o,
            o, o, o, c, o, o, o, o,
        ]

def circle(color):
    c = color
    o = (0, 0, 0)
    return [
            o, o, o, o, o, o, o, o,
            o, o, c, c, c, o, o, o,
            o, c, o, o, o, c, o, o,
            c, o, o, o, o, o, c, o,
            c, o, o, o, o, o, c, o,
            c, o, o, o, o, o, c, o,
            o, c, o, o, o, c, o, o,
            o, o, c, c, c, o, o, o,
        ]