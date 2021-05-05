# Advance Computer Graphics

# Environment set up
- Ubuntu 18.04 or later
- Install OpenGL (for C):

            sudo apt-get install mesa-common-dev libgl1-mesa-dev libglu1-mesa-dev freeglut3-dev
            
- Install PyOpenGL (for Python):

            # install python3
            sudo apt-get -y install python3-pip
            
            # install PyOpenGL and some support libraries
            sudo apt-get update
            pip3 install pyopengl
            pip3 install pyopengl_accelerate
            pip3 install numpy
            pip3 install pygame
            pip3 install Pillow # Python imaging library using for loading texture for texturing
            pip3 install glfw # for creating and managing windows and OpenGL contexts
            pip3 install pyrr # 3D mathematical function using Numpy

# Running
- C

            cd src/C
            mkdir output
            gcc -o output/square square.c -lGL -lGLU -lglut # compile
            ./output/square # running

- Python:

            cd src/Python/project
            python run.py # running