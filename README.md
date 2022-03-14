# TangentArt

A simple Python program which creates artistic pictures. It is originally inspired by this [Tweet](https://twitter.com/fermatslibrary/status/1466053485930160134?s=20&t=uLcnSNC4Nb_x4ZQJP1L_aA).

## Requirements

Tested on Python 3.9.7 (previous versions should work as fine). \
Additional libraries needed: [numpy](https://pypi.org/project/numpy/), [matplotlib](https://pypi.org/project/matplotlib/).

## How to use

Run the `.py` script using a terminal by specifying the following parameters: the desired boundaries of the independent variable; the desired function to plot **using the notation accepted by the numpy library**; the number of points where the function and the tangents are evaluated. \
**Each parameter must be enclosed by quotation marks**. As an example, to represent a sine and its tangents in the interval from -20 and +20 using 500 points, one must run: 
\
`python3 tangentart.py '-20' '20' 'np.sin(x)' '500'`. \
A figure will pop-up showing the generated picture. The chosen function is represented as a red soline line, whereas the tangents are shown as thin black lines.\
Note that: 1) the independent variable is always called `x`; 2) the function is defined using the rules set by the numpy library.

## Output examples
A few examples are embedded in the following. \
\
Example 1: `python3 tangentart.py '-20' '20' 'np.sin(x)' '500'`\
Picture of a sine plotted in the interval `-20 < x < +20` and evaluated in `500` points.
![Screenshot_20220314_202826](https://user-images.githubusercontent.com/99678674/158246733-01ef5ce6-828c-40eb-b714-6a5aa8e81b87.png)

Example 2: `python3 tangentart.py '-20' '20' 'x*np.sin(x)' '500'`\
Picture of the function `x*sin(x)` plotted in the interval `-20 < x < +20` and evaluated in `500` points.
![Screenshot_20220314_203129](https://user-images.githubusercontent.com/99678674/158247260-1ae2bbde-5b96-4790-9e47-80f9a7a33f08.png)

Example 3: `python3 tangentart.py '-20' '20' 'x*np.tan(x)' '500'`\
Picture of `tan(x)` plotted in the interval `-20 < x < +20` and evaluated in `500` points.
![Screenshot_20220314_203314](https://user-images.githubusercontent.com/99678674/158247459-388ef1f4-ee24-4d6e-9ea8-879ac0d8e9f4.png)
