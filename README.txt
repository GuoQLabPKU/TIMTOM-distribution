1. Scripts description
    anglesTIMToTOM.py: generate relative Euler angles of TIM relative to TOM
    rotate001vect.m: rotate the vector [0,0,1] according to the relative Euler angles of TIM relative to TOM 
    showLandscape.py: show the lanscape of TIM relative to TOM
2. System requirements
    dependencies:NEMO-TOC[1] and  TOM toolbox [2]
    operating systems: Any platform (linux/windows/macos) was tested
3. Demo and Instructions for use
    First, download all the required scripts and data, then run the `anglesTIMToTOM.py` script. This will generate the relative Euler angles of TIM with respect to TOM, saved as `allResAngleRELION.csv`.  
    Next, execute the `rotated001vect.m` script. This will produce the coordinates of the vector `[0, 0, 1]` after being rotated by the relative Euler angles, and save the results in `rot001vector_coord.txt`.  
    Finally, use the `showLandscape.py` script to visualize the landscape of TIM relative to TOM. The generated scatter plot will be saved as `scatter.png`.  

   
Jiang, W., Wagner, J., Du, W., Plitzko, J., Baumeister, W., Beck, F., and Guo, Q. (2022). A transformation clustering algorithm and its application in polyribosomes structural profiling. Nucleic Acids Res 50, 9001-9011.
Nickell,S., Forster,F., Linaroudis,A., Net,W.D., Beck,F., Hegerl,R., Baumeister,W. and Plitzko,J.M. (2005) TOM software toolbox: acquisition and analysis for electron tomography. J. Struct. Biol., 149, 227–234.


    
    