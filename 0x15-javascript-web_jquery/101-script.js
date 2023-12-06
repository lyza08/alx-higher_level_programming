document.addEventListener('DOMContentLoaded', function() {
  const addBtn = document.querySelector('div#add_item');
  const removeBtn = document.querySelector('div#remove_item');
  const clearBtn = document.querySelector('div#clear_list');
  const list = document.querySelector('ul.my_list');

  addBtn.addEventListener('click', () => list.appendChild(Object.assign(document.createElement('li'), {textContent: 'Item'})));
  removeBtn.addEventListener('click', () => list.removeChild(list.querySelector('li:last-child')));
  clearBtn.addEventListener('click', () => list.innerHTML = '');
});
