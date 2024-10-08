# CoverGenerator

CoverGenerator is a utility for generating simple book covers containing the book title nd author. The covers are generated using SVG and then rendered to an image file. This project is heavily inspired by [racovimge](https://github.com/anqxyr/racovimge/) and uses basically the same methods for creating covers, but this project has better multiline support and doesn't rely on any non-python applications for image exporting.

*NOTE:* Due to limitations with CairoSVG, CoverGenerator can't use embedded fonts and has to instead use system fonts. *For proper word spacing and formatting, [NotoSerif](https://fonts.google.com/noto/specimen/Noto+Serif) Bold & Bold Italic must be installed on your system.* The program will still work without it, but you might have some odd word wrapping.

# Installation

CoverGenerator can be downloaded from it's PyPI package using pip:

    pip3 install CoverGenerator

If you are installing from source, the following python packages are required:

* [CairoSVG](https://github.com/Kozea/CairoSVG/)
* [HTML-String-Tools](https://github.com/Drakovek/HTML-String-Tools)
* [Pillow](https://github.com/python-pillow/Pillow)

# Command Line Script

You can generate a random cover with:

    cover-generator -t "Title Text" -a "Author(s)"

You can specify the filename and image format with the `--output` tag, and set the width in pixels with the `--width` tag:

    cover-generator -t "JPEG Cover" -a Writer -o coverimage.jpg -w 900

You can also specify a specific cover style and/or color palette using the `--style` and `--palette` tags:

    cover-generator -t Title -a Author -s border -p ColorfulContrast

Available cover styles and color palettes are listed alongside options when using the `--help` command

# Basic Python Usage

    import cover_generator
    
    # Create a random cover image
    cover_generator.generate_cover(title="Title", author="author", path="/path/to/file.jpg")
    
    # Create a random cover image with a specific cover style and color palette
    cover_generator.generate_cover(title="Title", author="author", path="/path/to/file.jpg",
            cover_style="cross" palette_category="ColorfulContrast")
