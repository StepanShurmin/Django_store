import random

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from users.services import send_new_password
from users.forms import UserRegisterForm, UserForm
from users.models import User


class RegisterView(CreateView):
    """Выводит на экран форму для регистрации нового пользователя."""
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        """Проверяет валидность формы и сохраняет нового пользователя."""
        new_user = form.save(commit=False)
        new_user.verification_token = ''.join([str(random.randint(0, 9)) for _ in range(12)])
        new_user.save()
        send_mail(
            subject='Подтвердите вашу почту',
            message=f'Для подтверждения вашей почты, перейдите по ссылке: '
                    f'{self.request.build_absolute_uri(reverse(viewname="users:verify_email", args=[new_user.verification_token]))}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


def verify_email(request, token):
    """Подтверждает адрес электронной почты пользователя."""
    user = get_object_or_404(User, verification_token=token)
    if not user.email_verified:
        user.email_verified = True
        user.save()

    return render(request, 'users/verification_success.html')


class UserUpdateView(UpdateView):
    """Обновляет информацию о пользователе."""
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm
    template_name = 'users/user_form.html'

    def get_object(self, queryset=None):
        """Возвращает объект пользователя, который будет обновлен."""
        return self.request.user


def generate_new_password(request):
    """Генерирует новый пароль для пользователя, отправляет его по электронной почте и обновляет."""
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    send_new_password(request.user.email, new_password)
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('catalog:home'))
