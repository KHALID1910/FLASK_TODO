function validTodo(){
    var title = document.getElementById("title").value;
    var desc = document.getElementById("desc").value;

    if (title=="" || desc==''){
        alert("please fill the fields!!!!")
        return false;
    }else{
        return true;
    }
}