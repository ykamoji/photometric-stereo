![Question](https://github.com/ykamoji/photometric-stereo/blob/main/img_refs/question.png?raw=true)

<div style="text-align: center;">YaleB01</div>

![one](https://github.com/ykamoji/photometric-stereo/blob/main/img_refs/YaleB01-col-row.png?raw=true)

<hr>

<div style="text-align: center;">YaleB02</div>

![two](https://github.com/ykamoji/photometric-stereo/blob/main/img_refs/YaleB02-col-row.png?raw=true)

<hr>

<div style="text-align: center;">YaleB05</div>

![two](https://github.com/ykamoji/photometric-stereo/blob/main/img_refs/YaleB05-random.png?raw=true)

<hr>

<div style="text-align: center;">YaleB07</div>

![two](https://github.com/ykamoji/photometric-stereo/blob/main/img_refs/YaleB07-random.png?raw=true)

### Methods
#### Column-Row
We are first integrating (adding since these are discrete values) the columns and then rows. Here, we emphasis
more on the partial derivative of Z with respect to X which is p. From the recovered surface, we can observe that
the shape of mouth, eyes and nose seems to have the correct (or real) shape.

<hr>

#### Row-Column
Here we are first integrating the rows first and then columns. Here, we emphasis more on the partial derivative of
Z with respect to Y which is q. We get a pointy nose & mouth. Because we integrate from up to down, we added
more height to the nose, causing the shape of the nose to be stretched. Similarly, the mouth have the nose height
integrated from the top which is causing distorting the shape.

<hr>

#### Average

In this method, we are just taking the average of the previous two integration methods and averaging it. We can
observe that taking the average has given better surface height for nose. However, the mouth is still distorted since
the bottom of the surface has the largest height from the top bottom integration.

<hr>

#### Random

In this approach, an integration path is chosen randomly and then we average of these multiple paths. Since we
are taking random paths, we are giving equal weights to both p & q. This gives a more robust representation of
the surface height. However, due to the computation limits of the random paths, the best height representation
is difficult for this subject. There is a saturation of height representation after 30 random paths. To improve the
quality of the surface, we will have to employ more complex algorithms to use better randomization since the the
image quality is not increasing linearly with number of random paths.