


document.addEventListener('click',(event)=>{
    const iconHeartElement = event.target.closest('div .icon--heart')
    console.log(iconHeartElement)
    if(iconHeartElement.classList.contains('icon--heart')){
        iconHeartElement.classList.toggle('icon-red-heart')
    }
})