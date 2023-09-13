# installments required: pip install beautifulsoup4
# Second thing that we're going to use is parser method from beautifulsoup library.so,when we work with beautifulsoup we have to specify the method that we're going to use to parse html files into python objects.There are different methods to parse html code,one of the best is lxml parser since if we deal with default parser it doesn't deal with broken html code: pip install lxml

# importing libraries
from bs4 import BeautifulSoup

# Now our next step is accessing content inside home.html file,in order to do that we have to work with file objects
# The below code will allow us to open the specific file than read it's content.Once we applied the read method,that means we're basically applying the read method(htm_file.read())

# as html_file: This part of the code assigns the file object returned by open() to the variable html_file. This is done to make it easier to work with the file throughout the rest of the code. You can choose any valid variable name here; html_file is just a convention used to indicate that the variable represents a file.

# content = html_file.read(): This line reads the content of the opened file (html_file) using the read() method and assigns it to the variable content.So, html_file is simply a variable name that holds the file object for the 'home.html' file, allowing you to perform operations on that file using the variable throughout your code.


with open ('home.html','r') as html_file:
    content = html_file.read()
    # print(content),And when we print this you can notice that our info is same which was present in home.html
    # Now,we'll use beautifulsoup library to prettify html,and work with its tags.And for that we'll have to create instance of beautifulsoup,which is stored in a variable soup,argument passed will be the html file, that we want to scrap,and the second argument will be the parser method we want to use 
    
soup = BeautifulSoup(content,'lxml')
# print(soup.prettify()) , This prettify will allow us to present the html content in more pretty way,and you'll notice that the content is same as present in content file

# Now,let's assume that grab all the html tags as h5 tags,so for that we'll first create a new variable,in this case that is courses_html_tags,Now we will iterate through these html tags,as this is a list 

courses_html_tags=soup.find_all('h5')
print(tags)
for course in courses_html_tags:
    print(course.text)

# Our above code,goes through each item in the courses_html_tags collection.For each item (which is assumed to be an HTML element), it extracts the text content inside that element using the text attribute.
# It prints the extracted text content to the console.
 
#  Now,let's grab price for courses:First step will be grabbing all courses cards,and for that we'll find our div tag,and inside div we'll have to apply filter for being more specific,this underscore in class_,represents that this class is a built in keyword in python,and with this underscore the beautifulsoup will understand that we're relating to the class of html attribute

course_cards=soup.find_all('div',class_='card')
for course in course_cards:
    course_name = course.h5.text
    course_price = course.a.text
    
    print(course_name)
    print(course_price)
    # This will print our output like,
    # Python for beginners
    # Start for 20$
    # Python Web Development
    # Start for 50$
    # Python Machine Learning
    # Start for 100$
    
# For getting more specified results,like getting results like python for beginners costs 20$,we can do that using 
# split method to access the last element of that text because the price is located at the last word 

