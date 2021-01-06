import random
import string
import base64
import time
def random_strings(n): #генерация n случайных строк
    strings = set()
    while len(strings) < n:
        strings.add(''.join(random.choice(string.digits + string.ascii_letters) for i in range(random.randint(1, 20))))
    return strings
    
s = random_strings(20000)
a = list()
for i in range(100):
    el = random.sample(s, random.randint(1000, 15000))
    a.append(el)

_memomask = {}

def hash_function(n): #генерация случайной хэш-функции
  mask = _memomask.get(n)
  if mask is None:
    random.seed(n)
    mask = _memomask[n] = random.getrandbits(64)
  def myhash(x):
    return hash(x) ^ mask
  return myhash

def jaccard(a, b):
    a_ = set(a)
    b_ = set(b)
    return len(a_.intersection(b_)) / len(a_.union(b_))

def similarity(a, b):
    count =  0
    for i in range(len(a)):
        if a[i] == b[i]:
            count = count + 1
    return count / len(a)


def min_hash(a, b, k):
    A = []
    B = []
    h_func = []
    for i in range(k):
        temp_hf  = hash_function(i)
        h_func.append(hash_function(i))
        temp_a, temp_b = [], []
        for x in a:
            temp_a.append(temp_hf(x))
        A.append(min(temp_a))
        for x in b:
            temp_b.append(temp_hf(x)) 
        B.append(min(temp_b))
    res = similarity(A, B)
    return res

for i in range(len(a)):
    for j in range(i+1, len(a)):
        print ("Set ", i, "and Set ", j, ":  Approximate ", end = ' ')
        start_1 = time.time()
        minhashres = min_hash(a[i], a[j], 100)
        end_1 = time.time() - start_1
        start_2 = time.time()
        jaccres = jaccard(a[i], a[j])
        end_2 = time.time() - start_2
        print (minhashres, " Precise ", jaccres, "difference: ", abs(minhashres-jaccres), " min_hash time: ", end_1, " jacc time: ", end_2)
