const buttons = document.querySelectorAll('[data-js-delete-favorites]')

buttons.forEach((btn)=>{
    btn.addEventListener('click',(event)=>{
        const closest =  event.target.closest('.my-products__item')
        closest.remove()
    })
})