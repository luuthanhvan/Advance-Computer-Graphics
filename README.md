# Advance Computer Graphics

# Environment set up
- Ubuntu 18.04 or later
- Install OpenGL (for C++):

            sudo apt-get install mesa-common-dev libgl1-mesa-dev libglu1-mesa-dev freeglut3-dev
            
- Install PyOpenGL (for Python):

            # install python3
            sudo apt-get -y install python3-pip
            
            # install PyOpenGL
            sudo apt-get update
            pip3 install pyopengl
            pip3 install pyopengl_accelerate
            pip3 install numpy

# Running
- C++

            cd src/C++
            mkdir output
            gcc -o output/first_opengl_program first_opengl_program.c -lGL -lGLU -lglut # compile
            ./output/first_opengl_program # running

- Python:

            cd src/Python
            python3 Square.py # running