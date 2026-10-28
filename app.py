tasks = []

def add_task(task_name):
    """Thêm một công việc mới dưới dạng dictionary."""
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

def delete_task(task_index):
    """Xóa một công việc khỏi danh sách tasks dựa trên chỉ số (tính từ 1), có kiểm tra hợp lệ[cite: 5, 12]."""
    real_index = task_index - 1
    if 0 <= real_index < len(tasks):
        removed = tasks.pop(real_index)
        print(f"Đã xóa công việc: '{removed['name']}'")
    else:
        print("Chỉ số công việc không hợp lệ để xóa!")

def list_tasks():
    """Hiển thị danh sách công việc kèm trạng thái [x] hoặc [ ]."""
    print("\n--- DANH SÁCH CÔNG VIỆC ---")
    if not tasks:
        print("Danh sách trống.")
    for index, task in enumerate(tasks, start=1):
        status = "x" if task['completed'] else " "
        print(f"{index}. [{status}] {task['name']}")

# --- Điểm bắt đầu của chương trình
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    
    # Đánh dấu hoàn thành và kiểm tra
    complete_task(1)
    list_tasks()
    
    # Xóa công việc số 2 và kiểm tra lại
    delete_task(2)
    list_tasks()