import streamlit as st
import requests

st.title('To-Do App')

# Function to fetch todos
def fetch_todos():
    response = requests.get('http://localhost:8000/todos/')
    return response.json()

# Function to create a todo
def create_todo(task):
    todo = {'id': len(fetch_todos()) + 1, 'task': task, 'completed': False}
    requests.post('http://localhost:8000/todos/', json=todo)

# Display todos
todos = fetch_todos()
for todo in todos:
    st.write(f"{todo['task']} - {'Completed' if todo['completed'] else 'Not Completed'}")

# Input for new todo
new_todo = st.text_input('Add a new todo')
if st.button('Add'):
    create_todo(new_todo)
    st.experimental_rerun()
