from controllers.users_controller import users
from controllers.accounts_controller import auth
from controllers.profile_images_controller import profile_images

registerable_controllers = [
    auth,
    users,
    profile_images

]