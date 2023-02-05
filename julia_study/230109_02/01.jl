println("Hello World")


using Pkg
Pkg.add("GDAL")
Pkg.build("GDAL") 
Pkg.add("ArchGDAL") 
Pkg.add("ImageView")
Pkg.add("Images")
Pkg.add("Colors")
Pkg.add("GeoArrays")




