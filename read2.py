import sys
import pandas as pd
import numpy as np
import random as rd
import time

start_time = time.time()
class Book:
	def __init__(self,  ind = 0, isbn = None):
		self._isbn = isbn
		self._ind = ind
	def __str__(self):
		print("str")
		
class User:
	def __init__(self, ind = 0 ,user_id = 0 , loc = " ", age = 0): 
		self._ind = ind
		self._id = user_id
		self._loc = loc
		self._age = age
		self._rates = dict() ##_rates will be ind to rate.
		
	##Finds euclidian distance for the rates
	def	rates_len(self):
		if(len(self.rates.keys() == 0)):
			return 0
		ret = 0
		for val in self.rates.values():
			ret += val * val
		return np.sqrt(ret)	

	##regular dot product between vectors
	def dot(self, other):
		self_len = self.rates_len()
		other_len = other.rates_len()
		ret = 0
		if(self_len == 0 or other_len == 0):
			return 0
		for key in self._rates:
			other_val = other._rates.get(key)
			if(not other_val):
				pass
			self_val = self._rates(key)
			ret += sel_val * other_val
		return ret/(other_len * self_len)
		
	##finds the average value of the vector
	def average(self):
		ret = 0
		num = 0
		for val in self._rates.values():
			ret += val
			num += 1
		return ret / num
		
	##normalizes vector
	def normalize(self):
		av = self.average()
		for key in self.rates.keys():
			self.rates[key] -= av

##reads the books from DataFrame object of pandas. Organizes dictionary as str isbn -> Book book
def read_books(book_csv, dic):
	book_num = 0
	book_list = []
	for row in book_csv.itertuples():
		if(not pd.isnull(row[1])):
			_ind = book_num
			book_num += 1
			_isbn = row[1]
			book = Book(ind = _ind , isbn = _isbn )
			book_dict[_isbn] = book
			book_list.append(book)
		else:
			return book_list	
	return book_list
	

##reads the users from DataFrame object of pandas. Organizes dictionary as str user_id -> User user
def read_users(user_csv, user_dict): 
	user_csv["Age"].fillna("0",inplace = True )
	user_ind = 0
	user_list = []
	user = None
	loc = ""
	age = 0
	user_id = 0
	for row in user_csv.itertuples():
		user_id = int(row[1])	
		if(not pd.isnull(user_id)):
			user_id = int(user_id)
			loc = row[2]
			if(not pd.isnull(loc)):
				print(user_ind)
				loc = loc.strip().split(",")
				loc = loc[-1]
				loc = loc.strip(); loc = loc.strip("\""); loc = loc.strip()
			age = row[3]
			if(not pd.isnull(age)):
				age = int(age)
			else:
				age = 0
			user = User(user_ind, user_id,loc, age)
			user_list.append(user)
			user_dic[user_id] = user
			user_ind += 1	
		else:
			return user_list
	return user_list


##Main function starts
##argv[1] should be book_info.csv
book_csv = pd.read_csv(sys.argv[1], sep = ";", encoding = "latin-1",usecols = ["ISBN"])
print("----------------")
book_dict = dict() ##book dictionary where keys are ISBN string and values are book object
book_list = read_books(book_csv, book_dict ) ##returns the number of books to book_num
print("hurrayyyyyy")
print("--- %s seconds ---" % (time.time() - start_time))

##argv[2] should be user_info.csv
user_csv = pd.read_csv(sys.argv[2], sep = ";", encoding = "latin-1")
user_dict = dict()
user_list = read_users(user_csv, user_dict)

##test
##x = rd.randint(0, len(user_list) - 1)
##print(str(x) + "\n" + user_list[x]._loc)
##end test
##test 
##x = rd.randint(0,len(book_list) - 1)
##print(str(x) + "\t" + book_list[x]._isbn)
##end test




