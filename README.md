# NewtonFractalizer

A visualization and interactive app for exploring Newton’s Method fractals on the complex plane. This repository contains:

- **Python/Manim animations** showing the iterative convergence of Newton’s Method (inspired by 3Blue1Brown’s video).  
- **MATLAB App Designer** code for an interactive GUI that generates and explores Newton’s fractals.
- **MATLAB Fractal Generator** functions that compute and render Newton fractals, with support for generating static plots and animated GIFs.

---

## 🌀 What is Newton’s Fractal?

**Newton’s Fractal** is a beautiful and intricate visualization of how **Newton’s Method** behaves in the complex plane. Originally a numerical method for finding roots of equations, when extended to complex numbers and applied across a grid of starting points, it reveals mesmerizing fractal patterns.

Each point on the complex plane is colored based on which **root** the method converges to — and how fast. The result is a vibrant, often kaleidoscopic image where the **boundaries between convergence regions form fractals**.

> A single equation. Infinite beauty. The fractal showcases the sensitive dependence on initial conditions in Newton’s method — and how chaos and order intertwine.

To know more about it watch the following video: https://www.youtube.com/watch?v=-RdOwhmqP5s

Or read the following blog: https://blogs.mathworks.com/community/2023/12/05/newtons_method_fractals/?s_tid=srchtitle_site_search_1_newton+fractal

---

## 🎞️ Animations & Presentation Material

![ComplexPart](https://github.com/user-attachments/assets/97ac78da-c4b9-4454-967c-3d07bfb5a558)

The **Python animations** created using `animations.py` are designed as visual demonstrations for presentations and explanations of Newton’s Fractal behavior. These animations visually represent how points converge to different roots, how regions form, and how the fractal emerges over multiple iterations.

📺 You can view all animations in this [YouTube playlist](https://www.youtube.com/playlist?list=PLnVrRSoVk9qb1KdLNrmkVHYE_NczF53GQ).

### ⚙️ Manim

**Manim** is a powerful Python library used to create mathematical animations (originally created by 3Blue1Brown).

### 📦 Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Manim:

```bash
pip install manim
```

### 🚀 Usage

```python
from manim import *
```

Each class in the file (like `animations.py`) represents a different **scene**.

To render a scene and have it saved, run the following command in your terminal:

```bash
manim -pql [FILE_NAME] [CLASS_NAME]
```

This generates a folder called `media/` in the working directory that contains the rendered animations.

You can also specify quality using:

```bash
-q, --quality [l|m|h|p|k]
```

Which corresponds to:

- **l**: 854x480 (15 FPS)
- **m**: 1280x720 (30 FPS)
- **h**: 1920x1080 (60 FPS)
- **p**: 2560x1440 (60 FPS)
- **k**: 3840x2160 (60 FPS)

📚 For more info and configuration options, check the [official Manim documentation](https://docs.manim.community/en/stable/guides/configuration.html).

---

## 🖥️ MATLAB App Designer GUI

![appImage](https://github.com/user-attachments/assets/def1049a-d370-42e6-b09f-9e5001d14654)

The `NewtonsFractalAPP/` folder contains a MATLAB App Designer class (`app1.m`) plus supporting functions:

- **app1.m**: Defines the UI components and callbacks for:
  - Choosing the function _f(x)_.
  - Setting resolution , iteration count, and rotation factor.
  - Selecting display type: image or contour.
- **NewtonsFractalAD.m**: Implements Newton’s Method on a complex grid and finds the closest root.
- **FindClosestRoot.m**: Helper to assign each grid point to its nearest root.

### Running the App

1. Open MATLAB (R2021a or later).  
2. In the **Current Folder**, navigate to `matlab_app/`.  
3. Run:
   ```matlab
   app = app1;
   ```
4. Enter your function (e.g. `x^3 - 1`), set parameters, and click **Generate**.

Most common functions are located in `GeneratorFunctions/Tester.m`, copy paste them into the app.

---

## 🧮 MATLAB Generator Functions 

![Power3Creation](https://github.com/user-attachments/assets/33008830-08cd-4f96-868a-cf6a8bcd0ede)

![Power3Rotation](https://github.com/user-attachments/assets/8553013e-eba4-4c3b-9db9-8d6d38d82a14)

The folder `GeneratorFunctions/` contains the core MATLAB functions responsible for generating Newton’s Fractals and exporting them as static images or animated GIFs. These scripts handle everything from calculating convergence to coloring and exporting visuals.

---

#### 📌 Functions Overview

- **`FindClosestRoot.m`**  
  Determines which root each complex point in the grid converges to after applying Newton’s Method. Used for coloring the fractal.

- **`NewtonsFractal.m`**  
  Main script to generate a Newton fractal. Takes a symbolic function, resolution, number of iterations, and graph type (`"image"` or `"contour"`) as inputs.

- **`NewtonsFractalCreateGif.m`**  
  Generates an animated GIF showing the evolution of the Newton fractal as the number of iterations increases from 1 to _n_.

- **`NewtonsFractalRotationGif.m`**  
  Produces an animated GIF where the **rotation factor** is incremented from 1 to 47, revealing how this parameter affects convergence behavior and visual symmetry.


These functions are especially useful for:
- Experimenting with different polynomials.
- Creating high-resolution exports for presentations.
- Understanding the dynamics of Newton’s Method in the complex plane.

All output images and GIFs are exported using MATLAB’s `exportgraphics()` function with customized resolution and black background for clean visuals.

---

## 🙏 Credits & References

- **3Blue1Brown** – “Newton’s Method Fractals” video: https://www.youtube.com/watch?v=-RdOwhmqP5s  
- MATLAB blogs and community entries on Newton fractals:  
  - https://blogs.mathworks.com/cleve/2016/01/18/fractal-global-behavior-of-newtons-method/ 
  - https://www.mathworks.com/matlabcentral/communitycontests/contests/6/entries/15472
  - https://www.mathworks.com/matlabcentral/communitycontests/contests/6/entries/15467
  - https://www.mathworks.com/matlabcentral/communitycontests/contests/6/entries/13840
  - https://blogs.mathworks.com/community/2023/12/05/newtons_method_fractals/?s_tid=srchtitle_site_search_1_newton%20fractal

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
