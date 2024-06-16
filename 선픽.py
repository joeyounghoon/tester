import streamlit as st
import streamlit.components.v1 as components

# Custom CSS for styling
css = """
<style>
body {
    font-family: 'Spoqa Han Sans Neo', sans-serif;
}

.header {
    background-color: #333;
    color: white;
    padding: 20px;
    text-align: center;
    font-size: 25px;
}

.sidebar {
    width: 20%;
    float: left;
    padding: 20px;
}

.sidebar img {
    max-width: 100%;
    height: auto;
}

.main-content {
    width: 78%;
    float: right;
    padding: 20px;
}

.champion-grid {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 10px;
}

.champion-box {
    background-color: #f4f4f9;
    border: 1px solid #ddd;
    border-radius: 5px;
    text-align: center;
    padding: 10px;
}

.combo-box {
    background-color: #e3f2fd;
    width: 120px;
    height: 120px;
    display: inline-block;
    vertical-align: top;
    margin: 5px;
    text-align: center;
    padding: 20px;
    border-radius: 5px;
    border: 1px solid #ddd;
}

.counter-box {
    background-color: #fce4ec;
    width: 120px;
    height: 120px;
    display: inline-block;
    vertical-align: top;
    margin: 5px;
    text-align: center;
    padding: 20px;
    border-radius: 5px;
    border: 1px solid #ddd;
}

.clearfix::after {
    content: "";
    clear: both;
    display: table;
}
</style>
"""

js_code = """
<script>
function selectChampion(name) {
    alert("Selected Champion: " + name);
}
</script>
"""

# Header
st.markdown(f'<div class="header">OptimalBotAI</div>', unsafe_allow_html=True)

# Sidebar content
st.markdown('<div class="sidebar">', unsafe_allow_html=True)
st.text_input("Search Champions", "")
st.markdown('<p>챔피언 목록</p>', unsafe_allow_html=True)
champion_names = ["카이사", "진", "에쉬", "블츠", "룰루", "세라핀", "챔프7", "챔프8", "챔프9", "챔프10"]

# Display champions in a grid format
st.markdown('<div class="champion-grid">', unsafe_allow_html=True)
for name in champion_names:
    st.markdown(f'''
    <div class="champion-box" onclick="selectChampion('{name}')">
        {name}
    </div>
    ''', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Close sidebar div

# Main content
st.markdown('<div class="main-content clearfix">', unsafe_allow_html=True)
st.markdown('<p>챔피언을 선택해 주세요!</p>', unsafe_allow_html=True)

selections = {
    "조합": ["룰루", "룰루", "룰루"],
    "카운터": ["세라핀", "진"]
}

# Selections display
st.markdown('<div>', unsafe_allow_html=True)
for key, imgs in selections.items():
    st.markdown(f'<p>{key}</p>', unsafe_allow_html=True)
    for img in imgs:
        st.markdown(f'<div class="combo-box">{img}</div>', unsafe_allow_html=True)
    st.markdown('<div class="combo-box">+</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Embed JavaScript
components.html(js_code, height=0, width=0)

# Embed CSS
st.markdown(css, unsafe_allow_html=True)
