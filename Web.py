import streamlit as st
import Functions

todos = Functions.openfileread()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    Functions.openfilewrite(todos)

st.title('My todo App')
st.text('This is your todo list:')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        Functions.openfilewrite(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Type a todo",
              on_change=add_todo, key='new_todo')
