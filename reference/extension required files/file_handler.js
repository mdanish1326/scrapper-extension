function jsonCreator(){
    var url = document.getElementById("url").value
    var price = parseInt(document.getElementById("price").value)
    var email =  document.getElementById("email").value
    // alert(url)
    // alert(price)
    // alert(email)

    var fs = require("fs");
    var obj = {
        "url": url,
        "price": price,
        "email": email
    };

    fs.writeFile("./datafile.json", JSON.stringify(obj), function(err){
        if (err) throw err;
    });

}