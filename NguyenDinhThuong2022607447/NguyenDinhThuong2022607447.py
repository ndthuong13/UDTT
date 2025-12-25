








































#Tx2 Đề 1
# Cho tệp dữ liệu cpu.csv
# Sử dụng công cụ Python để:
# 1.	Chuẩn hóa dữ liệu cho 2 cột đầu về [0, 1] và các cột còn lại (trừ cột class) theo Standardize Data, số hóa cột class.
# 2.	Thực hiện biến đổi Furrier-Transform cho dữ liệu của 10 dòng đầu (thuận, nghịch). In dữ liệu các dòng này trước khi biến đổi, khi đã biến đổi thuận và khi biến đổi nghịch.
# 3.	Chia dữ liệu sao cho 95% dùng để train, 5% dùng để test
# 4.	Thực hiện phép chia dữ liệu trên bộ train để có dữ liệu sử dụng cho quy trình thực nghiệm kiểm tra chéo 5-fold.
# 5.	Thực hiện phân lớp bộ dữ liệu test trên 5-fold bằng mô hình Bayes. Cho biết có bao nhiêu mẫu test được mô hình phân lớp đúng, bao nhiêu mẫu phân lớp sai?
# 6.	Thực hiện phân lớp bộ dữ liệu test trên 5-fold bằng mô hình KNN. Cho biết có bao nhiêu mẫu test được mô hình phân lớp đúng, bao nhiêu mẫu phân lớp sai?
# 7.	Hiển thị kết quả: Accuracy, Precision, Recall của từng lần train 5-fold và trung bình, và các đồ thị tương ứng của chúng.
#Tx2 Đề 2
# Đề 2
# Cho tệp dữ liệu wine.csv
# Sử dụng công cụ Python để:
# a.	Chuẩn hóa dữ liệu cho 4 cột đầu về [0, 10] và các cột còn lại (trừ cột class) theo Normalize Data, số hóa cột class.
# b.	Thực hiện biến đổi cosin cho dữ liệu của 5 dòng đầu (thuận, nghịch). In dữ liệu của các dòng này trước khi biến đổi, khi đã biến đổi thuận và khi biến đổi nghịch.
# c.	Chia dữ liệu sao cho 97% dùng để train, 3% dùng để test
# d.	Thực hiện phép chia dữ liệu trên bộ train để có dữ liệu sử dụng cho quy trình thực nghiệm kiểm tra chéo 10-fold.
# e.	Thực hiện phân lớp bộ dữ liệu test trên 10-fold bằng mô hình SVM. Xác định độ chính xác của mô hình trên bộ test này.
# f.	Thực hiện phân lớp bộ dữ liệu test trên 10-fold bằng mô hình Logistic. Xác định độ chính xác của mô hình trên bộ test này.
# g.	Hiển thị kết quả: Accuracy, Precision, Recall của từng lần train và trung bình, và các đồ thị tương ứng của chúng.
#

#Tx1 Đề 1
#Câu 2
# Cho bộ dữ liệu trong file tương ứng:
#
# a)	Chuẩn hóa các cột số 1 theo phương pháp MinMaxScaler để đưa dữ liệu tương ứng về đoạn [0,1].
# b)	Chuẩn hóa cột 2 theo phương pháp sử dụng Standardize Data.
# c)	Chuẩn hóa cột 3 theo phương pháp sử dụng Normalize Data
# d)	Sử dụng công cụ thích hợp để thực hiện Furrier-Transform trên bộ dữ liệu trên.
# e)	Số hóa cột cuối cùng
#Tx1 Đề 2
#Câu 2
# Cho bộ dữ liệu trong file tương ứng:
#
# a)	Chuẩn hóa các cột số 1 theo phương pháp MinMaxScaler để đưa dữ liệu tương ứng về đoạn [1,5]
# b)	Chuẩn hóa cột 2 theo phương pháp sử dụng Standardize Data.
# c)	Chuẩn hóa cột 3 theo phương pháp sử dụng Normalize Data
# d)	Sử dụng công cụ thích hợp để thực hiện DCT trên bộ dữ liệu trên.//1
# e)	Số hóa cột cuối cùng
#Đề ôn tập bài 10
# Sử dụng công cụ Python để:
# a.	Đọc dữ liệu từ tệp cho trước và tiến hành chuẩn hóa dư liệu về [0, 1] cho tất cả các cột.
# b.	Chia bộ dữ liệu trên thành các bộ train và test sao cho: 60% dữ liệu train và 40% dữ liệu test. Thực hiện phép chia dữ liệu để có dữ liệu sử dụng cho quy trình thực nghiệm kiểm tra chéo 5-fold.
# c.	Thực hiện phân lớp bộ dữ liệu test trên 5-fold bằng mô hình Bayes.
# d.	Thực hiện phân lớp bộ dữ liệu test trên 5-fold bằng mô hình SVM.
# e.	Hiển thị kết quả: bảng kết quả có chứa Accuracy, Precision, Recall và các đồ thị tương ứng.
