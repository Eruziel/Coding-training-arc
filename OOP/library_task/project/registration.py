from project.user import User
from project.library import Library


class Registration:
    def add_user(self, user: User, library: Library):
        if user not in library.user_records:
            library.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User, library: Library):
        try:
            removed = next(filter(lambda u: u.username == user.username, library.user_records))
        except StopIteration:
            return "We could not find such user to remove!"



        library.user_records.remove(removed)

    def change_username(self, user_id, new_username, library: Library):

        for user in library.user_records:
            if user.user_id == user_id:
                if user.username != new_username:
                    user.username = new_username
                    try:
                        library.rented_books[new_username] = library.rented_books.pop(user.username)
                    except KeyError:
                        pass
                    return f"Useranme successfully changed to: {new_username} for user id: {user_id}"
                else:
                    return f"Please check again the provided username - it should be different than the username used so far!"

        else:
            return f"There is no user with id = {user_id}!"