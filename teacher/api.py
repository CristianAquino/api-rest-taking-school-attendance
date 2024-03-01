from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.errors import HttpError

from core.encrypt import get_jwt_token
from .bearer import AuthBearer
from .models import User
from .schemas.payload import PayloadUpdateMyAccount, PayloadPostAddUser, PayloadPostLoginUser
from .schemas.response import ResponseToken, ResponseUser
from .constants import Endpoints

router = Router()


@router.post(Endpoints.POST_LOGIN, auth=None, response=ResponseToken)
def login(request, data: PayloadPostLoginUser):
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
    auth=None,
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
    response=ResponseUser,
)
def get_my_account(request):
    """
    Get my user profile.
    """
    return request.user


@router.put(
    Endpoints.PATCH_MY_ACCOUNT,
    auth=AuthBearer(),
    response=ResponseUser,
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
