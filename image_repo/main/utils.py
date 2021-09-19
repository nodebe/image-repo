import os
import secrets
from PIL import Image
from image_repo import app

def save_picture(form_picture):
	picture_fn = []
	for i in form_picture:
		random_hex = secrets.token_hex(8)
		_, f_ext = os.path.splitext(i.filename)
		pic_name = random_hex + f_ext
		picture_fn.append(pic_name)
		picture_path_normal = os.path.join(app.root_path, "static/images", pic_name)

		j = Image.open(i)
		j.save(picture_path_normal)

	return picture_fn