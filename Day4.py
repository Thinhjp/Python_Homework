class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current_index = 0

    def visit(self, url: str) -> None: 
        # -> None nghĩa là hàm này không trả về giá trị nào, 
        # nó chỉ thực hiện hành động cập nhật lịch sử trình duyệt
        self.history = self.history[:self.current_index + 1]
        # 
        self.history.append(url)
        self.current_index += 1

    def back(self, steps: int) -> str:
        self.current_index = max(0, self.current_index - steps)
        return self.history[self.current_index]

    def forward(self, steps: int) -> str:
        self.current_index = min(len(self.history) - 1, self.current_index + steps)
        return self.history[self.current_index]
h = BrowserHistory("trang-chu")
h.visit("san-pham/ao-thun")
h.back(1)
h.visit("san-pham/quan-jean")
h.visit("gio-hang")


print(h.back(1))
print(h.back(1))
print(h.forward(1))
print(h.back(3))