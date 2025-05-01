

document.addEventListener('click',(event)=>{
    event.preventDefault()

    const svgIcon = document.querySelector('svg')
   const pathIcon = document.querySelector('path')
          const iconHeartElement = event.target.closest('div')

  
    if( event.target === pathIcon){
        const favID = iconHeartElement.id
        console.log(favID)
       
    }

    // fetch('', {
    //     method: 'post',
    //     body: JSON.stringify({
    //         iD: iconHeartElement.id
    //     })
    // })
    

        
})
