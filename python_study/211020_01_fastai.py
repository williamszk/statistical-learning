# https://www.fast.ai/
# https://course.fast.ai/
# https://github.com/fastai/fastbook
# https://github.com/fastai/fastbook/blob/master/01_intro.ipynb


import fastai.vision.all as fa

path = fa.untar_data(fa.URLs.PETS)/"images"

def is_cat(x):
    return x[0].isupper()


# https://github.com/fastai/fastbook/blob/master/01_intro.ipynb
# continue from this page
# fa.ImageDataLoaders.from_name_func(
#     path, fa.get_image_files?
# )



