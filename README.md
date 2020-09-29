# Photometry-Toolkit

### Python library requirements:
  1. pyfits
	2. scipy
	3. datetime
	4. mpl_toolkits
	5. matplotlib
	6. numpy

### TO OBTAIN CLEAN SCIENCE FRAMES (MANDATORY)

Follow the steps sequentially as mentioned:

1. Extract the data files from data.tar.gz

2. Go to Bias directory from the terminal and list all the bias files using the command "ls bias* > bias.in". Edit the "bias.in" file to remove all the "*"(asterisks) after the names, if present. There should only be the names of the files in each line.

3. From folder "codes" copy "mbias.py" and "statistics.py" and paste in the "Bias" folder.

4. Execute "mbias.py" (A file named "mbias.fits" will be generated.)

5. Copy the mbias.fits file and paste it in the folder "Flat".

6. Go to Flat directory from the terminal and list all the flat files using the command "ls flat* > flat.in". Edit the "flat.in" file to remove all the "*"(asterisks) after the names, if present. There should only be the names of the files in each line.

7. From folder "codes" copy "nmflat.py" and "statistics.py" and paste in the "Flat" folder.

8. Execute "nmflat.py" (A file named "nmflat.fits" will be generated.)

9. Copy the generated files: "mbias.fits" and "nmflat.fits" in the folder "Obj".

10. From folder "codes" copy "clean.py" and paste in the "Obj" folder.

11. Go to the Obj directory from the terminal and list all the science files using the command "ls J* > sci.in ". Edit the "sci.in" file to remove all the "*"(asterisks) after the names, if present. There should only be the names of the files in each line.

12. Create an empty folder named "Clean" within "Obj".

13. Execute "clean.py" 

14. From folder "codes" copy "crop.py" and "crop_data.py" and paste in the folder "Clean".

15. Go to the Clean directory from the terminal and list all the clean frames using the command "ls J* > clean.in ".

16. Create an empty folder named "Crop" within "Clean".

17. Execute "crop.py" 

18. From folder "codes" copy statistics.py , Analysis.py , gaussfit.py , sky.py , photometry.py , 3dplot_target_object.py , 3d_profiles.py , header_update.py ,
    light_curve.py , plot_light_curve.py , coordinate.dat and paste them in the folder "Crop".

19. Go to the "Crop" directory from the terminal and list all the cropped files using the command "ls J* > crop.in".

20. Open the file "header_update.py" in a text editor and mention the complete path of "sci.in" file and "Obj" directory in the prompted area.

21. Execute "header_update.py"

### STEPS TO OBTAIN THE LIGHT CURVE

1. After completion of the above mandatory procedure, go to the "Crop" directory.

2. Execute light_curve.py ( A .txt file will be generated.)

3. Execute plot_light_curve.py ( Light curve of our target objects will be plotted. )

### TO GET 3D PLOTS OF OUR TARGET OBJECTS FROM THE FRAME

1. After completion of the above mandatory procedure, go to the "Crop" directory.

2. Execute 3dplot_target_objects.py


