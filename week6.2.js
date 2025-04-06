let itemId = 1; // Starting ID for new items
        
function addItem() {
    const name = document.getElementById('name').value;
    const description = document.getElementById('description').value;
    const category = document.getElementById('category').value;
    const price = parseFloat(document.getElementById('price').value).toFixed(2);
    
    if (!name || !description) {
        alert('Please fill in all required fields');
        return;
    }
    
    const itemCard = document.createElement('div');
    itemCard.className = 'item-card';
    itemCard.innerHTML = `
        ID: ${itemId++}, 
        Name: ${name}, 
        Description: ${description}, 
        Category: ${category}, 
        Price: $${price}
    `;
    
    document.getElementById('items-list').prepend(itemCard);
    
    // Clear form
    document.getElementById('name').value = '';
    document.getElementById('description').value = '';
    document.getElementById('price').value = '';
}