"""
Author: pham cong hoang
Date: 18/10/2021

Problem: Describe how a row-major traversal visits every position in a two-dimensional grid.
Solution:
Thiết bị lấy mẫu đo các giá trị màu rời rạc tại các điểm riêng biệt trên lưới hai chiều. Những giá trị
là các pixel, đã được giới thiệu trước đó trong chương này. Về lý thuyết, càng nhiều pixel được lấy mẫu,
hình ảnh kết quả sẽ xuất hiện liên tục và trung thực hơn. Tuy nhiên, trong thực tế, mắt người
không thể phân biệt các đối tượng gần nhau hơn 0,1 mm, do đó, lấy mẫu 10 pixel trên mỗi tuyến tính
milimet (250 pixel trên inch và 62.500 pixel trên inch vuông) sẽ rất chính xác.
Do đó, một hình ảnh 3 inch x 5 inch sẽ cần xấp xỉ một megapixel. Đối với hầu hết các mục đích,
tuy nhiên, bạn có thể quyết định kích thước lấy mẫu thấp hơn nhiều và do đó, ít pixel hơn trên mỗi inch vuông.

"""
