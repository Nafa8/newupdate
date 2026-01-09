// --- Highlight Selling Module Workspace ---
frappe.ready(function() {
    const ws = document.querySelectorAll('.workspace[data-module="Selling"] .workspace-card');
    ws.forEach(card => {
        card.style.cursor = "pointer";
        card.addEventListener('mouseenter', () => {
            card.style.transform = "translateY(-5px)";
            card.style.boxShadow = "0 6px 16px rgba(0,0,0,0.7)";
        });
        card.addEventListener('mouseleave', () => {
            card.style.transform = "translateY(0)";
            card.style.boxShadow = "0 4px 12px rgba(0,0,0,0.5)";
        });
    });
});
