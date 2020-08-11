#you may need to run "pip3 install pdf2jpg"
#you also need to have java installed

from pdf2jpg import pdf2jpg
inputfile = r"<path to your pdf>"
outputpath = r"<path to your output dir>"

result = pdf2jpg.convert_pdf2jpg(inputpath, outputpath, dpi=300, pages="ALL"

#Look in the output folder and you should have a JPG!
