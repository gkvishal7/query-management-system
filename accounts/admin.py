from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from accounts.models import user

class UserCreationForm(forms.ModelForm):
    username = forms.CharField(label="username")
    email=forms.EmailField(label="Email id",widget=forms.EmailInput)
    password1=forms.CharField(label="Password",widget=forms.PasswordInput)
    password2=forms.CharField(label="Password Again",widget=forms.PasswordInput)

    class Meta():
        model = user
        fields = ('email', 'username','password1','password2')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm,self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserAdmin(admin.ModelAdmin):
    model=user
    list_display = ('username', 'email', 'is_superuser','is_staff')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('username', 'email','password1','password2')}),

        ('Permissions', {'fields': ('is_superuser','is_staff')}),
    )
    form =  UserCreationForm
    search_fields =  ('username', 'email')
    ordering = ('username','email')
    filter_horizontal = ()
admin.site.register(user,UserAdmin)
admin.site.unregister(Group)