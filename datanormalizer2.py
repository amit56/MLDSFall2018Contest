import tensorflow as tf
print(tf.__version__)
import numpy as np
#from ApplicationEntry import ApplicationEntry
#from TensorflowApplicationEntry import TensorflowApplicationEntry
import traceback
import os, shutil
import csv
import sys
csv.field_size_limit(sys.maxsize)
class DataNormalizer2():
	def __init__(self, csvFileName):
		self.csvFileName = csvFileName;

	def cleanTestData(self, labelCol, meanArray, standardDeviationArray, csvFileName = None, outputFileName = None):
		features = list()
		if csvFileName is None:
			csvFileName = self.csvFileName
		else:
			self.csvFileName = csvFileName

		origTestFeaturesHeader = ""
		with open(csvFileName) as csvfile:
			reader = csv.reader(csvfile)
			first = True
			for row in reader:
				if(first):
					first = False
					origTestFeaturesHeader = ",".join(row[0:len(row)-1])
					continue
				if len(row) <= 1:
					continue
				#features.append(row[0:labelCol-1])
				#features.append(row[0:labelCol-1])

				features.append(row[1:labelCol-1])

		'''newFeatures = list()

		for feature in features:
			feature = [float(numeric_string) for numeric_string in feature]
			newFeatures.append(feature)

		features = newFeatures


		print (len(features[0]))


		print ("length of testFeatures: " + str(len(features)))

		columns = list()

		for i in range(len(features[0])):
			col = list()
			for j in range(len(features)):
				feature = features[j][i]
				col.append(feature)
			columns.append(col)


		meanArray = [0] * len(columns)
		standardDeviationArray = [0] * len(columns);
		minArray = [0] * len(columns)
		maxArray = [0] * len(columns)
		for i in range(len(columns)):
			col = columns[i]
			#print (col)
			meanArray[i] = np.mean(col);
			standardDeviationArray[i] = np.std(col)
			minArray[i] = min(col)
			maxArray[i] = max(col)
			#print (meanArray[i])
			#print (standardDeviationArray[i])
			#print ("\n\n\n\n")

		#print ("len(features[0]): " + str(len(features[0])))
		#print ("len(columns): " + str(len(columns)))
		#print (meanArray)
		#print ("-----")
		#print (standardDeviationArray)
		'''
		for feature in features:
			for i in range(len(feature)):
				#feature[i] = float(feature[i] - minArray[i])/float(maxArray[i] - minArray[i])
				if(standardDeviationArray[i] == 0):
					feature[i] = meanArray[i]
				else:
					x = float(feature[i])
					mu = float(meanArray[i])
					sigma = float(standardDeviationArray[i])

					feature[i] = (x - mu)/sigma
					#print ("feature[i]: " + str(feature[i]))

				#feature[i] *= 2
				#feature[i] -= 1


		features = np.asarray(features)
		print ("--------------------Features retrieved-----------------------")
		#print(features)
		print ("--------------------Features Printed-----------------------")

		f = open(outputFileName, 'w')
		f.write(origTestFeaturesHeader + ",text\n")
		for i in range(len(features)):
			print (i)
			f.write(str(i) + ",")
			for j in range(0, len(features[i])):
				f.write(str(features[i][j]) + ",")
			f.write("fakeText")
			f.write("\n")


	def cleanData(self, labelCol, csvFileName = None, outputFileName = None):
		labels = list()
		features = list()
		if csvFileName is None:
			csvFileName = self.csvFileName
		else:
			self.csvFileName = csvFileName

		origTrainFeaturesHeader = ""
		with open(csvFileName) as csvfile:
			reader = csv.reader(csvfile)
			first = True
			for row in reader:
				if(first):
					first = False
					origTrainFeaturesHeader = ",".join(row[0:len(row)-2])
					continue
				if len(row) <= 1:
					continue
				#features.append(row[0:labelCol-1])
				#features.append(row[0:labelCol-1])

				newFeature = row[1:labelCol-1]
				features.append(newFeature)

				if(row[labelCol] == "prose"):
					labels.append([0])
				else:
					labels.append([1])

		newFeatures = list()
		for feature in features:
			feature = [float(numeric_string) for numeric_string in feature]
			newFeatures.append(feature)

		features = newFeatures
		print ("length of features: " + str(len(features)))

		columns = list()

		for i in range(len(features[0])):
			col = list()
			for j in range(len(features)):
				feature = features[j][i]
				col.append(feature)
			columns.append(col)


		meanArray = [0] * len(columns)
		standardDeviationArray = [0] * len(columns);
		for i in range(len(columns)):
			col = columns[i]
			#print (col)
			meanArray[i] = np.mean(col);
			standardDeviationArray[i] = np.std(col)
			#print (meanArray[i])
			#print (standardDeviationArray[i])
			#print ("\n\n\n\n")

		#print ("len(features[0]): " + str(len(features[0])))
		#print ("len(columns): " + str(len(columns)))
		#print (meanArray)
		#print ("-----")
		#print (standardDeviationArray)
		for feature in features:
			for i in range(len(feature)):
				if(standardDeviationArray[i] == 0):
					feature[i] = meanArray[i]
				else:
					feature[i] = float(feature[i] - meanArray[i])/float(standardDeviationArray[i])



		labels = np.asarray(labels)

		features = np.asarray(features)
		print ("--------------------Features retrieved-----------------------")
		print(features)
		print ("--------------------Features Printed-----------------------")

		f = open(outputFileName, 'w')
		f.write(origTrainFeaturesHeader + ",text,class\n")
		for i in range(len(features)):
			print (i)
			f.write(str(i) + ",")
			for j in range(0, len(features[i])):
				f.write(str(features[i][j]) + ",")
			f.write("fakeText,")
			if(labels[i][0] == 1):
				f.write("poetry")
			else:
				f.write("prose")
			f.write("\n")

		return meanArray, standardDeviationArray

'''dataCleaner = DataCleaner("training_dataset.csv");
dataCleaner.cleanData(labelCol = 28, outputFileName = "clean_training_dataset.csv")

dataCleaner = DataCleaner("test_dataset.csv");
dataCleaner.cleanTestData(labelCol = 28, outputFileName = "clean_test_dataset.csv")'''

dataCleaner = DataNormalizer2("denoised_normalized_extra_extra_training_dataset.csv");
meanArray, standardDeviationArray = dataCleaner.cleanData(labelCol = 2002, outputFileName = "normalized_denoised_normalized_extra_extra_training_dataset.csv")

dataCleaner = DataNormalizer2("denoised_normalized_extra_extra_test_dataset.csv");
dataCleaner.cleanTestData(labelCol = 2002, meanArray = meanArray, standardDeviationArray = standardDeviationArray, outputFileName = "normalized_denoised_normalized_extra_extra_test_dataset.csv")

#dataCleaner = DataCleaner("extra_test_dataset.csv");
#dataCleaner.cleanTestData(labelCol = 334, outputFileName = "clean_extra_test_dataset.csv")
