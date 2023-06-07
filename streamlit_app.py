import streamlit as st
tabs = ["Tab 1", "Tab 2", "Tab 3"]
def main():
    
    current_tab = st.sidebar.radio("Select a tab", tabs)
    
    if current_tab == "Tab 1":
        tab1()
    elif current_tab == "Tab 2":
        tab2()
    elif current_tab == "Tab 3":
        tab3()

def tab1():
    st.title("Tab 1")
    st.write("Content for Tab 1")
    next_tab_button("Tab 2")

def tab2():
    st.title("Tab 2")
    st.write("Content for Tab 2")
    next_tab_button("Tab 3")

def tab3():
    st.title("Tab 3")
    st.write("Content for Tab 3")
    next_tab_button("Tab 1")

def next_tab_button(next_tab):
    col1, col2, col3 = st.columns(3)
    if col2.button("Next Tab", key=next_tab):
        next_tab_index = (tabs.index(next_tab) + 1) % len(tabs)
        st.experimental_set_query_params(tab=tabs[next_tab_index])

if __name__ == "__main__":
    main()
