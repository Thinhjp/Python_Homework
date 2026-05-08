#Bài 1
class BrowserHistory:
    def __init__(self, homepage: str):
        self.current = homepage 
        # Lịch sử trình duyệt được lưu trữ trong một danh sách, 
        # bắt đầu với trang chủ (homepage)
        self.backward_stack = []
        # backward_stack lưu trữ các trang đã truy cập trước đó để có thể quay lại
        self.forward_stack = []
        # forward_stack lưu trữ các trang đã truy cập sau khi quay lại để có thể đi tiếp
    def visit(self, url: str) -> None:
        self.backward_stack.append(self.current)
        # Khi người dùng truy cập một trang mới, 
        # trang hiện tại được thêm vào backward_stack
        self.current = url
        # Cập nhật trang hiện tại thành URL mới
        self.forward_stack.clear()
        # Khi người dùng truy cập một trang mới, 
        # tất cả lịch sử phía trước của current_index sẽ bị xóa bỏ
    def back(self, steps: int) -> str:
        for i in range(steps):
            self.forward_stack.append(self.current)
            # Khi người dùng nhấn nút "back",
            # trang hiện tại được thêm vào forward_stack
            if self.backward_stack:    
                self.current = self.backward_stack.pop()
            # Cập nhật trang hiện tại thành trang cuối cùng trong backward_stack
        return self.current

    def forward(self, steps: int) -> str:
        for i in range(steps):
            self.backward_stack.append(self.current)
            # Khi người dùng nhấn nút "forward",
            # trang hiện tại được thêm vào backward_stack
            if self.forward_stack: # Kiểm tra nếu forward_stack không rỗng trước khi pop
                self.current = self.forward_stack.pop()
            # Cập nhật trang hiện tại thành trang cuối cùng trong forward_stack
        return self.current