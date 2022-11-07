# based on playlist:
# https://www.youtube.com/playlist?list=PLYokS5qr7lSsvgemrTwMSrQsdk4BRqJU6

# notes based on:
# https://www.youtube.com/watch?v=WficzyoTSsg&ab_channel=DylanFalconer

touch .gitignore


# not sure if it is correct
# https://github.com/libsdl-org/SDL/releases/tag/release-2.24.1
curl -LO https://github.com/libsdl-org/SDL/releases/download/release-2.24.1/SDL2-2.24.1.tar.gz
tar -xf SDL2-2.24.1.tar.gz 

# not sure if it is correct
# https://www.libsdl.org/projects/mixer/
curl -LO https://www.libsdl.org/projects/mixer/release/SDL_mixer-1.2.7.tar.gz
tar -xf SDL_mixer-1.2.7.tar.gz

# FreeType2
# not sure if it is correct
# https://download.savannah.gnu.org/releases/freetype/?C=M&O=D
curl -LO https://download.savannah.gnu.org/releases/freetype/freetype-2.12.0.tar.xz
tar -xf freetype-2.12.0.tar.xz

# glad.dav1d.de
# https://glad.dav1d.de/#language=c&specification=gl&api=gl%3D3.3&api=gles1%3Dnone&api=gles2%3Dnone&api=glsc2%3Dnone&profile=compatibility&loader=on
curl -LO https://glad.dav1d.de/generated/tmpg3gznl4zglad/glad.zip
mkdir glad
unzip glad.zip -d ./glad

# =========================
mkdir engine-from-scratch
mkdir include/SDL2

cp -r  SDL2-2.24.1/include/* include/SDL2/
# rm -rf include/SDL2/include

# stopped at:
# https://youtu.be/WficzyoTSsg?t=151