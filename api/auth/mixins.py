from werkzeug.security import generate_password_hash, check_password_hash
from http import HTTPStatus
from flask_restx import marshal
from .models import User, RoleOptions
from .serializers import register_serializer

class UserCreationMixin(object):

    @classmethod
    def create_user(self, data):
        role_input = data.get('role')
        try:
            role = RoleOptions[role_input]
        except KeyError:
            return {
                "messsage": f"Role input <{role_input}> not in defined roles: {[r.value for r in RoleOptions]} "}, HTTPStatus.BAD_REQUEST

        new_user = User(
                first_name = data.get('first_name'),
                last_name = data.get('last_name'),
                username = data.get('username'),
                email = data.get('email'),
                password = generate_password_hash(data.get('password')),
                role=role
            )
    

        new_user.save()

       
        return marshal(new_user, register_serializer), HTTPStatus.CREATED
    
    def update_user(self, user_instance):
        pass
    
