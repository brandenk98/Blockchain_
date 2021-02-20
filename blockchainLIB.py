'''
Creating a very simple Blockchain Using a Hash function

Blockchain will include:
	date, index , some data(a messsage in this example, and hash of previous block)


Cryptography
- secure data
A hash must be valid, so in my case a hash will start with the first four charaters being '0'


If hash is not valid we use a nonce in hash
	- We get our data (date, message, previous hash, index) 
	and a nonce of 1. If the hash we get with these is not valid, 
	we try with a nonce of 2. And we increment the nonce until we
	 get a valid hash.




First block in chain will be called  Genesis Block


'''

import hashlib	
import time



blocks = []

def string_encrypt(hash_string):
	sha_signature = \
		hashlib.sha256(hash_string.encode()).hexdigest()
	return sha_signature

#check to make sure  hash  is valid
def isValidHash(hash):
	if hash.startswith("0000"):
		return True
	return False


#create hash
def hashBlock(data,timestamp,previousHash, index):
	# _for internal use only

	_hash = ""
	#nonce or not valid
	nonce = 0

	while not isValidHash(_hash):
		_input = data + str(timestamp) + str(previousHash)
		_hash = string_encrypt(_input)
		nonce += 1
		print(nonce)
	blocks.append(_hash)


def lastHash():
	return blocks[len(blocks)-1]

def addNewBlock(nmessage):
	_index = len(blocks)
	#method of Time module is used to get the time in seconds since epoch
	timestamp = time.time()
	previousHash = getLastHash()
	hashBlock(nmessage,timestamp,previousHash,_index)

def allBocks():
	for i in range(0,len(blocks)):
		print(blocks[i])

def initBlock():
	data = "hello world"
	timestamp = time.time()
	previousHash = 0
	index = 0
	hashBlock(data, timestamp, previousHash,index)







