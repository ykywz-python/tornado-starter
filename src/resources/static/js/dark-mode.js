document.addEventListener('DOMContentLoaded', () => {
    const themeToggles = document.querySelectorAll('.theme-toggle');
    // Jika tombol tidak ditemukan, hentikan eksekusi skrip
    if (!themeToggles.length) {
        console.warn('Tombol tidak ditemukan.');
        return;
    }

    const body = document.body;
    const themeStorageKey = 'theme';
    const lightThemeValue = 'light';
    const darkThemeValue = 'dark';
    const lightIcon = '☀️';
    const darkIcon = '🌙';

    /**
     * Menerapkan tema ke body dan memperbarui ikon.
     * @param {string} theme - Tema yang akan diterapkan ('light' atau 'dark').
     */
    const applyTheme = (theme, iconSpan) => {
        
        if (theme === lightThemeValue) {
            body.setAttribute('data-theme', lightThemeValue);
            if (iconSpan) iconSpan.textContent = darkIcon;
        } else {
            body.removeAttribute('data-theme');
            if (iconSpan) iconSpan.textContent = lightIcon;
        }
    };

    // 1. Apply saved theme on page load
    const savedTheme = localStorage.getItem(themeStorageKey) || darkThemeValue; // Default ke dark
    applyTheme(savedTheme);

    // 2. Add event listener for each toggle button
    themeToggles.forEach(themeToggle => {
        themeToggle.addEventListener('click', () => {
            // Check current theme by looking at the data-theme attribute
            const isLight = body.hasAttribute('data-theme');
            const newTheme = isLight ? darkThemeValue : lightThemeValue;
            const iconSpan = themeToggle.querySelector('.icon');

            localStorage.setItem(themeStorageKey, newTheme);
            applyTheme(newTheme, iconSpan);
        });
    });
});
