with open('home/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Replace the click listener with capture phase listener
old_listener = """document.addEventListener('click', function(e) {
  var a = e.target.closest('a');
  if (!a) return;
  var href = a.getAttribute('href');
  if (href && href.startsWith('#') && href.length > 1) {
    var id = href.substring(1);
    var target = document.getElementById(id) || 
                 document.querySelector('.' + id) || 
                 document.querySelector('[id*="' + id + '"]');
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      try { history.pushState(null, null, '#' + id); } catch(err) {}
    }
  }
});"""

new_listener = """// High-priority CAPTURE phase click delegator for instant, unblockable smooth scrolling
document.addEventListener('click', function(e) {
  var a = e.target.closest('a');
  if (!a) return;
  var href = a.getAttribute('href');
  if (href && href.startsWith('#') && href.length > 1) {
    var id = href.substring(1);
    var target = document.getElementById(id) || 
                 document.querySelector('.' + id) || 
                 document.querySelector('[id*="' + id + '"]');
    if (target) {
      e.preventDefault();
      e.stopPropagation();
      e.stopImmediatePropagation();
      var headerOffset = 90;
      var elementPosition = target.getBoundingClientRect().top;
      var offsetPosition = elementPosition + window.pageYOffset - headerOffset;
      window.scrollTo({
        top: offsetPosition,
        behavior: 'smooth'
      });
      try { history.pushState(null, null, '#' + id); } catch(err) {}
    }
  }
}, true);"""

html = html.replace(old_listener, new_listener)

with open('home/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated click delegator to capture phase!")
