# CP1404 Assignment 2: Reading Tracker 2.0 by Zhang Tianyi

Brief Project Description: Use kivy to build a reading tracker GUI that can mark book state and add new book GitHub
URL: https://github.com/JCUS-CP1404/assignment-2-Tianyi2

## 1. How long did the entire project (assignment 2) take you?

The entire project takes me around 10hours. Near half of the time was used to complete the kivy functions. 2 hours were
spent on documentation, and 1 hour modifying the format and checking errors. The rest of the 2 hours were spent on
completing the two classes and using the class in a1_classes.

## 2. What are you most satisfied with?

The part I am most satisfied with would be the kivy part. I do not know much about it at first. However, I completed it
with accomplished all the requirements by searching the Internet and asking my teacher and classmates in the end. I feel
proud of myself.

## 3. What are you least satisfied with?

The part I am least satisfied with is also the kivy part. I was frustrated with doing it at first. All the functions I
wrote are not working, even though I have spent much time trying to fix them.

## 4. What worked well in your development process?

I would like to say asking others and searching worked well in my development process. There are a few parts that I do
not know how to code, by asking others and searching on the Internet they were solved. However, the knowledge or
experience in coding also helps me a lot. Without them, I cannot easily understand what my friends and the blog on the
Internet are talking about and apply them to my program. Besides, planning before doing, gives me a very clear path on
what I should do first and increase my efficiency.

## 5. What about your process could be improved the next time you do a project like this?

The next time I do a project like this I would learn about the programming language going to use before starting doing
the project. In this case kivy language. This is because if one does not understand the language it will be very
disappointing while doing the project. He will find all his codes are not working, feel the project is a hard task, and
keep procrastinating. Therefore, it is important to understand or have some knowledge of the programming language going
to use. Moreover, I would write the docstring while writing the function. In this project, I wrote all the functions at
first and go back to write docstrings. I feel it has lower efficiency, and you need some time to recall what the
function is about before writing the docstrings.

## 6. Describe what learning resources you used and how you used them.

The KivyDemos in GitHub is one of the resources that I used. I ran all the demos and note down those that might be
useful to the project. When I do not know how to code some parts of the program, I will refer to those demos. Stack
Overflow is a website that I visited to ask questions about coding.

## 7. Describe the main challenges or obstacles you faced and how you overcame them.

The function to change the change of book button when clicking is the main challenge for me. I was trying to use the
button state to determine the color of the button. For example, the book is completed and will give a "down" state and
background color of gray. The book is required will be "normal" state and with the background color of light blue.
However, this method failed as I do not know how to check the book state (required or completed) of the book button.
After taking a break, I tried to note down some possible choices on how could I accomplish the change color function.
Then I chose the one with the higher chance of completing the function. After searching through the Internet, and
thinking by myself, I completed it. Moreover, the reason why it is a challenge for me is that I am not used to the
class. I could simply use "str(book)" to call the "__str__" method in book class and bind the book object to the button.
Then I only need to write "book.is_completed" to determine the state of a book.

## 8. Briefly describe your experience using classes and if/how they improved your code.

There are two classes, Book and BookCollection classes, used in the program. Book class is used in a1_classes program,
and both classes are used in the Kivy project. The use of classes make the code shorter and clearer as I can just call
the methods instead of creating new functions. 