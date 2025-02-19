import numpy as np

def photometricStereo(imarray, lightdirs):

    height, width, imageCount = imarray.shape
    total_pixel = height * width
    I = np.zeros((imageCount, total_pixel))

    for i in range(imageCount):
        I[i, :] = imarray[:, :, i].reshape(1, total_pixel)

    g = np.linalg.lstsq(lightdirs, I, rcond=None)[0]

    albedo = np.zeros(total_pixel)
    normal = np.zeros((3, total_pixel))

    for i in range(total_pixel):
        albedo[i] = np.linalg.norm(g[:, i])
        normal[:, i] = g[:, i] / albedo[i]

    albedoImage = albedo.reshape(height, width)
    surfaceNormals = np.stack((normal[0, :].reshape(height, width),
                                normal[1, :].reshape(height, width),
                                normal[2, :].reshape(height, width)), axis=2)

    return albedoImage, surfaceNormals
