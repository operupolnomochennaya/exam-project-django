// Основные JavaScript функции
document.addEventListener('DOMContentLoaded', function() {
    // Автоматическое скрытие сообщений через 5 секунд
    setTimeout(function() {
        const alerts = document.querySelectorAll('.alert');
        alerts.forEach(function(alert) {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);

    // Подтверждение удаления
    const deleteButtons = document.querySelectorAll('.btn-delete');
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            if (!confirm('Вы уверены, что хотите удалить этот элемент?')) {
                e.preventDefault();
            }
        });
    });

    // Рейтинг звездами
    const ratingInputs = document.querySelectorAll('input[name="rating"]');
    ratingInputs.forEach(function(input) {
        input.addEventListener('change', function() {
            const rating = this.value;
            const starsContainer = this.closest('.rating-container');
            if (starsContainer) {
                const stars = starsContainer.querySelectorAll('.rating-star');
                stars.forEach(function(star, index) {
                    if (index < rating) {
                        star.classList.add('text-warning');
                    } else {
                        star.classList.remove('text-warning');
                    }
                });
            }
        });
    });
});