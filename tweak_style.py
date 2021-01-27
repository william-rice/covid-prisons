# Reads in the "rates.html" document and throws some <style> tags into the header
# which change the map's final appearance. Output is saved to "styled.html".

from bs4 import BeautifulSoup
doc = BeautifulSoup(open("rates.html"), features="html.parser")

slider = """
input[type=range] {
  width: 100%;
  margin: 14px 0;
  background-color: transparent;
  -webkit-appearance: none;
}
input[type=range]:focus {
  outline: none;
}
input[type=range]::-webkit-slider-runnable-track {
  background: #ffffff;
  border: 0;
  border-radius: 25px;
  width: 100%;
  height: 7px;
  cursor: pointer;
}
input[type=range]::-webkit-slider-thumb {
  margin-top: -14px;
  width: 15px;
  height: 35px;
  background: rgba(255, 255, 255, 0.9);
  border: 2.1px solid rgba(129, 129, 129, 0.8);
  border-radius: 4px;
  cursor: pointer;
  -webkit-appearance: none;
}
input[type=range]:focus::-webkit-slider-runnable-track {
  background: #ffffff;
}
input[type=range]::-moz-range-track {
  background: #ffffff;
  border: 0;
  border-radius: 25px;
  width: 100%;
  height: 7px;
  cursor: pointer;
}
input[type=range]::-moz-range-thumb {
  width: 15px;
  height: 35px;
  background: rgba(255, 255, 255, 0.9);
  border: 2.1px solid rgba(129, 129, 129, 0.8);
  border-radius: 4px;
  cursor: pointer;
}
input[type=range]::-ms-track {
  background: transparent;
  border-color: transparent;
  border-width: 15px 0;
  color: transparent;
  width: 100%;
  height: 7px;
  cursor: pointer;
}
input[type=range]::-ms-fill-lower {
  background: #f2f2f2;
  border: 0;
  border-radius: 50px;
}
input[type=range]::-ms-fill-upper {
  background: #ffffff;
  border: 0;
  border-radius: 50px;
}
input[type=range]::-ms-thumb {
  width: 15px;
  height: 35px;
  background: rgba(255, 255, 255, 0.9);
  border: 2.1px solid rgba(129, 129, 129, 0.8);
  border-radius: 4px;
  cursor: pointer;
  margin-top: 0px;
  /*Needed to keep the Edge thumb centred*/
}
input[type=range]:focus::-ms-fill-lower {
  background: #ffffff;
}
input[type=range]:focus::-ms-fill-upper {
  background: #ffffff;
}
"""

slider_value = """
#slider-value {
    font-family: monospace;
    font-weight: 900;
    color: white;
    }
"""

body = """
body {
background-color: black;
}
"""

legend = """
.legend {
font-family: monospace;
font-weight: 900;
background-color: rgba(255,255,255,0.5);
border-radius: 5px;
}
"""

background = """
#map_88dc0f05dae54f55a8927d640ca3bbc7 {
background-color: black;
}
"""

style_tag = doc.new_tag("style")
doc.head.append(style_tag)
style_tag.string = slider + slider_value + body + legend + background

filename = "styled.html"
with open(filename, 'w') as f:
    f.write(str(doc))
