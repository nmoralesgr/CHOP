# CHOP Flask App 

This an group website project created for the FintechFocus Fellowship during Summer of 2022. Introduced me to Python and the Flask framework. 

---

## File Overview

### ← README.md

## Anatomy of the app<a id="anatomy"></a>

Here's everything inside the Flask template. Almost everything else operates more behind the scenes, and can be a later focus. 

<pre>
flaskproject
├── app.py - This is the main file for our app.
├── model.py - This is where we will write the logic of our app.
├── readme.md - That's this file!
├── static - This is where we house assets like images and stylesheets.
│   ├── css - Put stylesheets here.
│   │   └── style.css
│   └── images - Put images here.
│       └── micropig.jpg
└── templates - Put templates (views) in this folder.
    └── index.html - This will be the first template we render.
</pre>


### Files focused on:

#### The `app.py`

This code tells the application how to respond to the requests users make when they visit the main page, main differentiation of this web application from a standard website. 

#### The `model.py`

The `app.py` is really just meant to be air-traffic control for our web application's visitors - the complex logic should live here in `model.py`. 

#### The `templates` folder

Templates can be injected with Python to generate new content. Instead of needing to code out 100 `myaccount` for 100 users, one can code just 1 page, and use template logic to provide each user with a customized experience. 

#### The `static` folder

For images and for CSS, which are two of the most common things encountered in a web application's public folder.
