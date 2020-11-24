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
    DTL_CLR = ["#515BD4", "#69E641", "#F3455D", "#F9C946", "#8F46D1", "#3EA23E", "#0FF0A5"]
    WIN_HEIGHT = 500  # window's height, px
    OVERLAY_WIDTH = 150  # px
    X_BLOCKS = 11  # blocks
    Y_BLOCKS = 20  # blocks
    LEVEL_CONDITION = 8
    POINTS_FOR_LINES = [0, 100, 300, 700, 1500]
    DTL_BORDER_WIDTH = 4
    DTL_TYPES = [
        [
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ], [
            [0, 0, 0],
            [1, 1, 1],
            [0, 1, 0]
        ], [
            [1, 1],
            [1, 1]
        ], [
            [1, 1, 0],
            [0, 1, 0],
            [0, 1, 0]
        ], [
            [0, 1, 1],
            [0, 1, 0],
            [0, 1, 0]
        ], [
            [0, 0, 0],
            [0, 1, 1],
            [1, 1, 0]
        ], [
            [0, 0, 0],
            [1, 1, 0],
            [0, 1, 1]
        ]
    ]
    # Don't touch
    DTL_BRD_CLR = list(map(get_border_clr, DTL_CLR))
    WIN_HEIGHT = WIN_HEIGHT - WIN_HEIGHT % Y_BLOCKS
    WIN_WIDTH = WIN_HEIGHT * X_BLOCKS // Y_BLOCKS + OVERLAY_WIDTH
    DTL_OFFSET = DTL_BORDER_WIDTH // 2
    DTL_SIZE = WIN_HEIGHT // Y_BLOCKS
