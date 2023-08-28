#!/usr/bin/env python
# coding: utf-8

# In[8]:


text = "Python Exercises, PHP exercises."
print(re.sub("[ ,.]", ":", text));


# In[11]:


text = "Python Exercises, PHP exercises."
list = re.findall("[ae]\w+", text);
print(list);


# In[15]:


text = "Python Exercises, PHP exercises";
regex = r"\b\w{4,}\b";
reg_compile = re.compile(regex);
result = re.findall(regex, text);
print(result);


# In[17]:


text = "Python Exercises, PHP exercises";
regex = r"\b\w{3,5}\b";
reg_compile = re.compile(regex);
result = re.findall(regex, text);
print(result);


# In[33]:


words = ["example (.com)", "hr@fliprobo(.com)", "github (.com)", "Hello(Data Science World)","Data (Scientist)"];
for item in words:
    print(re.sub("[ (\b)]", "", word))


# In[34]:


items = ["example (.com)", "hr@fliprobo(.com)", "github (.com)", "Hello(Data Science World)","Data (Scientist)"];
for item in items:
    print(re.sub(r" ?\([^)]+\)", "", item))


# In[36]:


text = "ImportanceOfRegularExpressionInPython";
result = re.split('(?<=.)(?=[A-Z])',text);
print(result);


# In[37]:


text = 'RegularExpression1IsAn2ImportantTopic3InPython';
res = re.sub("[A-Za-z]+", lambda ele: " " + ele[0] + " ", text);
print(res);


# In[43]:


text = "Hello my name is Data Science and my email address is xyz@domain.com and alternate email address is xyz.abc@sdomain.com. please contact us at hr@fliprobo.com for further information."
findemail = re.findall(r"[\w\.-]+@[\w\.-]+", text);
print(findemail);


# In[46]:


def matchFunction(text):
        patterns = '^[a-zA-Z0-9_]*$'
        if re.search(patterns,  text):
                return 'String Match Found!'
        else:
                return('Match Not Found!')

print(matchFunction("Hello my name is Data Science and my email address is xyz@domain.com"));
print(matchFunction("This_IS_my_Assignment_2"));


# In[48]:


def matchFunction(string):
    text = re.compile(r"^7")
    if text.match(string):
        return 'Matched!'
    else:
        return 'Unmatched!'
print(matchFunction('7-star'))
print(matchFunction('5-star'))


# In[50]:


ip_address = "182.001.040.001"
parts = ip_address.split(".")
parts = [int(part) for part in parts]
parts = [str(part) for part in parts]
ip_address = ".".join(parts)
print(ip_address)


# In[68]:


patterns = [ 'fox', 'dog', 'horse']
text = "The quick brown fox jumps over the lazy dog."
for pattern in patterns:
    print('Searching for "%s" in "%s" ->' % (pattern, text),)
    if re.search(pattern,  text):
        print ('Found!')
    else:
        print('Not Found!')


# In[64]:


pattern = "fox";
sample_text = "The quick brown fox jumps over the lazy dog.";
match = re.search(pattern, sample_text);
a = match.start()
print('Found "%s" in "%s" at %d ' %     (match.re.pattern, match.string, a))


# In[69]:


sample_text = "Python exercises, PHP exercises, C# exercises"
pattern = "exercises"
for match in re.findall(pattern, sample_text):
    print('Found "%s"' % match)


# In[70]:


def modify_date_format(date):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', date)
date = "2023-08-06"
print("New date in DD-MM-YYYY Format: ",modify_date_format(date))


# In[76]:


sample_text = "Python Exercises, 100 PHP exercises."
for m in re.finditer("\d+", sample_text):
    print(m.group(0))
    print("Index position:", m.start())


# In[77]:


def capital_letter_saggragation(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

print(capital_letter_saggragation("RegularExpressionIsAnImportantTopicInPython"))


# In[78]:


def find_match(text):
        patterns = '[A-Z]+[a-z]+$'
        if re.search(patterns, text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(find_match("DatAScience"))


# In[ ]:




