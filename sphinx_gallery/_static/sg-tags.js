// Author: Stuart Mumford
// License: 3-clause BSD
// This script extracts and filters tags

// Track currently selected tags
let selectedTags = new Set();

// Extract all unique tags and populate the tag list
function extractTags() {
    const gridItems = document.querySelectorAll('[data-sgtags]');
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
    if (allTags.size > 0) {
        nameElement = document.createElement('div');
        nameElement.className = 'sphx-glr-tag-label';
        nameElement.textContent = "🏷 Tags:";
        tagList.prepend(nameElement);

        let clearElement = document.createElement('div');
        clearElement.id = 'sphx-glr-tag-clear';
        clearElement.className = 'sphx-glr-tag-label';
        clearElement.textContent = "Clear";
        clearElement.style.display = 'none';  // Hide the element until there is a selected tag
        clearElement.addEventListener('click', () => clearAllTags());
        tagList.appendChild(clearElement);
    }

    const searchParams = new URLSearchParams(window.location.search);
    sgTagsParam = searchParams.get("sg-tags");
    if (sgTagsParam !== null && sgTagsParam !== "") {
        const urlTags = searchParams.get("sg-tags").split(",");
        console.log(urlTags);
        urlTags.forEach(tag => {
            toggleTag(tag);
        });
    }
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
    const clearElement = document.getElementById('sphx-glr-tag-clear')
    if (selectedTags.size > 0) {
        clearElement.style.display = 'block';
    } else {
        clearElement.style.display = 'none';
    }

    // Add tags to URL query params
    const searchParams = new URLSearchParams(window.location.search);
    if (selectedTags.size > 0) {
        const tagStr = Array.from(selectedTags).join(",")
        searchParams.set("sg-tags", tagStr);
    } else {
        searchParams.delete("sg-tags");
    }
    // Update the URL
    const newUrl = `${window.location.pathname}?${searchParams.toString()}`;
    window.history.replaceState({}, "", newUrl);
}

// clear all tags
function clearAllTags () {
    selectedTags.clear();

    const searchParams = new URLSearchParams(window.location.search);
    searchParams.delete("sg-tags");
    const newUrl = `${window.location.pathname}?${searchParams.toString()}`;
    window.history.replaceState({}, "", newUrl);
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
            itemTags = new Set(JSON.parse(item.dataset.sgtags));
        }
        const matchesAllSelected = [...selectedTags].every(tag => itemTags.has(tag));
        item.style.display = matchesAllSelected || selectedTags.size === 0 ? 'block' : 'none';
    });
}

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    extractTags();
});
