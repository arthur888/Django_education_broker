from allauth.account.adapter import DefaultAccountAdapter

# class AccountAdapter(DefaultAccountAdapter):
#     def save_user(self, request, user, form, commit=False):
#         data = form.cleaned_data
#         user.username = data['username']
#         user.email = data['email']
#         user.first_name = data['first_name']
#         user.last_name = data['last_name']
#         user.gender = data['gender']
#         user.birth_date = data['birth_date']
#         user.city = data['city']
#         user.country = data['country']
#         if 'password1' in data:
#             user.set_password(data['password1'])
#         else:
#             user.set_unusable_password()
#         self.populate_username(request, user)
#         if commit:
#             user.save()
#         return user

class AccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=False):
        data = form.cleaned_data
        user.email = data.get('email')
        user.username = data.get('username')
        # all your custom fields
        user.date_of_birth = data.get('date_of_birth')
        user.gender = data.get('gender')
        if 'password1' in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            user.save()
        return user