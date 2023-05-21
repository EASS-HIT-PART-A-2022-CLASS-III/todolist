import streamlit as st
import requests

# FastAPI backend URL
backend_url = "http://localhost:8000"

# Streamlit app
def main():
    st.title("Todo App")

    menu = ["Create", "Read", "Update", "Delete"]
    choice = st.sidebar.selectbox("Select Operation", menu)

    if choice == "Create":
        st.subheader("Add Task")
        task = st.text_input("Enter Task")
        if st.button("Add"):
            todo = {"title": task}
            response = requests.post(f"{backend_url}/api/todo", json=todo)
            if response.status_code == 200:
                st.success("Task added successfully!")
            else:
                st.error("Failed to add task")

    elif choice == "Read":
        st.subheader("View Tasks")
        response = requests.get(f"{backend_url}/api/todo")
        if response.status_code == 200:
            todos = response.json()
            for todo in todos:
                st.write(f"- {todo['title']}")
        else:
            st.error("Failed to retrieve tasks")

    elif choice == "Update":
        st.subheader("Update Task")
        response = requests.get(f"{backend_url}/api/todo")
        if response.status_code == 200:
            todos = response.json()
            todo_list = [todo["title"] for todo in todos]
            selected_task = st.selectbox("Select Task", todo_list)
            new_task = st.text_input("Enter New Task")
            if st.button("Update"):
                todo = {"title": selected_task, "description": new_task}
                response = requests.put(f"{backend_url}/api/todo/{selected_task}", json=todo)
                if response.status_code == 200:
                    st.success("Task updated successfully!")
                else:
                    st.error("Failed to update task")
        else:
            st.error("Failed to retrieve tasks")

    elif choice == "Delete":
        st.subheader("Delete Task")
        response = requests.get(f"{backend_url}/api/todo")
        if response.status_code == 200:
            todos = response.json()
            todo_list = [todo["title"] for todo in todos]
            selected_task = st.selectbox("Select Task", todo_list)
            if st.button("Delete"):
                response = requests.delete(f"{backend_url}/api/todo/{selected_task}")
                if response.status_code == 200:
                    st.success("Task deleted successfully!")
                else:
                    st.error("Failed to delete task")
        else:
            st.error("Failed to retrieve tasks")

if __name__ == "__main__":
    main()
