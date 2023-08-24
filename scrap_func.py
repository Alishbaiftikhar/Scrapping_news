import time
from scrap_ary import ary;
from scrap_bol import bol;
from scrap_geo import geo;
from scrap_thenews import thenews;
from scrap_tribune import tribune;
startime = time.time()
ary()
bol()
geo()
thenews()
tribune()
endtime = time.time()
print("11111111111111111111111111111111111111111111111111111111111111111111111111111111111")
print("Total time taken in seconds:",endtime-startime)