# Scientific-Programming-in-Python-
## Intruduction
This is a data-anlysis project based on the Stellar Classification Dataset - SDSS17 https://www.kaggle.com/datasets/fedesoriano/stellar-classification-dataset-sdss17 with the aim to create a machine learning model that can predict classification to a high standard using a hold out test set.


The project will be split into three sections: 
1. **Representation**: data-analysis: using *matplotlib library, data-imputation: using KNN if needed.
2. **Optimisation**: Feature selection using the *filter* corellation and using the library *statsmodel*, Hyper-paramater tuning, using training and validation set.
4. **Evaluation**: final evaluation using the hold-out test set of the models unseen data. Other classification methods have been attenpted with high accuracy upto 98% using SVM and Random Forest. To make this project different i will attempt to use classes written from  https://github.com/python-engineer/MLfromscratch/tree/master/mlfromscratch to help with my understanding of the scructure of the algorithms. 

Representation and optimisation my overlap.

## Features
The data consists of 100,000 observations of space taken by the SDSS (Sloan Digital Sky Survey). Every observation is described by 17 feature columns and 1 class column which identifies it to be either a star, galaxy or quasar.

   1. obj_ID = Object Identifier, the unique value that identifies the object in the image catalog used by the CAS
   2. alpha = Right Ascension angle (at J2000 epoch)
   3. delta = Declination angle (at J2000 epoch)
   4. u = Ultraviolet filter in the photometric system
   5. g = Green filter in the photometric system
   6. r = Red filter in the photometric system
   7. i = Near Infrared filter in the photometric system
   8. z = Infrared filter in the photometric system
   9. run_ID = Run Number used to identify the specific scan
   10. rereun_ID = Rerun Number to specify how the image was processed
   11. cam_col = Camera column to identify the scanline within the run
   12. field_ID = Field number to identify each field
   13. spec_obj_ID = Unique ID used for optical spectroscopic objects (this means that 2 different observations with the same spec_obj_ID must share the output class)
   14. class = object class (galaxy, star or quasar object)
   15. redshift = redshift value based on the increase in wavelength
   16. plate = plate ID, identifies each plate in SDSS
   17. MJD = Modified Julian Date, used to indicate when a given piece of SDSS data was taken
   18. fiber_ID = fiber ID that identifies the fiber that pointed the light at the focal plane in each observation
