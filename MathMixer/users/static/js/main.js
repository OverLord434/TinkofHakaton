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

//Создание графика статистики с использованием библиотеки Chart.js
const ctx = document.getElementById('accuracyChart').getContext('2d');

function generateLabelsForLastWeek() {
    const labels = [];
    const today = new Date();
    const lastWeek = new Date(today.getFullYear(), today.getMonth(), today.getDate() - 7);
    for (let i = 0; i < 7; i++) {
        const date = new Date(lastWeek);
        date.setDate(lastWeek.getDate() + i);
        const formattedDate = `0${date.getDate()}.0${date.getMonth() + 1}`;
        labels.push(formattedDate);
    }
    return labels;
}

const labelsForLastWeek = generateLabelsForLastWeek();

const accuracyChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: labelsForLastWeek,
        datasets: [{
            label: 'Правильность ответов (%)',
            data: [85, 90, 78, 88, 92, 85, 91],
            borderColor: 'rgba(75, 192, 192, 1)',
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            fill: true,
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true,
                max: 100
            }
        }
    }
});


