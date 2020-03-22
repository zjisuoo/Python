Vision = namedtuple('Vision', ['left', 'combined', 'right'])
vision = Vision(9.5, 9.2, 8.8)
vision.left # still correct
vision.right # still correct (though now is vision[2])
vision.combined # the new vision[1]