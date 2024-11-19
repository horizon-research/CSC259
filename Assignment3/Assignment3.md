# Programming Assignment 3
## Due: December 4th, 11:30 AM

## Introduction
This programming assignment asks you to implement perspective projection, a key stage in the rasterization pipeline.
You can implement this using a transformation matrix, or you can implement this using similar triangles. 
The two implementations are equivalent, and we talked about both in class.

## Files
The relevant C++ files can be found in this directory. There are three files:
1. `main.cpp`: **This is the file you should modify!** Only insert code in the two code sites, marked by `TODO` comments (lines 49-53 and lines 75-77). Understanding the entirety of the code base is important. Read the entire program before starting for least frustration.
2. `geometry.h`: Relevant data structures are defined here. Feel free to read through it, but for this assignment, the most important data structure defined in that file is `Vec3f`, which stores a point.
3. `vertexdata.h`: Defines all points that need to be projected.

## Tips
You might notice that in `vertexdata.h`, only vertices are defined.
The points are not yet connected to form triangles.
In this assignment you are required only to project points without having to consider depth (i.e., occlusion).
For that reason, in `main.cpp` we do not define the near clipping plane and the far clipping plane, which are used to perform depth-based culling of points outside the frustum.

You are not expected to implement the perspective projection using a transformation matrix. If you choose to use a transformation matrix, try doing the following steps:
1. Define a near clipping plane and far clipping plane
2. Construct the transformation matrix

If you plan to use similar triangles to individually calculate the coordinates of a projected point without a transformation matrix, you shouldn’t have to add more than 10 lines of code!
As a hint, you will have to go through two steps:
1. Calculate the focal length from the `angleOfView`
2. Perspective project using the focal length and similar triangles

We also provide a sample image `out.ppm`, which is how the output should look like.
If your output is upside down, think about why!

## What to submit
Zip the `.cpp` and `.h` files in the directory, and submit the resulting file to blackboard.
I will compile it on a `cycle*.csug.rocheter.edu` machine with the following command:

```
g++ main.cpp -std=c++11
```

It's best practice to confirm that your code will compile as expected on the csug machines before submitting the assignment!

## Grading
If you code doesn't compile you get 0!
**Please double-check that your code compiles on the csug machines before submission!**
If you get the correct output you get full credit.
If you get the upside down image, you get 80%.
If you are not able to generate either, I will look at the code and assign the grade appropriately.

**Please double-check that your code compiles on the csug machines before submission!**

## Acknowledgement
The start kit is derived from code on [scratchapixel](https://www.scratchapixel.com/index.html).