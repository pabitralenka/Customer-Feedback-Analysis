import pandas as pd 
import numpy as np
import csv
def read_data(arg1, arg2):
	data_train1 = pd.read_csv(arg1, sep = '\t')
	data_train2 = pd.read_csv(arg2)

	nf = open("sample_development.txt",'a+')
	#tot = "id" + "\t" + "review" + "\t" + "label" + "\n"
	for x in range(data_train1.consumer_complaint_narrative.shape[0]):
		text1 = data_train1.consumer_complaint_narrative[x]
		id1 = data_train1.id[x]
		tag = data_train2.tags[x]

		if tag == 0:
			lab = "bug"
		elif tag == 1:
			lab = "comment"
		elif tag == 2:
			lab = "complaint"
		elif tag == 3:
			lab = "meaningless"
		elif tag == 4:
			lab = "request"
		elif tag == 5:
			lab = "undetermined"
		tot = str(id1) + "\t" + str(text1) + "\t" + str(lab) + "\n"
		nf.write(tot)

	nf.close()


read_data("test.tsv", "tags.txt") 


