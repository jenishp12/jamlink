let profileMenu = document.getElementById("profileMenu");

function toggleMenu() {
    profileMenu.classList.toggle("open-menu");
}

const searchInput = document.getElementById("searchInput");
const posts = document.querySelectorAll(".post");

searchInput.addEventListener("input", function () {
    const searchTerm = searchInput.value.toLowerCase();

    posts.forEach((post) => {
        const author = post.querySelector(".post-author h1").textContent.toLowerCase();
        const content = post.querySelector("p").textContent.toLowerCase();
        if (author.includes(searchTerm) || content.includes(searchTerm)) {
            post.style.display = "block";
        } else {
            post.style.display = "none";
        }
    });
});

// Like button functionality
const likeButtons = document.querySelectorAll(".like-button");

likeButtons.forEach((button) => {
    button.addEventListener("click", function () {
        const post = button.closest(".post");
        const likeCountSpan = post.querySelector(".like-count");
        let currentLikes = parseInt(likeCountSpan.textContent) || 0;
        likeCountSpan.textContent = `${currentLikes + 1} likes`;
        
        // Add liked effect
        button.classList.add("liked");
        setTimeout(() => {
            button.classList.remove("liked");
        }, 300); // Remove effect after 300ms
    });
});

// Comment button functionality
const commentButtons = document.querySelectorAll(".comment-button"); /* CHANGED: Added comment toggle logic */
commentButtons.forEach((button) => {
    button.addEventListener("click", function () {
        const post = button.closest(".post");
        const commentSection = post.querySelector(".comment-section");
        commentSection.style.display = commentSection.style.display === "none" ? "block" : "none";
    });
});

// Submit comment functionality
const submitCommentButtons = document.querySelectorAll(".submit-comment"); /* CHANGED: Added comment submit logic */
submitCommentButtons.forEach((button) => {
    button.addEventListener("click", function () {
        const post = button.closest(".post");
        const commentInput = post.querySelector(".comment-input");
        const commentsList = post.querySelector(".comments-list");
        const commentText = commentInput.value.trim();

        if (commentText) {
            const comment = document.createElement("p");
            comment.textContent = commentText;
            commentsList.appendChild(comment);
            commentInput.value = ""; // Clear input
        }
    });
});

// Share button functionality
const shareButtons = document.querySelectorAll(".share-button"); /* CHANGED: Added share popup logic */
const sharePopup = document.querySelector(".share-popup");
const shareLinkInput = document.querySelector(".share-link");
const copyLinkButton = document.querySelector(".copy-link");
const closePopupButton = document.querySelector(".close-popup");

shareButtons.forEach((button, index) => {
    button.addEventListener("click", function () {
        const post = button.closest(".post");
        const postId = post.getAttribute("data-post-id");
        shareLinkInput.value = `jamlink.com/post/${postId}`;
        sharePopup.style.display = "flex";
        sharePopup.classList.add("active");
    });
});

copyLinkButton.addEventListener("click", function () {
    copyLinkButton.classList.add("copied");
    copyLinkButton.textContent = "Copied!";
    setTimeout(() => {
        copyLinkButton.classList.remove("copied");
        copyLinkButton.textContent = "Copy Link";
    }, 1000);
});

closePopupButton.addEventListener("click", function () {
    sharePopup.style.display = "none";
    sharePopup.classList.remove("active");
});

// JamLink logo and Home icon reload page
const jamlinkLogo = document.querySelector(".logo"); /* CHANGED: Added reload for logo */
const homeIcon = document.querySelector(".active-link"); /* CHANGED: Added reload for home */

jamlinkLogo.addEventListener("click", function (event) {
    event.preventDefault(); // Stop default link behavior
    window.location.reload(); // Reload page
});

homeIcon.addEventListener("click", function (event) {
    event.preventDefault(); // Stop default link behavior
    window.location.reload(); // Reload page
});