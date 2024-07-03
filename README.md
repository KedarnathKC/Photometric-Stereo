# Photometric-Stereo

Python code for performing Photometric Stereo on the given images using shape from shading algorithm.

Data folder contains images of four subjects each having 64 images taken from different angles with the same light source.

Output folder contains the albedo image, estimated surface normals and recovered surface of the four subjects.

Here is a sample input and output images.

![Input](data/photometricStereo/yaleB01/yaleB01_P00_Ambient.pgm)
![Albedo](output/PhotometricStereo/AlbedoYaleB01.png)
![Surface_Normal](output/PhotometricStereo/EstimatedSurfaceYaleB01.png)
![Integrated_Height_Map](output/PhotometricStereo/SurfaceNormalsYaleB01.png)