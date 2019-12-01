# Podcast Time Machine

Podcast time machine allows you to subscribe to a podcast but delay all entries
by a number of days.

## Why?

One of my favourite podcasts (Harmontown) ends. I only started to listen to it
a few years ago. Now I want to re-experience it from the beginning.

## Usage

You can use the builtin webserver or use the `wsgi` interface with nginx.
For a tutorial: https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-16-04


I added this to my nginx config:

```
location /timemachine {
    rewrite /timemachine/(.*) /$1 break;
    include uwsgi_params;
    uwsgi_pass unix:/home/maweki/podcast-timemachine/myproject.sock;
}
```

## Todo
I don't know how to properly do service files and all this stuff. PRs welcome.
