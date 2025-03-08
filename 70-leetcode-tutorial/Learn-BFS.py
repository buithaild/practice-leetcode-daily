#1. Khởi tạo: Đưa đỉnh nguồn đã cho vào hàng đợi và đánh dấu là đã được truy cập.
#2.  Khám phá: Trong khi hàng đợi không trống:
    # Xóa một nút khỏi hàng đợi và truy cập nút đó (ví dụ: in giá trị của nút đó).
    # Đối với mỗi hàng xóm chưa được truy cập của nút đã bị loại khỏi hàng đợi:
    # Thêm hàng xóm vào hàng đợi.
    # Đánh dấu người hàng xóm đã ghé thăm.
#3. Kết thúc: Lặp lại bước 2 cho đến khi hàng đợi trống.
import collections


def bfsOfGraph(adj, s):
    #Lấy số đỉnh
    V = len(adj)
    # tạo một mảng để lưu trữ quá trình duyệt
    res = []

    q = collections.deque()
    # Đầu tiên đánh dấu tất cả các đỉnh là chưa được thăm
    visited = [False] * V

    # Đánh dấu nút nguồn là đã truy cập và xếp hàng nó
    visited[s] = True
    q.append(s)

    while q:
        #Hủy 1 đỉnh khỏi hàng queue và lưu nó
        curr = q.popleft()
        res.append(curr)

        # Lấy tất cả các đỉnh liền kề của hàng đợi đã loại bỏ
        # đỉnh hiện tại Nếu một đỉnh liền kề chưa được
        # ghé thăm, hãy đánh dấu nó đã ghé thăm và xếp hàng

        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)
    return res

if __name__ == "__main__":
    adj = [ [2, 3, 1], [0], [0, 4], [0], [2] ]
    src = 0
    ans = bfsOfGraph(adj, src)
    for i in ans:
        print(i, end=" ")

