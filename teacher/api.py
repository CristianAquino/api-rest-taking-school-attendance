from ninja import Router
from ninja.errors import HttpError

from core.encrypt import get_jwt_token
from course.models import Course

from .bearer import AuthBearer
from .constants import Endpoints
from .models import User
from .schemas.payload import (PayloadPostAddUser, PayloadPostLoginUser,
                              PayloadUpdateMyAccount)
from .schemas.response import (ResponseMe, ResponseMessage, ResponseToken,
                               ResponseUser)

router = Router()


@router.post(
    Endpoints.POST_LOGIN,
    response=ResponseToken
)
def login_user(request, data: PayloadPostLoginUser):
    """
    Returns the access token if correct credentials
    """
    try:
        error_msg = "Your email and/or password are wrong."
        user = User.objects.get(email=data.email)
        if not user.check_password(data.password):
            raise HttpError(403, error_msg)
        return dict(token=get_jwt_token(user))
    except:
        raise HttpError(403, error_msg)


@router.post(
    Endpoints.POST_ADD_USER,
    response={201: ResponseMessage},
)
def register_user(request, data: PayloadPostAddUser):
    """
    Registration of a user account.
    """
    try:
        user_data = data.dict(
            include={
                'name',
                'first_name',
                'second_name',
                'email',
                'password',
            }
        )
        User.objects.create_user(**user_data)
        return dict(message="Registered teacher account")
    except:
        raise HttpError(403, "Cannot register account")


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
    return {'user': request.user, 'courses': courses}


@router.put(
    Endpoints.PATCH_MY_ACCOUNT,
    auth=AuthBearer(),
    response={201: ResponseMessage},
)
def put_my_account(request, data: PayloadUpdateMyAccount):
    """
    Edit my user account.
    """
    try:
        user = request.user
        patch_data = data.dict(exclude_unset=True)

        for key, value in patch_data.items():
            setattr(user, key, value)

        user.save()
        return dict(message="Updated teacher account")
    except:
        raise HttpError(403, "Cannot updated account")
