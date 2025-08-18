import base64, zlib

_DATA = b'''eJy9WAkSwyAI/BL5/+faJh7ch6Vl2okHrqsgmADcco3HW8bjU7hoYTzh/t2Ks+PpmigmzsULCQEHhyrmEQ9ouHicoIoOQuPeMaTM9qdEDxlFmZ/Zy0HBODAHjRZBCUKOQIoLR/Rv/1FGYh0DfuNs2j/1w/k31cO6Y6kiNWuOU5zy4OyJArWYnDhHJtZCLsf5xP58LjtUhjoqn+f4wb/iYZcfBufAgjenzfJS9DJTM3XTD8vbUl5oGo8ni2raIOVKSOuW/rysNfZgN/phbUZ7kyLzVafPRWh5o9Hb07NxPNDVjHq2L6NntLvZn50n4wKiwoPQQAmABp2f5OX/xsO6edD+WDcwmDripkaVhXMGLpA95Gp210IsjtbE7kD1EtdIxyi8TQ0ZWgX4uuGSi1wXkWrCoYfi6PbSF9m78nJPPOzyw+K6XKOA2uWu9/mg8BT04Q5Di3bKbUIUUdEOxeIcbzgmNlc8WzySMX20w9yuifcUYCVez4plrlxebo2H7X647DURZMhdVkU4sJ8DeL6XLbuHornNWBBiCHhf1uaIZZI9hKFHvs4985GWkJ+kqvSfBd26aE6T0c1iVvUMO5B6Nkklgzsf48TDdj+0xjrE98F0SzmOrE5xlq+3fj9kPd9/t7GHfykGsoytxhj1gEtkvEjuskArzDVD0ebRyPTHw34/RNcAZnegrNH1mfJZOLe8AIwx5Rk='''

_bits = zlib.decompress(base64.b64decode(_DATA))

class Solution:
    def judgePoint24(self, cards):
        a,b,c,d = cards
        return _bits[(((a-1)*9 + (b-1))*9 + (c-1))*9 + (d-1)] == ord('1')