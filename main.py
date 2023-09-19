import streamlit as st
import os


def main():
    st.sidebar.title("Lyrics Viewer")
    uploaded_file = st.sidebar.file_uploader("Upload a text file", type="txt")
    folder_path = 'songs'
    file_names = os.listdir(folder_path)
    selected_file = st.sidebar.selectbox("Select a file", file_names)

    start_button = st.button("Start")
    next_button = st.button("Next")
    back_button = st.button("Back")
    font_size = st.sidebar.slider("Font Size", min_value=10, max_value=30, step=2, value=16)

    # if uploaded_file is not None:
    #     file_contents = uploaded_file.read().decode("utf-8").splitlines()
    #     state = st.session_state.get("state", {"index": 0, "lines": []})

    if selected_file:
        file_path = os.path.join(folder_path, selected_file)
        with open(file_path, "r") as file:
            file_contents = file.read().splitlines()
            state = st.session_state.get("state", {"index": 0, "lines": []})

        if start_button:
            state["lines"] = file_contents[:3]
            state["index"] = 0
            st.markdown(f"<h1 style='font-size:{font_size*2}px'><b>{state['lines'][0]}</b></h1>", unsafe_allow_html=True)
            st.markdown(f"<h1 style='font-size:{font_size}px'>{state['lines'][1]}</h1>", unsafe_allow_html=True)
            st.markdown(f"<h1 style='font-size:{font_size}px'>{state['lines'][2]}</h1>", unsafe_allow_html=True)

        if next_button:
            state["lines"] = file_contents[:]
            if state["index"] < len(state["lines"]) - 1:
                state["index"] += 1
                st.markdown(f"<h1 style='font-size:{font_size}px'><b>{state['lines'][state['index']-1]}</b></h1>",
                            unsafe_allow_html=True)
                st.markdown(f"<h1 style='font-size:{font_size*2}px'><b>{state['lines'][state['index']]}</b></h1>", unsafe_allow_html=True)
                st.markdown(f"<h1 style='font-size:{font_size}px'><b>{state['lines'][state['index']+1]}</b></h1>",
                            unsafe_allow_html=True)

            elif state["index"] == len(state["lines"]) - 1:
                state["index"] += 1
                if state["index"] < len(file_contents):
                    state["lines"] = file_contents[state["index"]:state["index"] + 3]
                    st.markdown(f"<h1 style='font-size:{font_size}px'><b>{state['lines'][0]}</b></h1>", unsafe_allow_html=True)
                    st.markdown(f"<h1 style='font-size:{font_size}px'>{state['lines'][1]}</h1>", unsafe_allow_html=True)
                    st.markdown(f"<h1 style='font-size:{font_size}px'>{state['lines'][2]}</h1>", unsafe_allow_html=True)
                else:
                    st.write("End of lyrics.")

        if back_button:
            if state["index"] > 0:
                state["index"] -= 1
                st.markdown(f"<h1 style='font-size:{font_size}px'><b>{state['lines'][state['index'] - 1]}</b></h1>",
                            unsafe_allow_html=True)
                st.markdown(f"<h1 style='font-size:{font_size * 2}px'><b>{state['lines'][state['index']]}</b></h1>",
                            unsafe_allow_html=True)
                st.markdown(f"<h1 style='font-size:{font_size}px'><b>{state['lines'][state['index'] + 1]}</b></h1>",
                            unsafe_allow_html=True)

        st.session_state["state"] = state
        # st.write(state)


if __name__ == "__main__":
    main()