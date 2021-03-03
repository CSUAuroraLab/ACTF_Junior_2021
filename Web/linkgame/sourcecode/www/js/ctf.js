document.onkeydown = function(e) {
    if (e.ctrlKey &&
    (e.keyCode === 65 ||
    e.keyCode === 67 ||
    e.keyCode === 73 ||
    e.keyCode === 74 ||
    e.keyCode === 80 ||
    e.keyCode === 83 ||
    e.keyCode === 85 ||
    e.keyCode === 86 ||
    e.keyCode === 117
    )) {
    return false;
    }
    if(e.keyCode==18||e.keyCode==123){return false}
    };
document.oncontextmenu = function () {  
    return false;  
}