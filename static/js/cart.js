console.log("Welcome to cart.js")

var updateButtons = document.getElementsByClassName("update-cart");

for(var i = 0; i < updateButtons.length; i++){
    updateButtons[i].addEventListener("click",function(){
       var productId = this.dataset.product
       var action = this.dataset.action
       console.log("Product id:",productId,"Action",action)
    
    if (user == "AnonymousUser"){
        addToCartError()
    } 
    else{
        updateCart(productId,action)
    }
    
})
}

function updateCart(productId,action){
    var productId = productId;
    var action = action;
    var url = "members/update-cart"
    console.log("URL:",url)

    fetch(url,{
        method :"POST",
        headers : {
            "Content-Type":"application/json",
            "X-CSRFToken" : csrftoken
        },
        body : JSON.stringify({"productId":productId,"action":action}) 
    })
    .then((response) =>{
        return response.json()
    })
    .then((data) =>{
     console.log(data)
     location.reload()
    })
    
}

function addToCartError(){
    console.log("You are not logged in!")
    alert("You must be logged in to add product in cart!")
    
}