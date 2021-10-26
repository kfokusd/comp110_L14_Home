import matplotlib.pyplot
import Lecture14 as L14

(depths, mags) = L14.get_data("eqs.csv")
r_dm = L14.pearson_r(depths, mags)
matplotlib.pyplot.title("Magnitude vs. Depth ({})".format(r_dm))
matplotlib.pyplot.scatter(depths, mags)
matplotlib.pyplot.xlabel("Depth (km)")
matplotlib.pyplot.ylabel("Magnitude")
matplotlib.pyplot.show()