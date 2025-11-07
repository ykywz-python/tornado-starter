document.addEventListener('DOMContentLoaded', () => {
    const sidebar = document.getElementById("sidebar");
    const overlay = document.getElementById("sidebar-overlay");
    
    // Selector untuk semua elemen yang memicu aksi
    const openTriggers = document.querySelectorAll('[data-action="open"]');
    const closeTriggers = document.querySelectorAll('[data-action="close"]');

    /**
     * Membuka Offcanvas Sidebar (hanya di mobile).
     */
    function openNav() {
        if (window.innerWidth < 768) {
            sidebar.classList.add('open');
            overlay.classList.add('open');
            document.body.classList.add('body-no-scroll');
        }
    }

    /**
     * Menutup Offcanvas Sidebar.
     */
    function closeNav() {
        sidebar.classList.remove('open');
        overlay.classList.remove('open');
        document.body.classList.remove('body-no-scroll');
    }
    
    // --- EVENT LISTENERS ---

    // 1. Listeners untuk MEMBUKA Offcanvas
    openTriggers.forEach(trigger => {
        trigger.addEventListener('click', openNav);
    });

    // 2. Listeners untuk MENUTUP Offcanvas
    closeTriggers.forEach(trigger => {
        trigger.addEventListener('click', closeNav);
    });
    
    // 5. Listener untuk menutup Offcanvas saat resize ke desktop
    window.addEventListener('resize', () => {
            if (window.innerWidth >= 768) {
            closeNav();
            }
    });

    // --- DROPDOWN LOGIC ---
    const dropdownToggles = document.querySelectorAll('.dropdown-toggle');

    dropdownToggles.forEach(clickedToggle => {
        clickedToggle.addEventListener('click', (e) => {
            e.preventDefault();

            // Check if the clicked dropdown was already open
            const wasOpen = clickedToggle.classList.contains('open');

            // First, close all dropdowns
            dropdownToggles.forEach(otherToggle => {
                otherToggle.classList.remove('open');
                const otherContent = otherToggle.nextElementSibling;
                if (otherContent && otherContent.classList.contains('dropdown-content')) {
                    otherContent.style.maxHeight = "0px";
                }
            });

            // If the clicked dropdown was NOT already open, then open it.
            if (!wasOpen) {
                clickedToggle.classList.add('open');
                const content = clickedToggle.nextElementSibling;
                content.style.maxHeight = content.scrollHeight + "px";
            }
        });
    });

    // --- HIGHLIGHT PARENT DROPDOWN OF ACTIVE SUB-MENU ---
    // This runs once on page load to set the initial state.
    const activeSubMenuLink = document.querySelector('.dropdown-content .offcanvas-link.active');

    if (activeSubMenuLink) {
        const parentDropdown = activeSubMenuLink.closest('.offcanvas-dropdown');
        if (parentDropdown) {
            const dropdownToggle = parentDropdown.querySelector('.dropdown-toggle');
            if (dropdownToggle) {
                // 1. Add 'active' class to highlight the parent dropdown link
                dropdownToggle.classList.add('active');

                // 2. Also open the dropdown to show the active sub-menu item
                dropdownToggle.classList.add('open');
                const content = dropdownToggle.nextElementSibling;
                // Ensure we are targeting the correct content element
                content.style.maxHeight = content.scrollHeight + "px";
            }
        }
    }

    // --- TAB COMPONENT LOGIC ---
    const tabContainers = document.querySelectorAll('.tab-container');

    tabContainers.forEach(container => {
        const tabLinks = container.querySelectorAll('.tab-link');
        const tabPanes = container.querySelectorAll('.tab-pane');

        tabLinks.forEach(clickedLink => {
            clickedLink.addEventListener('click', (e) => {
                e.preventDefault();

                const targetTabId = clickedLink.getAttribute('data-tab');

                // Remove active class from all links and panes in this container
                tabLinks.forEach(link => link.classList.remove('active'));
                tabPanes.forEach(pane => pane.classList.remove('active'));

                // Add active class to the clicked link and its corresponding pane
                clickedLink.classList.add('active');
                container.querySelector(`#${targetTabId}`).classList.add('active');
            });
        });
    });

    // --- LINK-BASED TAB COMPONENT LOGIC (URL HASH) ---
    const tabLinkContainers = document.querySelectorAll('.tab-link-container');

    tabLinkContainers.forEach(container => {
        const tabLinks = container.querySelectorAll('.tab-nav .tab-link');
        const tabPanes = container.querySelectorAll('.tab-content .tab-pane');

        function activateTab(hash) {
            // If no hash, default to the first tab's hash
            if (!hash) {
                const firstLink = tabLinks[0];
                if (firstLink) {
                    hash = firstLink.hash;
                } else {
                    return; // No links found
                }
            }

            let hasActiveTab = false;
            tabLinks.forEach(link => {
                if (link.hash === hash) {
                    link.classList.add('active');
                    hasActiveTab = true;
                } else {
                    link.classList.remove('active');
                }
            });

            tabPanes.forEach(pane => {
                pane.classList.toggle('active', `#${pane.id}` === hash);
            });
        }

        // Activate tab on initial page load
        activateTab(window.location.hash);
        // Activate tab when the hash changes
        window.addEventListener('hashchange', () => activateTab(window.location.hash));
    });
});