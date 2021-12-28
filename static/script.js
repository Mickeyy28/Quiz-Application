window.onload = initall;
var saveBookButton;
function initall() {
    saveBookButton = document.getElementById('save_ans');
    saveBookButton.onclick = save_ans;
}
function save_ans() {
    var ans = $("input:radio[name=name]:checked").val();
    var url = '/save_ans?ans=' + ans;
    var req = new XMLHttpRequest();

    req.open("GET", url, true);
    req.send();
}