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

import streamlit as st

# Image links to be displayed
image_links = [
    "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Ashe.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274",
    "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Caitlyn.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274",
    "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Jhin.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274",
    "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Kaisa.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
]

# Other image links to be displayed on click
other_image_links = [
    "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Samira.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274",
    "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/MissFortune.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274",
    "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Vayne.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274",
    "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Xayah.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
]

st.title("Image Gallery with Streamlit and JavaScript")
st.write("Click on an image to see a different image on the right side.")

# Display the images in a row
st.markdown(
    """
    <div style="display: flex;">
    """,
    unsafe_allow_html=True
)

for i, link in enumerate(image_links):
    st.markdown(
        f"""
        <div id="image-{i}" style="margin-right: 10px;">
            <img src="{link}" onclick="displayDifferentImage({i})"
                 style="cursor: pointer;" width="150" height="150" />
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    """
    </div>
    <h3>Selected Image:</h3>
    <div id="selected-image" style="margin-top: 10px;">
        <img id="main-image" src="" width="300" height="300" />
    </div>
    
    <script>
    let otherImageLinks = [
        "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Samira.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274",
        "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/MissFortune.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274",
        "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Vayne.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274",
        "https://opgg-static.akamaized.net/meta/images/lol/14.12.1/champion/Xayah.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto:good,a_0,f_webp,w_160,h_160&v=1717557723274"
    ];

    function displayDifferentImage(index) {
        document.getElementById('main-image').src = otherImageLinks[index];
    }
    </script>
    """,
    unsafe_allow_html=True
)

# Embed CSS
st.markdown(css, unsafe_allow_html=True)
