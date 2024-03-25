import allure
import pytest

from configtest import (create_and_delete_user, create_user, create_pet_with_status_sold, create_and_delete,
                        created_book)

from pages.api_testing.user.get_user import GetUser
from pages.api_testing.petstore.get_by_status import FindByStatus
from pages.api_testing.petstore.create_pet import CreatePet
from pages.api_testing.petstore.delete_pet import DeletePet
from pages.api_testing.petstore.find_by_id import FindById
from pages.api_testing.user.create_user import CreateUser
from pages.api_testing.user.delete_user import DeleteUser
from pages.api_testing.user.update_user import UpdateUser
from pages.api_testing.user.auth import Auth
from pages.api_testing.booker.create_book import CreateBook
from pages.api_testing.placeholder.get_posts import GetPosts
from pages.api_testing.placeholder.get_comments import GetComments
from pages.api_testing.placeholder.delete_post import DeletePost
from pages.api_testing.placeholder.put_post import Update


@pytest.mark.api_testing
@pytest.mark.petstore
def test_find_by_status_available():
    find_by_status = FindByStatus()

    with allure.step('Get all pets with ID available'):
        find_by_status.get_pets(status='available')

    with allure.step('Compare expected result and actual result'):
        assert find_by_status.is_status(status='available') and find_by_status.is_status_code_200()


@pytest.mark.api_testing
@pytest.mark.petstore
def test_find_by_status_pending():
    find_by_status = FindByStatus()

    with allure.step('Get all pets with ID pending'):
        find_by_status.get_pets(status='pending')

    with allure.step('Compare expected result and actual result'):
        assert find_by_status.is_status(status='pending') and find_by_status.is_status_code_200()


@pytest.mark.api_testing
@pytest.mark.petstore
def test_find_by_status_sold():
    find_by_status = FindByStatus()

    with allure.step('Get all pets with ID sold'):
        find_by_status.get_pets(status='sold')

    with allure.step('Compare expected result and actual result'):
        assert find_by_status.is_status(status='sold') and find_by_status.is_status_code_200()


@pytest.mark.api_testing
@pytest.mark.petstore
def test_create_pet():
    create_pet = CreatePet()

    with allure.step('Create pet'):
        create_pet.create_pet()

    with allure.step('Compare expected result and actual result'):
        assert create_pet.is_status_code_200() and create_pet.check_pet_name()


@pytest.mark.api_testing
@pytest.mark.petstore
def test_delete_pet(create_pet_with_status_sold):
    delete_pet = DeletePet()

    with allure.step('Delete pet'):
        delete_pet.delete_pet()

    with allure.step('Compare expected result and actual result'):
        assert delete_pet.is_status_code_200() and delete_pet.is_id_correct()


@pytest.mark.api_testing
@pytest.mark.petstore
def test_find_by_id(create_and_delete):
    find_by_id = FindById()

    with allure.step('Find pet by id'):
        find_by_id.get_pet_by_id()

    with allure.step('Compare expected result and actual result'):
        assert find_by_id.is_status_code_200() and find_by_id.check_pet_name()


@pytest.mark.api_testing
@pytest.mark.user
def test_create_user():
    create_user = CreateUser()

    with allure.step('Create user'):
        create_user.create_user()

    with allure.step('Compare expected result and actual result'):
        assert create_user.is_status_code_200() and create_user.check_response_status()


@pytest.mark.api_testing
@pytest.mark.user
def test_delete_user(create_user):
    delete_user = DeleteUser()

    with allure.step('Delete suer'):
        delete_user.delete_user()

    with allure.step('Compare expected result and actual result'):
        assert delete_user.is_status_code_200() and delete_user.check_nickname()


@pytest.mark.api_testing
@pytest.mark.user
def test_get_user(create_and_delete_user):
    get_user = GetUser()

    with allure.step('Find user by nickname'):
        get_user.get_user_by_nickname()

    with allure.step('Compare expected result and actual result'):
        assert get_user.is_status_code_200() and get_user.check_nickname()


@pytest.mark.api_testing
@pytest.mark.user
def test_update_user(create_and_delete_user):
    update_user = UpdateUser()

    with allure.step('Update user information'):
        update_user.update_user()

    with allure.step('Get user by nickname'):
        update_user.get_user()

    with allure.step('Compare expected result and actual result'):
        assert update_user.is_status_code_200() and update_user.check_nickname()


@pytest.mark.api_testing
@pytest.mark.user
def test_auth(create_and_delete_user):
    auth = Auth()

    with allure.step('Authorize with an alias and password'):
        auth.auth_user()

    with allure.step('Compare expected result and actual result'):
        assert auth.is_status_code_200() and auth.check_response_status()


@pytest.mark.api_testing
@pytest.mark.booker
def test_get_books_id(created_book):
    create_book = CreateBook()

    with allure.step('Get created book id'):
        create_book.get_created_book_id()

    with allure.step('Get created book'):
        create_book.get_created_book()

    with allure.step('Compare expected result with actual result(by initials)'):
        assert create_book.is_status_code_200() and create_book.check_initials()


@pytest.mark.api_testing
@pytest.mark.booker
def test_filter_by_dates(created_book):
    create_book = CreateBook()

    with allure.step('Get created book id'):
        create_book.get_created_book_id()

    with allure.step('Get created book'):
        create_book.get_created_book()

    with allure.step('Compare expected result with actual result(by dates)'):
        assert create_book.is_status_code_200() and create_book.check_dates()


@pytest.mark.api_testing
@pytest.mark.placeholder
def test_comments_from_first_post():
    get_comments = GetComments()

    with allure.step('Find comments from post'):
        get_comments.get_comments()

    with allure.step('Compare expected result and actual result'):
        assert get_comments.is_status_code_200() and get_comments.check_comments()


@pytest.mark.api_testing
@pytest.mark.placeholder
def test_delete_post():
    delete_post = DeletePost()

    with allure.step('Get first post'):
        delete_post.get_first_post()

    with allure.step('Delete first post'):
        delete_post.delete_post()

    with allure.step('Compare expected result and actual result'):
        assert delete_post.compare_posts()


@pytest.mark.api_testing
@pytest.mark.placeholder
def test_put_post():
    put_post = Update()

    with allure.step('Update post by PUT method'):
        put_post.put_post()

    with allure.step('Compare expected result and actual result'):
        assert put_post.is_status_code_200() and put_post.compate_titles()


@pytest.mark.api_testing
@pytest.mark.placeholder
def test_patch_post():
    put_post = Update()

    with allure.step('Update post by PATCH method'):
        put_post.patch_post()

    with allure.step('Compare expected result and actual result'):
        assert put_post.is_status_code_200() and put_post.compare_user_id()


@pytest.mark.api_testing
@pytest.mark.placeholder
def test_posts():
    get_posts = GetPosts()

    with allure.step('Get posts'):
        get_posts.get_posts()

    with allure.step('Compare expected result and actual result'):
        assert get_posts.is_status_code_200() and get_posts.check_posts()
