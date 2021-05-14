# Internship Assignment (Python/Django)

### steps to follow to run this project

* create virtual envirorment

* pip install -r requirements.txt

* python manage.py runserver


---

### endpoints of the app

1. **create user** :
        *  http://127.0.0.1:8000/users/
        * _request_ :{ "email":"mailaddress@.com",
            "Name":"name of the user",
    

            "password":"password",
            "re_password":"re_password"


         }
         
2. **user activatiom** :
        *_endpoint_: http://127.0.0.1:8000/users/activation/
        *_request_ : {
            "uid":"uid",
            "token":"---token------"
            }
        **after registertion mail will be sended**
        
3. **user login** :
        * _endpoint_: http://127.0.0.1:8000/jwt/create/
        * _request_ : {
            "email":"kc5082s975@gmail.com",
            "password":"123456789kc"
        }
        * _response_ : auth_token
        
        
4. **advisor create** :
        **must be login**
          - to login place the auth token in header files 

        * _endpoint_: http://127.0.0.1:8000/admin/advisor/
        * _request_ : {
            "Advisor_name":"<---name---->",
            "Advisor_Photo_URL":"<----url of profile---->"
        }
        * _response_ : {
            200_OK if the request is successful/
            400_BAD_REQUEST if any of the above fields are missing

        }
        
        
5. **list all advisor** :
        **must be login**
          - to login place the auth token in header files 
        - **method**: get
        * _endpoint_: /user/<user-id>/advisor
        
        * _response_ : {
            200_OK if the request is successful/
            

        }


6. **book call with advisor** :
        **must be login**
          - to login place the auth token in header files 
        - **method**: get
        * _endpoint_: /user/<user-id>/advisor/<advisor-id>/

        * _request_ : {
            "booking_time":"<---booking_time---->",
            
        }
        * _response_ : {
            200_OK if the request is successful
           
        }
        }


7. **list all booked calls** :
        **must be login**
          - to login place the auth token in header files 
        - **method**: get
        * _endpoint_: /user/<user-id>/advisor/booking/<advisor-id>/

        * _request_ : NOne
        * _response_ : {
            200_OK if the request is successful
           
        }


        