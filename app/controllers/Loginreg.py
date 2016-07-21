"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Loginreg(Controller):
    def __init__(self, action):
        super(Loginreg, self).__init__(action)
        """
        This is an example of loading a model.
        Every controller has access to the load_model method.
        """
        self.load_model('LoginregModel')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """
        # all_course = self.models['Course'].get_all_courses_m()

        # query = "SELECT * FROM courses"
        # all_courses = self.db.query_db(query)
        # print all_course
        return self.load_view('index.html')

    def add(self):
        # print "REQUEST.FORM IS", request.form
        user_details = request.form
        reg_name = self.models['LoginregModel'].add_one_user_m(user_details)
        message = "registered and logged in!"
        return self.load_view('success.html', s_f_name=reg_name, s_msg=message)

    # def success(self):
    #     if session['reg_id']:
    #         user = self.models['LoginregModel'].success_m(session['reg_id'])
    #         print "XXXXXX", user
    #         user_f_name = user[0]['first_name']
    #         print "User First name is", user_f_name
    #         message = "registered!"
    #         return self.load_view('success.html', s_f_name=user_f_name, s_msg=message)
    #     elif session['login_id']:
    #         user = self.models['LoginregModel'].success_m(session['login_id'])
    #         print "BBBBBBB", user
    #         user_f_name = user[0]['first_name']
    #         print "User First name is", user_f_name
    #         message = "logged in!"
    #         return self.load_view('success.html', s_f_name=user_f_name, s_msg=message)

    def login(self):
        user_details = request.form
        login_user = self.models['LoginregModel'].login_m(user_details)
        if not login_user:
            flash("Wrong Password!",'error')
            return redirect('/')
        else:
            print "AAAAAAAAA", login_user
            session['login_id'] = login_user['id']
            message = "logged in!"
            return self.load_view('success.html', s_f_name=login_user['first_name'], s_msg=message)
    
    def logout(self):
        session.clear()
        return redirect('/')

