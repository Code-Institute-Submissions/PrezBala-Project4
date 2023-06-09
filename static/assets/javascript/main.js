// NavBar
function hideIconBar() {
  var iconBar = document.getElementById("iconBar");
  var navigation = document.getElementById("navigation");
  var navbar = document.querySelector(".navbar");
  iconBar.setAttribute("style", "display:none;");
  navigation.classList.remove("hide");
  navbar.classList.add("expanded");
}

function showIconBar() {
  var iconBar = document.getElementById("iconBar");
  var navigation = document.getElementById("navigation");
  var navbar = document.querySelector(".navbar");
  iconBar.setAttribute("style", "display:block;");
  navigation.classList.add("hide");
  navbar.classList.remove("expanded");
}

// Comment
function showComment() {
  var commentArea = document.getElementById("comment-area");
  // Use toggle instead of remove
  commentArea.classList.toggle("hide");
}

// Reply
function showReplies(id) {
  var replyArea = document.getElementById(id);
  // Use toggle instead of remove
  replyArea.classList.toggle("hide");
}
