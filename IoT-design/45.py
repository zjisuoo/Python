from collections import namedtuple
Vision = namedtuple('Vision', ['left', 'right'])
vision = Vision(9.5, 8.8)
vision[0]
vision.left # same as vision[0], but explicit
vision.right # same as vision[1], but explicit