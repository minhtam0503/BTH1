import tkinter as tk
from sympy import symbols, diff, integrate, limit, Eq, solve
# Tạo cửa sổ ứng dụng
app = tk.Tk()
app.title("Phần mềm hỗ trợ học tập Giải tích")

# Tạo biến ký tự
x, y = symbols('x y')

# Hàm tính đạo hàm
def calculate_derivative():
    expression = expression_entry.get()
    try:
        derivative = diff(expression, x)
        result_label.config(text=f"Đạo hàm: {derivative}")
    except:
        result_label.config(text="Lỗi! Kiểm tra biểu thức đầu vào.")

# Hàm tính tích phân
def calculate_integral():
    expression = expression_entry.get()
    start= start_entry.get()
    stop= stop_entry.get()
    try:
        integral = integrate(expression, (x,start,stop))
        result_label.config(text=f"Tích phân: {integral}")
    except:
        result_label.config(text="Lỗi! Kiểm tra biểu thức đầu vào.")

# Hàm tính giới hạn
def calculate_limit():
    limit_point = limit_point_entry.get()
    expression = expression_entry.get()
    try:
        value = limit(expression, x, limit_point)
        result_label.config(text=f"Giới hạn tại x = {limit_point}: {value}")
    except:
        result_label.config(text="Lỗi! Kiểm tra giới hạn hoặc biểu thức đầu vào.")

# Hàm giải phương trình
def solve_equation():
    equation = equation_entry.get()
    try:
        equation = Eq(eval(equation))
        solution = solve(equation, (x, y))
        result_label.config(text=f"Giải phương trình: {solution}")
    except:
        result_label.config(text="Lỗi! Kiểm tra phương trình đầu vào.")

# Tạo giao diện
expression_label = tk.Label(app, text="Nhập biểu thức (dùng x):")
expression_label.pack()

expression_entry = tk.Entry(app)
expression_entry.pack()

calculate_derivative_button = tk.Button(app, text="Tính Đạo hàm", command=calculate_derivative)
calculate_derivative_button.pack()

start_label = tk.Label(app, text="điểm đầu:")
start_label.pack()

start_entry = tk.Entry(app)
start_entry.pack()

stop_label = tk.Label(app, text="điểm cuối:")
stop_label.pack()

stop_entry = tk.Entry(app)
stop_entry.pack()

calculate_integral_button = tk.Button(app, text="Tính Tích phân", command=calculate_integral)
calculate_integral_button.pack()

limit_point_label = tk.Label(app, text="Nhập điểm giới hạn (x):")
limit_point_label.pack()

limit_point_entry = tk.Entry(app)
limit_point_entry.pack()

calculate_limit_button = tk.Button(app, text="Tính Giới hạn", command=calculate_limit)
calculate_limit_button.pack()

equation_label = tk.Label(app, text="Nhập phương trình (ví dụ: x**2 + x - 1):")
equation_label.pack()

equation_entry = tk.Entry(app)
equation_entry.pack() 

solve_button = tk.Button(app, text="Giải phương trình", command=solve_equation)
solve_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()