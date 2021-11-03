"""
Author: pham cong hoang
Date: 22/10/2021


Problem: Explain how an algorithm solves a general class of problems and how a function
definition can support this property of an algorithm.
Solution:
Vấn đề là bộ não con người có thể tự quấn lấy một vài thứ cùng một lúc
(các nhà tâm lý học nói thoải mái ba điều, và nhiều nhất là bảy điều). Mọi người đối phó với sự phức tạp bằng cách phát triển
một cơ chế để đơn giản hóa hoặc ẩn nó. Cơ chế này được gọi là một sự trừu tượng hóa. Nói một cách dễ hiểu nhất,
một sự trừu tượng che giấu chi tiết và do đó cho phép một người xem nhiều thứ chỉ là một thứ.
Chúng tôi sử dụng trừu tượng để chỉ những công việc phổ biến nhất trong cuộc sống hàng ngày. Ví dụ, hãy xem xét
cụm từ "đang giặt quần áo của tôi." Biểu thức này đơn giản, nhưng nó đề cập đến một quá trình phức tạp
liên quan đến việc lấy quần áo bẩn từ thùng rác, tách chúng thành màu trắng và màu, tải
chúng vào máy giặt, chuyển chúng vào máy sấy, và gấp chúng lại và cho vào tủ ủi.
Thật vậy, nếu không có sự trừu tượng, hầu hết các hoạt động hàng ngày của chúng ta sẽ không thể thảo luận, lập kế hoạch,
hoặc thực hiện. Tương tự như vậy, các nhà thiết kế hiệu quả phải phát minh ra các trừu tượng hữu ích để kiểm soát sự phức tạp. Trong
phần này, chúng tôi xem xét các cách khác nhau mà các hàm đóng vai trò là cơ chế trừu tượng trong một chương trình.Vấn đề là bộ não con người có thể tự quấn lấy một vài thứ cùng một lúc
(các nhà tâm lý học nói thoải mái ba điều, và nhiều nhất là bảy điều). Mọi người đối phó với sự phức tạp bằng cách phát triển
một cơ chế để đơn giản hóa hoặc ẩn nó. Cơ chế này được gọi là một sự trừu tượng hóa. Nói một cách dễ hiểu nhất,
một sự trừu tượng che giấu chi tiết và do đó cho phép một người xem nhiều thứ chỉ là một thứ.
Chúng tôi sử dụng trừu tượng để chỉ những công việc phổ biến nhất trong cuộc sống hàng ngày. Ví dụ, hãy xem xét
cụm từ "đang giặt quần áo của tôi." Biểu thức này đơn giản, nhưng nó đề cập đến một quá trình phức tạp
liên quan đến việc lấy quần áo bẩn từ thùng rác, tách chúng thành màu trắng và màu, tải
chúng vào máy giặt, chuyển chúng vào máy sấy, và gấp chúng lại và cho vào tủ ủi.
Thật vậy, nếu không có sự trừu tượng, hầu hết các hoạt động hàng ngày của chúng ta sẽ không thể thảo luận, lập kế hoạch,
hoặc thực hiện. Tương tự như vậy, các nhà thiết kế hiệu quả phải phát minh ra các trừu tượng hữu ích để kiểm soát sự phức tạp. Trong
phần này, chúng tôi xem xét các cách khác nhau mà các hàm đóng vai trò là cơ chế trừu tượng trong một chương trình.

"""