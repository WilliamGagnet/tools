# problem 4
def non_repeating(input):
    output = None
    for i in range(len(input)):
        if input[i+1] != input[i]:
            output = input[i]
            break
    return output

# problem 5
'''
# brute force
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
'''

# hashmap implementation
def two_sum(nums, target):
    seen = {}
    for i in range(len(nums)):
        looking_for = target - nums[i]
        if looking_for in seen:
            return (seen[looking_for], i)
        if nums[i] not in seen:
            seen[nums[i]] = i

# problem 7
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    s = "".join(sorted(s))
    t = "".join(sorted(t))
    for i in range(0, len(s)):
        if s[i] != t[i]:
            return False
    return True

'''
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    if sorted(s) != sorted(t):
        return False
    else:
        return True
'''

def string_to_list(text):
    return list(text)

#output = string_to_list("hello")
#print(output)

def move_zeros(lst):
    new_lst = []
    zeros = 0
    for i in range(0, len(lst)):
        if lst[i] == 0:
            zeros += 1
        else:
            new_lst.append(lst[i])
    for i in range(0, zeros):
        new_lst.append(0)
    return new_lst

'''
problem 10
return: true or false
plan: use a hashmap to compare each value in the list
data: list of ints
'''
def contains_duplicate(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False

'''
problem 11
return: true/false
plan: use a stack to validate if the correct closing parentheses are present
data: string
'''
def valid_parenthesis(s):
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    stack = []

    for i in range(0, len(s)):
        if s[i] in ["(", "[", "{"]:
            stack.append(s[i])
        if s[i] in [")", "]", "}"]:
            if stack:
                if stack[-1] != pairs[s[i]]:
                    return False
                else:
                    stack.pop()
            else:
                return False
    
    if len(stack) != 0:
        return False
    
    return True

# anagram hashmap - no sorting
def anagram_hashmap(s, t):
    pass


# k frequent elements
def k_frequent_elements(nums, k):
    counts = {}
    for item in nums:
        counts[item] = counts.get(item, 0) + 1

    lst = []
    for i in range(0, k):
        most_frequent_key = None
        most_frequent_value = 0
        for key, value in counts.items():
            if (value > most_frequent_value) and key not in lst:
                most_frequent_key = key
                most_frequent_value = value
        lst.append(most_frequent_key)
    
    return lst

#print(k_frequent_elements([1,1,1,2,2,3], 2))

'''
def k_frequent_elements(nums, k):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    result = []
    used = set()

    for _ in range(k):
        max_key = None
        max_val = 0

        for key, val in counts.items():
            if key not in used and val > max_val:
                max_key = key
                max_val = val

        result.append(max_key)
        used.add(max_key)

    return result
'''

# one reddit user says "kill yourself"
def product_array_but_self(arr):
    new_arr = []
    for i in range(0, len(arr)):
        pass

def product_except_self(nums):
    n = len(nums)
    res = [1] * n

    print(res)

    left_product = 1
    for i in range(n):
        res[i] = left_product
        left_product *= nums[i]

    print(res)

    right_product = 1
    for i in range(n - 1, -1, -1):
        res[i] *= right_product
        right_product *= nums[i]

    print(res)

    return res

#product_except_self([1,2,3,4])

def FirstReverse(strParam):

  # code goes here
  print(strParam)
  char_list = list(strParam)
  char_list.reverse()
  char_list = "".join(char_list)


  return char_list

# keep this function call here 
#print(FirstReverse("hello"))

def count_vowels(s):
    vowels = {"a", "i", "e", "o", "u"}
    count = 0
    s_list = list(s)
    for char in s_list:
        if char in vowels:
            count += 1
    return count

def reverse_string(s):
    return s[::-1]

#print(reverse_string("cat"))

def list_max(lst):
    highest = lst[0]
    for item in lst:
        if item > highest:
            highest = item
    return highest

#print(list_max([3, 7, 2, 9, 5]))


def two_sum_again(lst, target):
    seen = {}
    for i in range(0, len(lst)):
        if (target - lst[i]) in seen:
            return [(seen[target - lst[i]]), i]
        elif lst[i] not in seen:
            seen[lst[i]] = i
    return None

#print(two_sum_again([2, 7, 11, 15], target = 9))

def count_frequencey(s):
    counts = {}
    s = list(s)
    for item in s:
        counts[item] = counts.get(item, 0) + 1
    return counts

#print(count_frequencey("aabbbc"))

def remove_duplicates(lst):
    seen = set()
    new_lst = []
    for item in lst:
        if item not in seen:
            new_lst.append(item)
            seen.add(item)
    return new_lst

#print(remove_duplicates([1,2,2,3,3,3]))

def longest_word(s):
    s = s.split(" ")
    longest_text = s[0]
    longest_length = len(s[0])
    for item in s:
        if len(item) > longest_length:
            longest_length = len(item)
            longest_text = item
    return longest_text

#print(longest_word("I love programming and figs"))

def FizzBuzz():
    for i in range(1, 101):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# OOP practice

# 1. basic class
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def describe(self):
        print(f"{self.make} {self.model}")

'''car = Car(make="Honda", model="CR-V")
print(car.make)
car.describe()'''


# 2. counter -- depends on if you want a global counter or not
class Counter:
    count = 0

    @classmethod
    def increment(cls):
        cls.count += 1

    @classmethod
    def reset(cls):
        cls.count = 0

'''counter = Counter()
for i in range(0, 3):
    counter.increment()
print(counter.count)
counter.reset()
print(counter.count)
'''

# 3. bank account
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Not enough funds.")

# 4. rectangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return (self.width * 2) + (self.height * 2)

# 5. student tracker
class Student:
    def __init__(self, name: str, grades: list):
        self.name = name
        self.grades = grades

    def add_grade(self, score):
        self.grades.append(score)

    def average(self):
        total = 0
        for grade in self.grades:
            total += grade
        
        return total / len(self.grades)
    

# 6. inventory item
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

# 7. simple game character
class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def take_damage(self, amount):
        if amount > self.hp:
            self.hp = 0
        else:
            self.hp -= amount
    
    def attack_target(self, other_character):
        other_character.take_damage(self.attack)

'''character1 = Character(name="Satoru", hp=100, attack=25)
character2 = Character(name="Suguru", hp=75, attack=15)

while character1.hp > 0 and character2.hp > 0:
    character1.attack_target(character2)
    character2.attack_target(character1)
    print(character1.hp)
    print(character2.hp)

if character1.hp == 0 and character2.hp == 0:
    print("It's a draw!")
elif character2.hp == 0:
    print(f"{character1.name} wins!")
else:
    print(f"{character2.name} wins!")'''


# 8. inheritance practice
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_info(self):
        return self.name, self.salary

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_info(self):
        return self.name, self.salary, self.team_size


# encapsulation test
class Number:
    def __init__(self, value):
        self.value = value
    
'''num = Number(1)
print(num.value)
num.value = 2
print(num.value)'''

'''# brute force On3 solution
def three_sum(nums):
    triples = set()

    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    triples.add(tuple(sorted([nums[i], nums[j], nums[k]])))
    
    return triples'''

# On2 solution
def three_sum(lst):
    triples = []

    lst.sort() # put the list's items in order from least to greatest

    for i in range(0, len(lst) - 1):
        if (i > 0) and (lst[i] == lst[i-1]): # skip duplicates
            continue

        left = i + 1 
        right = len(lst) - 1 
        total = lst[i] + lst[left] + lst[right]
        
        while (right > left):
            total = lst[i] + lst[left] + lst[right]

            if total == 0:
                triples.append([lst[i], lst[left], lst[right]])
                print("append")

                while (right > left) and (lst[left] == lst[left+1]): # skip duplicates
                    left += 1
                
                while (right > left) and lst[right] == lst[right-1]: # skip duplicates
                    right -= 1
           
                left += 1
                right -= 1

            elif total < 0:
                left += 1
                print("left plus 1")

            else:
                right -= 1
                print("right minus 1")
    
    return triples

'''#nums = [-5, -4, -3, -2, -2, -2, -1, -1, -1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 4, 5]
nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))'''


# brute force practice
def pairs_sum_to_ten(lst):
    pairs = set()
    for i in range(0, len(lst)):
        for j in range(i+1, len(lst)):
            pair = tuple(sorted([lst[i], lst[j]]))
            if lst[i] + lst[j] == 10:
                pairs.add(pair)
    return [list(p) for p in pairs]

def triples_sum_to_ten(lst):
    triples = set()
    for i in range(0, len(lst)):
        for j in range(i+1, len(lst)):
            for k in range(j+1, len(lst)):
                triple = tuple(sorted([lst[i], lst[j], lst[k]]))
                if lst[i] + lst[j] + lst[k] == 10:
                    triples.add(triple)
    return triples

# im not doing quadruples_sun_to_ten(), i understand it now, sets also cant have duplicates


'''def longest_substring(s):
    seen_chars = set()
    curr_longest = ""
    longest = ""
    has_reset = False

    for i in range(0, len(s)):
        if s[i] not in seen_chars:
            curr_longest += s[i]
            seen_chars.add(s[i])
            print("if: " + curr_longest)
            
            if len(curr_longest) > len(longest):
                longest = curr_longest
        else:
            if len(curr_longest) > len(longest):
                longest = curr_longest
            
            seen_chars.clear()
            
            if s[i-1] != s[i]:
                curr_longest = s[i-1] + s[i]
                seen_chars.add(s[i-1])
                seen_chars.add(s[i])
            else:
                curr_longest = s[i]
                seen_chars.add(s[i])

            has_reset = True
            print("else: " + curr_longest)
            print(has_reset)
            print(longest)

    if has_reset:
        return len(longest)
    else:
        return len(curr_longest)'''


'''def longest_substring(s):
    longest = ""
    seen_chars = {}
    left = 0
    right = 0

    for i in range(0, len(s)):
        if s[i] not in seen_chars:
            seen_chars[s[i]] = i
            right += 1
            
            #print("if")
            #print(s[left:right])
        else:
            left = seen_chars[s[i]] + 1
            right += 1
            seen_chars.clear()
            for j in range(left, right):
                seen_chars[s[j]] = j
            
            #print("else")
            #print(s[left:right])

        if len(s[left:right]) > len(longest):
                longest = s[left:right]

    return len(longest)'''


'''# alternate version
def longest_substring(s):
    seen_chars = {}
    left = 0
    longest = 0

    for i in range(len(s)):
        if s[i] in seen_chars:
            left = max(left, seen_chars[s[i]] + 1)

        seen_chars[s[i]] = i

        longest = max(longest, i - left + 1)

    return longest'''

def longest_substring(s):
    longest = ""
    seen_chars = {}
    left = 0
    right = 0

    for i in range(0, len(s)):
        if s[i] not in seen_chars:
            seen_chars[s[i]] = i
            right += 1
        else:
            left = max(left, seen_chars[s[i]] + 1)
            seen_chars[s[i]] = i
            right += 1

        if len(s[left:right]) > len(longest):
                longest = s[left:right]

    return len(longest)


'''s = "anviaj"
print(longest_substring(s))'''


'''def group_anagrams(anagrams):
    sorted_words = set()

    for i in range(0, len(anagrams)):
        sorted_words.add("".join(sorted(anagrams[i]))) # no duplicates in sets by default

    result = []

    for item in sorted_words:
        sub_list = []

        for i in range(0, len(anagrams)):
            if "".join(sorted(anagrams[i])) == item:
                sub_list.append(anagrams[i])
        
        result.append(sub_list)

    return result'''

def group_anagrams(anagrams):
    sorted_words = {}

    for word in anagrams:
        sorted_word = "".join(sorted(word))

        if sorted_word not in sorted_words:
            sorted_words[sorted_word] = []
        
        sorted_words[sorted_word].append(word)
    
    return list(sorted_words.values())

            




anagrams = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(anagrams))