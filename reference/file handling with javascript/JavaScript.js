function jsonCreator(){
    var fs = require("fs");
    
    var obj = {
        "name": "prodcut price",
        "comment": "Yay! My file."
    };
    
    fs.writeFile("newfile.json", JSON.stringify(obj), function(err){
        if (err) throw err;
    });
}