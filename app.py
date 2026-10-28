# Thay đổi cấu trúc danh sách tasks thành danh sách các dictionary[cite: 11]
tasks = []

def add_task(task_name):
    """Thêm một công việc mới dưới dạng dictionary với trạng thái completed là False."""
    tasks.append({'name': task_name, 'completed': False})
    print(f"Đã thêm công việc: '{task_name}'")

def complete_task(task_index):
    """Đánh dấu công việc là hoàn thành dựa trên chỉ số (tính từ 1)."""
    real_index = task_index - 1
    if 0 <= real_index < len(tasks):
        tasks[real_index]['completed'] = True
        print(f"Đã hoàn thành công việc: '{tasks[real_index]['name']}'")
    else:
        print("Chỉ số công việc không hợp lệ!")

def list_tasks():
    """Hiển thị danh sách công việc kèm trạng thái [x] hoặc [ ][cite: 11]."""
    print("\n--- DANH SÁCH CÔNG VIỆC ---")
    for index, task in enumerate(tasks, start=1):
        status = "x" if task['completed'] else " "
        print(f"{index}. [{status}] {task['name']}")

# --- Điểm bắt đầu của chương trình
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    
    # Đánh dấu công việc số 1 là đã hoàn thành
    complete_task(1)
    
    # Hiển thị lại danh sách kiểm tra
    list_tasks()