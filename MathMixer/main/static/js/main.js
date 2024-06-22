// Добавляем обработчики событий для кнопок выпадающего списка с тренажерами
document.addEventListener('DOMContentLoaded', function() {
    var dropdown = document.querySelectorAll('.dropdown-btn');
    dropdown.forEach(function(btn) {
        btn.addEventListener('click', function() {
            var dropdownContainer = this.nextElementSibling;
            dropdownContainer.classList.toggle('show');
        });
    });
});