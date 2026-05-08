# 1. Lịch sử điều hướng trang [STACK]
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
        
h = BrowserHistory("trang-chu")
h.visit("san-pham/ao-thun")
h.back(1)
h.visit("san-pham/quan-jean")
h.visit("gio-hang")


print(h.back(1))
print(h.back(1))
print(h.forward(1))
print(h.back(3))

# 2. Kiểm tra cú pháp JSON hợp lệ [STACK]


def is_valid_brackets(s: str) -> bool: 
    # Hàm này nhận một chuỗi s; bool là kiểu dữ liệu boolean, có giá trị True hoặc False.
    stack = [] # Sử dụng một stack để lưu trữ các dấu ngoặc mở
    bracket_map = {')': '(', '}': '{', ']': '['} 
    # Bản đồ để kiểm tra dấu ngoặc đóng tương ứng với dấu ngoặc mở

    for char in s: # Duyệt qua từng ký tự trong chuỗi s
        if char in bracket_map.values(): 
            # Nếu ký tự là một dấu ngoặc mở, thêm nó vào stack
            stack.append(char)
        elif char in bracket_map.keys(): 
            # Nếu ký tự là một dấu ngoặc đóng, 
            # kiểm tra xem stack có rỗng không 
            # hoặc phần tử cuối cùng của stack có phải là dấu ngoặc mở tương ứng không
            if not stack or stack.pop() != bracket_map[char]: 
                #stack.pop() sẽ lấy phần tử cuối cùng của stack và loại bỏ nó khỏi stack.
                return False
            

    return len(stack) == 0

# Kiểm tra hàm với một số chuỗi mẫu
print(is_valid_brackets('{"name": "An", "items": [1, 2]}')) # True
print(is_valid_brackets('{"data": [{"id": 1}')) # False (Do thiếu đóng ngoặc vuông)
print(is_valid_brackets('(())')) # True
print(is_valid_brackets('{"data": [{"id": 1]}')) # False (Do vị trí đóng ngoặc vuông sai)

# 3. Viết hàm validate_transaction_order(events) kiểm tra list event có tuân theo flow: INIT →
# PROCESSING → COMPLETED hoặc INIT → PROCESSING → FAILED.

events1 = [
{"txn_id": "T1", "event": "INIT"},
{"txn_id": "T2", "event": "INIT"},
{"txn_id": "T2", "event": "PROCESSING"},
{"txn_id": "T2", "event": "COMPLETED"},
{"txn_id": "T1", "event": "PROCESSING"},
{"txn_id": "T1", "event": "FAILED"},
]
events2 = [
{"txn_id": "T3", "event": "INIT"},
{"txn_id": "T3", "event": "COMPLETED"}, # thieu PROCESSING
]




def validate_transaction_order(events): 
    txn_states = {} 
    # Lưu trạng thái hiện tại của mỗi giao dịch (txn_id)
    completed_count = 0 
    # Đếm số giao dịch hoàn thành hợp lệ
    errors = [] 
    # Lưu trữ các lỗi phát hiện trong quá trình kiểm tra

    for event in events:
        txn_id = event["txn_id"]
        action = event["event"]

        if action == "INIT":
            txn_states[txn_id] = "INIT" 
            # Khi gặp sự kiện INIT, đặt trạng thái của giao dịch đó là "INIT"
        elif action == "PROCESSING": 
            # Khi gặp sự kiện PROCESSING, kiểm tra xem giao dịch đã ở trạng thái "INIT" chưa
            if txn_states.get(txn_id) != "INIT":
                errors.append(f"{txn_id}: thieu buoc INIT")
            else:
                txn_states[txn_id] = "PROCESSING" 
                # Nếu đúng, cập nhật trạng thái thành "PROCESSING"
        elif action in ["COMPLETED", "FAILED"]:
            if txn_states.get(txn_id) != "PROCESSING":
                errors.append(f"{txn_id}: thieu buoc PROCESSING")
            else:
                completed_count += 1
                del txn_states[txn_id]

    valid = len(errors) == 0 
    # Nếu không có lỗi nào trả về True, ngược lại trả về False
    return {"valid": valid, "completed": completed_count, "errors": errors}

print(validate_transaction_order(events1))
print(validate_transaction_order(events2))

# 4. Hàng đợi ưu tiên giao hàng [QUEUE]
# Shipping service ưu tiên đơn VIP và đơn Express trước đơn thường.
# Viết class PriorityShippingQueue dùng heapq. Mức ưu tiên: express=1, vip=2, normal=3. Cùng mức thì
# FIFO.
# Gợi ý: Sử dụng “python priority queue”

import heapq # heapq là một module trong Python 
# Mặc định heapq tạo ra một min-heap, vì vậy phần tử có mức ưu tiên cao nhất (priority thấp nhất) sẽ được xử lý trước.

class PriorityShippingQueue:
    def __init__(self):
        self.queue = [] # Sử dụng một list để lưu trữ các đơn hàng trong heap
        self.counter = 0  # Đếm số lượng đơn hàng để đảm bảo FIFO
        self.priority_map = {
            "express": 1, 
            "vip": 2, 
            "normal": 3
        } # Bản đồ để xác định mức ưu tiên của từng loại đơn hàng
        # FIFO (First In, First Out) được thêm vào trước sẽ được xử lý trước nếu có cùng mức ưu tiên.

    def enqueue(self, shipment: dict): 
        # Enqueue nghĩa là thêm một phần tử vào hàng đợi. 
        # shipment là một dictionary chứa thông tin về đơn hàng
        priority = self.priority_map.get(shipment["type"], 3) 
        # Lấy mức ưu tiên từ shipment, mặc định là 3 nếu không xác định được loại
        heapq.heappush(self.queue, (priority, self.counter, shipment)) 
        # heappush sẽ thêm phần tử vào heap. Heap so sánh từ trái sang phải của tuple.
        # trong heap, giá trị nhỏ hơn sẽ đưa lên trước.
        # thứ tự ưu tiên từ priority, = nhau thì so counter (ai vào trước)
        self.counter += 1 
        # Tăng counter sau mỗi lần thêm đơn hàng để đảm bảo FIFO
    def dequeue(self): 
        # Dequeue - ra khỏi hàng đợi.
        if not self.queue:
            return None  # Trả về None nếu hàng đợi rỗng
        return heapq.heappop(self.queue)[2] 
        # [2] là thứ tự trong chuỗi self.queue để lấy phần shipment từ tuple (priority, counter, shipment)
        

psq = PriorityShippingQueue()
psq.enqueue({"id": "S1", "type": "normal", "dest": "HN"})
psq.enqueue({"id": "S2", "type": "express", "dest": "HCM"})
psq.enqueue({"id": "S3", "type": "vip", "dest": "DN"})
psq.enqueue({"id": "S4", "type": "express", "dest": "HN"})

print(psq.dequeue())
print(psq.dequeue())
print(psq.dequeue())

# 5. Mô phỏng hàng chờ thanh toán tại quầy [QUEUE]
# POS system cần mô phỏng hàng chờ tại nhiều quầy thanh toán để tối ưu staffing.
# Viết hàm simulate_checkout(customers, n_counters): khách xếp vào quầy ít người nhất, trả về thống kê
# mỗi quầy xử lý bao nhiêu khách.

customers = [
{"id": "C1", "items": 5},
{"id": "C2", "items": 12},
{"id": "C3", "items": 3},
{"id": "C4", "items": 8},
{"id": "C5", "items": 1},
]

def simulate_checkout(customers, n_counters):
    counters = {f"counter_{i+1}": {"customers": [], "total_items": 0} for i in range(n_counters)} 
    # Tạo một dictionary để lưu trữ thông tin về mỗi quầy thanh toán, và vòng for tương ứng với n_counters
    #bao gồm danh sách khách hàng và tổng số mặt hàng đã xử lý.

    for customer in customers:
        # Duyệt qua từng khách hàng trong danh sách customers
        least_busy_counter = min(counters.keys(), key=lambda c: len(counters[c]["customers"])) 
        # Tìm quầy có ít khách hàng nhất bằng cách sử dụng hàm min 
        # với key là độ dài của danh sách khách hàng tại mỗi quầy.
        counters[least_busy_counter]["customers"].append(customer["id"]) 
        # Thêm ID của khách hàng vào danh sách khách hàng của quầy được chọn
        counters[least_busy_counter]["total_items"] += customer["items"] 
        # Cập nhật tổng số mặt hàng 
    return counters 
    # Trả về dictionary chứa thông tin về mỗi quầy sau khi đã phân bổ tất cả khách hàng

print(simulate_checkout(customers, n_counters=2))