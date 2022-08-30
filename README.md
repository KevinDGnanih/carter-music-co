# Carter Music & Co.

Link to [Deployed Site](https://carter-music-co.herokuapp.com//)

[Carter Music & Co.](https://carter-music-co.herokuapp.com/) is an online music shop, which offers great instruments for any budgets.
So that the customers can enjoy their favourite instruments without breaking their bank account.
The shop allows customer to leave a comment to any instrument.

<div align="center"><img src = "#" width=900></div>

This image is created with [ami.responsivedesign](http://ami.responsivedesign.is/).

## Table of Contents

1. [UX](#ux)
    - [Project Goals](#project-goals)
    - [User Stories](#user-stories)
    - [Design](#design)

2. [Features](#features)
    - [Existing Features](#existing-features)
        - [Landing Page](#landing-page)
        - [Product Page](#product-page)
        - [Cart Page](#bag-page)
        - [Checkout Page](#checkout-page)
        - [Profiles Page](#profiles-page)
        - [Admin Product Managment](#admin-product-managment)
        - [Django allauth features](#django-allauth-features)
    - [Features Left to Implement](#features-left-to-implement)
    - [Defensive Design](#defensive-design)

3. [Information Architecture](#information-architecture)
    - [Database Choice](#database-choice)
    - [Data Modeling](#data-modeling)

4. [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Libraries and Packages](#libraries-and-packages)
    - [Tools](#tools)
    - [Databases](#databases)

5. [Testing](#testing)

6. [Deployment](#deployment)
    - [Heroku Deployment with Cloudinary](#heroku-deployment-with-aws)
    - [Local Deployment](#local-deployment)

7. [Credits](#credits)

8. [Disclaimer](#disclaimer)

# UX
## Project Goals
### Target Audience
- People / Proffesionals who are looking to buy instruments / music equipment
- People who love intruments / music equipment
- People who want to try to learn an instrument

### Visitor / User Goals
- Purchase products in a smooth and secure way
- Get informed with the products before buying by product reviews / product information
- Gain interesting knowledge about the gear from instrument selected page and leave a comment

### Business Goals (Site Owner's Goals)
- Provide customers with a secure and safe ecommerce shop
- Establish the shop's brand image
- Expand their business effectively
- Make profit from selling products / services

<div><a href="#table-of-contents">Back to top</a></div>

## User Stories

- Viewing and Navigation

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User/ Shopper | I can view a list of products, so that I can select some to purchase |
| Shopper | I can view individual product details, so that I can identify the price, description, product rating, product images and available sizes. | 
| Shopper | I can quickly identify deals, clearance items and special offers, so that I can take advantage of special savings on products I'd like to purchase. |
| Shopper | Have a shopping bag icon on nav bar | Always check the current order and checkout when I want |

<br/>

- Registration, User Accounts and User Community

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Site User | Easily register for an account | Have a personal account where I can edit my information |  
| Site User | View my order history | Purchase the same product again in the next order |
| Site User | Easily recover my password in case I forget it | Recover access to my account |
| Site User | Receive an email confirmation after registering | Verify that my account registration was successful |
| Site Owner | Let the site users log in when they leave reviews |

<br/>

- Online shopping

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Shopper | Search a product with keywords | Find the most appropriate products |
| Shopper | View individual product pages that have prices, descriptions, etc | Get detailed information about the product before purchasing |
| Shopper | Filter by a specific category | Easily find products in a specific category |
| Shopper/Site Owner | Leave/View product reviews with scores | Understand which products are popular with other customers |
| Site Owner | Easily add a new product | Make sure the online site has the latest catalogue |

<br/>

- Bag, Purchasing and Checkout

| AS A/AN     | I WANT TO BE ABLE TO ... | SO THAT I CAN... |
| ----------- | ----------- | ----------- |
| Shopper | Easily select the quantity and the color (if applicable) of a product after adding a product to a bag | Ensure I don't accidentally select the wrong product and the quantity | 
| Shopper | The delivery information is prefilled if logged in | Smoothly proceed with my purchase | 
| Shopper | Automatically suggest to log in if I did not log in | Smoothly proceed with my purchase | 

<br/>

<div><a href="#table-of-contents">Back to top</a></div>

## Design
### Wireframes
Wireframes were created by hands.
You can find the wireframes [here](#).

### Brand Identity
- Vision: Simple design to shocase the intruments with ease.
- Mission: Provide a wide range of music gear that suit special anyone which can be purchased with one click online. without the hassle of going to a physical shops.
- Values: Happiness - Improve your happiness with the power of music!

### Brand Logo
Logo design is the cornerstone in your brand identity and presents a company's name, product and brand. I used [Affinity Photo](https://affinity.serif.com/en-gb/photo/?trial&mc=AFFPPC01&gclid=CjwKCAjwx7GYBhB7EiwA0d8oe-kgVX1F7VU0CM0nqeyFV_FV5Ubl5KroxO8iUyloQOa2VovEBqekGBoCNYgQAvD_BwE) to create the brand logo file. The font represents the brand value `Arial`.
<p align="center"><img src = ""></p>

<div "text-align: right;"><a href="#table-of-contents">Back to top</a></div>

# Features

## Existing Features
This website is composed of 5 applications: `home`, `bag`, `checkout`, `products`, `profiles`.

## Landing Page
Landing Page is designed as a single page website to provide site visitors with enough information so they can understand what the business is about of this site. This page has minimal amount of information to let the site visitors take next actions.

### Navbar
Navbar is fixed at the top of pages across the site, so that the site visitors easily navigate the whole site.  Navbar contains  `Brand Logo`, `Search Box`, `My Account dropdown`, `Bag icon` and `Site Menu` below.
- Search box: This search box function allows the visitors to search the products on online shop with keywords. The keywords are searched over `name` and `description` field of Product Model. (Details of these models will be described at the [Information Architecture](#information-architecture)) 
- Site Menu & My Account dropdown: The site menu collapses to toggle icon less than 992px width. My Account dropdown is included to toggle menu for smaller screen.
- Bag icon: The number next to the Bag icon shows the total of items added to the bag.

Navbar for larger screensizes (width > 992px)
<div align="center"><img src = "#" width=900></div>

Navbar for smaller screensizes (width < 992px)
<div align="center"><img src = "#" width=900></div>

### Footer
The footer section consists of two sections: 1. General information of the Shop and Quick Link, 2. newsletter subscription form.
1. General Info and Quick Links: The first footer section includes the shop address and its quick links to the pages within the site.
<div align="center"><img src = "#" width=700></div>

2. Social media icons: In this milestone project, Social Media icon is linked to my bussiness page on social media, for social media marketing purposes.
<div align="center"><img src = "#" width=700></div>

<div><a href="#table-of-contents">Back to top</a></div>

## Product Page
### Any categories
By clicking 'Electric, or Bass etc' on the site menu, you can go to the product page. This page is filtered with 'all categories' category as a default as the shop owner wants to promote products that suits anyone. However, the site visitor can adjust the filter condition very easily.  
There is a category selection bar, and you can filter products with `electric`, `drums`, etc`.
<div align="center"><img src = "#" width=250></div>

- Result Number: It's shown above the product cards. Customers can see how many results were found in total at a glance.
<div align="center"><img src = "#" width=350></div>

- Product Card: The products are displayed in cards that have `Product Name`, `Price`, `Category`, `Brand name` and `Rating`. 
If the user is logged in as a superuser, Edit / Delete option is also shown on each card.

Product Card
<div align="center"><img src = "#" width=500></div>

- Pagination Bar: At the bottom of this online shop page, I've set a pagination bar for easy navigation when there are many results to show. Setting up a pagination bar and limiting the number of the products reduce the loading time and make the site look more organized, which is crucial for a site like which offers many products for sale.

### Product Detail Page
- Product Information: On the right side of the product detail page, there is a `Product Name`, `Price`, `Category`, `Rate`, `Description`, `Quantity`, `Color` option, `Add to bag` button. `Color` option is only visible when the product has the options. Also for superuser, Edit / Delete option will be shown.
- Product Testimony Section: Customers can see the product scores and review messages by other customers.

<div align="center"><img src = "" width=700></div>

## Bag Page
- The left side of this bag page shows the products added to the bag. Customers are able to change the quantity or remove the products in this bag page.
- On the right side of this bag page, there is an Order Summary section that shows `Bag Total`, `Delivery` and `Grand Total`. This way, customers are able to check the order summary at first glance even if they have added a lot of products to the shopping bag.

<div align="center"><img src = "#" width=700></div>

## Checkout Page
### Checkout Page
- On the checkout page, customers are asked to fill in delivery details. The customer can also select if they want gift wrapping for the product or not. At the moment, this shop does not collect user's billing information within the User Profile model or Order model.(However, the billing data is recorded in Stripe from the billing information added by the customer.) One of the features left to implement is to add the billing details on the Checkout page.
- Though the customer can complete the checkout process without having an account, if the customer hasn't logged in, the message "Create an account or login to save this information" is shown at the checkout page.

### Checkout Success Page
- A thank you message will be displayed after the checkout process as well as the table that holds the order details.
- `Keep Shopping` button is placed at the end of the page, and if the customer has been logged into their account, `Back to Profile` will be shown.

<div><a href="#">Back to top</a></div>

### Add/Edit Product
- If user is logged in as superuser, they can access to Add / Edit Blog post page.

## Profiles Page
`My Profile` page is available for authenticated users and will be shown in the `My Account` Dropdown menu at the navbar which appears when you log into your account.
### My Profile Page
- In Profile Page, authenticated users can 1. edit `Delivery Information` and 2. see `Order History`.

## Admin Product Managment
Only authenticated superusers can access the admin page (1.products/add/, 2. products/edit/, 3. products/delete/, 4. 5. 6. ). If non-logged in users try to access the url directly, it will redirect to the sign in page. If a non-superuser tries to access the url, an error message pops up which says that only a superuser can access this page.

## Django-allauth features
Base template for allauth has `Back to Home` button at the end of the page, for easy navigation for users.
- Sign Up: The users will be asked to fill out `E-mail`, `User Name` and `Password` to create an account. When the sign up form is submitted, a verification email will be sent to the user's email address to complete the sign up process.
- Log In: Users will be asked to input `User Name` or `Email`, and `Password` to login. If the user successfully logged in, a success message will pop up and redirect to the landing page.
- Log out: Log out page is accessible from the site menu. After the user successfully signed out button on the sign out page, a success message will appear and redirect to the landing page.
- Forgot password: Forgot password page is accessible from Sign In page. Users will be asked to put in an email address which they have used for their registration to the site. An email with a link to reset the password will be sent after submitting the form.

<div><a href="#table-of-contents">Back to top</a></div>

## Features Left to Implement
There are some of features left to implement in the future which I could not add to the project this time due to time constraints. These features are great to be added for a more complete online shop service which would lead to higher customer satisfaction.

## Issues known
Remove button in the bag doesn't work properly.

### 1. Limit the user who can leave product review
At the moment, all the authenticated users can leave reviews to any products if they are logged in. It should be limited to those who actually purchased the product for the validity of the reviews.

### 2. Custumer could rate any item
Let the customer that have an account could rate from 1 to 5.

### 3. Social Account Login
This function allows users to sign up / log into their account of the site, using an existing third party account such as Google and Facebook. This is beneficial to users and the site owners. For users, it's hassle free for remembering a password for the site and it gives the users a smooth registration process. For the site owners, there are many benefits gained by social login - such as increasing user sign ups, reducing bounce rate and gaining a user's social account details which is beneficial for marketing purpose.

### 4. Social Media Share Icons
For social media marketing purpose, adding a social media icon with a link to share products and blog posts would be effective.

### 5. Order Tracking System
To keep the customers informed with the status of their purchase, it would be nice if the site provides the order status such as shipment information in order history and email notifications.


## Defensive Design
### Error views (404)
If 404 error occured within the site, a page that has the message of the error. The templates of 404.html added. [the root template directory](https://docs.djangoproject.com/en/3.1/ref/views/))

### Form Validation
- Django Form Validation

<div><a href="#table-of-contents">Back to top</a></div>

# Information Architecture
## Database choice
- Development phase
**SQLight** database was used for the development which is installed with Django. 

- Deployment phase
**PostgreSQL** was used on deployment stage, which is provided as add-on by Heroku application.

- User model is provided as a default by [Django's authentication system](https://docs.djangoproject.com/en/3.1/ref/contrib/auth/).

## Data Modeling
Following is Entity Relationship Diagram of this project. I created this diagram with [dbdiagram.io](https://dbdiagram.io/home).
When I designed this ERD, I referred to [this article](https://launchschool.com/books/sql/read/table_relationships). 
<p align="center"><img src = "#" width=900></p>

### Product App
A instrument could have several types of colors. And have target `category` and `brand`

### Checkout App
`Chekcout` model collects the delivery information, stripe_pid and order information. All the fields except `user_profile` field have `null=false`. The reason why `user_profile` does not have `null=false` is that guest customers (not authenticated users) can also purchase products and complete the checkout process without creating an account. `Order` model is connected to `OrderLineItem` model which collects information of purchased products.

### Profile App
`Profile` is used for my profile page where the authenticated users can see their delivery details and their order history.

<div><a href="#table-of-contents">Back to top</a></div>

# Technologies Used
The main frontend development was created using HTML, CSS, JavaScript and their libraries. The main backend development was powered by Python and Django.

## Languages
- HTML, CSS, JavaScript, Python

## Libraries and Packages
- [Django](https://www.djangoproject.com/)
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [Bootstrap (v4.4.1)](https://www.bootstrapcdn.com/)
- [JQuery](https://jquery.com/)
- [JQuery-UI](https://jqueryui.com/)
- [Font Awesome](https://fontawesome.com/)
- [Stripe](https://stripe.com/ie)
- [Google Fonts](https://fonts.google.com/)
- [Cloudinary](https://www.cloudinary.com/)
)

## Tools
- Git/GitHub
- Gitpod
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/)

## Databases
- [SQlite3](https://www.sqlite.org/index.html)- database used for development.
- [PostgreSQL](https://www.postgresql.org/) - database used for production.

<div><a href="#table-of-contents">Back to top</a></div>

# Deployment
## Heroku Deployment with AWS
This website is deployed on [Heroku](https://www.heroku.com/), following these steps:
1. Install these packages to your local environment, since these packages are required to deploy a Django project on Heroku.
- [gnicorn](https://gunicorn.org/): `gnicorn` is Python WSGI(web server gataway interface) server for UNIX.
- [gninx](https://www.nginx.com/): `gninx` is a free, open-source, high-performance HTTP server and reverse proxy, as well as an IMAP/POP3 proxy server.
- [psycopg2-binary](https://pypi.org/project/psycopg2-binary/): `psycopg2-binary` is PostgreSQL database adapter for the Python programming language.
- [dj-database-url](https://pypi.org/project/dj-database-url/): `dj-database-url` allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.
2. Create a `requirements.txt` file and freeze all the modules with the command `pip3 freeze > requirements.txt` in the terminal.
3. Create a `Procfile` write `web: gunicorn boutique_ado.wsgi:application` in the file.
4. `git add` and `git commit` and `git push` all the changes to the Github repositoty of this project.
5. Go to Heroku and create a **new app**. Set a name for this app and select the closest region (Europe) and click **Create app**.
6. Go to **Resources** tab in Heroku, then in the **Add-ons** search bar look for **Heorku Postgres**(you can type postgres), select **Hobby Dev — Free** and click **Submit Order Form** button to add it to your project.
7. In the heroku dashboard for the application, click on **Setting** > **Reveal Config Vars** and set the values as follows:

| Key | Value |
| ----------- | ----------- |
| CLOUDINARY_URL | `Your cloudinary cloud storage` |
| DATABASE_URL | `Your Postgres Database URL` |
| EMAIL_HOST_PASS | `Your Email Password (generated by Gmail)` |
| EMAIL_HOST_USER | `Your Email Address` |
| SECRET_KEY | `Your Secret Key` |
| STRIPE_PUBLIC_KEY | `Your Stripe Public Key` |
| STRIPE_SECRET_KEY | `Your Stripe Secret Key` | 
| STRIPE_WH_SECRET | `Your Stripe WH Key` |

8. Comment out the current database setting in settings.py, and add the code below instead. This is done temporarily to migrate the datbase on Heroku.
```
  DATABASES = {     
        'default': dj_database_url.parse("<your Postrgres database URL here>")     
    }
```
9. Migrate the database models to the Postgres database using the following commands in the terminal:
`python3 manage.py migrate`

10. Create a superuser for the Postgres database by running the following command:
`python3 manage.py createsuperuser`
11. Replace the database setting with the code below, so that the right database is used depending on development/deployed environment.
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```
12. Disable collect static, so that Heroku won't try to collect static file with: `heroku config:set DISABLE_COLLECTSTATIC=1`
13. Add `'carter-music-co.herokuapp.com', 'localhost', '127.0.0.1'` to `ALLOWED_HOSTS` in settings.py.
```
ALLOWED_HOSTS = ['flowerydays.herokuapp.com', 'localhost', '127.0.0.1']
```
14. In Stripe, add Heroku app URL a new webhook endpoint.
15. Update the settings.py with the new Stripe environment variables and email settings.
16. Commit all the changes to Heroku. Medial files are not connected to the app yet but the app should be working on Heroku.
17. Delete DISABLE_COLLECTSTATIC from Heroku Config Var.
18. Push all the changes to Github/Heroku and all the static files will be uploaded to S3 bucket.
By setting up above, Heroku will run python3 manage.py collectstatic during the build process and look for static and media files.

### Automatic Deploy on Heroku
You can enable automatic deploy in the following steps that pushes update to Heroku everytime you push to github.
1. Go to Deploy in Heroku dashboard.
2. At `Automatic deploys`, choose a github repository you want to deploy.
3. Click `Enable Automatic Deploys`.


## Local Deployment
For local deployment, you need to have an IDE (I used Gitpod for this project) and you need to install the following:
- Git, Python3, PIP3
Also, you need to create account in the following services if you don't own yet:
- Stripe, Gmail

1. In the IDE you are using, copy and paste the following commane into the terminal to clone this repository.
    `git clone https://github.com/KevinDGnanih/carter-music-co`
(the other ways to clone a repository are written in this [GitHub documentation](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository))
2. Set up environment variable in your selected IDE, or you can create `.env` file in your root directory and add `.env` to `.gitignore` file, and add the followings to the `.env` file.
```
import os  
os.environ["DEVELOPMENT"] = "True"    
os.environ["SECRET_KEY"] = "<Your Secret Key>"
os.environ["STRIPE_PUBLIC_KEY"] = "<Your Stripe Public Key>"    
os.environ["STRIPE_SECRET_KEY"] = "<Your Stripe Secret Key>"    
os.environ["STRIPE_WH_SECRET"] = "<Your Stripe WH Secret Key>"    
```
3. Install all the required packages with `pip3 install -r requirements.txt`
4. Migrate the models to crete a database using in your IDE with `python3 manage.py makemigrations` and `python3 manage.py migrate`

Create a superuser for the Postgres database by running with `python3 manage.py createsuperuser`
Now you can access the app using the command `python3 manage.py runserver`

<div><a href="#table-of-contents">Back to top</a></div>

# Credits

### Content & Code
- I constantly read [Django](https://docs.djangoproject.com/en/3.1/), [Stripe](https://stripe.com/docs) and [Python](https://docs.python.org/3/) documenation and tutorial throughout the development.
- For `Blog` app, I referred to [this tutorial](https://djangocentral.com/building-a-blog-application-with-django/).
- I refered to [this code snippet](https://bootsnipp.com/snippets/k2RdV) for the Testinonial section on the landing page.
- For search product function, I refered to several articles and video. [Stack Overflow 1](https://stackoverflow.com/questions/3171717/django-search-for-strings-containing-spaces), [Stack Overflow 2](https://stackoverflow.com/questions/34831511/django-prefetch-related-failing-to-pass-data-to-template), [Stack Overflow 3](https://stackoverflow.com/questions/3171717/django-search-for-strings-containing-spaces), [Combine 2 Django Querysets from Different Models](https://chriskief.com/2015/01/12/combine-2-django-querysets-from-different-models/), [Django Queryset:value_list() flat=True](https://amittbhardwj.wordpress.com/2015/10/27/django-querysetvalue_list/).
- For the hover show button on the product card, I refered to this [code snippet](https://codepen.io/philcheng/pen/YWyYwG).
- For multiselect dropdown menu which is used for the product filter function, I referred to these article: [Stack Overflow 1](https://stackoverflow.com/questions/50895806/bootstrap-4-multiselect-dropdown/50897096), [bootstrap-select](https://developer.snapappointments.com/bootstrap-select/).
- For creating custome template tags used in `Product` apps, I refered to The code Institute Botiq Ado project.
- This project was developed refering to the Boutique Ado Django mini-project from Code Institute course materials. The codes are customized and modified to fit the purpose of this milestone project.

### Images & Media
- All the icons in this website were provided by [Font Awesome](https://fontawesome.com/).

### Acknowledgements
- Thanks to: my Code Institute Mentor Guido Cecilio Garcia Bernal for his advice throughout the development process.
- Code Institute Slack Community that gave me a light when I was stuck in my coding.

### Disclaimer
This website is created for educational purpose only.