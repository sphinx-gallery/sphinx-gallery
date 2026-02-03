// Author: Stuart Mumford
// License: 3-clause BSD
// This script extracts and filters tags

// Track currently selected tags
let selectedTags = new Set();

// Extract all unique tags and populate the tag list
function extractTags() {
    const gridItems = document.querySelectorAll('[data-sgtags]');
    console.log(gridItems);
    const allTags = new Set();

    gridItems.forEach(item => {
        if (item.dataset.sgtags) {
            const tags = JSON.parse(item.dataset.sgtags);
            tags.forEach(tag => allTags.add(tag));
        }
    });

    const tagList = document.getElementById('sg-tag-list');
    allTags.forEach(tag => {
        const tagElement = document.createElement('div');
        tagElement.className = 'sphx-glr-tag';
        tagElement.textContent = tag;
        tagElement.addEventListener('click', () => toggleTag(tag));
        tagList.appendChild(tagElement);
    });
}

// Toggle a tag's selected state and update the grid
function toggleTag(tag) {
    if (selectedTags.has(tag)) {
        selectedTags.delete(tag);
    } else {
        selectedTags.add(tag);
    }

    // Update UI and filter grid
    updateTagUI();
    filterGrid();
}

// Update the UI to reflect selected tags
function updateTagUI() {
    const tags = document.querySelectorAll('.sphx-glr-tag');
    tags.forEach(tagElement => {
        tagElement.classList.toggle(
            'active',
            selectedTags.has(tagElement.textContent)
        );
    });
}

// Filter grid items based on selected tags
function filterGrid() {
    const gridItems = document.querySelectorAll('.sphx-glr-thumbcontainer');

    gridItems.forEach(item => {
        let itemTags = new Set();
        if (item.dataset.sgtags) {
            const itemTags = new Set(JSON.parse(item.dataset.sgtags));
        }
        const matchesAllSelected = [...selectedTags].every(tag => itemTags.has(tag));
        item.style.display = matchesAllSelected || selectedTags.size === 0 ? 'block' : 'none';
    });
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    extractTags();
});
