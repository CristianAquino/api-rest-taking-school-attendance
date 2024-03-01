from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.errors import HttpError

from core.encrypt import get_jwt_token
from course.models import Course
from .bearer import AuthBearer
from .models import User
from .schemas.payload import PayloadUpdateMyAccount, PayloadPostAddUser, PayloadPostLoginUser
from .schemas.response import ResponseMe, ResponseToken, ResponseUser
from .constants import Endpoints

router = Router()


@router.post(
    Endpoints.POST_LOGIN,
    response=ResponseToken
)
def login_user(request, data: PayloadPostLoginUser):
    """
    Returns the access token if correct credentials
    """
    error_msg = "Your email and/or password are wrong."
    user = get_object_or_404(User, email=data.email)
    if user.check_password(data.password):
        return dict(token=get_jwt_token(user))

    raise HttpError(403, error_msg)


@router.post(
    Endpoints.POST_ADD_USER,
    response={201: ResponseUser},
)
def register_user(request, data: PayloadPostAddUser):
    """
    Registration of a user account.
    """
    user_data = data.dict(
        include={
            'name',
            'first_name',
            'last_name',
            'email',
            'password',
        }
    )
    return User.objects.create_user(**user_data)


@router.get(
    Endpoints.GET_ME,
    auth=AuthBearer(),
    response=ResponseMe,
)
def get_my_account(request):
    """
    Get my user profile.
    """
    id = request.user.id
    courses = Course.objects.filter(teacher_id=id)
    return {'user': request.user, 'course': courses}


@router.put(
    Endpoints.PATCH_MY_ACCOUNT,
    auth=AuthBearer(),
    response={201: ResponseUser},
)
def put_my_account(request, data: PayloadUpdateMyAccount):
    """
    Edit my user account.
    """
    user = request.user
    patch_data = data.dict(exclude_unset=True)

    for key, value in patch_data.items():
        setattr(user, key, value)

    user.save()
    return user
