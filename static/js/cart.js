var updateBtn = document.getElementsByClassName("update-cart")


for(var i=0;i<updateBtn.length;i++){
    updateBtn[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId: ',productId, ' Action: ',action)
        console.log('USER: ',user)
        if(user === 'AnonymousUser'){
            console.log('User Not Logged In')
        }else{
            UpdateUserOrder(productId,action)
        }
    })
}

function UpdateUserOrder(productId ,Action){
    console.log('User Is Logged In, Sending Data')
    url = '/update_cart/'
    fetch(url,{
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken' : csrftoken,
        },
        body:JSON.stringify({'productId': productId , 'action': Action})
    }).then((response)=>{
        return response.json()
    }).then((data)=>{
        console.log("Data: " , data)
    })
}