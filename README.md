Quickly created a way to generate large amount of augmented features for research purposes needing large data. The code is not efficient, and
specifically functions for the purpose I developed it for.

Run program:
python main.py

Customisation:
Edit 'length' in main function to an integer less than or equal to 60. Length represents
the dimensions of a square image. The number of augmented features created the square of set length.

If you want to generate more features or different types of features, add to trans_functions.py.
This will also increase the limit of 'length' as it's dependant on number of available transformations.