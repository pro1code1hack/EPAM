let contentMinus = document.getElementsByClassName('amount')
let item = document.getElementsByClassName('cart__item')
let contentItems = document.getElementsByClassName('content__items')
let price = document.getElementsByClassName('price')
let allPrice = 0
let quantity = document.getElementsByClassName('quantity')



function onClickPlus(id) {

    let removeId = 'remove-id-'+id;

    document.getElementsByClassName(removeId)[0].children[2].children[1].innerText = Number(document.getElementsByClassName(removeId)[0].children[2].children[1].innerText) + 1;

    if (Number(document.getElementsByClassName(`${removeId}`)[0].children[2].children[1].innerText) <= 0) {
        document.getElementsByClassName(`${removeId}`)[0].children[2].children[1].innerText = 0;
    }
    else {

        allPrice += Number(document.getElementsByClassName(removeId)[0].querySelector('.data').getAttribute('data-price'))
        price[0].textContent = `${allPrice} руб.`
        price[1].textContent = `${allPrice} руб.`
    }
}

function clearCard() {
    contentItems[0].innerHTML = ''
}

function onClickMinus(id) {
    let removeId = 'remove-id-'+id;
    document.getElementsByClassName(removeId)[0].children[2].children[1].innerText = Number(document.getElementsByClassName(removeId)[0].children[2].children[1].innerText) - 1;


    if ( Number(document.getElementsByClassName(removeId)[0].children[2].children[1].innerText)<= 0) {
        document.getElementsByClassName(removeId)[0].children[2].children[1].innerText = 0;
    }
    else {

        allPrice -= Number(document.getElementsByClassName(`${removeId}`)[0].querySelector('.data').getAttribute('data-price'));
    price[0].textContent = `${allPrice} руб.`;
    price[1].textContent = `${allPrice} руб.`;
    }
}
async function removeItem(id) {
    let  removeId = 'remove-id-'+id;
    allPrice -= Number(document.getElementsByClassName(removeId)[0].querySelector('.data').getAttribute('value'))*Number(document.getElementsByClassName(removeId)[0].getElementsByClassName('data')[0].getAttribute('data-price'));
    try {
        document.getElementsByClassName(`${removeId}`)[0].remove();
        await fetch('https://61a63b4a8395690017be919c.mockapi.io/ff/'+ id , {
        method: 'DELETE',
    })
    } catch (error) {
        alert('Не удалось удалить елемент, попробуйте позже!')
        console.log(error)
    }
    quantity[0].innerHTML = item.length;
    quantity[1].innerHTML = `${item.length} шт.`;

    price[0].textContent = `${allPrice} руб.`;
    price[1].textContent = `${allPrice} руб.`;
}




let data = [];
let dataId = [];



async function renderData() {

    let response = await fetch('http://127.0.0.1:8000/posts');
    let responseId = await fetch('https://61a63b4a8395690017be919c.mockapi.io/ff');

    if (response.ok) {
        data = await response.json();
    } else {
        alert('error', response.status);
    }
    if (responseId.ok) {
        dataId = await responseId.json();
    } else {
        alert('error', responseId.status);
    }



    data.forEach(items => {

    for (let i = 0; i < dataId.length; i++) {
        if(items.uuid == dataId[i].uuid){
            contentItems[0].innerHTML += `<div class="cart__item remove-id-${items.uuid}" >
    <div class="cart__item-img">
        <img class="block__image" src="${items.image}" alt="Kovka" />
    </div>
    <div class="cart__item-info">
        <h3>${items.product_name}</h3>
        <p> ${items.description}</p>
    </div>
    <div class="cart__item-count">
        <div class="button button--outline button--circle cart__item-count-minus"
            onclick="onClickMinus(${items.uuid })">
            <svg width="10" height="10" viewBox="0 0 10 10" fill="none"
                xmlns="http://www.w3.org/2000/svg">
                <path
                    d="M5.92001 3.84V5.76V8.64C5.92001 9.17016 5.49017 9.6 4.96001 9.6C4.42985 9.6 4.00001 9.17016 4.00001 8.64L4 5.76L4.00001 3.84V0.96C4.00001 0.42984 4.42985 0 4.96001 0C5.49017 0 5.92001 0.42984 5.92001 0.96V3.84Z"
                    fill="#EB5A1E" />
                <path
                    d="M5.75998 5.92001L3.83998 5.92001L0.959977 5.92001C0.429817 5.92001 -2.29533e-05 5.49017 -2.29301e-05 4.96001C-2.2907e-05 4.42985 0.429817 4.00001 0.959977 4.00001L3.83998 4L5.75998 4.00001L8.63998 4.00001C9.17014 4.00001 9.59998 4.42985 9.59998 4.96001C9.59998 5.49017 9.17014 5.92001 8.63998 5.92001L5.75998 5.92001Z"
                    fill="#EB5A1E" />
            </svg>

        </div>
        <b class="amount data" id="${items.uuid }"  value="${items.amount}" data-price="${items.price}">${items.value}</b>
        <div class="button button--outline button--circle cart__item-count-plus"
            onclick="onClickPlus(${items.uuid})">
            <svg width="10" height="10" viewBox="0 0 10 10" fill="none"
                xmlns="http://www.w3.org/2000/svg">
                <path
                    d="M5.92001 3.84V5.76V8.64C5.92001 9.17016 5.49017 9.6 4.96001 9.6C4.42985 9.6 4.00001 9.17016 4.00001 8.64L4 5.76L4.00001 3.84V0.96C4.00001 0.42984 4.42985 0 4.96001 0C5.49017 0 5.92001 0.42984 5.92001 0.96V3.84Z"
                    fill="#EB5A1E" />
                <path
                    d="M5.75998 5.92001L3.83998 5.92001L0.959977 5.92001C0.429817 5.92001 -2.29533e-05 5.49017 -2.29301e-05 4.96001C-2.2907e-05 4.42985 0.429817 4.00001 0.959977 4.00001L3.83998 4L5.75998 4.00001L8.63998 4.00001C9.17014 4.00001 9.59998 4.42985 9.59998 4.96001C9.59998 5.49017 9.17014 5.92001 8.63998 5.92001L5.75998 5.92001Z"
                    fill="#EB5A1E" />
            </svg>

        </div>
    </div>
    <div class="cart__item-price">
        <b>${items.price} ₽</b>
    </div>
    <div class="cart__item-remove">
        <div class=" button button--outline button--circle" data-id="${items.uuid}" onclick="removeItem(${items.uuid})">
            <svg width="10" height="10" viewBox="0 0 10 10" fill="none"
                xmlns="http://www.w3.org/2000/svg">
                <path
                    d="M5.92001 3.84V5.76V8.64C5.92001 9.17016 5.49017 9.6 4.96001 9.6C4.42985 9.6 4.00001 9.17016 4.00001 8.64L4 5.76L4.00001 3.84V0.96C4.00001 0.42984 4.42985 0 4.96001 0C5.49017 0 5.92001 0.42984 5.92001 0.96V3.84Z"
                    fill="#EB5A1E" />
                <path
                    d="M5.75998 5.92001L3.83998 5.92001L0.959977 5.92001C0.429817 5.92001 -2.29533e-05 5.49017 -2.29301e-05 4.96001C-2.2907e-05 4.42985 0.429817 4.00001 0.959977 4.00001L3.83998 4L5.75998 4.00001L8.63998 4.00001C9.17014 4.00001 9.59998 4.42985 9.59998 4.96001C9.59998 5.49017 9.17014 5.92001 8.63998 5.92001L5.75998 5.92001Z"
                    fill="#EB5A1E" />
            </svg>

        </div>
    </div>
</div>`
    }

    }
     })

    // function getPrice() {
    //     data.forEach(el => {
    //         allPrice += Number(el.price);
    //     })
    //     price[0].innerHTML = allPrice
    // }
    // getPrice()

    let r =[...item]
    r.forEach((items) =>{
        allPrice +=  Number(items.querySelector('.data').getAttribute('value')) * Number(items.querySelector('.data').getAttribute('data-price'));
    })
    price[0].textContent = `${allPrice} руб.`
    price[1].textContent = `${allPrice} руб.`

    quantity[0].innerHTML = item.length 
    quantity[1].innerHTML = `${item.length} шт.` 
}

renderData();