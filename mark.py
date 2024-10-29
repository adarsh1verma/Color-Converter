import streamlit as st
from streamlit import color_picker
from PIL import ImageColor

#st.title("All-in-One Color Converter")
st.markdown("""
    <h1 style='
        color: #9054e6;
        padding: 20px;
        text-align: center;
        border-radius: 10px;
        font-size: 36px;
        font-weight: bold;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    '>
        Color Converter: HSL, HEX & RGB
    </h1>
""", unsafe_allow_html=True)

def hex_to_hsl(hex_color):
    # Convert hex to RGB
    r, g, b = ImageColor.getrgb(hex_color)

    # Normalize RGB values to [0, 1]
    r /= 255.0
    g /= 255.0
    b /= 255.0

    mx = max(r, g, b)
    mn = min(r, g, b)
    l = (mx + mn) / 2

    if mx == mn:  # Achromatic
        h = s = 0
    else:
        c = mx - mn
        if mx == r:
            h = (g - b) / c
        elif mx == g:
            h = (b - r) / c + 2
        else:
            h = (r - g) / c + 4

        s = c / (1 - abs(2 * l - 1))
        h *= 60  # Convert to degrees
        if h < 0:
            h += 360

    # Convert to percentage
    s = s * 100
    l = l * 100

    return round(h), round(s), round(l)


    #return " h : " +str(round(h))+"%", " s : " +str(round(s))+"%", " l : " +str(round(l))+"%"

col1, col2, col3 = st.columns([2, 2, 2])  # Adjust column ratios as needed

with col1:
    st.write("Choose a color:")
    hex = st.color_picker("IN HEX")
    st.write(hex)

with col2:

    st.write("Choose a color:")

    z =  st.color_picker("IN RGB")
    n = ImageColor.getrgb(z)

    st.write("Red:", f"{n[0]}%")
    st.write("Green:", f"{n[1]}%")
    st.write("Blue:", f"{n[2]}%")

    st.write(n)

with col3:

    st.write("Choose a color:")

    z = st.color_picker("IN HSL")
    b = hex_to_hsl(z)

    st.write("Hue:", f"{b[0]}%")
    st.write("Saturation:", f"{b[1]}%")
    st.write("Lightness:", f"{b[2]}%")

    st.write(b)






