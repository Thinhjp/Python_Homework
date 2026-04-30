h = BrowserHistory("trang-chu")
h.visit("san-pham/ao-thun")
h.visit("san-pham/quan-jean")
h.visit("gio-hang")


print(h.back(1))
print(h.back(1))
print(h.forward(1))
print(h.back(3))