# A function for tweaking the style of the initial html documents generated by
# map_viz.ipynb before they go on display in the index.html iframes.

from bs4 import BeautifulSoup
import re

# Get the font-family of the parent webpage for the theme
css = open("style.css", "r")
rules = css.read()
ff_loc = rules.split("font-family: ")
ff = ff_loc[1].split(";")[0]

def adjust(htmldoc):
    # Reads in either the "rates.html" document or the "counts.html" and throws
    # some <style> tags into the header which change the map's final appearance.
    # Output is saved to "styled_rates.html" or "styled_counts.html".

    doc = BeautifulSoup(open(htmldoc), features="html.parser")
    font_family = ff

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
    #slider-value {{
        font-family: {};
        font-weight: 900;
        color: white;
        }}
    """.format(font_family)

    body = """
    body {
    background-color: black;
    }
    """

    legend = """
    .legend {{
    font-family: {};
    font-weight: 900;
    background-color: rgba(255,255,255,0.5);
    border-radius: 5px;
    }}
    """.format(font_family)

    background = """
    .folium-map {
    background-color: black;
    }
    """

    tooltips = """
    .foliumtooltip {{
    font-family: {};
    }}
    """.format(font_family)


    # New <style> tag in header
    style_tag = doc.new_tag("style")
    doc.head.append(style_tag)
    style_tag.string = slider + slider_value + body + legend + background + tooltips

    # Change initial slider value (this part is not robust to changes in rates.html)
    last_script_tag_on_page = doc.find_all("script")[-1]
    js = last_script_tag_on_page.string
    modified_script = re.sub('"value", 0', '"value", 25', js)
    js.replace_with(modified_script)

    # Save output
    filename = "site-pages/styled_{}".format(htmldoc.split("/")[1])
    with open(filename, 'w') as f:
        f.write(str(doc))

def main():
    adjust("site-pages/rates.html")
    adjust("site-pages/counts.html")

if __name__ == '__main__':
    main()
