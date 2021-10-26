import math

# get_data()
#  Parameter(s): 
#    filename: csv filename (string) 
#  Return:
#    Tuple with 2 items as List.  1st list is the list of depths(3rd index position of the csv), and 
#    2nd list is the corresponding magnitude (4th index position of the csv)
####################
# TO DO
####################
# End of get_data()


# mean()
def mean(x_vals):
    total = 0
    for i in range(len(x_vals)):
        total = total + x_vals[i]
    return total / len(x_vals)
# End of mean()

# pearson_r()
def pearson_r(x_vals, y_vals):
    x_mean = mean(x_vals)
    y_mean = mean(y_vals)
    numerator = 0
    x_diffs = 0
    y_diffs = 0
    for i in range(len(x_vals)):
        xd = (x_vals[i] - x_mean)
        yd = (y_vals[i] - y_mean)
        numerator = numerator + (xd*yd)
        x_diffs = x_diffs + xd**2
        y_diffs = y_diffs + yd**2

    denom = math.sqrt(x_diffs) * math.sqrt(y_diffs)
    return numerator/denom
# End of pearson_r()