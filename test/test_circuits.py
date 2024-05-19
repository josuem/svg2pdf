from svg2pdf import Svg2pdf 

folder = "./"
input_svg_file = "test_inkscape"
pages  = [1, 2, 3, 4]
suffix = ["circuito", "corrientes", "malla_01", "malla_02"]
          
image_inkscape = Svg2pdf(folder=folder, 
                        pages=pages, 
                        input_svg_file=input_svg_file,
                        suffix=suffix)
image_inkscape.run()