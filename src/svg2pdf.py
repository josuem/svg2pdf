
import subprocess

class Svg2pdf:
    def __init__(self, **kwargs):
        self.folder = kwargs["folder"]
        self.input_svg_file = kwargs["input_svg_file"]
        self.pages = kwargs["pages"]
        
        self.suffix = kwargs.get("suffix")
        
    def run(self):
      for i, page in enumerate(self.pages):
        print("Page: ", page)

        if self.suffix is not None:
          tmp = f"{self.folder}{self.input_svg_file}_{self.suffix[i] }"
        else:
          tmp = f"{self.folder}{self.input_svg_file}_page{page:02d}"

        comando = f'inkscape --export-page={page} --actions="export-filename:{tmp}.pdf; export-do" {self.folder}{self.input_svg_file}.svg'

        # Ejecuta el comando utilizando subprocess
        print("Ejecutando: ", comando)
        print(comando)
        proceso = subprocess.Popen(comando, shell=True)

        # Espera a que el proceso termine
        proceso.wait()

      print("Done")

