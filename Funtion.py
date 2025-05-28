from db import get_connection

def addlist():
    title = input("Enter task title: ").strip()
    status = False
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO INFO(Title, Status) VALUES(%s, %s)", (title, status))
    conn.commit()
    conn.close()
    print("Task added.")


def viewlist():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT ID, Title, Status FROM INFO ORDER BY ID")
    rows = cursor.fetchall()  

    if not rows:
        print("No task found")
    else:
        for row in rows:
            status = "Done" if row[2] else "Pending"
            print(f"{row[0]} | {row[1]} | {status}")
    conn.close()


def mark_as_completed():
    task_id = input("Enter task ID to mark as complete: ").strip()
    if not task_id.isdigit():
        print("Enter valid ID")
        return
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE INFO SET Status = TRUE WHERE ID = %s", (task_id,))
    conn.commit()
    if cursor.rowcount == 0:
        print("Task ID not found.")
    else:
        print("Task marked as completed.")
    conn.close()


def delete_list():
    task_id = input("Enter task ID to delete: ").strip()
    if not task_id.isdigit():
        print("Enter valid ID")
        return
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM INFO WHERE ID = %s", (task_id,))
    conn.commit()
    if cursor.rowcount == 0:
        print("Task ID not found.")
    else:
        print("Task deleted.")
    conn.close()
