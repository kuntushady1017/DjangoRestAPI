const loginFrom = document.getElementById('login-form')
const productContianer = document.getElementById('container')
const baseEndpoint = "http://localhost:8000/api"
if (loginFrom) {
    loginFrom.addEventListener('submit', handleLogin)
}

function handleLogin(event){
    event.preventDefault()
    const loginEndpoint = `${baseEndpoint}/token/`
    let loginData = new FormData(loginFrom)
    let loginObject = Object.fromEntries(loginData)
    const options = {
        method: "POST",
        headers:{
            "Content-Type": "application/json"
        },
        body: JSON.stringify(loginObject)
    }
    fetch(loginEndpoint, options).then(response =>{
        // console.log(response)
        return response.json()
    }).then(data=>{
        handleAuthData(data, getProductList)
    }).catch(error =>{
        console.log(error)
    })
}

function handleAuthData(authData, callback){
    localStorage.setItem('access', authData.access)
    localStorage.setItem('refresh', authData.refresh)
    if (callback) {
        callback()
    }
}

function writeProduct(data){
    if(productContianer){
        productContianer.innerHTML ="<pre>" + JSON.stringify(data, null, 4) + "<pre>"
    }
}


function getFetchOptions(method, body){
    return {
        method: method === null ? "GET" : method,
        headers:{
            "Content-Type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem('access')}`,
        },
        body: body ? body: null,
    }
}


function getProductList(){
    const endpoint = `${baseEndpoint}/products/`
    const options = getFetchOptions("GET")
    fetch(endpoint, options).then(response =>response.json()).then(data => {
        console.log(data)
        writeProduct(data)
    }).catch(error =>{
        console.log(error)
    })
}