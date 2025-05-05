
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.querySelector('[data-js-header-input]');
    const searchResults = document.getElementById('search-results');
    const searchForm = document.querySelector('[data-js-header-form]');
    let searchTimeout;

    // Обработчик ввода в поисковую строку
    searchInput.addEventListener('input', function() {
        clearTimeout(searchTimeout);
        const query = this.value.trim();

        if (query.length < 2) {
            searchResults.innerHTML = '';
            searchResults.style.display = 'none';
            return;
        }

        searchTimeout = setTimeout(() => {
            fetch(`/goods/api/search/?q=${encodeURIComponent(query)}`)
                .then(response => response.json())
                .then(data => {
                    if (data.results.length > 0) {
                        searchResults.innerHTML = data.results.map(product => `
                            <div class="search-result-item">
                                <a href="${product.url}">
                                    <div class="product-info">
                                        <h4>${product.name}</h4>
                                        <div class="product-category">${product.category}</div>
                                    </div>
                                </a>
                            </div>
                        `).join('');
                        searchResults.style.display = 'block';
                    } else {
                        searchResults.innerHTML = '<div class="no-results">Товары не найдены</div>';
                        searchResults.style.display = 'block';
                    }
                })
                .catch(error => {
                    console.error('Ошибка поиска:', error);
                });
        }, 0);
    });

    // Обработчик отправки формы (полноценный поиск)
    searchForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const query = searchInput.value.trim();
        if (query) {
            window.location.href = `/goods/list/?q=${encodeURIComponent(query)}`;
        }
    });

    // Скрываем результаты при клике вне поля поиска
    document.addEventListener('click', function(e) {
        if (!searchInput.contains(e.target) && !searchResults.contains(e.target)) {
            searchResults.style.display = 'none';
        }
    });
});
