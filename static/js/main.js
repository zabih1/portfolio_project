// Add this JavaScript for enhanced interaction
document.addEventListener('DOMContentLoaded', function() {
    const sidebar = document.getElementById('sidebarMenu');
    const backdrop = document.createElement('div');
    backdrop.className = 'sidebar-backdrop';
    
    sidebar.addEventListener('show.bs.collapse', function() {
        document.body.appendChild(backdrop);
        document.body.style.overflow = 'hidden';
    });

    sidebar.addEventListener('hide.bs.collapse', function() {
        document.body.removeChild(backdrop);
        document.body.style.overflow = '';
    });

    backdrop.addEventListener('click', function() {
        bootstrap.Collapse.getInstance(sidebar).hide();
    });
});
