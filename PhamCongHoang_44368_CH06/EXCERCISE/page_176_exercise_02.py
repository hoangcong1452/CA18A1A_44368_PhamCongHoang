"""
Author: pham cong hoang
Date: 22/10/2021
Problem: Describe the processes of top-down design and stepwise refinement. Where does
the design start, and how does it proceed?
Solution:
Một chiến lược thiết kế phổ biến cho các chương trình có quy mô và độ phức tạp đáng kể được gọi là thiết kế từ trên xuống.
Chiến lược này bắt đầu với một cái nhìn toàn cầu về toàn bộ vấn đề và chia vấn đề thành các phần nhỏ hơn,
các vấn đề con dễ quản lý hơn — một quá trình được gọi là phân rã vấn đề. Vì mỗi vấn đề con được tách biệt,
giải pháp của nó được gán cho một chức năng. Sự phân hủy vấn đề có thể tiếp tục xuống các cấp thấp hơn, bởi vì
đến lượt nó, một vấn đề con có thể chứa hai hoặc nhiều vấn đề cấp thấp hơn để giải quyết. Khi các chức năng được phát triển
để giải quyết từng vấn đề con, giải pháp cho vấn đề tổng thể dần dần được điền vào chi tiết.
Quá trình này còn được gọi là sàng lọc từng bước.
Các ví dụ về chương trình ban đầu của chúng tôi trong Chương 1–4 đủ đơn giản để chúng có thể được phân tách thành
ba phần — đầu vào của dữ liệu, quá trình xử lý dữ liệu và đầu ra của kết quả. Không có bộ phận nào trong số này bắt buộc
nhiều hơn một hoặc hai câu lệnh mã và tất cả chúng đều xuất hiện trong một chuỗi câu lệnh duy nhất.
Tuy nhiên, bắt đầu với chương trình phân tích văn bản của Chương 4, các vấn đề nghiên cứu điển hình của chúng tôi trở nên phức tạp
đủ để đảm bảo phân rã và gán cho các chức năng bổ sung do lập trình viên xác định. Vì mỗi
vấn đề có một cấu trúc khác, thiết kế của giải pháp có một con đường hơi khác. Phần này
xem lại từng chương trình, để khám phá cách thiết kế của họ đã hình thành.
"""