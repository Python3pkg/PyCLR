from .sequences import styles


def func_builder(style):
    def func(s):
        return styles[style]['open'] + s + styles[style]['close']
    func.__name__ = style
    return func


for style in styles:
    globals()[style] = func_builder(style)
