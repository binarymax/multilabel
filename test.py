import numpy as np
import multilabel as ml

errors = []
def err(str):
	errors.append(str)

labels = ml.MultiLabel()

assert (len(labels.combine("foo"))==0), "Combination with empty label set violation"

labels.add("news")
labels.add("tech")
labels.add("law")
labels.add("culture")
labels.add("politics")
labels.add("linux")
labels.add("python")
assert (len(labels)==7), err("Length is incorrect")

labels.add("python")
assert (len(labels)==7), err("Length is incorrect after redundant label")

combine_test1 = np.array([1.,0.,0.,1.,0.,0.,0.])
combine_test2 = labels.combine(["news","culture"])
assert (np.all(np.equal(combine_test1,combine_test2))), err("Combination is correct")

if(len(errors)==0):
	print("All tests passed")