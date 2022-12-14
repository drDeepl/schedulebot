from pdf2image import convert_from_path, convert_from_bytes
import io
# import os
from PIL import Image


def convert_pdf_to_image():
    # poppler_path = "C:\\Users\\Math-Lab\\Desktop\\scheduleBot\\poppler\\Library\\bin"
    # print(os.getcwd())
    path = "./images/"
    image = convert_from_path(f"{path}schedule.pdf", fmt="png", output_file="prepare_schedule")
    buf = io.BytesIO()
    im_resize = image[0].resize((700, 1200))
    im_resize.save(buf, format="PNG")
    byte_image = buf.getvalue()
    return byte_image