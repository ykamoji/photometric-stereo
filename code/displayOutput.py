import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize
from mpl_toolkits.mplot3d import Axes3D

def displayOutput(albedo, height, method='', path='/'):
    hgt, wid = height.shape
    X,Y = np.meshgrid(np.arange(wid), np.arange(hgt))
    H = np.flipud(np.fliplr(height))
    A = np.flipud(np.fliplr(albedo))

    min = 0.0
    max = 1.0

    scalarMap = cm.ScalarMappable(norm=Normalize(vmin=min, vmax=max), cmap='gray')
    A_colored = scalarMap.to_rgba(A)

    plt.imshow(albedo, cmap='gray')
    plt.savefig('../output/photometricStereo/'+path+'/albedo')
    plt.show()

    views = [ (30,5), (-30,5), (-50, 30), (50, 30)]

    for view in views:

        plt.figure()
        ax = plt.axes(projection='3d')
        _ = ax.plot_surface(H, X, Y, facecolors=A_colored, linewidth=0.4, rstride=1, cstride=1, shade=False)
        ax.grid(False)
        ax.azim = view[0]
        ax.elev = view[1]

        # ax.dist = 10

        plt.title('Estimated surface')
        plt.savefig('../output/photometricStereo/' + path + f'/recovered_surface_{method}_{view}')
        plt.show(block=False)


if __name__ == '__main__':
    displayOutput(np.zeros((50, 50)), np.zeros((50, 50)))
