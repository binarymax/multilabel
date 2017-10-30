import numpy as np

class MultiLabel:
	def __init__(self):
		self.labels = {}
		self.lookup = []
		self.idx = 0

	def __len__(self):
		return self.idx

	def add(self,key):
		if key not in self.labels.keys():
			self.labels[key]=self.idx
			self.lookup.append(key)
			self.idx+=1
			self.categorical = np.zeros([self.idx,self.idx])
			for i in range(self.idx):
				self.categorical[i,i] = 1.

	def combine(self,labels):
		combined = np.zeros(self.idx)
		if self.idx>0:
			for label in labels:
				i = self.labels[label]
				combined = combined + self.categorical[i]
		return combined
