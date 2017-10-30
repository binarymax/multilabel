# MultiLabel
Multi-hot label encoding for NumPy

Add labels to set, and combine them to form multihot encoded numpy arrays.

## Usage

```python
import numpy as np
import multilabel as ml

labels = ml.MultiLabel()
labels.add("news")
labels.add("tech")
labels.add("law")
labels.add("culture")
labels.add("politics")
labels.add("linux")
labels.add("python")

print(labels.combine(["news","python"]))
#> [ 1.  0.  0.  0.  0.  0.  1.]
```