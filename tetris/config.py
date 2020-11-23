def get_border_clr(clr):
    CONTRAST = 50
    return '#%02x%02x%02x' % tuple(map(
        lambda x: max(0, x - CONTRAST),
        tuple(int(clr[i:i+2], 16) for i in (1, 3, 5))
    ))


class Configuration:
    # Settings
    BG_CLR = "#111"
    FG_CLR = "gray"
    TXT_CLR = "white"
    DTL_CLR = ["#515BD4", "#69E641", "#F3455D", "#F9C946", "#8F46D1"]
    START_INTERVAL = 100  # ms
    HEIGHT = 500  # window's height, px
    OVERLAY_WIDTH = HEIGHT // 4  # px
    FIELD_WIDTH = 10  # blocks
    FIELD_HEIGHT = 20  # blocks
    DTL_BORDER_WIDTH = 4
    DTL_TYPES = [
        [
            [1, 1, 1, 1]
        ], [
            [1, 1, 1],
            [0, 1, 0]
        ], [
            [1, 1],
            [1, 1]
        ], [
            [1, 1, 1],
            [1, 0, 0]
        ], [
            [0, 1, 1],
            [1, 1, 0]
        ]
    ]
    # Don't touch
    MAX_OVERLAY_WIDTH = HEIGHT // 3
    DTL_BRD_CLR = list(map(get_border_clr, DTL_CLR))
    DTL_OFFSET = DTL_BORDER_WIDTH // 2
    DTL_SIZE = HEIGHT // FIELD_HEIGHT
