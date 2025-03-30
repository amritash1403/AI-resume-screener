document.addEventListener("DOMContentLoaded", function () {
    const darkModeToggle = document.getElementById("darkModeToggle");
    const theme = document.getElementById("theme");

    // Load the saved theme from localStorage
    if (localStorage.getItem("darkMode") === "enabled") {
        theme.classList.add("dark-mode");
        darkModeToggle.checked = true;
    }

    // Toggle dark mode on switch click
    darkModeToggle.addEventListener("change", function () {
        if (this.checked) {
            theme.classList.add("dark-mode");
            localStorage.setItem("darkMode", "enabled");
        } else {
            theme.classList.remove("dark-mode");
            localStorage.setItem("darkMode", "disabled");
        }
    });
});
