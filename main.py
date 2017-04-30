# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import webapp2
import jinja2

from google.appengine.api import users
from google.appengine.ext.webapp import template

JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)


class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        params = {'user': user}
        if user:
            params['user_url'] = users.create_logout_url(self.request.uri)
        else:
            params['user_url'] = users.create_login_url(self.request.uri)

        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render(params))

class AboutPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        params = {'user': user}
        if user:
            params['user_url'] = users.create_logout_url(self.request.uri)
        else:
            params['user_url'] = users.create_login_url(self.request.uri)

        template = JINJA_ENVIRONMENT.get_template('templates/about.html')
        self.response.write(template.render(params))


app = webapp2.WSGIApplication([
    ('/about', AboutPage),
    ('/', MainPage)
], debug=True)

