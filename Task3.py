import random
import string
import base64
import time
def random_strings(n): #генерация n случайных строк
    strings = set()
    while len(strings) < n:
        strings.add(''.join(random.choice(string.digits + string.ascii_letters) for i in range(random.randint(1, 20))))
    return list(strings)
    
s = random_strings(20000)
a = []
for i in range(100):
    a.append(random.sample(s, random.randint(1000, 15000)))

def jaccard(a, b):
    a_ = set(a)
    b_ = set(b)
    return len(a_.intersection(b_)) / len(a_.union(b_))
_memomask = {}

def hash_function(n): #генерация случайной хэш-функции
  mask = _memomask.get(n)
  if mask is None:
    random.seed(n)
    mask = _memomask[n] = random.getrandbits(64)
  def myhash(x):
    return hash(x) ^ mask
  return myhash

def similar_elements(a, b): 
    sim_el = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                sim_el = sim_el + 1
                break
    return sim_el

def unique_elements(a, b):
    d = dict()
    for i in range(len(a)):
        d[a[i]] = i
    for i in range(len(b)):
        d[b[i]] = i
    return len(d)

def min_hash(a, b, k):
    A = []
    B = []
    h_func = []
    for i in range(k):
        temp_hf  = hash_function(i)
        h_func.append(hash_function(i))
        temp_a, temp_b = [], []
        for a_idx in range(len(a)):
            temp_a.append(temp_hf(a[a_idx]))
        A.append(min(temp_a))
        for b_idx in range(len(b)):
            temp_b.append(temp_hf(b[b_idx])) 
        B.append(min(temp_b))
    return similar_elements(A, B)/unique_elements(A, B)


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