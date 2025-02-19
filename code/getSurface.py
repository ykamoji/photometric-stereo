import numpy as np


def get_height_map(height, p, q, width, row=True):

    temp = np.zeros((height, width))
    if row:
        temp[0, 1:] = np.cumsum(p[0, 1:])
        temp[1:, :] = q[1:, :]
        heightMap = np.cumsum(temp, axis=0)
    else:
        temp[1:, 0] = np.cumsum(q[1:, 0])
        temp[:, 1:] = p[:, 1:]
        heightMap = np.cumsum(temp, axis=1)

    return heightMap

def getSurface(surfaceNormals, method, image_size):

        height = image_size[0]
        width = image_size[1]

        N1 = surfaceNormals[:, :, 0]
        N2 = surfaceNormals[:, :, 1]
        N3 = surfaceNormals[:, :, 2]

        p = N1 / N3
        q = N2 / N3

        if method == 'column-row':
            heightMap = get_height_map(height, p, q, width, row=False)

        elif method == 'row-column':
            heightMap = get_height_map(height, p, q, width, row=True)

        elif method == 'average':
            heightMap = (get_height_map(height, p, q, width, row=False) + get_height_map(height, p, q, width, row=True)) / 2.0

        elif method == 'random':
            n = 30
            heightMap = np.zeros((height, width))

            for row in range(height):
                for col in range(width):
                    if row == 0 and col == 0:
                        heightMap[row, col] = 0
                    else:
                        for i in range(n):
                            csum = 0
                            path = 0
                            w = 0
                            h = 0
                            randomWalk = np.random.randint(0, 2, size=row + col)
                            while w < col or h < row:

                                if w >= col:
                                    randomWalk[path] = 1
                                if h >= row:
                                    randomWalk[path] = 0

                                if randomWalk[path] == 0:
                                    csum += p[h, w]
                                    w = w + 1
                                else:
                                    csum += q[h, w]
                                    h = h + 1
                                path = path + 1

                            heightMap[row, col] = csum + heightMap[row, col]

                        heightMap[row, col] = heightMap[row, col] / n

        return heightMap

