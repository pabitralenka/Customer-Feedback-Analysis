import pandas as pd 
import numpy as np
import csv
def read_data(arg1,arg2):
	data_train1 = pd.read_csv(arg1, sep = '\t')
	data_train2 = pd.read_csv(arg2, sep = '\t') 
	#data_train2 = pd.read_csv(arg2)

	nf = open("sample_development.txt",'a+')
	#tot = "tags" + "\n"
	#nf.write(tot)
	#tot = "id" + "\t" + "review" + "\t" + "label" + "\n"
	for x in range(data_train1.Descript.shape[0]):
		text1 = data_train1.Descript[x]
		id1 = data_train1.id[x]
		tag = data_train2.Predicted[x]
		#for y in range(data_train2.tweets.shape[0]):
			#if text1 == data_train2.tweets[y]:
				#tag = data_train2.y_predicted[y]

		tot = str(id1) + "\t" + str(text1) + "\t" + str(tag) + "\n"
		#tot = str(tag) + "\n"
		nf.write(tot)

	nf.close()


read_data("test.tsv","predictions_all.tsv") 


