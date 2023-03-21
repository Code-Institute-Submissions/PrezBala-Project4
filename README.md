# Astro - Project 4

<img src="https://github.com/PrezBala/Project4/blob/main/static/assets/images/astrohome.png">

This project is based on the Battleship game which is a game that is very widely know. This game is Python based game which runs within the Code Institite mock terminal within Heroku. The main purpose of the game is for the user to play against the computer and the user will have 10 turns to find all of their opponents ships before there ship gets destroyed. 

This project is  based on a forum 'Astro' Community, the ultimate online destination for all space enthusiasts! Where all users can connect with fellow stargazers, aspiring astronauts, and astrophysicists alike. The websites mission is to create a thriving, supportive community where members can explore the wonders of the universe, share their knowledge, and engage in fascinating discussions about space and beyond.

Astro Community utilizes external Python modules to deliver a seamless and efficient user experience. 

To ensure a personalized experience, my platform offers user-friendly login and signup options. Once the user created their account, they'll be able to post and reply to comments, making there voice heard in the vast expanse of the Astro Community.

[Live link to the game](https://prasena-project-3-battleships.herokuapp.com/)

<hr>

# Table of contents   
- [Astro Community](#astrocommunity)
- [Table of contents](#table-of-contents)
- [User-Experience-Design](#user-experience-design)
  * [Site Goals](#site-goals)
  * [Agile Planning](#agile-planning)
  * [Scope](#scope)
  * [Structure](#structure)
    + [Astro Community Features](#astrocommunity-features)
    + [Home Page](#home-page)
    + [Footer](#footer)
    + [Browse Ideas](#browse-ideas)
    + [Idea Detail](#idea-detail)
    + [Sign in, log in, log out](#sign-in--log-in--log-out)
    + [Create Idea](#create-idea)
    + [Edit and Delete Idea](#edit-and-delete-idea)
  * [Features left to impliment](#features-left-to-impliment)
- [Wireframes](#wireframes)
- [Database](#database)
- [Admin Role](#adminrole)
- [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Profile Pictures](#profilepics)
- [Technologies](#technologies)
  * [External Python Modules](#external-python-modules)
- [Testing](#testing)
  * [Functional Testing](#functional-testing)
    + [Navigation Links](#navigation-links)
    + [Footer](#footer-1)
    + [Sign Up Page](#sign-up-page)
    + [Log out Page](#log-out-page)
    + [Log in](#log-in)
    + [Create Idea Page](#create-idea-page)
    + [Edit Idea](#edit-idea)
    + [Delete a post](#delete-a-post)
    + [Comment on a post](#comment-on-a-post)
    + [User test](#user-test)
  * [Accessibility](#accessibility)
  * [Validator Testing](#validator-testing)
  * [PP8 Validator](#pp8-validator)
  * [Lighthouse Report](#lighthouse-report)
- [Responsiveness](#responsiveness)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [References](#references)
- [Acknowledgements](#acknowledgements)



# User-Experience-Design

## Site Goals

Astro Community aims to unite space enthusiasts in a thriving online platform, fostering knowledge exchange, stimulating discussions, and encouraging the exploration of the wonders of the universe. My goal is to create an engaging, supportive space where members can connect, learn, and share their passion for the cosmos.

## Agile Planning

This project was developed using agile methodologies, delivering small features over 4 sprints spaced out over 5 weeks.  Each issue was labelled must have, should have and could have.  The must have features were completed first, then the should have's, then the could have's.  It was done this way to ensure a complete website is made with the nice to have features added if there is capacity.

My kanban board was made using github projects which can be viewed [here](https://github.com/users/PrezBala/projects/1/views/1).  Each view can be clicked in to obtain further information.

![kanban](/static/images/kanban.png)

The user stories were grouped into different Epics

Epic 1 - Set up

The base setup of the Django app was done first as nothing else can be completed before this is done. I completed the base html, the header and footer. I also included deployment in this section so as to avoid complications at the end.

Epic 1 user stories

- As a developer, I need to set up the project so that it is ready for implementing core features
- As a developer, I want to create a base HTML page so that all pages can use the same format.
- As a user, I want to be able to navigate easily around the site easily on my mobile
- As a site owner, I want to share social media links.
- As a developer, I want to deploy to heroku early to avoid any problems later on

Epic 2 - Database model and admin.

Setting up database model and admin functions and template pages to be able to view the ideas when not logged in

Epic 2 User Stories

- As a developer, I want to lay the foundations of the database to enable users to update their own posts later on.
- As a user that is not logged in, I want to be able to browse ideas from other users

Epic 3 - Setting up login signup and logout pages

Epic 3 User Stories

- As a new user, I want to be able to sign up easily and intuitively
- As a returning user, I want to be able to log in easily.
- As a user, I want to be able to log out of the site safely and easily.

Epic 4 - CRUD

Adding CRUD functionality for users adding editing and deleting ideas

Epic 4 User Stories

- As a user, I want to be able to input my own ideas of things to do into the site in an easy and intuitive way so that I can easily share ideas with others
- As a user, I want to be able to comment and like other people’s ideas
- As a user, I want to be able to edit ideas I have created
- As a user, I want to be able to delete ideas that I have created
- As the site owner I want to ensure only the creator of an idea can edit or delete it

Epic 5 - Styling

Epic 5 User Stories

- As a user I want the front page to be clear and self-explanatory so I know I am in the right place
- As a developer, I want to ensure the styling is correct
- As a developer, I want to ensure the forms are all the same style and look good on all devices

Epic 6 - Documentation

Epic 6 Tasks

- Complete Readme documentation
- Complete testing and writeup

## Scope
- Responsive Design
- Home page with information about Kidsbored
- Ability to perform CRUD functionality on ideas
- Restricted features for not logged in users

## Structure

### Kidsbored Features

Navbar

user story - As a user I want to be able to navigate easily around the site easily from any devise

Navigation Menu

When the user is not logged in the navigation menu links to the Home page Browse Ideas page and the Sign in page

![Navbar before login](/static/images/navbar-before-login.png)

Once the user has signed in the navigation menu changes to Home, Browse Ideas, Create Idea and Log out

The user will also receive a toast message saying they have successfully signed in.

![Navbar](/static/images/navbar.png)

The sign in, log in, log out pages were made using allauth.

on smaller devices, the menu options collapse into a button

![Mobile Navbar](/static/images/mob-navbar.png)

### Home Page

- User Story - As a user I want the front page to be clear and self-explanatory so I know I am in the right place

The front page contains a hero image of some happy children eating ice cream.  This will make it evident to the user that the website is for children.

![Hero Image](/static/images/hero-image-for-readme.png)

Under this is information about the site and how to share and browse activity ideas.

![Welcome Text](/static/images/welcome-text.png)

### Footer

- User Story: As site owner, I want to share social media links and contact details

The Footer has been added to the bottom of the site and contains links to social media sites so that users can also share their ideas and promote the site via social media.

![Footer](/static/images/kidsbored-footer.png)

### Browse Ideas

- User Story: As a user that is not logged in, I want to be able to browse ideas from other users.

Anybody can use the website to browse ideas, they are shown in the browse ideas page with the activity title and pictures in rows of 3.  The activity Title is a link to open up each activity with further information about it.

![Brows Ideas Page](/static/images/browse-ideas.png)

### Idea Detail 

- User Story: As a user, I want to be able to comment and like otherpeople’s ideas

Each user story opens up to a full page which contains the image, a link to the activity website if applicable, the age range the activity is aimed at, activity cost per person, the location of the activity and a review.

![Detail Page](/static/images/detail-page.png)

Logged-on users can also comment on and like the ideas.

![comments](/static/images/comments.png)

### Sign in, log in, log out

User Stories
- As a new user, I want to be able to sign up easily and intuitively
- As a returning user, I want to be able to log in easily.
- As a user, I want to be able to log out of the site safely and easily.
- As a developer, I want to ensure the forms are all the same style and look good on all devices

Users can sign in and out using various forms and confirmation pages. These forms were made using allauth and edited using bootstrap

![Sign in page](/static/images/sign-in-page.png)

![Sign up Page](/static/images/sign-up.png)

![Sign out page](/static/images/sign-out.png)

As you can see all of the sign in out pages have a similar design to them, with the dark writing on the white background.  

I went with a light background and dark writing for the log in/out pages and the reverse for the  Create, Edit and Delete pages, but kept the styling the same.  This connects the forms throughout the website but differentiates between the two areas

### Create Idea

- User Story: As a user, I want to be able to input my own ideas of things to do into the site in an easy and intuitive way so that I can easily share ideas with others

Once the user is logged in they can create their own idea using the create Idea form.  The forms were made using crispy forms which were used in conjunction with bootstrap.

The picture below is from a mobile view.  You can see that the forms colapse down so they can easily be used on a mobile device.

![Create idea form](/static/images/create-idea-form.png)

### Edit and Delete Idea

User Stories
- As a user, I want to be able to edit ideas I have created
- As a user, I want to be able to delete ideas that I have created
- As the site owner I want to ensure only the creator of an idea can edit or delete it

The creator of an idea will be able to view edit and delete icons on their idea detail page.  The edit button will take them to the create idea form but it will be pre-populated with information that is already saved.  The user can then update the information and save it again where they will be redirected back to the ideas page.

They will get a toast message to advise them that their creation/edit has been successful

![Edit Idea](/static/images/edit-idea.png)

The delete button will take the user to a confirmation page asking them to confirm they wish to delete that idea.  Once an idea is deleted all comments will be deleted with it.

![Delete Idea](/static/images/delete-idea.png)

The delete and edit views use LoginRequiredMixin and UserPassesTestMixin to ensure that only the idea creator who is logged in can update or delete their idea.

![edit and delete](/static/images/edit-and-delete.png)

## Features left to impliment

- I had planned to add a profile page where the user could add their picture and details about themselves.  This would also show all their ideas in one place for easy editing or deleting. Unfortunately, I ran out of time to add this feature 

- Once the profile page was in place I could add an option to show the creator’s picture as well as their name on their ideas.

- I had also planned to add search options on the brows ideas page allowing users to search by Activity name, location, price or age range.

- In a future development I would like to add CRUD functionality to the comments section and to enable users to comment on comments so more social interaction could be had.

- The site could also be taken further with a social development where users could arrange meet ups and get together in person.

# Wireframes

Home Page

![Home page wireframe](/static/images/home-page-wireframe.png)

Sign Up

![Sign up wireframe](/static/images/sign-up-wireframe.png)

Log In

![Log in wireframe](/static/images/log-in-wireframe.png)

Log out

![log out wireframe](/static/images/log-out-wireframe.png)

Browse Ideas

![Browse Ideas wireframe](/static/images/browse-ideas-wireframe.png)

Idea Detail

![Idea Detail wireframe](/static/images/idea-detail-wireframe.png)

Create/Edit Idea Form

![Create/Edit Idea wireframe](/static/images/create-idea-wireframe.png)

Delete Idea Conirmation

![Delete Idea wireframe](/static/images/delete-idea-wireframe.png)

# Database

The data was designed to give the user CRUD functionality once signed in.  Ideas are connected to the author by foreign key which allows users to edit and delete ideas connected to their account. 

# Security

Views were secured by using the django based view mixin, UserPassesTestMixin.  A test function was created to use the mixin and checks that the user is authorised to access the page.  an if statement is also used in idea_detail.html to hide the delete and edit buttons if the user is not authorised.  

Environment variables were stored in an env.py file for security purposes to ensure no secret keys, api keys or sensitive information were added to the repository.  These variables were added to heroku config vars within the project

# Design

## Colour Scheme

I opted for a simple colour scheme.  It needed to be gender neutral and although the site is about children it is aimed at adults so I wanted a more adult feel to it.  I also wanted it to be neutral so that the user ides stood out.  with this in mind, I went for a background colour of #041121

![Background colour](/static/images/background-colour.png)

and a text colour of rgb(237, 233, 249.

![Text colour](/static/images/text-colour-1.png)

## Typogropny

I used Yusei Magic for the body of the site and Ranchers for the Kidsbored heading.

I downloaded these from google fonts and imported them into the style sheet

## Imagery  

The hero image used is a picture of my own.  I sought permission from the parents of the children.

The placeholder image was taken from pexels and is royalty free.  I chose a generic picture of children running through a field.  It is bright and colourful.

# Technologies

- HTML
  - The structure of the site was made using HTML
- CSS
  - The website was styled using CSS in an external stylesheet 
- Python 
  - Python was the main programming language used within the django app
- Github
  - Source code was hosted in Github
- Git
  - Git was used to write, commit and push code during development 
- Font Awesome
  - Various Font Awesome icons were used throughout the site
- Balsamiq
  - Balsamiq wireframes were used to plan 
- javascript
  - I used a very small amount of javascript to make the toast messages disappear
- [GitHub Wiki TOC generator](http://ecotrust-canada.github.io/markdown-toc/)
  - I used this to enter my table of contents.

## External Python Modules
- cloudinary==1.29.0 - cloudinary was used to store imagery for the site and to upload user images
- dj-database-url==0.5.0 - used to parse database url for production environment
- dj3-cloudinary-storage==0.0.6 - Storage system for cloudinary
- Django==3.2.13 - Framework used to build the application
- django-allauth==0.51.0 - Used for the sites sign in and sign out authentication system 
- django-cloudinary-storage==0.3.0 - Storage for cloudinary
- django-crispy-forms==1.14.0 - used to style forms 
- django-summernote==0.8.20.0 - used in admin panel
- gunicorn==20.1.0 - Installed as a dependency with another package
- oauthlib==3.2.0 - Installed as a dependency with another package
- Pillow==9.2.0 - Installed to upload images but ended up using cloudinary istead,  left incase needed for future development
- psycopg2==2.9.3 Needed for heroku deployment 
- whitenoise==6.2.0 - Installed to deploy static files to heroku.

# Testing

## Functional Testing

### Navigation Links

Testing was performed on on all navigation links throughout the site.  I achieved this by clicking on each link to ensure it went to the correct place.

kidsbored Logo => index.html
Home page => index.html
Browse Ideas => ideas.html
Idea Title => ideas_detail.html
Delete Button => idea_delete.html
Edit Button => idea_edit_form.html
Edit Button Submit Button => ideas.html
Activity Website => chosen website(opens in new tab)
Register => signup.html
Add Idea = > create_idea.html
Add Idea Submit Button => ideas.html
Log In => login.html
Log Out => logout.html

All navigation links worked as expected

### Footer

All the font awesome icons in the footer opened to their respective websites, in a new window, as expected.

### Sign Up Page

Testing was taken out to ensure a user could sign up to the website.
Steps:
- Navigate to [Kidsbored](https://kids-bored.herokuapp.com/)
- Navigate to the Register page
- Enter User Name and Password, email is optional
- Click Sign Up

Expected outcome: User is redirected to the home page.  The Navbar changed to show the create Idea potion and log out option.
Actual outcome: User is redirected to the home page.  The Navbar changed to show the create Idea potion and log out option.

### Log out Page

Testing was taken out to ensure a user could log out of the website.
Steps:
- Navigate to Log Out page
- Click Confirm button

Expected outcome: User is taken back to the homepage with the Create Idea option hidden and the Register option showing.
Actual outcome: User is taken back to the homepage with the Create Idea option hidden and the Register option showing.

### Log in

Testing was taken out to ensure a user could log in to the website.
Steps:
- Navigate to [Kidsbored](https://kids-bored.herokuapp.com/)
- Navigate to Log In page
- Enter User Name and Password
- Click Sign in

Expected outcome: User is redirected to the home page.  The Navbar changes to show the create idea option and log out options. A message appears to say they have successfully logged in.
Actual outcome: User is redirected to the home page.  The Navbar changed to show the create Idea potion and log out option. A message appears to say they have successfully logged in.

### Create Idea Page

Testing was taken out to ensure the user could create a new idea.

Assuming user is already logged in
Steps:
- Navigate to Add Idea page
- Complete form
  - Activity Name
  - Upload Image (optional)
  - Activity Location
  - Age Range
  - Price
  - Activity Website(optional)
  - Review (optional)
- Click Submit

  Expected Outcome if all fields are filled in correctly the user will be redirected to the Brows Ideas page where they can view their idea.  A message appears to say they have successfully created their idea.

  Expected outcome if the fields are not filled in correctly: A nocies to complete the field appears and the cursor goes to the field that needs to be completed.

  Both of these outcomes happened correctly when tested.

### Edit Idea

Tested to ensure the user could edit their idea.

Assuming the user is logged in
Steps:
- Navigate to the browse ideas page
- Click on the Activity Name
- If the user is the Author of the activity, they will see a delete button and an Edit button under the Activity Name
- Click the edit button
- Update the fields you wish to update
- Click Submit

Expected outcome:  The user will be redirected back to the browse ideas page which will show the new information, and a message appears to say they have succesfully updated their idea.

The outcome was as expected.

### Delete a post

Tested to ensure a user could delete their idea.

Assuming the user is logged in
Steps:
- Navigate to the browse ideas page
- Click on the Activity Name
- If the user is the Author of the activity, they will see a delete button and an Edit button under the Activity Name
- Click the delete button
- User is taken to a Delete confirmation page asking them if their wish to delete that idea showing the activity name.
- Click Submit

Expected outcome:  The user will be redirected back to the browse ideas page and the idea along with the comments will be deleted.

The outcome was as expected.

### Comment on a post

First I checked the comment section when the user is Logged out.
As expected there is no option to enter a comment at all.  You can view other people’s comments but the box to write your own comment is hidden.

If the user is logged in:
Steps
- Navigate to Browse Ideas
- Click on the activity name
- scroll down to the comments section.
- Write your comment in the comments box
- Click submit

Expected outcome: The comment will appear in the comment section to the left of the comment box.

The outcome was as expected.

### User test

I asked my brother to use the site, upload an idea and give me feedback.  He found the site easy to use but found a problem, when he uploaded his picture it cut his daughters head off.  She was most upset about this.  This highlighted a bug which I have written about in the bug section.

## Accessibility

I used the [Wave Accessibility](https://wave.webaim.org/)tool to check for aid accessibility testing.

All pages came up with zero errors.

They are showing Alerts that show redundant links, on the home page the site logo and the home link on the nav bar are the same.

I have chosen to leave these links as they are because I think they make navigation around the site better.

## Validator Testing

All pages were run through the [w3 HTML validator](https://validator.w3.org/).  Initially, there were some errors, for example there were some missing closing tags and a <p> tag that was used incorrectly inside a <span>.  

All issues were fixed and all pages ran through the checker with no errors.

Due to the use of django language within the HTML files to complete this check I had to retrieve the html code from the open web page and right-click to view the source code.  I could then copy and paste this into the validator.

![w3 HTML Validator](/static/images/html-check.png)

## PP8 Validator

All pages were run through the [PEP8 Validator  ](http://pep8online.com/).  There were some errors, for example, lines to long and whitespace. All issues were corrected and all pages apart from the settings.py page have passed.  The settings file contains code that is not mine so I did not change it.

![PEP8 Validator](/static/images/pep8.png)

I didn't use any javascript in my project so there was nothing to test here.

## Lighthouse Report

The lighthouse report initially showed a low score on performance.  I compressed my hero image which fixed the problem.  

![Lighthouse](/static/images/lighthouse.png)

# Responsiveness

I checked the website for responsiveness on all devices from 320px and up.  I checked on Chrome, Edge, Firefox and Opera browers.

I did this by using developer tools and resising the website to down to 320px.

As expected there were no responsiveness issues.

# Bugs

- I initially had a bug in the URLs that was confusing the browse ideas page with the idea detail page and causing an error.  I solved this by adding post/ to the front of the url.
>path('post/<slug:pk>/<str:activity_name>/', views.IdeaDetail.as_view(

- I had a bug that stopped the images being uploaded from the front end.  They could be uploaded from admin.
After a lot of investigation, I finally worked out that I needed to add the encoding type to the form for it to recognise the image.
>enctype="multipart/form-data"

- There was a bug that stopped the nav bar working when it collapsed down to a button on smaller screens.  The issue was the bootstap link was slightly wrong.  Once corrected the bug was solved.

- I had arranged the image size to all be the same size so that the cards are a uniform height.  I had ‘cover’ on this but this option was cutting the top of the picture off.  To solve this I have changed the css to ‘contain’.  This does not entirely fix the problem because it would be nice to have the pictuers all the same size. In a future development, I would like to add a function for the user to be able to pick the area of the picture they want to upload.

# Deployment

To deploy my site to Heroku I followed the following steps

- Navigate to heroku and create/log into account
- Click the new button in the top right corner
- Select create new app
- Enter app name (kids-bored)
- Select region and click create app (europe)
- Click the resources tab and search for Heroku Postgres
- Select hobby dev and continue
- Go to the settings tab and then click reveal config vars
- Add the following config vars:
  - SECRET_KEY: (Your secret key)
  - DATABASE_URL: (This should already exist with add on of postgres)
  - EMAIL_HOST_USER: (email address)
  - EMAIL_HOST_PASS: (email app password)
  - CLOUNDINARY_URL: (cloudinary api url)
- Click the deploy tab
- Scroll down to Connect to GitHub and sign in / authorize when prompted
- In the search box, find the repository you want to deploy and click connect
- Scroll down to Manual deploy and choose the main branch
- Click Deploy

The app should now be deployed

# References
- I used a couple of other peoples projects to reference kanbans and ideas on what code I could google.
  - https://github.com/Gareth-McGirr/Portfolio-Project-4-SizzleAndSteak
  - https://github.com/MattBCoding/pp4-the-pantry
- I also followed the Code Institute Blog walkthrough to start my project off.
- I used the django documentation 
- I used the summernote documentation
- I used the bootstrap documentation

# Acknowledgements


