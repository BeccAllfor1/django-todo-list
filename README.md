<h1 align="center">Family Organiser</h1>

<p align="center">
<img src="INSERT RESPONSIVE WEBSITE IMAGE HERE" width="600" height="100%">
</p>

This is a full-stack framework project built using Django, Python, HTML and CSS. My goal is to create a functioning and responsive website, that allows users to post tasks, comment/respond to tasks allocated to them and have an organised easy to read and understand management system to refer to. This project has been built for the purpose of helping busy families who are looking for a task management solution, to ease their day to day lives, and assit in freeing up time to spend with their families.

# About
Family Organiser is a application where users can allocate tasks and access an organised and easy to use task management system. Many families in todays society have very busy lives, both parents may work, children have after school clubs, hobbies and social events. Its a struggle to stay organised, events, parties or clubs can be missed causing stress and arguments. The family organiser app keeps a record of not only what tasks need to be done but also who is responsible for carrying out the task, this eliminates confusion, keeping a track of who is doing what and when. Freeing up time to enjoy other activities and removing stress and arguments .

This page is primarily targeted at busy families who are looking for a task management solution, to ease their day to day lives, but can be utilised by anyone and everyone who are looking for an easy to use task management solution.

# Table of Contents 
1. [UX](#ux)
    - [User Stories](#user-stories)

2. [Scope](#scope)
    - [Features](#features)
    - [Future Features](#future-features)

3. [Structure](#structure)

4. [Wireframes](#wireframes)

5. [Database schema](#database-schema)

6. [Surface](#surface)

7. [Technologies Used](#technologies-used)

8. [Testing](#testing)

9. [Deployment](#deployment)

10. [Credits](#credits)

#
# UX
Using the core UX principles I first started with Strategy, thinking about the target audience & the features they would benefit from.

The target audience for 'Family Organiser' are:

- Families in todays society have very busy lives
- Anyone looking for an easy to use management system
- Parents who work long hours or who struggle due to shift work to have regular conversations about social events or childrens activities and need a tool to keep each other updated.


These users will be looking for:
- An easy to use website, with tasks that are easy to read and easy-to-find 
- A website that offers a way to communicate what tasks are upcoming
- Ability to make a user account in order to interact with the site content
- Ability to allocate tasks to each other,
- Ability to communicate an update or provide a response regarding the task,
- Ability to update the allocated tasks, and a way to remove the tasks when complete.

This website will offer all of these things whilst also allowing for intuitive navigation and conformability of use.

## User Stories 

**Epic: User Registration and Authentication**
- As a new user I can register an account so that I can access and allocate tasks to   the site
- As a registered user I can log in to my account so that I can update tasks I have added on the site
- As a registered user i can be confident unregistered users can not alter or delete m 
 my tasks.

**Epic: Viewing Tasks**
- As a logged-in User I can view a list of tasks so that I can browse through and respond or read tasks allocated to me
- As a logged-in User I can view information about tasks so that I can see what needs doing or attending, and 
  act upon those task
- As a logged-in User I can be confident my tasks are private to myself and known registered users.

**Epic: Task Management**
- As a logged-in User I can edit tasks I have made so that I can update or amend them
- As a logged-in User I can delete tasks so that I can remove any completed or no longer relevent tasks that I 
  have posted
- As a logged-in User I can respond to tasks i have been allocated so that  the author knows what has 
  been completed or why it has not

**Epic: Administrative Features**
- As a site Admin I can access the dashboard so that I can manage users that are no longer part of the families site

# Scope 

## **Features**
- User registration and login to ensure task privacy and personalised experience.

- Clear easy to read tasks so users know what needs to be done.

- Clear date and name of who has allocated the task to them so user knows who has given them this task and on 
  what date.

- Clear details of who its allocated to so the person knows the task is for them.

- Visible button to remove the task so the person who allocated can take it off when its complete.

- Visible button to edit the task in case anything changes or a mistake is made in the details of the task.

- Visible delete button so the person who allocated the task can delete it, if needed or when complete.

- User login so only registered users can create tasks and allocate them to other registered users, preventing 
  anyone else editing or adding fake tasks.

- Response/comment button so allocated user’s can add details of when task was completed or why task has not 
 been completed yet.


### **Home Page**
*Navigation bar:* 
- The navigation bar appears on every page so users can easily navigate through the site
- Navigation bar has links for 'Home', 'Tasks' and 'Login/Register'.
- The navbar is fully responsive, collapsing into a hamburger menu for medium and small screen size

<p align="center">
<img src="INSERT NAVIGATION BAR FEATURES IMAGE HERE" width="100%" height="100%">
</p>


*Hero Image:*
- The hero image welcomes the user with a short message advertising what the website is about
- The Login / Register button will take users to the login page, if users do not have an account there is a 
 link to the registration page

<p align="center">
<img src="INSERT HERO IMAGE HERE" width="100%" height="100%">
</p>


*Our Organiser:*
- Our Organiser section shows the tasks added so users can quickly see recently entered tasks
- The Our Organiser section is fully responsive, showing a scrolling list of tasks with a section to add more
- Users can see a title, date, Task details, allocated by, allocated too and number of buttons to Edit, Delete 
  and Respond.
- Responses by allocated to user will appear below the task

<p align="center">
<img src="INSERT IMAGE HERE" width="100%" height="100%">
</p>


*Footer:*
- Appears on every page snd contains social links
- Links are opened in a new tab to avoid dragging users from our site
<p align="center">
<img src="INSERT IMAGE HERE" width="100%" height="100%">
</p>


### **Login/Register**
- The Login / Register button takes users to the login page where they can also find a link to the Register 
  page where they can create an account
<p align="center">
<img src="INSERT IMAGE HERE" width="100%" height="100%">
</p>

<p align="center">
<img src="INSERT IMAGE HERE" width="100%" height="100%">
</p>


### **Response page**
- The main body of the page contains a response form, with a section for title, a shortdescription for the response and a date.
- only a logged in user who task is allocated to can leave a response.
<p align="center">
<img src="INSERT IMAGE HERE" width="100%" height="100%">
</p>

<p align="center">
<img src="INSERT IMAGE HERE" width="100%" height="100%">
</p>


### **Future Features**
 -Task categories and filtering for improved organisation and prioritisation. 
 -To be completed by date to help organise tasks and help prioritisation.
 -Allocated user views to help allocated user organise their own tasks, improving management of those tasks.
 -Email notification to let users know when they have new tasks or when tasks they have allocated have been completed.


### **Structure**
 
Since our aim is to make this site simple and easy to use for busy families, the structure idea
for Family Organiser was to keep it simple. Simplicity helps users to quickly and easily navigate and utilise the app in a time saving manner.

The website is made from one app:
- Todo


# Wireframes
All wireframes were created used [Balsamiq](https://balsamiq.com/)

Wireframes for each device are linked here:
- [Desktop](assets/documents/Desktop-wireframes)
- [Tablet](assets/documents/Tablet-wireframes)
- [Mobile](assets/documents/Mobile-wireframes)


# Database schema

<p align="center">
<img src="static/images/database.png" width="900" height="100%">
</p>

## Models
### **Todo Model**

<p align="center">
<img src="static/images/Todo_model.png" width="900" height="100%">
</p>

### **Response Model**

<p align="center">
<img src="INSERT IMAGE HERE" width="900" height="100%">
</p>

### **User Flow Chart**

<p align="center">
<img src="static/images/user_flow.png" width="900" height="100%">
</p>

## Surface

## Design 

## Chosen Color 
Color palette from [Coolors](https://coolors.co/9df57a-3c444c-fee73b-ff4f98-2daaf3-a9bedb)
<p align="center">
<img src="INSERT IMAGE HERE" width="800" height="300">
</p>

- **#BBBBBB** - navbar background color. It fits nicely with the hero image.
- **#FFC107** - buttons color. I choose this color because it matches nicely with the rest of the page and it elevates the look of the page
- **#F9F9F9** - body site color. Fits nicely with the rest of the page. I choose this color because normal white color is to bright
- **#F1E3CF**- background color for login/register forms. I choose this color because it fits nicely with side image
- **#484747** - footer background color



## Font 
- Mulish, sans-serif - main font
- Patric Hand- for navbar logo and welcome message


# Technologies Used

## Languages 
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [Python](https://www.python.org/)


## Frameworks, Libraries & Programs Used
[GitHub](https://github.com/) - Holds the repository of my project, GitHub connects to GitPod and Heroku.

[GitPod](https://gitpod.io/workspaces) – Connected to GitHub, GitPod hosted the coding space, allowing the project to be built and then committed to the GitHub repository. 

[Heroku](https://www.heroku.com/) - Connected to the GitHub repository, Heroku is a cloud application platform used to deploy this project so the backend language can be utilised/tested. 

[Django](https://www.djangoproject.com/) - This framework was used to build the foundations of this project

[Gunicorn](https://gunicorn.org/) - Gunicorn is a pure-Python HTTP server for WSGI applications.

[Dj Database URL](https://pypi.org/project/dj-database-url/) - This allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.

[Bootstrap](https://getbootstrap.com/) - Used to quickly add design to my website, Bootstrap focuses on mobile first design meaning this website is responsive across multiple devices ans screen sizes. 

[Cloudinary](https://cloudinary.com/?utm_source=google&utm_medium=cpc&utm_campaign=Rbrand&utm_content=492438439811&utm_term=cloudinary&gclid=Cj0KCQiAt8WOBhDbARIsANQLp96hTerzfFJ_P9lX0tEYEdtM3tSsYB6fhw-x3wQxOO0oc4hXm-A2ZBUaAptIEALw_wcB) - Used to store images online for the recipe posts. 

[Summernote](https://summernote.org/)

[Google Fonts](https://fonts.google.com/https://fonts.google.com/) - provide fonts for the website.

[Font Awesome](https://fontawesome.com/) -was used for icons.

[Balsamiq](https://balsamiq.com/) - was used to create site wireframes.

[Am I Responsive](http://ami.responsivedesign.is/) - to check if the site is responsive on different screen sizes.

[Pixabay](https://pixabay.com/) and [Unsplash](https://unsplash.com/) - were used for all the images

[W3C Markup Validator](https://validator.w3.org/#validate_by_input) - was used to validate HTML

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - was used to validate CSS

[Beautify](https://www.jpkc.com/tools/beautify/) - was used to correct indentation issues and get rid of too much whitespace - HTML, CSS

[Coolors](https://coolors.co/9df57a-3c444c-fee73b-ff4f98-2daaf3-a9bedb) - to make color palette


# Testing


## User Story Testing

### **Testing Users Stories form (UX) Section**

**EPIC: User Registration and Authentication**
1. As a new user I can register an account so that I can access and allocate tasks to the site
<p align="center">
<img src="INSERT IMAGE HERE" width="500" height="300">
</p>

2. As a registered user I can log in to my account so that I can update access and delete tasks on the sit
<p align="center">
<img src="INSERT IMAGE HERE" width="500" height="300">
</p>

**EPIC: Viewing and Searching Recipes**
1. As a logged-in User I can view a list of tasks so that I can browse through and respond or read tasks 
  allocated to me
<p align="center">
<img src="INSERT IMAGE HERE" width="500" height="300">
</p>

2. As a logged-in User I can view information about tasks so that I can see what needs doing or attending, and 
  act upon those task
<p align="center">
<img src="INSERT IMAGE HERE" width="300" height="200">
</p>

3. As a logged-in User I can be confident my tasks are private to myself and known registered users.
<p align="center">
<img src="INSERT IMAGE HERE" width="300" height="200">
</p>

**EPIC: Task Management**
1. As a logged-in User I can delete tasks so that I can remove any completed or no longer relevent tasks that  
  I have posted
<p align="center">
<img src="INSERT IMAGE HERE" width="600" height="100%">
</p>

2. As a logged-in User I can edit tasks I have made so that I can update or amend them
<p align="center">
<img src="INSERT IMAGE HERE" width="500" height="100%">
</p>

3. As a logged-in User I can respond to tasks i have been allocated so that i can update the author 
<p align="center">
<img src="INSERT IMAGE HERE" width="600" height="100%">
</p>

**EPIC: Administrative Features**
1. As a site Admin I can access the dashboard so that I can manage/remove users that are no longer part of the families site
<p align="center">
<img src="INSERT IMAGE HERE" width="1000" height="100%">
</p>


This was tested by accessing the Django Admin Panel. By creating a Superuser we can access the Django Admin Panel where the administrator can perform all the CRUD functionalities


## Bugs and Issues
- I had a problem where my edit button would not function. 
The error was corrected by moving the cancel and confirm button so it was inside the form.

- 
# Deployment
This project was deployed using Github and Heroku.

## Github 
To create a new repository I took the following steps:

- Logged into Github.
- Clicked over to the ‘repositories’ section.
- Clicked the green ‘new’ button. This takes you to the create new repository page.
- Once there under ‘repository template’ I chose the code institute template from the dropdown menu.
- I input a repository name then clicked the green ‘create repository button’ at the bottom of the page.
- Once created I opened the new repository and clicked the green ‘Gitpod’ button to create a workspace in Gitpod for editing.

## Django and Heroku 
- To get the Django framework installed and set up I followed the Code institutes [Django Blog cheatsheet](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf)

# Credits

- [Summernote](https://github.com/summernote/django-summernote) - I learnt how to change summernote toolbar
- [Code Institute](https://codeinstitute.net/ie/) - 'I think therefore I blog' project helped me with the Nav bar.
- [Django documentation](https://docs.djangoproject.com/en/4.0/topics/pagination/) 
- [GeeksforGeeks](https://www.geeksforgeeks.org/python-todo-webapp-using-django/)-I used this site to help me get the basics of a todo list



## Media
- All images were taken from[Pixabay](https://pixabay.com/) and [Unsplash](https://unsplash.com/)


## Acknowledgements
- Thanks to Code Institute and facilitator
