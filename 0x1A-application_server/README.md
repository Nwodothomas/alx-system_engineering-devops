0x1A. Application server

# Background Context

Your web infrastructure is already serving web pages via Nginx that you installed in your [ first web stack project.](https://intranet.alxswe.com/projects/266)
While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your Nginx and make is serve your Airbnb clone project.

# Resources

### Read or watch:

- Application server vs web server[D[D[
- [ Application server vs web server ](https://intranet.alxswe.com/rltoken/B9fOBzIxX_t1289WAuRzJw)
- [ How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://intranet.alxswe.com/rltoken/kpG6RwmwRJHzRmGUM_ERcA)
- [ Running Gunicorn ](https://intranet.alxswe.com/rltoken/2LF1j7xKJGYaUtD1HKgUeQ)
- [ Be careful with the way Flask manages slash in route - strict_slashes](https://werkzeug.palletsprojects.com/en/0.14.x/routing/)
- [ Upstart documentation ](https://doc.ubuntu-fr.org/upstart)


# Tasks

### 0. Set up development with Python

Let’s serve what you built for [  AirBnB clone v2 - Web framework ](https://intranet.alxswe.com/projects/290) on web-01. This task is an exercise in setting up your development environment, which is used for testing and debugging your code before deploying it to production.

Requirements:

- Make sure that task #3 of your SSH project is completed for web-01. The checker will connect to your servers.
Git clone your AirBnB_clone_v2 on your web-01 server.
- Configure the file web_flask/0-hello_route.py to serve its content from the route /airbnb-onepage/ on port 5000.
- Your Flask application object must be named app (This will allow us to run and check your code).
