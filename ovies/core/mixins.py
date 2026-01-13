from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin


class OwnerRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Миксин для проверки, что пользователь - владелец объекта
    """
    permission_denied_message = "У вас нет прав для редактирования этого объекта."

    def test_func(self):
        obj = self.get_object()
        return obj.added_by == self.request.user or self.request.user.is_staff


class SuccessMessageMixinWithRedirect(SuccessMessageMixin):
    """
    Миксин с сообщением об успехе
    """
    success_message = "Операция выполнена успешно."